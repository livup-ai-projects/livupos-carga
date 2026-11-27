#!/usr/bin/env python3
"""Confere os rascunhos da estratégia (empresa, diretorias e projetos) e lista o que falta por diretoria.

Uso:
  python3 conferir_estrategia.py <pasta> [--existentes existentes.txt] [--codigos codigos.csv]
                                 [--areas-sem-leitura people,tech] [--subareas producao=operacoes]

<pasta>: os documentos a conferir, um .md por documento, no caminho do LivupOS
  (<pasta>/liv-up/estrategia/2027.md, <pasta>/growth/estrategia/2027.md,
   <pasta>/growth/projetos/regua-de-retencao/visao-geral.md). Pode trazer também documentos já publicados que
   importam para a conta (a estratégia da empresa publicada, um projeto de que outro depende), copiados do LivupOS.
--existentes: caminhos que já existem no LivupOS (um por linha), tirados do listar: indicadores e projetos.
--codigos: a lista de códigos do acompanhamento, como ela vier (CSV com cabeçalho, separado por vírgula ou ponto e
  vírgula, UTF-8 ou Latin-1). Coluna do código obrigatória (`codigo` ou `código`); `projeto` ou `nome`, `diretoria` e
  `dono` (e-mail ou nome) opcionais. Marco: a coluna `marco` (PRJ-001/M01) ou a linha cujo código tem barra. Uma
  linha por marco, com o código do projeto repetido, é aceita.
--subareas: as subáreas que existem no LivupOS, cada uma com a diretoria-pai (producao=operacoes,last-mile=logistica).
  O que falta num projeto de subárea vai para a lista da diretoria-pai, que é quem confere. Projeto cuja primeira
  pasta não é diretoria com estratégia, subárea declarada nem área que existe é apontado.
--areas-sem-leitura: as áreas que quem roda não lê; o que aponta para elas sai como "não conferido", não como
  "não existe".

Saída: markdown na saída padrão, uma seção por área, cada linha com o documento, o que falta e quem responde (papel,
não e-mail). Depois, à parte e fora da contagem, "Para confirmar com quem se espera": o que um projeto diz esperar de
outro projeto ou de uma área, para quem se espera confirmar ("Quem espera algo deste projeto" só se preenche na
conferência com o diretor). Fica fora dos arquivos o que esbarra numa decisão sigilosa (references/estrategia.md,
seção 3, C2). É material de trabalho: para o diretor, a skill traduz em linguagem simples. Só lê arquivos; não chama nada de fora.
Sem PyYAML, faça a conferência à mão (references/estrategia.md, seção 5).
"""
import csv
import io
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("PyYAML não está disponível: faça a conferência à mão (references/estrategia.md, seção 5).")
    sys.exit(2)

CODIGO = re.compile(r"^PRJ-\d{3,}$")
MARCO = re.compile(r"^(PRJ-\d{3,})/M\d{2,}$")
MESES = (r"janeiro|fevereiro|mar[cç]o|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro"
         r"|jan|fev|mar|abr|mai|jun|jul|ago|set|out|nov|dez")
DATA_NO_TEXTO = re.compile(
    r"(?P<dm>\b(?P<d>\d{1,2})/(?P<m>\d{1,2})(?:/(?P<a1>\d{2,4}))?\b)"
    r"|\b(?:" + MESES + r")\.?(?:/(?P<a2>\d{2,4})|\s+de\s+(?P<a3>\d{4}))\b"
    r"|\b(?:fim|final|in[ií]cio|meio|metade)\s+de\s+(?P<a4>\d{4})\b"
    r"|\b\d{1,2}[ºo]?\s+(?:tri|trimestre|semestre)\b|\b[1-4]T\d{2,4}\b|\bQ[1-4]\b",
    re.IGNORECASE,
)
ANTES_DE_DATA = re.compile(r"(?:\bem|\bat[eé]|\bdia|\bdesde|\bde|\bpara|\bpartir de|\bentre|[—–:(-])\s*$", re.IGNORECASE)
SECOES_PROJETO = ["Tese", "Como saber se funcionou", "Fora do escopo", "Riscos"]
ABRE_EM = {"soma", "media", "nao abre"}
QUEM_MONTOU = "quem montou os rascunhos"
CAMPOS_DE_SISTEMA = ("camada", "autoridade", "status", "owner", "owner_id", "revisar_em")
TIPOS_META = {"chegar a", "manter", "entrega"}  # D148; sem tipo é chegar_a
SENTIDOS = {"no minimo", "no maximo"}
PERIODOS = {"mensal", "trimestral", "semestral", "anual"}
PRAZO = re.compile(r"^\d{4}(-(0[1-9]|1[0-2])(-\d{2})?|-[TtQq][1-4]|-[Ss][12])?$")  # mês, trimestre, semestre, ano, data
PROPRIO = "proprio-da-area"  # projeto só da área, sem objetivo da empresa, por decisão (não é falta)
# D160 (OKR): objetivo → resultado-chave (a meta) ← projeto; projeto-chave é a marca `chave: true` no projeto.
LIMITE_PROJETOS_CHAVE = 5  # o padrão; a estratégia do ano da área pode declarar outro em `limite_projetos_chave`
LIMITE_RESULTADOS_POR_OBJETIVO = 5  # o método pede de 3 a 5 resultados-chave por objetivo


def norm(txt):
    txt = unicodedata.normalize("NFKD", str(txt)).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", txt).strip()


def ler_doc(arquivo):
    texto = arquivo.read_text(encoding="utf-8", errors="replace")
    if not texto.startswith("---"):
        return None, texto
    partes = texto.split("\n---", 1)
    corpo = partes[1].split("\n", 1)[1] if len(partes) > 1 and "\n" in partes[1] else ""
    try:
        cab = yaml.safe_load(partes[0][3:])
    except yaml.YAMLError as erro:
        marca = getattr(erro, "problem_mark", None)
        return {"_erro": f"o cabeçalho não é YAML válido{f' (linha {marca.line + 2})' if marca else ''}"}, corpo
    if cab is None:
        cab = {}
    if not isinstance(cab, dict):
        return {"_erro": "o cabeçalho não é uma lista de campos (campo: valor)"}, corpo
    return cab, corpo


def valor(txt):
    """'R$ 111 mi' -> (111e6, 'R$'); '38%' -> (38, '%'); '+3 p.p.' -> (3, 'pp'). None se não der para ler."""
    if txt is None or isinstance(txt, (list, dict)):
        return None
    s = str(txt).strip().lower().replace(" ", " ").replace("−", "-").replace("–", "-")
    unidade = ""
    if "r$" in s:
        unidade = "R$"
    elif re.search(r"p\.\s?p\b|\bpp\b", s):
        unidade = "pp"
    elif "%" in s:
        unidade = "%"
    m = re.search(r"[-+]?\d[\d.]*(,\d+)?", s)
    if not m:
        return None
    num = m.group(0)
    if "," in num:
        num = num.replace(".", "").replace(",", ".")
    elif num.count(".") > 1 or re.search(r"\.\d{3}$", num):
        num = num.replace(".", "")
    try:
        n = float(num)
    except ValueError:
        return None
    resto = s[m.end():]
    if re.match(r"\s*(tri\b|trilh)", resto):
        n *= 1e12
    elif re.match(r"\s*(bi\b|bilh)", resto):
        n *= 1e9
    elif re.match(r"\s*(mil\b|k\b)", resto):
        n *= 1e3
    elif re.match(r"\s*(mi\b|milh|mm\b)", resto):
        n *= 1e6
    return n, unidade


def sem_aspas(v):
    """Número escrito sem aspas no YAML: `para: 1.750` chega aqui como 1.75. O molde manda texto entre aspas."""
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def br(n, casas=2):
    """1234567.5 -> '1.234.567,5'."""
    txt = f"{n:,.{casas}f}".replace(",", "_").replace(".", ",").replace("_", ".")
    return txt.rstrip("0").rstrip(",") if "," in txt else txt


def escrever(n, unidade):
    if unidade == "R$":
        for div, suf in ((1e12, " tri"), (1e9, " bi"), (1e6, " mi"), (1e3, " mil")):
            if abs(n) >= div:
                return f"R$ {br(n / div)}{suf}"
        return f"R$ {br(n)}"
    return br(n) + {"%": "%", "pp": " p.p."}.get(unidade, "")


def sem_partes_permitidas(corpo):
    """Tira do texto o que pode ter data: a linha de Fonte, "Fora do escopo" e "Em aberto"."""
    corpo = re.sub(r"^>\s*Fonte:.*(\n>.*)*", "", corpo, flags=re.MULTILINE)
    return re.sub(r"^#{2,4}\s+(Fora do escopo|Em aberto).*?(?=^#{2,4}\s|\Z)", "", corpo,
                  flags=re.MULTILINE | re.DOTALL | re.IGNORECASE)


def datas_no_texto(corpo, ano):
    """Datas de marco ou entrega no texto. Data com ano anterior ao da estratégia é citação de fonte e passa."""
    texto = sem_partes_permitidas(corpo)
    achadas = set()
    for m in DATA_NO_TEXTO.finditer(texto):
        if m.group("dm"):
            d, mes = int(m.group("d")), int(m.group("m"))
            if not (1 <= d <= 31 and 1 <= mes <= 12):
                continue  # "7/21/40" não é data
            if not m.group("a1") and not ANTES_DE_DATA.search(texto[max(0, m.start() - 14):m.start()]):
                continue  # "24/7", "1/3 da base": sem ano e sem "em", "até", "dia"... antes
        a = m.group("a1") or m.group("a2") or m.group("a3") or m.group("a4")
        if a and ano and (int(a) + (2000 if len(a) == 2 else 0)) < ano:
            continue
        achadas.add(m.group(0))
    return sorted(achadas)


def mesmo_dono(a, b):
    """Compara dono por e-mail ou por nome: "Marina Exemplo" ou "Marina" bate com marina.exemplo@livup.com.br."""
    a, b = str(a).lower().strip(), str(b).lower().strip()
    if not a or not b:
        return True
    if "@" in a and "@" in b:
        return a == b
    if "@" not in a and "@" not in b:
        return norm(a) == norm(b)
    email, nome = (a, b) if "@" in a else (b, a)
    partes = [norm(x) for x in re.split(r"[._-]", email.split("@")[0]) if x]
    nomes = norm(nome).split()
    return all(x in partes for x in nomes) or all(x in nomes for x in partes)


def secoes(corpo):
    return {norm(m.group(2)) for m in re.finditer(r"^(#{2,4})\s+(.+?)\s*$", corpo, re.MULTILINE)}


def trecho_da_secao(corpo, titulo):
    m = re.search(r"^#{2,4}\s+" + re.escape(titulo) + r".*?$(.*?)(?=^#{2,4}\s|\Z)", corpo,
                  re.MULTILINE | re.DOTALL | re.IGNORECASE)
    return m.group(1) if m else ""


def ler_codigos(arq):
    dados = arq.read_bytes()
    try:
        texto = dados.decode("utf-8-sig")
    except UnicodeDecodeError:
        texto = dados.decode("latin-1")
    try:
        dialeto = csv.Sniffer().sniff(texto[:4096], delimiters=",;\t")
    except csv.Error:
        dialeto = csv.excel
    leitor = csv.reader(io.StringIO(texto), dialeto)
    cabecalho = [norm(c).replace(" ", "_") for c in next(leitor, [])]
    if "codigo" not in cabecalho:
        return None, None
    codigos, marcos, nomes = {}, set(), defaultdict(set)
    for celulas in leitor:
        linha = dict(zip(cabecalho, (c.strip() for c in celulas)))
        cod, marco = linha.get("codigo", ""), linha.get("marco", "")
        if MARCO.match(marco):
            marcos.add(marco)
        if MARCO.match(cod):
            marcos.add(cod)
            continue
        if not CODIGO.match(cod):
            continue
        # nome do projeto: a coluna `projeto`; `nome` só vale em linha que não é de marco
        nome = linha.get("projeto") or ("" if marco else linha.get("nome", ""))
        if nome:
            nomes[cod].add(norm(nome))
        atual = codigos.setdefault(cod, {"nome": "", "dono": "", "diretoria": ""})
        atual["nome"] = atual["nome"] or nome
        atual["dono"] = atual["dono"] or linha.get("dono", "")
        atual["diretoria"] = atual["diretoria"] or linha.get("diretoria", "")
    for cod, conj in nomes.items():
        if len(conj) > 1:
            codigos[cod]["_repetido"] = True
    return codigos, marcos


def lista_de_campos(cab, campo, falta, caminho, quem):
    """O campo tem de ser uma lista de itens com campos; o que não for vira achado e conta como vazio."""
    v = cab.get(campo)
    if v in (None, ""):
        return []
    if not isinstance(v, list) or not all(isinstance(x, dict) for x in v):
        falta(caminho, f"o campo `{campo}` não está no formato de lista de itens (- campo: valor)", quem)
        return []
    return v


def opcao(args, nome):
    if nome not in args:
        return None
    i = args.index(nome)
    if i + 1 >= len(args) or args[i + 1].startswith("--"):
        print(f"Falta o valor de {nome}.", file=sys.stderr)
        sys.exit(1)
    return args[i + 1]


def main():
    args = sys.argv[1:]
    if not args or args[0].startswith("--"):
        print(__doc__)
        sys.exit(1)
    pasta = Path(args[0])
    sem_leitura = {a.strip() for a in (opcao(args, "--areas-sem-leitura") or "").split(",") if a.strip()}
    pai = {}
    for par in (opcao(args, "--subareas") or "").split(","):
        if "=" in par:
            sub, p_ = (x.strip() for x in par.split("=", 1))
            if sub and p_:
                pai[sub] = p_

    def dona(area):
        """A diretoria que confere: a própria área, ou a diretoria-pai, se é subárea declarada."""
        return pai.get(area, area)
    existentes, codigos, marcos = set(), {}, set()
    if opcao(args, "--existentes"):
        arq = Path(opcao(args, "--existentes"))
        existentes = {l.strip().strip("/").removesuffix(".md") for l in
                      arq.read_text(encoding="utf-8", errors="replace").splitlines() if l.strip()}
    aviso_codigos = None
    if opcao(args, "--codigos"):
        codigos, marcos = ler_codigos(Path(opcao(args, "--codigos")))
        if codigos is None:
            codigos, marcos = {}, set()
            aviso_codigos = "> A lista de códigos não tem a coluna do código (`codigo`): não foi usada.\n"

    arquivos = sorted(pasta.rglob("*.md")) if pasta.is_dir() else []
    if not arquivos:
        print(f"Nenhum documento .md em {pasta}: nada foi conferido.", file=sys.stderr)
        sys.exit(1)
    docs = {}
    for arq in arquivos:
        docs[arq.relative_to(pasta).as_posix().removesuffix(".md")] = ler_doc(arq)

    achados = defaultdict(list)  # area -> [(doc, o que falta, quem responde)]
    confirmar = defaultdict(list)  # area de quem se espera -> [(doc, o que confirmar, quem responde)]

    def falta(caminho, texto, quem, area=None):
        achados[dona(area or caminho.split("/")[0])].append((caminho, texto, quem))

    def a_confirmar(caminho, texto, quem, area=None):
        """O outro lado de uma dependência: "Quem espera algo deste projeto" só se preenche na conferência com o diretor,
        então isto não é falta; é pergunta a quem se espera."""
        confirmar[dona(area or caminho.split("/")[0])].append((caminho, texto, quem))

    def limpo(c):
        return str(c).strip().strip("/").removesuffix(".md")

    def existe(c):
        c = limpo(c)
        return c in existentes or c in docs

    def nao_vejo(c):
        return limpo(c).split("/")[0] in sem_leitura

    def sem_valor(v):
        return v in (None, "") or (isinstance(v, str) and norm(v).startswith("a confirmar"))

    validos = {}
    for caminho, (cab, corpo) in docs.items():
        if cab is None:
            falta(caminho, "o documento não tem cabeçalho (frontmatter)", QUEM_MONTOU)
        elif "_erro" in cab:
            falta(caminho, cab["_erro"], QUEM_MONTOU)
        else:
            validos[caminho] = (cab, corpo)
            proibidos = [str(c) for c in cab if str(c).lower() in CAMPOS_DE_SISTEMA]
            if proibidos:
                dica = " (o dono do projeto vai em `dono`)" if any(c.lower() == "owner" for c in proibidos) else ""
                falta(caminho, f"o cabeçalho tem campo do sistema ({', '.join(proibidos)}), que o LivupOS recusa: tire{dica}", QUEM_MONTOU)

    def tags(cab):
        t = cab.get("tags") or []
        return [str(x) for x in t] if isinstance(t, list) else [str(t)]

    estrategias = [c for c in validos if re.match(r"^[a-z0-9-]+/estrategia/\d{4}$", c)]
    empresa = [c for c in estrategias if c.startswith("liv-up/")]
    diretorias = [c for c in estrategias if not c.startswith("liv-up/")]
    ano_estrategia = max(int(c.rsplit("/", 1)[1]) for c in estrategias) if estrategias else None
    # O documento do projeto é a visao-geral da pasta dele; documento de trabalho ao lado dela (mesmo com a tag) não é.
    projetos = [c for c, (cab, _) in validos.items()
                if re.search(r"(^|/)projetos/[^/]+/visao-geral$", c)
                or ("projeto" in tags(cab) and not re.search(r"(^|/)projetos/[^/]+/[^/]+$", c))]

    for caminho in estrategias:
        cab, _ = validos[caminho]
        if cab.get("tipo") != "referencia" or "estrategia" not in tags(cab):
            falta(caminho, "o cabeçalho precisa de `tipo: referencia` e `tags: [estrategia]`", QUEM_MONTOU)
    for caminho in projetos:
        cab, _ = validos[caminho]
        if cab.get("tipo") != "referencia" or "projeto" not in tags(cab):
            falta(caminho, "o cabeçalho precisa de `tipo: referencia` e `tags: [projeto]`", QUEM_MONTOU)

    objetivos, metas_empresa = {}, {}
    for caminho in empresa:
        cab, _ = validos[caminho]
        for obj in lista_de_campos(cab, "objetivos", falta, caminho, "diretoria executiva"):
            oid = obj.get("id")
            if not isinstance(oid, str) or not oid:
                falta(caminho, "objetivo sem id", "diretoria executiva")
                continue
            if oid in objetivos:
                falta(caminho, f"objetivo `{oid}` aparece duas vezes", "diretoria executiva")
            if norm(oid) == norm(PROPRIO):
                falta(caminho, f"o id `{oid}` é reservado para projeto só da área: dê outro id ao objetivo", "diretoria executiva")
            objetivos[oid] = obj
            if not obj.get("nome"):
                falta(caminho, f"objetivo `{oid}` sem nome", "diretoria executiva")
        for meta in lista_de_campos(cab, "metas", falta, caminho, "diretoria executiva"):
            if isinstance(meta.get("id"), str):
                metas_empresa[meta["id"]] = (caminho, meta)

    def conferir_indicador(caminho, ind, prefixo, quem):
        if sem_valor(ind) or not isinstance(ind, str):
            falta(caminho, f"{prefixo}falta o documento do indicador", quem)
        elif nao_vejo(ind):
            falta(caminho, f"{prefixo}o indicador `{limpo(ind)}` não foi conferido (quem montou não lê a área); existe?", quem)
        elif not existe(ind):
            falta(caminho, f"{prefixo}o indicador `{limpo(ind)}` não existe no LivupOS (quem cria?)", quem)

    objetivos_area = defaultdict(dict)  # D148: objetivos da área, com serve_a (os pilares da empresa)

    def conferir_objetivo(caminho, obj, prefixo, quem, obrigatorio):
        da_area = objetivos_area.get(caminho.split("/")[0], {})
        if sem_valor(obj):
            if obrigatorio:
                falta(caminho, f"{prefixo}falta dizer a que objetivo da empresa serve" + (", ou se é só da área" if not prefixo else ""), quem)
        elif not isinstance(obj, str):
            dica = "" if prefixo else "; para mais de um, use `objetivos: [...]`"
            falta(caminho, f"{prefixo}`objetivo` tem de ser UM objetivo (está: {obj}){dica}", quem)
        elif norm(obj) == norm(PROPRIO):
            falta(caminho, f"{prefixo}`{PROPRIO}` vale só em projeto; uma meta serve a um objetivo da empresa", quem)
        elif objetivos and obj not in objetivos and obj not in da_area:
            falta(caminho, f"{prefixo}o objetivo `{obj}` não está entre os objetivos da empresa nem os da área", quem)

    todas_metas = {}  # id -> (caminho, meta): as metas da empresa e das diretorias desta pasta (D160)

    def conferir_aspiracao(caminho, meta, tipo, pre, quem):
        """D160: a aspiração (o alvo além do comprometido) existe no chegar_a e no manter, e não fica aquém dele."""
        asp = meta.get("aspiracao")
        if sem_valor(asp):
            return
        if tipo == "entrega":
            falta(caminho, f"{pre}a entrega é sim ou não na data: não tem aspiração (tire a `aspiracao`)", QUEM_MONTOU)
            return
        relativo = lambda v: str(v).strip().startswith(("+", "-"))
        if tipo == "chegar a" and relativo(asp) and relativo(meta.get("para")):
            # As duas relativas ao mesmo `de` ("+20%" e "+10%"): compara as variações, no sentido do para.
            p_, a = valor(meta.get("para")), valor(asp)
            if p_ and a and p_[1] == a[1] and p_[0] != 0 and ((a[0] < p_[0]) if p_[0] > 0 else (a[0] > p_[0])):
                falta(caminho, f"{pre}a aspiração ({asp}) fica aquém do valor de chegada ({meta.get('para')}): a aspiração vai além do comprometido", quem)
            return
        a = None if relativo(asp) else valor(asp)
        if tipo == "chegar a":
            d, p_ = valor(meta.get("de")), None if relativo(meta.get("para")) else valor(meta.get("para"))
            if a and d and p_ and d[1] == p_[1] == a[1] and p_[0] != d[0]:
                if (a[0] < p_[0]) if p_[0] > d[0] else (a[0] > p_[0]):
                    falta(caminho, f"{pre}a aspiração ({asp}) fica aquém do valor de chegada ({meta.get('para')}): a aspiração vai além do comprometido", quem)
        elif tipo == "manter":
            lim, sentido = valor(meta.get("limite")), norm(meta.get("sentido") or "")
            if a and lim and a[1] == lim[1] and ((sentido == "no maximo" and a[0] > lim[0]) or (sentido == "no minimo" and a[0] < lim[0])):
                falta(caminho, f"{pre}a aspiração ({asp}) fica aquém do limite ({meta.get('limite')}): a aspiração é um nível melhor que o comprometido", quem)

    def conferir_meta(caminho, meta, quem, da_empresa):
        mid = meta.get("id")
        if not isinstance(mid, str) or not mid:
            falta(caminho, "meta sem id", quem)
            return
        pre = f"meta `{mid}`: "
        if mid in todas_metas:
            falta(caminho, f"{pre}o id também está em `{todas_metas[mid][0]}`: cada meta tem um id só (ponha a área no id)", QUEM_MONTOU)
        todas_metas[mid] = (caminho, meta)
        if da_empresa and sem_valor(meta.get("indicador")):
            # Enquanto `liv-up/indicadores` não tem os indicadores da empresa, a meta somada ou por média fica "a
            # confirmar": uma pergunta só a quem decide `liv-up`, não uma linha por meta (juntada depois do laço).
            empresa_sem_indicador.append((caminho, mid))
        else:
            conferir_indicador(caminho, meta.get("indicador"), pre, quem)
        tipo = norm(meta.get("tipo") or "chegar_a")
        if tipo not in TIPOS_META:
            falta(caminho, f"{pre}o tipo `{meta.get('tipo')}` não existe (chegar_a, manter ou entrega)", QUEM_MONTOU)
        elif tipo == "chegar a":
            sem_de, sem_de_em = sem_valor(meta.get("de")), sem_valor(meta.get("de_em"))
            if sem_de or sem_de_em:  # uma linha só: valor e mês de hoje são a mesma pergunta
                o_que = "o valor de hoje e o mês dele" if sem_de and sem_de_em else ("o valor de hoje" if sem_de else "o mês do valor de hoje")
                falta(caminho, f"{pre}falta {o_que}", quem)
            for campo, o_que in (("para", "o valor de chegada"), ("prazo", "o prazo")):
                if sem_valor(meta.get(campo)):
                    falta(caminho, f"{pre}falta {o_que}", quem)
        elif tipo == "manter":
            if sem_valor(meta.get("limite")):
                falta(caminho, f"{pre}meta de manter sem o limite", quem)
            if norm(meta.get("sentido") or "") not in SENTIDOS:
                falta(caminho, f"{pre}meta de manter sem dizer se o limite é mínimo ou máximo (no_minimo ou no_maximo)", quem)
            if meta.get("periodo") not in (None, "") and norm(meta.get("periodo")) not in PERIODOS:
                falta(caminho, f"{pre}o período `{meta.get('periodo')}` não existe (mensal, trimestral, semestral ou anual)", QUEM_MONTOU)
        else:
            if sem_valor(meta.get("criterio")):
                falta(caminho, f"{pre}meta de entrega sem o critério de pronto", quem)
            if sem_valor(meta.get("prazo")):
                falta(caminho, f"{pre}falta o prazo", quem)
        conferir_aspiracao(caminho, meta, tipo, pre, quem)
        if meta.get("parciais") and tipo != "chegar a":
            falta(caminho, f"{pre}parciais só valem em meta de chegar a um número", QUEM_MONTOU)
        for campo in ("prazo", "de_em"):
            v = meta.get(campo)
            if not sem_valor(v) and not PRAZO.match(str(v).strip()):
                falta(caminho, f"{pre}o `{campo}` ({v}) não é mês, trimestre, semestre nem ano (2027-03, 2027-T1, 2027-S1, 2027)", QUEM_MONTOU)
        for campo in ("de", "para", "limite", "aspiracao"):
            if sem_aspas(meta.get(campo)):
                falta(caminho, f"{pre}o `{campo}` está sem aspas (o YAML leu {br(meta.get(campo), 6)}): escreva o número como no material, entre aspas (\"1.750\"); sem aspas, o YAML pode ler outro número (1.750 vira 1,75)", QUEM_MONTOU)
        if da_empresa:
            conferir_objetivo(caminho, meta.get("objetivo"), pre, quem, True)
            if norm(meta.get("abre_em") or "") not in ABRE_EM:
                falta(caminho, f"{pre}falta dizer como abre nas diretorias (soma, media ou nao_abre)", quem)
        elif meta.get("compoe"):
            if (objetivos or metas_empresa) and meta["compoe"] not in metas_empresa:
                falta(caminho, f"{pre}diz compor a meta da empresa `{meta['compoe']}`, que não existe", quem)
        elif meta.get("objetivo"):
            conferir_objetivo(caminho, meta.get("objetivo"), pre, quem, False)
        elif objetivos:
            falta(caminho, f"{pre}não diz a que meta ou objetivo da empresa serve", quem)

    def conferir_tabela(caminho, metas, corpo, quem):
        blocos, atual = [], []
        for l in corpo.splitlines():
            if l.strip().startswith("|"):
                atual.append([c.strip() for c in l.strip().strip("|").split("|")])
            elif atual:
                blocos.append(atual)
                atual = []
        if atual:
            blocos.append(atual)
        linhas = []  # (celulas, indice das colunas)
        for bloco in blocos:
            cols = {norm(c): i for i, c in enumerate(bloco[0])}
            for celulas in bloco[1:]:
                linhas.append((celulas, cols))
        ids = {m.get("id") for m in metas}
        for meta in metas:
            mid = meta.get("id")
            if not mid:
                continue
            achada = next(((c, cols) for c, cols in linhas if c and f"`{mid}`" in c[0] or (c and norm(c[0]) == norm(mid))), None)
            if achada is None:
                falta(caminho, f"meta `{mid}` está no cabeçalho e não está na tabela do texto", quem)
                continue
            celulas, cols = achada
            for campo in ("de", "para", "prazo"):
                v = meta.get(campo)
                if v in (None, "") or sem_aspas(v):
                    continue  # sem aspas já sai como achado próprio; comparar daria um erro de tabela que não é
                i = cols.get(campo)
                alvo = celulas[i] if i is not None and i < len(celulas) else " ".join(celulas)
                if not re.search(r"(^| )" + re.escape(norm(v)) + r"( |$)", norm(alvo)):
                    falta(caminho, f"meta `{mid}`: o {campo} da tabela do texto ({alvo}) não bate com o do cabeçalho ({v})", quem)
        for celulas, _ in linhas:
            m = re.search(r"`([a-z0-9-]+)`", celulas[0]) if celulas else None
            if m and m.group(1) not in ids:
                falta(caminho, f"a tabela do texto tem a meta `{m.group(1)}`, que não está no cabeçalho", quem)

    empresa_sem_indicador = []
    for caminho in empresa:
        cab, corpo = validos[caminho]
        metas = lista_de_campos(cab, "metas", lambda *a, **k: None, caminho, "")
        for meta in metas:
            conferir_meta(caminho, meta, "diretoria executiva", True)
        conferir_tabela(caminho, metas, corpo, "diretoria executiva")

    for caminho in diretorias:  # D148: os objetivos da área (antes das metas e dos projetos que apontam para eles)
        cab, _ = validos[caminho]
        quem = f"diretor(a) de {caminho.split('/')[0]}"
        for obj in (cab.get("objetivos") or []) if isinstance(cab.get("objetivos"), list) else []:
            oid = obj.get("id") if isinstance(obj, dict) else None
            if not isinstance(oid, str) or not oid:
                falta(caminho, "objetivo da área sem id", quem)
                continue
            objetivos_area[caminho.split("/")[0]][oid] = obj
            serve = obj.get("serve_a")
            if not isinstance(serve, list) or not serve:
                falta(caminho, f"objetivo `{oid}`: falta dizer a que objetivos da Liv Up (pilares) ele serve (`serve_a`)", quem)
            elif objetivos:
                for pilar in serve:
                    if pilar not in objetivos:
                        falta(caminho, f"objetivo `{oid}`: o pilar `{pilar}` não está entre os objetivos da Liv Up", quem)

    compoe = defaultdict(list)
    limite_chave = {}  # D160: a área (a própria, não a diretoria-pai) -> (caminho, `limite_projetos_chave`)
    for caminho in diretorias:
        cab, corpo = validos[caminho]
        quem = f"diretor(a) de {caminho.split('/')[0]}"
        if "limite_projetos_chave" in cab:
            limite_chave[caminho.split("/")[0]] = (caminho, cab.get("limite_projetos_chave"))
        metas = lista_de_campos(cab, "metas", falta, caminho, quem)
        for meta in metas:
            conferir_meta(caminho, meta, quem, False)
            if meta.get("compoe"):
                compoe[meta["compoe"]].append((caminho, meta))
        conferir_tabela(caminho, metas, corpo, quem)
        datas = datas_no_texto(corpo, ano_estrategia)
        if datas:
            falta(caminho, f"datas no texto ({', '.join(datas[:4])}): data de entrega ou de marco vai para o acompanhamento", QUEM_MONTOU)

    juntar = []
    for caminho, mid in empresa_sem_indicador:
        partes = compoe.get(mid, [])
        if len(partes) == 1:
            c, m = partes[0]
            ind = m.get("indicador")
            dica = f" (`{limpo(ind)}`)" if isinstance(ind, str) and not sem_valor(ind) else ""
            falta(caminho, f"meta `{mid}`: só {c.split('/')[0]} compõe esta meta; aponte para o indicador dela{dica} em vez de \"a confirmar\"", QUEM_MONTOU)
        else:
            juntar.append((caminho, mid))
    if juntar:
        ids = ", ".join(f"`{mid}`" for _, mid in juntar)
        falta(juntar[0][0], f"{len(juntar)} meta(s) da empresa sem documento do indicador ({ids}): quem cria os indicadores da empresa em `liv-up`?", "diretoria executiva")

    junto = "diretoria executiva e diretorias que compõem"
    for mid, (caminho, meta) in metas_empresa.items():
        modo = norm(meta.get("abre_em") or "")
        partes = compoe.get(mid, [])
        if modo in ("soma", "media") and diretorias and not partes:
            falta(caminho, f"meta `{mid}` abre por {modo}, e nenhuma diretoria diz compor essa meta", "diretoria executiva")
            continue
        if modo == "nao abre" and partes:
            falta(caminho, f"meta `{mid}` diz que não abre, e {len(partes)} meta(s) de diretoria dizem compor ela", "diretoria executiva")
        if modo not in ("soma", "media") or not partes:
            continue
        tipo_empresa = norm(meta.get("tipo") or "chegar_a")
        diferentes = [c.split("/")[0] for c, m in partes if norm(m.get("tipo") or "chegar_a") != tipo_empresa]
        if diferentes:
            falta(caminho, f"meta `{mid}`: as partes de {', '.join(diferentes)} têm outro tipo de meta; confira à mão", junto)
            continue
        if tipo_empresa != "chegar a":
            continue  # manter compõe por "todas dentro" e entrega por "todas entregues": não há conta de soma
        nomes = ", ".join(f"{c.split('/')[0]} ({m.get('para')})" for c, m in partes)
        if sem_aspas(meta.get("para")) or any(sem_aspas(m.get("para")) for _, m in partes):
            continue  # o número sem aspas já é achado do documento dele; a conta fica para depois das aspas
        alvo = valor(meta.get("para"))
        como = "somadas" if modo == "soma" else "pela média simples"
        # Parte "a confirmar": a conta segue com as conhecidas e diz quanto falta (item 7 do ensaio da captura).
        abertas = [c.split("/")[0] for c, m in partes if sem_valor(m.get("para"))]
        conhecidas = [(c, m) for c, m in partes if not sem_valor(m.get("para"))]
        vals = [valor(m.get("para")) for _, m in conhecidas]
        if any(v is None for v in vals):
            falta(caminho, f"meta `{mid}`: não consegui ler os números das diretorias ({nomes}); confira à mão", junto)
            continue
        if len({v[1] for v in vals}) > 1 or (alvo and any(v[1] != alvo[1] for v in vals)):
            falta(caminho, f"meta `{mid}`: as metas estão em unidades diferentes ({meta.get('para')}; {nomes}); confira à mão", junto)
            continue
        if abertas:
            if not vals:
                falta(caminho, f"meta `{mid}`: todas as metas das diretorias estão a confirmar ({nomes}); a conta fica para depois", junto)
                continue
            unid = alvo[1] if alvo else vals[0][1]
            soma = sum(v[0] for v in vals)
            nomes_conh = ", ".join(c.split("/")[0] for c, _ in conhecidas)
            if modo == "soma":
                ja = f"as conhecidas ({nomes_conh}) somam {escrever(soma, unid)}"
            else:
                ja = f"as conhecidas ({nomes_conh}) têm média simples {escrever(soma / len(vals), unid)}"
            quem_falta = ", ".join(abertas)
            if alvo is None:
                if not sem_valor(meta.get("para")):
                    falta(caminho, f"meta `{mid}`: não consegui ler o valor de chegada ({meta.get('para')}); {ja}, e {quem_falta} está a confirmar", junto)
                else:
                    falta(caminho, f"meta `{mid}`: o valor de chegada e a parte de {quem_falta} estão a confirmar; {ja}", junto)
                continue
            precisa = alvo[0] - soma if modo == "soma" else alvo[0] * len(partes) - soma
            tol = max(abs(alvo[0]) * 0.001, 1e-9)
            plural = len(abertas) > 1
            if modo == "soma" and abs(precisa) <= tol:
                texto = f"{ja}, que já fecham a meta; {quem_falta} (a confirmar) precisa{'m' if plural else ''} dar zero para não passar"
                para_aberta = "zero, para não passar"
            elif modo == "soma" and precisa * alvo[0] < 0:
                texto = f"{ja}, que já passam da meta em {escrever(abs(precisa), unid)}, com {quem_falta} a confirmar"
                para_aberta = None
            elif modo == "soma":
                texto = f"{ja}; para fechar, {quem_falta} (a confirmar) precisa{'m dar juntas' if plural else ' dar'} {escrever(precisa, unid)}"
                para_aberta = escrever(precisa, unid) + (f", junto com {quem_falta}" if plural else "")
            else:
                cada = precisa / len(abertas)
                acima = " (as conhecidas já levam a média acima da meta)" if cada * alvo[0] < 0 else ""
                if plural:
                    texto = f"{ja}; para a média simples fechar, {quem_falta} (a confirmar) precisam ter, juntas, média {escrever(cada, unid)}{acima} (se a média tem peso, diga o peso)"
                else:
                    texto = f"{ja}; para a média simples fechar, {quem_falta} (a confirmar) precisa dar {escrever(cada, unid)}{acima} (se a média tem peso, diga o peso)"
                para_aberta = escrever(cada, unid) + (" em média, junto com " + quem_falta if plural else "") + ", pela média simples"
            falta(caminho, f"meta `{mid}` ({meta.get('para')}): {texto}", junto)
            if para_aberta:
                # A diretoria aberta vê o número na linha que ela já tem, sem linha a mais.
                for c, m in partes:
                    if not sem_valor(m.get("para")):
                        continue
                    area_ab = c.split("/")[0]
                    alvo_txt = f"meta `{m.get('id')}`: falta o valor de chegada"
                    achados[area_ab] = [(d, (t + f" (para fechar a meta da empresa `{mid}`, precisa dar {para_aberta})") if d == c and t == alvo_txt else t, q)
                                        for d, t, q in achados[area_ab]]
            continue
        total = sum(v[0] for v in vals) if modo == "soma" else sum(v[0] for v in vals) / len(vals)
        if alvo is None:
            falta(caminho, f"meta `{mid}`: o valor de chegada está a confirmar; as metas das diretorias, {como}, dão {escrever(total, vals[0][1])} ({nomes})", junto)
        elif abs(total - alvo[0]) > max(abs(alvo[0]) * 0.001, 1e-9):
            peso = " (se a média tem peso, diga o peso)" if modo == "media" else ""
            falta(caminho, f"meta `{mid}` ({meta.get('para')}): as metas das diretorias, {como}{peso}, dão {escrever(total, alvo[1])} e não fecham ({nomes})", junto)

    def codigo_de(cab):
        v = cab.get("id_acompanhamento")
        return str(v).strip() if v not in (None, "") else ""

    por_codigo = defaultdict(list)
    id_do_projeto = {}
    for caminho in projetos:
        cod = codigo_de(validos[caminho][0])
        id_do_projeto[caminho.removesuffix("/visao-geral")] = cod
        if cod:
            por_codigo[cod].append(caminho)

    lista = "responsável pela lista de códigos"
    chaves = defaultdict(list)  # D160: a diretoria -> [(projeto-chave, metas que move, indicadores da contribuição)]
    areas_conhecidas = {c.split("/")[0] for c in docs} | {c.split("/")[0] for c in existentes} | sem_leitura | {"liv-up"}
    for caminho in projetos:
        cab, corpo = validos[caminho]
        area = caminho.split("/")[0]
        diretor = f"diretor(a) de {dona(area)}"
        dono = cab.get("dono")
        um_dono = isinstance(dono, str) and "@" in dono and "," not in dono and " e " not in dono
        quem = "dono do projeto" if um_dono else diretor  # papel, não e-mail: a lista vai ao diretor
        cod = codigo_de(cab)
        if not cod or norm(cod) in ("a confirmar", "a dar", "codigo a dar"):
            falta(caminho, "projeto sem código do acompanhamento (não vai na proposta sem código)", lista)
        elif not CODIGO.match(cod):
            falta(caminho, f"código `{cod}` fora do formato PRJ-001", lista)
        else:
            if len(por_codigo[cod]) > 1:
                falta(caminho, f"o código `{cod}` também está em {', '.join(c for c in por_codigo[cod] if c != caminho)}", lista)
            if codigos:
                if cod not in codigos:
                    falta(caminho, f"o código `{cod}` não está na lista de códigos", lista)
                else:
                    linha = codigos[cod]
                    if linha.get("_repetido"):
                        falta(caminho, f"o código `{cod}` está com dois nomes de projeto na lista de códigos", lista)
                    nome, titulo = norm(linha.get("nome", "")), norm(cab.get("titulo", ""))
                    if nome and nome not in titulo and titulo not in nome:
                        falta(caminho, f"o nome na lista de códigos é \"{linha.get('nome')}\" e o título aqui é \"{cab.get('titulo')}\": é o mesmo projeto?", lista)
                    if linha.get("dono") and um_dono and not mesmo_dono(linha["dono"], dono):
                        falta(caminho, f"o dono na lista de códigos é {linha['dono']} e aqui é {dono}", diretor)
        if sem_valor(dono):
            falta(caminho, "projeto sem dono", diretor)
        elif not um_dono:
            falta(caminho, f"o dono precisa ser UMA pessoa, pelo e-mail (está: {dono})", diretor)
        # D160: `objetivo` e `objetivos` (o projeto que serve a mais de um) se somam, como no painel.
        obj = cab.get("objetivo")
        objs = cab.get("objetivos")
        if sem_valor(objs):
            objs = []
        elif not isinstance(objs, list):
            falta(caminho, f"`objetivos` é uma lista ([a, b]); está: {objs}", QUEM_MONTOU)
            objs = []
        if objs and any(not isinstance(o, str) for o in objs):
            falta(caminho, f"`objetivos` leva só os ids dos objetivos ([a, b]); está: {objs}", QUEM_MONTOU)
        acusado = obj is not None and not isinstance(obj, str)
        if acusado:
            conferir_objetivo(caminho, obj, "", quem, True)  # "tem de ser UM objetivo", com a dica do `objetivos`
            obj = None
        com_valor = [o for o in [obj, *objs] if isinstance(o, str) and not sem_valor(o)]
        proprios = [o for o in com_valor if norm(o) == norm(PROPRIO)]
        reais = [o for o in com_valor if norm(o) != norm(PROPRIO)]
        if not com_valor and not acusado:
            conferir_objetivo(caminho, None, "", quem, True)
        if proprios and reais:
            falta(caminho, f"`{PROPRIO}` junto de outros objetivos ({', '.join(reais)}): o projeto serve a objetivos ou é só da área", quem)
        for o in reais:
            conferir_objetivo(caminho, o, "", quem, False)
        partes_cam = caminho.split("/")
        if re.match(r"^[a-z0-9-]+/projetos/[^/]+/visao-geral$", caminho):
            if not (area in pai or area in {c.split("/")[0] for c in diretorias} or area in {c.split("/")[0] for c in existentes}
                    or area in sem_leitura):
                falta(caminho, f"a pasta `{area}/` não é diretoria com estratégia, subárea declarada (--subareas) nem área que existe: confira se a subárea existe; se não, o projeto vai para a diretoria", QUEM_MONTOU)
        elif "projetos" in partes_cam[1:-2] and partes_cam[-1] == "visao-geral":
            falta(caminho, f"projeto numa pasta `projetos/` dentro de `geral/` ou de uma frente: ali ele não abre para a empresa; mova para `{area}/projetos/` (ou para a subárea do time, se ela existe)", QUEM_MONTOU)
        elif "projetos" not in partes_cam:
            falta(caminho, f"documento com a tag `projeto` fora de `projetos/`: o projeto mora em `{area}/projetos/<projeto>/visao-geral`", QUEM_MONTOU)
        contrib = lista_de_campos(cab, "contribuicao", falta, caminho, quem)
        # D160: a meta (o resultado-chave) que o projeto move, pelo id.
        mp = cab.get("meta")
        bruto_meta = [mp] if isinstance(mp, str) else mp if isinstance(mp, list) else ([] if mp is None else [mp])
        if any(not isinstance(m, str) for m in bruto_meta):
            falta(caminho, f"`meta` leva o id da meta (ou uma lista de ids), como texto; está: {mp}", QUEM_MONTOU)
        ids_meta = [m for m in bruto_meta if isinstance(m, str) and not sem_valor(m)]
        com_estrategia = {dona(c.split("/")[0]) for c in diretorias}
        for mid in ids_meta:
            if mid not in todas_metas and dona(area) in com_estrategia:
                falta(caminho, f"a meta `{mid}` não está na estratégia de {dona(area)} nem nas outras desta pasta", quem)
        if not contrib and not ids_meta:
            falta(caminho, "falta como saber se funcionou: a meta que o projeto move (`meta`) ou a contribuição (indicador, efeito e até quando)", quem)
        ch = cab.get("chave")
        if ch is not None and not isinstance(ch, bool):
            falta(caminho, f"`chave` é true ou false (está: {ch})", QUEM_MONTOU)
        elif ch is True:
            chaves[area].append((caminho, set(ids_meta), {c.get("indicador") for c in contrib if isinstance(c.get("indicador"), str)}))
        pai_ = cab.get("pai")
        por_cod = {v: k for k, v in id_do_projeto.items() if v}
        if sem_valor(pai_):
            pass
        elif not isinstance(pai_, str):
            falta(caminho, f"`pai` é o caminho da visão geral de um projeto, como texto; está: {pai_}", QUEM_MONTOU)
        elif pai_.strip().endswith(".md") or pai_.strip().startswith("/") or pai_.strip().endswith("/"):
            falta(caminho, f"`pai` ({pai_}): escreva o caminho sem `.md` e sem barra no começo ou no fim (`<area>/projetos/<projeto>/visao-geral`)", QUEM_MONTOU)
        else:
            alvo_pai = por_cod.get(pai_.strip(), limpo(pai_).removesuffix("/visao-geral"))
            if alvo_pai == caminho.removesuffix("/visao-geral"):
                falta(caminho, "o projeto é pai de si mesmo", QUEM_MONTOU)
            elif alvo_pai + "/visao-geral" in validos:
                if not sem_valor(validos[alvo_pai + "/visao-geral"][0].get("pai")):
                    falta(caminho, f"o pai `{alvo_pai}` também tem pai: o subprojeto tem um nível só", quem)
            elif not (existe(alvo_pai + "/visao-geral") or existe(alvo_pai) or nao_vejo(alvo_pai)):
                falta(caminho, f"o pai `{alvo_pai}` não está publicado nem nos rascunhos", quem)
        for c in contrib:
            ind = c.get("indicador")
            conferir_indicador(caminho, ind, "", quem)
            if sem_aspas(c.get("efeito")):
                falta(caminho, f"contribuição em `{ind}`: o efeito está sem aspas ({c['efeito']}): escreva entre aspas, com a unidade", QUEM_MONTOU)
            if sem_valor(c.get("efeito")) or sem_valor(c.get("ate")):
                falta(caminho, f"contribuição em `{ind}` sem efeito ou sem até quando", quem)
        for d in lista_de_campos(cab, "depende_de", falta, caminho, quem):
            alvo = limpo(d.get("projeto") or "").removesuffix("/visao-geral")
            area_alvo = alvo.split("/")[0] if alvo else str(d.get("area") or "")
            marco = "" if sem_valor(d.get("marco")) else str(d.get("marco"))  # "a confirmar" = sem marco
            espera = d.get("espera") or "?"
            if not alvo and not area_alvo:
                falta(caminho, "dependência sem dizer de qual projeto ou área", quem)
                continue
            if not d.get("espera"):
                falta(caminho, f"dependência de `{alvo or area_alvo}` sem dizer o que espera", quem)
            de_quem = f"diretor(a) de {area_alvo}"
            if area_alvo not in areas_conhecidas:
                falta(caminho, f"depende de `{alvo or area_alvo}`, e a área `{area_alvo}` não aparece no LivupOS, nos rascunhos nem nas áreas que quem montou não lê: confira o id", QUEM_MONTOU)
                continue
            cod_marco = MARCO.match(marco).group(1) if MARCO.match(marco) else None
            if not alvo:
                a_confirmar(caminho, f"espera de `{area_alvo}`: {espera}; está combinado?", de_quem, area=area_alvo)
            elif nao_vejo(alvo):
                a_confirmar(caminho, f"diz que depende de `{alvo}` ({espera}); não conferido (quem montou não lê a área); está combinado?", de_quem, area=area_alvo)
            elif alvo + "/visao-geral" in validos:
                lado = trecho_da_secao(validos[alvo + "/visao-geral"][1], "Quem espera algo deste projeto")
                meu = caminho.removesuffix("/visao-geral")
                if meu not in lado and (not cod or cod not in lado):
                    a_confirmar(alvo + "/visao-geral", f"`{meu}` diz que depende deste projeto ({espera}); confirmar e registrar em \"Quem espera algo deste projeto\" com o código {cod if CODIGO.match(cod or '') else 'dele, quando houver'}", de_quem)
            elif existe(alvo + "/visao-geral") or existe(alvo):
                falta(caminho, f"diz que depende de `{alvo}` ({espera}); não conferido: o projeto está publicado e não está na pasta (copie o documento dele para conferir o outro lado)", QUEM_MONTOU)
            elif cod_marco and cod_marco in codigos:
                falta(caminho, f"depende de `{alvo}`, que está na lista de códigos ({cod_marco}) e não tem documento no LivupOS", quem)
                a_confirmar(caminho, f"diz que depende do projeto {cod_marco} ({espera}); está combinado?", de_quem, area=area_alvo)
            else:
                falta(caminho, f"depende do projeto `{alvo}`, que não está publicado nem nos rascunhos (pode estar numa proposta sem decisão, ou não existir)", quem)
                a_confirmar(caminho, f"diz que depende de `{alvo}` ({espera}); esse projeto existe e está combinado?", de_quem, area=area_alvo)
            if marco:
                m = MARCO.match(marco)
                if not m:
                    falta(caminho, f"o marco `{marco}` está fora do formato PRJ-001/M01", quem)
                else:
                    cod_alvo = id_do_projeto.get(alvo) if alvo else None
                    if cod_alvo and CODIGO.match(cod_alvo) and m.group(1) != cod_alvo:
                        falta(caminho, f"o marco `{marco}` não é do projeto `{alvo}` (código {cod_alvo})", quem)
                    if marcos and marco not in marcos:
                        falta(caminho, f"o marco `{marco}` não está na lista de códigos", lista)
        tem = secoes(corpo)
        for s in SECOES_PROJETO:
            if norm(s) not in tem:
                falta(caminho, f"falta a seção \"{s}\"", quem)
        if cab.get("depende_de") and norm("Depende de") not in tem:
            falta(caminho, "falta a seção \"Depende de\"", quem)
        anos = [int(str(c.get("ate"))[:4]) for c in contrib if re.match(r"^\d{4}", str(c.get("ate") or ""))]
        datas = datas_no_texto(corpo, ano_estrategia or (min(anos) if anos else None))
        if datas:
            falta(caminho, f"datas no texto ({', '.join(datas[:4])}): marco e data vão para o acompanhamento, não para o documento", QUEM_MONTOU)

    # D160: projetos-chave demais; meta que nenhum projeto-chave move (só onde a diretoria marcou algum); objetivo
    # com mais de 5 resultados-chave. Informativos, como no painel: o diretor decide.
    for area, lst in sorted(chaves.items()):
        limite = LIMITE_PROJETOS_CHAVE
        if area in limite_chave:
            c_lim, v = limite_chave[area]
            if isinstance(v, int) and not isinstance(v, bool) and v > 0:
                limite = v
            else:
                falta(c_lim, f"`limite_projetos_chave` ({v}) não é um número inteiro positivo: vale o padrão, {LIMITE_PROJETOS_CHAVE}", QUEM_MONTOU)
        if len(lst) > limite:
            falta(f"{area}/projetos", f"{len(lst)} projetos-chave em {area} (o limite é {limite}): escolha os que ficam com a marca (informativo)", f"diretor(a) de {dona(area)}")
    todos_chave = [x for lst in chaves.values() for x in lst]
    for mid, (c_meta, meta) in todas_metas.items():
        area = c_meta.split("/")[0]
        if area == "liv-up" or area not in chaves:  # só onde a própria área marcou algum projeto-chave
            continue
        ind = meta.get("indicador") if isinstance(meta.get("indicador"), str) else None
        if not any(mid in ids or (ind and ind in inds) for _, ids, inds in todos_chave):
            falta(c_meta, f"meta `{mid}`: nenhum projeto-chave a move (informativo)", f"diretor(a) de {dona(area)}")
    por_objetivo = defaultdict(list)
    for mid, (c_meta, meta) in todas_metas.items():
        if isinstance(meta.get("objetivo"), str) and not sem_valor(meta.get("objetivo")):
            por_objetivo[(c_meta, meta["objetivo"])].append(mid)
    for (c_meta, oid), mids in sorted(por_objetivo.items()):
        if len(mids) > LIMITE_RESULTADOS_POR_OBJETIVO:
            falta(c_meta, f"objetivo `{oid}` com {len(mids)} metas (o método pede de 3 a 5): {', '.join(mids)} (informativo)", f"diretor(a) de {dona(c_meta.split('/')[0])}" if not c_meta.startswith("liv-up/") else "diretoria executiva")

    if empresa:
        usados = {validos[c][0].get("objetivo") for c in projetos if isinstance(validos[c][0].get("objetivo"), str)}
        usados |= {o for c in projetos if isinstance(validos[c][0].get("objetivos"), list)
                   for o in validos[c][0]["objetivos"] if isinstance(o, str)}
        usados.discard(PROPRIO)
        usados |= {m.get("objetivo") for _, m in metas_empresa.values() if isinstance(m.get("objetivo"), str)}
        for oid in objetivos:
            if oid not in usados:
                falta(empresa[0], f"objetivo `{oid}` sem nenhuma meta nem projeto (informativo)", "diretoria executiva")

    for caminho, (cab, corpo) in validos.items():
        base = Path(caminho).parent
        for m in re.finditer(r"(!?)\[[^\]]*\]\(([^)\s]+)\)", corpo):
            if m.group(1):
                continue  # imagem
            alvo = m.group(2).split("#")[0]
            if not alvo or re.match(r"^[a-z]+:", alvo):
                continue  # http, mailto
            if not alvo.endswith(".md"):
                falta(caminho, f"link `{alvo}` fora do formato (relativo, com .md)", QUEM_MONTOU)
                continue
            partes = []
            for parte in (base / alvo).as_posix().split("/"):
                if parte == "..":
                    if partes:
                        partes.pop()
                elif parte not in ("", "."):
                    partes.append(parte)
            destino = "/".join(partes).removesuffix(".md")
            if nao_vejo(destino):
                falta(caminho, f"link para `{destino}` não conferido (quem montou não lê a área): só fica se o documento estiver publicado", QUEM_MONTOU)
            elif not existe(destino):
                falta(caminho, f"link para `{destino}`, que não está publicado nem nesta leva: troque por texto (nome e área)", QUEM_MONTOU)

    total = sum(len(v) for v in achados.values())
    print(f"# O que falta ({total})\n")
    if not empresa:
        print("> Sem a estratégia da empresa na pasta: objetivo e `compoe` não foram conferidos.\n")
    if aviso_codigos:
        print(aviso_codigos)
    elif not codigos:
        print("> Sem a lista de códigos: código, nome, dono e marco dos projetos não foram conferidos contra ela.\n")
    if not total:
        print("Nada falta nos documentos conferidos.")
    for area in sorted(achados):
        print(f"## {area}\n")
        for caminho, texto, quem in achados[area]:
            fim = "" if texto.endswith(("?", ".")) else "."
            print(f"- `{caminho}`: {texto}{fim} Responde: {quem}.")
        print()
    n_conf = sum(len(v) for v in confirmar.values())
    if n_conf:
        print(f"# Para confirmar com quem se espera ({n_conf})\n")
        print("> O que um projeto diz esperar de outro projeto ou de uma área. Não conta como falta: \"Quem espera algo deste")
        print("> projeto\" só se preenche na conferência com o diretor. Vai ao arquivo de quem se espera, menos o que esbarra")
        print("> numa decisão sigilosa (fica só na conversa).\n")
        for area in sorted(confirmar):
            print(f"## {area}\n")
            for caminho, texto, quem in confirmar[area]:
                fim = "" if texto.endswith(("?", ".")) else "."
                print(f"- `{caminho}`: {texto}{fim} Responde: {quem}.")
            print()


if __name__ == "__main__":
    main()
