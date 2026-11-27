# Estratégia do ano: captura e conferência (molde v1, dezembro de 2026)

A estratégia de 2027 sai do retreat da liderança. Esta referência tem duas partes, feitas por pessoas diferentes:

- **Captura** (semana de 07/12): alguém do time central transforma o material do retreat em rascunhos, confere e
  manda cada diretoria receber a dela. Ninguém publica nada nessa parte.
- **Conferência** (14 a 18/12, etapa de estratégia da sessão do diretor): o owner da área confere os rascunhos da diretoria
  dele com a lista do que falta, responde o que dá e publica.

A estratégia da empresa (`liv-up/estrategia/2027`) segue o mesmo caminho: a captura monta, e quem decide a área
`liv-up` confere e publica rodando a etapa de estratégia em `liv-up`.

O molde é a versão 1, para usar até a revisão de fevereiro de 2027. Nada aqui é regra nova da plataforma.

## 1. Onde cada coisa mora

| O quê | Caminho |
|---|---|
| Objetivos e metas da Liv Up | `liv-up/estrategia/2027` |
| Metas da diretoria, ligadas às da empresa | `<area>/estrategia/2027` |
| Um projeto: tese, objetivo, dono, contribuição, dependências | `<area ou subárea>/projetos/<projeto>/visao-geral` |
| Datas, marcos, situação, atualizações | a ferramenta de acompanhamento (fora do LivupOS) |
| O valor medido de cada indicador | a fonte que o documento do indicador aponta |

- O nome da pasta do projeto vem do nome do projeto, em minúsculas, sem acento, com hífen. Não leva o código nem o ano:
  o projeto muda de nome e atravessa o ano, e o código fica só no cabeçalho.
- O projeto mora na área da diretoria dona, ou na subárea dela (abaixo). Projeto de duas diretorias tem uma dona; a
  outra aparece em "Depende de" ou em "Quem espera algo deste projeto".
- **Projeto de um time:** se o time é uma subárea que existe no LivupOS, o projeto mora em
  `<subárea>/projetos/<projeto>/` (o id da subárea abre o caminho: `operacoes-producao/projetos/...`, e não
  `operacoes/geral/producao/projetos/...`, que é uma frente: `projetos` é nome reservado dentro de `geral/` e ali não
  abre para a empresa). Se a subárea não existe, mora em `<diretoria>/projetos/`,
  com o dono do time em `dono`. Nunca numa pasta `projetos/` dentro de `geral/` ou de uma frente: ela não abre para a empresa (e `projetos` é nome reservado dentro de `geral/`). Em
  subárea sigilosa que já existe, o projeto mora na diretoria-pai, porque a subárea não abre.
- **A subárea não é diretoria:** não tem `estrategia/2027` nem arquivo próprio. Os projetos dela entram com os da
  diretoria-pai: no arquivo da diretoria, na lista do que falta dela e na conferência do diretor, que publica e decide
  também na subárea (owner e substituto da área-pai publicam nas subáreas). A proposta é por área: a subárea tem a
  dela, e a justificativa diz que faz parte da estratégia da diretoria-pai. A subárea que só recebe projeto ganha só a
  visão geral de `projetos/`.
- **Pedido de subárea:** a skill não cria subárea. Na captura, o material que diz que o diretor quer uma subárea vira
  pergunta no arquivo da diretoria, e o projeto fica na diretoria. Na etapa de estratégia, se o diretor pede, siga
  `references/subareas.md` (seções 2 e 3) e entregue o arquivo `areas-de-dentro-<area>-AAAA-MM-DD.md` no fechamento (E3);
  quando a subárea for criada, o projeto muda de lugar com ela.
- `estrategia/` e `projetos/` são lidas pela empresa toda, mesmo numa área fechada. Uma meta ou um projeto que não pode
  ser lido pela empresa não entra no documento aberto. Vira pergunta ao diretor, e só com o sim dele vai para um
  documento à parte com `fora_da_empresa: true` (`references/fora-da-empresa.md`). **Com pessoa identificável**
  (corte de vaga ou desligamento em que dá para saber quem é, caso de pessoa), vale a regra da seção 3 (C2), não esta: o projeto fica fora de todo
  arquivo, nem em documento fechado.
- **Visão geral das pastas reservadas.** A área que recebe rascunho e ainda não tem a pasta ganha a visão geral de
  texto fixo dela (`references/forma-comum.md`, seção 4), junto com o primeiro documento: a de `estrategia/` sempre
  (menos na subárea, que só recebe projeto), a de `projetos/` só se a área tem projeto. Em área que quem roda não lê, as visões gerais vão no arquivo da diretoria,
  marcadas "só se a área ainda não tiver". `liv-up` tem texto fixo próprio (mesma seção).

## 2. O molde v1

Os três documentos usam `tipo: referencia` e uma tag, não um tipo próprio. Os campos do cabeçalho abaixo são os únicos
que esta parte acrescenta aos de `references/moldes.md` (a plataforma aceita todos eles em `referencia`, conferido em
23/11/2026). Fora eles, nada de campo novo: nunca `camada`, `autoridade`, `status`, `owner`, `owner_id` nem
`revisar_em`, que são do sistema e são recusados (o dono do projeto vai em `dono`), e nada de data de marco nem de
situação.

### Estratégia da empresa: `liv-up/estrategia/2027`

```markdown
---
tipo: referencia
titulo: "Estratégia da Liv Up 2027"
resumo: "Os objetivos da Liv Up para 2027 e as metas da empresa, com o indicador, o valor de hoje e o de chegada."
tags: [estrategia]
objetivos:
  - id: reter-quem-ja-comprou
    nome: Reter quem já comprou
metas:
  - id: recompra-90-dias-2027
    objetivo: reter-quem-ja-comprou
    indicador: liv-up/indicadores/recompra-90-dias   # quando existir; até lá, a regra abaixo
    de: "31%"
    de_em: 2026-10
    para: "36%"
    prazo: 2027-12
    abre_em: media
---

# Estratégia da Liv Up 2027

> Fonte: <material do retreat, com data>.

## Objetivos

### Reter quem já comprou
<o porquê, numa ou duas frases, como saiu do retreat>

## Metas

| Meta | Indicador | De | Para | Prazo | Como abre |
|---|---|---|---|---|---|
| `recompra-90-dias-2027` | [Recompra em 90 dias](../indicadores/recompra-90-dias.md) | 31% (out/2026) | 36% | 2027-12 | média das diretorias |

## Em aberto
- <o que falta, com quem responde; a data entra na conferência com o diretor>
```

- `id` do objetivo e da meta: minúsculas, sem acento, com hífen. A meta leva o ano no id. Uma vez publicado, o id não
  muda, porque projetos e metas das diretorias apontam para ele.
- `de` é o valor de hoje e `de_em` é o mês desse valor (AAAA-MM). `para` é o valor de chegada e `prazo` é quando:
  mês (`2027-12`), trimestre (`2027-T1`), semestre (`2027-S1`) ou ano (`2027`). O molde acima é de uma meta
  `chegar_a`; os outros tipos estão em "Metas com tipo", abaixo. Os valores de `de`, `para` e `efeito` vão **sempre** entre aspas, com a unidade: `"R$ 111 mi"`, `"36%"`,
  `"4,2 dias"`, e também o número sem unidade: `"1.750"`. Sem aspas, o YAML lê `1.750` como 1,75, e a conta das metas
  sai errada no painel e na conferência, às vezes sem aviso. Ao alterar um documento, não tire as aspas. O que o material não
  dá fica `"a confirmar"` (vale também para `objetivo` e `indicador`, aqui e na contribuição do projeto), e a
  conferência aponta.
- `indicador` é o caminho do documento do indicador. Em área que quem roda não lê, escreva o caminho provável e passe
  a área em `--areas-sem-leitura`: a conferência diz "não conferido", não "não existe".
- **Indicador da meta da empresa, enquanto `liv-up/indicadores` não tem o dela** (o molde acima mostra o caminho de
  quando ele existir). A meta que uma diretoria carrega sozinha aponta para o indicador dessa diretoria
  (`growth/indicadores/recompra-90-dias`), e a tabela leva o link dele. A meta somada ou por média de
  mais de uma diretoria, e a que não abre (`nao_abre`) sem indicador, fica `indicador: "a confirmar"`, com **uma** pergunta só a quem decide `liv-up`: "quem cria os
  indicadores da empresa?". Não é uma linha por meta; a conferência junta as metas numa linha. Não invente caminho em
  `liv-up/indicadores`.
- **Valor de hoje da meta que abre nas diretorias:** é a soma (`soma`) ou a média (`media`) dos `de` das diretorias,
  quando todas têm documento do indicador medido no mesmo mês (esse é o `de_em`). Se o material da empresa dá o
  número e ele bate com essa conta, use o número e o mês, mesmo que uma das partes seja de área que quem roda não lê:
  o "não conferido" dessa parte vai só para o "Em aberto". Se a conta não dá para fazer, ou os meses divergem,
  `"a confirmar"`, com os valores e os meses na lista do que falta.
- **Valor aproximado** ("~6%", "cerca de 1.100"): escreva como o material dá, entre aspas, e ponha no "Em aberto"
  para confirmar o número e o mês. O número de hoje que o material dá
  para uma diretoria só não vale para a empresa.
- `abre_em` diz como a meta se reparte nas diretorias: `soma` (as metas das diretorias somam a da empresa), `media`
  (a média simples delas dá a da empresa) ou `nao_abre` (nenhuma diretoria tem uma parte dela). Meta que uma
  diretoria carrega sozinha é `soma`, com uma meta compondo.
- O `id` da meta da diretoria é o nome do indicador, a área e o ano (`recompra-90-dias-growth-2027`), para não repetir
  o da empresa. Se o nome do indicador já tem a área, não repita: `receita-varejo-2027`, não
  `receita-varejo-varejo-2027`.
- Se o material não liga uma meta da empresa a um objetivo, ligue pelo nome só quando não há dúvida (receita em
  "Crescer com margem"), e ponha no "Em aberto" para confirmar. Se há dúvida, `"a confirmar"`.
- A tabela do texto repete o cabeçalho, para quem lê no Atlas. Escreva a tabela a partir do cabeçalho, na mesma
  versão. O cabeçalho é a fonte: se os dois divergem, a conferência aponta.

### Estratégia da diretoria: `<area>/estrategia/2027`

Mesmo formato, sem os objetivos da empresa; pode ter **objetivos da área**, cada um com `serve_a` (abaixo). Título
"Estratégia de `<Área>` 2027". Cada meta traz `compoe: <id da meta da
empresa>` (um id ou uma lista) quando é parte dela, e `objetivo: <id do objetivo>` (da área ou da empresa) para dizer a
que objetivo serve. A meta própria da diretoria (que não compõe nenhuma meta da empresa) leva só o `objetivo`; a que
compõe uma meta da empresa e é resultado-chave de um objetivo da área leva os dois. Na tabela, a coluna "Como abre" vira "Compõe": o id da
meta da empresa ou, na meta própria, "própria: `<nome do objetivo>`". Depois da
tabela, uma seção "Por que estas metas" com as escolhas que o material explica, e "Em aberto". Data de entrega ou de
marco também não entra no texto da estratégia: vai para o acompanhamento. O documento da diretoria traz só os números
dela. Se alguma meta compõe uma da empresa, a tabela é seguida da frase fixa "O fechamento com as metas da Liv Up está
na estratégia da Liv Up.", tenha a soma fechado ou não: a conta entre diretorias, e o que não fecha, ficam só no
documento da empresa, e assim ninguém reabre o da diretoria por causa dela. O diretor fica sabendo pela lista do que
falta dele, que leva a linha "a soma das diretorias não fecha a meta `<nome>` da Liv Up", sem os números das outras
áreas. Metas e o fechamento entre diretorias são
abertos para a empresa por desenho; a regra de "número comercial de outra área" de `fora-da-empresa.md` vale para os
números das outras áreas, que ficam no documento da empresa.

### O modelo: objetivo, resultado-chave, projeto e projeto-chave (D160)

A estratégia segue o modelo de OKR que a plataforma usa desde 26/11/2026 (D160):

- o **objetivo** é aonde a área quer chegar;
- o **resultado-chave** é a meta do objetivo (`metas`), com indicador, o valor comprometido e, se houver, a
  aspiração;
- o **projeto** é a iniciativa que move um ou mais resultados-chave: aponta a meta pelo id (`meta`) e, se quiser, o
  efeito num indicador (`contribuicao`);
- o **projeto-chave** é uma marca (`chave: true`) nos projetos que a área leva ao retreat como projetos-chave. Não é
  um nível acima dos outros projetos. O que fica abaixo de um projeto-chave é o subprojeto (`pai`).

A árvore que a liderança usa: cada objetivo tem pelo menos um resultado-chave (com indicador) e cada resultado-chave
tem pelo menos um projeto-chave que o move.

Nos documentos das áreas, o KPI do projeto quase sempre repete, pelo nome, um KPI do objetivo. Escreva no projeto o
id dessa meta (`meta`). Não crie meta dentro do projeto.

- O número do projeto não substitui o da meta. Se ele diverge do número da meta, vai como `efeito` na
  `contribuicao`, e a divergência vai ao diretor. Nunca troque o `para` da meta por ele.
- Se o KPI que o projeto cita não é meta de nenhum objetivo, pergunte ao diretor se ele vira resultado-chave do
  objetivo ou se fica só como contribuição num indicador.

**Quem é projeto-chave (27/11/2026, decisão da liderança):** tudo o que a área leva ao retreat como projeto-chave é
projeto-chave. É o retreat que corta a lista, não a carga.

- Marque `chave: true` em todo projeto que a tabela-resumo do material (o apêndice A2, coluna "Projetos-chave") lista.
  Isso vale mesmo quando a coluna traz quase todos os projetos da área.
- Projeto que só aparece no texto (seção 4) e não está na coluna da A2 não leva a marca. É o caso de "aposta",
  "outros projetos com potencial" e "oportunidades", quando a área separa esses da lista.
- A prioridade que o material dá ("top 3", "essencial", alta, média, baixa) não decide a marca. Ela vai no texto do
  projeto e no resumo ao diretor, para a conversa do corte no retreat.
- Um item da coluna que é etapa de outro projeto ("fluxo X, etapa do projeto 2") não vira projeto-chave. Siga a regra
  do `pai`, abaixo: etapa é marco; subprojeto com dono e KPI próprios é projeto com `pai`.
- Sem a A2, ou com a coluna vazia ou só com o exemplo do modelo, pergunte ao diretor: "todos os projetos da seção 4
  vão ao retreat como projetos-chave? Se não, quais?". Não marque nada antes da resposta, e não escolha por ele.
- **Limite (D166, 27/11/2026):** não há limite padrão de projetos-chave por área. Não escreva
  `limite_projetos_chave` por conta própria. Ele só entra se o diretor (ou a liderança, depois do retreat) quiser um
  teto para a área: aí vai na estratégia do ano da área, e o painel avisa quando a área passa dele.
- Escreva exatamente `chave: true` (não `sim` nem `yes`, nem `"true"` entre aspas: a plataforma só reconhece o
  booleano `true`, e com aspas o documento publica sem contar como projeto-chave).

### Metas com tipo e objetivos da área (D148)

Nem toda meta é chegar a um número. Cada item de `metas` (da empresa e das áreas) tem um `tipo`; sem `tipo`, é
`chegar_a` (o molde acima). A conferência (`scripts/conferir_estrategia.py`) confere os três.

```yaml
metas:
  - id: receita-varejo-2027              # chegar_a: de, de_em, para, prazo
    tipo: chegar_a
    compoe: receita-2027
    indicador: varejo/indicadores/sell-in
    de: "R$ 60 mi"
    de_em: 2026-10
    para: "+20%"                          # aceita o relativo: "+20%" sobre o de, "+3 p.p." num de em %
    aspiracao: "+30%"                     # opcional (D160): o alvo ambicioso, além do para (o comprometido)
    prazo: 2027-12
    parciais:                             # opcional, só em chegar_a: o caminho até o para
      - { ate: 2027-S1, valor: "40%" }    # na unidade da meta, ou "%" do caminho de de a para
  - id: ruptura-varejo-2027              # manter: limite, sentido, periodo (sem de)
    tipo: manter
    objetivo: varejo-em-novas-redes
    indicador: varejo/indicadores/ruptura
    limite: "3%"
    sentido: no_maximo                    # no_minimo | no_maximo
    periodo: mensal                       # mensal (padrão) | trimestral | semestral | anual
  - id: rede-nova-varejo-2027            # entrega: critério de pronto e prazo, sim ou não na data
    tipo: entrega
    objetivo: varejo-em-novas-redes
    criterio: "primeira rede nova com pedido faturado"
    prazo: 2027-S1
    dono: dono.exemplo@livup.com.br       # opcional, em qualquer tipo: quem registra o realizado
objetivos:                                # só na estratégia de uma área: objetivos dela
  - id: varejo-em-novas-redes
    nome: Entrar em novas redes
    serve_a: [crescer]                    # os ids dos objetivos de liv-up/estrategia/<ano> (os pilares)
```

- **Escolha do tipo pelo que o material diz:** número a atingir até uma data é `chegar_a`; um nível que não pode
  passar (ou cair) durante o ano é `manter` ("ruptura abaixo de 3% todo mês"); algo que fica pronto ou não numa data é
  `entrega` ("abrir a primeira rede nova até junho"). Não se chama "marco": marco é a etapa de um projeto. Na dúvida
  entre dois, pergunte ao diretor com as duas formas escritas.
- Os valores de `limite` e de `aspiracao` vão entre aspas, com a unidade, como `de` e `para`.
- **Comprometido e aspiração (D160):** quando o material traz dois números para a mesma meta ("budget e ambição",
  "mínimo e alvo", "conservador e otimista", "budget e cenário otimista"), o comprometido vai no `para` (ou no
  `limite`) e o ambicioso em `aspiracao`. O número ambicioso que só aparece no texto de um projeto também é da meta:
  leve-o para a `aspiracao` da meta que o projeto move, e não deixe só no `efeito` da contribuição.
  - Na meta de manter um nível, a aspiração é um nível melhor que o limite, no mesmo sentido.
  - Na entrega, não há aspiração.
  - Aspiração aquém do comprometido, ou aspiração na entrega, é falta (conta na lista).
  - Com um número só, não há aspiração: não invente.
- **Quantos resultados-chave por objetivo:** de 3 a 5. Com mais de 5 metas de uma área no mesmo objetivo, a
  conferência avisa, como informativo. É o diretor quem decide se corta.
- **Composição:** `chegar_a` compõe por soma ou média, como antes; `manter` compõe por "todas dentro" e `entrega` por
  "todas entregues", sem conta. As partes de uma meta da empresa têm o mesmo tipo dela.
- **Objetivo da área:** a meta ou o projeto da área pode apontar um objetivo da área em `objetivo`; o projeto conta
  para ele e para cada pilar de `serve_a`. Objetivo da área sem `serve_a` vira pergunta ao diretor.
- **Mudar** `tipo`, `limite`, `sentido`, `periodo`, `criterio`, `parciais` ou `aspiracao` de uma meta publicada pede uma entrada nova
  em `revisoes`, como `de`, `para` e `prazo` (D146): na conferência, a skill nunca troca esses campos em silêncio.
- **Na tabela do texto,** a coluna do valor diz o que a meta é: "de X para Y" (`chegar_a`), "no máximo 3% todo mês"
  (`manter`), "entrega: <critério>" (`entrega`).

### Projeto: `<area ou subárea>/projetos/<projeto>/visao-geral`

```markdown
---
tipo: referencia
titulo: "Régua de retenção"
resumo: "Régua que fala com o cliente novo no dia 7, 21 e 40 para ele fazer o segundo pedido; serve à retenção."
tags: [projeto]
id_acompanhamento: PRJ-016
objetivo: reter-quem-ja-comprou
meta: recompra-90-dias-growth-2027
chave: true
dono: dono.exemplo@livup.com.br
contribuicao:
  - indicador: growth/indicadores/recompra-90-dias
    efeito: "+3 p.p."
    ate: 2027-12
depende_de:
  - projeto: tech/projetos/base-de-recompra
    espera: Tabela diária por cliente com a data do último pedido
    marco: PRJ-015/M02
---

# Régua de retenção

> Fonte: <material do retreat, com data>.

## Tese
<por que o projeto existe, em 3 a 5 frases>

## Como saber se funcionou
<o indicador (link) e o efeito esperado; o "até quando" fica só no `ate` do cabeçalho. Se o indicador não existe,
diga e aponte quem cria>

## Fora do escopo
<o que ficou de fora, com a data e onde foi decidido>

## Riscos
<os que o material ou o dono apontam>

## Depende de
- [Base de recompra](../../../tech/projetos/base-de-recompra/visao-geral.md): a tabela diária por cliente (marco
  PRJ-015/M02).

## Quem espera algo deste projeto
- <na captura, sempre a frase "Quem depende deste projeto entra aqui quando a diretoria dona confirma."; na conferência, as linhas confirmadas entram no lugar dela>

## Em aberto
- <o que falta, com quem responde; a data entra na conferência com o diretor>
```

- **"Em aberto"** sai do documento quando não há nada em aberto.
- **`efeito` da contribuição** é texto livre, sempre entre aspas e com a unidade, pelo mesmo motivo das metas:
  `"+3 p.p."`, `"de 90 para 45 dias"`, `"60%"`. Escreva como o material diz.
- **Contribuição cujo indicador não existe:** `indicador: "a confirmar"`; o "Como saber se funcionou" diz o que medir,
  e a lista do que falta diz quem cria o indicador.
- **Obrigatórios:** `id_acompanhamento`, `objetivo`, `dono` e o que o projeto move: `meta` (o id do resultado-chave,
  ou uma lista) ou `contribuicao`. Os dois juntos é o melhor. `depende_de` só quando houver.
- **`meta`** aponta a meta da estratégia do ano pelo id (da área ou da empresa). Meta que não está nos rascunhos nem na
  estratégia da área é falta.
- **`chave: true`** só no projeto-chave (seção "O modelo", acima). Sem o campo, o projeto não é chave: não escreva
  `chave: false` em todos.
- **`objetivos: [a, b]`** é para o projeto que serve a mais de um objetivo. Pode ficar sem o `objetivo` ou junto
  dele, e os dois se somam. `proprio-da-area` não entra na lista.
- **`pai`** é para o subprojeto: o caminho da visão geral do projeto de que ele é parte, sem `.md` e sem barra no
  começo ou no fim (`growth/projetos/regua/visao-geral`; o código do projeto, `PRJ-016`, também vale). É um nível só, então o pai
  não tem pai. Etapa, onda ou fase não é subprojeto: vai como marco na lista do acompanhamento. Subprojeto que o
  material lista sem dono, código nem KPI próprio também não vira projeto: entra no texto do projeto, em "Tese" ou
  "Fora do escopo".
  `condutor` (quem toca no dia a dia, se não é o dono) e `patrocinador` (a diretoria que cobra) são opcionais.
- **Projeto com código e sem dono ou sem objetivo vai na proposta,** com `"a confirmar"` no campo e a linha na lista
  do diretor. Só o projeto sem código fica fora da proposta.
- **Projeto que é só da área, sem objetivo da empresa, de propósito** (comum em subárea): `objetivo: proprio-da-area`.
  Só com o material dizendo isso com todas as letras ("projeto interno do time, não ligado aos objetivos da
  empresa") ou com a resposta explícita do diretor; nunca por chute. Na coluna de objetivo de uma planilha, vazio,
  traço, "N/A", "interno" ou o nome da área é silêncio, não "só da área": fica `"a confirmar"`. O `proprio-da-area`
  que só a planilha diz entra, como todo objetivo que só a planilha dá, no "Em aberto" para o diretor confirmar. Se o material não diz o objetivo, o campo fica `"a confirmar"` e a pergunta ao diretor
  dá as duas saídas ("serve a qual objetivo da Liv Up, ou é só da área?"). Projeto `proprio-da-area` não entra no que
  falta por falta de objetivo; ainda precisa de dono, código e o que move (a `meta` ou a contribuição num indicador da
  própria área).
- **`dono` é UMA pessoa, pelo e-mail.** Ele e o `condutor` são a única exceção à troca de nome por papel desta skill:
  o projeto precisa de quem responde por ele. Quem toca o projeto, decidido no retreat, é dado do projeto (`condutor`), não mudança de
  lotação. O resto do texto segue a regra (papel, não nome).
- **`depende_de`:** `projeto` é o caminho da pasta do projeto do qual este depende. Se a dependência é de uma área sem
  projeto, use `area: <id>`. `espera` diz o que este projeto espera dela, e `marco` o código do marco. A data fica no
  acompanhamento.
- **"Termos deste projeto"** entra antes de "Fora do escopo" só quando o projeto usa um termo do glossário com outro
  sentido. Escreva o sentido do projeto e ponha o link do oficial.
- **Link** só para documento publicado ou que vai na mesma chamada, no formato relativo com `.md` de
  `references/moldes.md`. Projeto ou indicador de outra área que ainda não está publicado entra como texto: o nome e a
  área ("Base de recompra, de Tech"). A conferência aponta link fora disso.
- **"Quem espera algo deste projeto"** é o outro lado de `depende_de`. A captura escreve só a frase "Quem depende deste projeto entra aqui quando a diretoria dona confirma." Na conferência,
  o diretor da área dona confirma cada dependência que outra diretoria declarou e ela entra aí, uma linha por
  projeto, começando pelo código: "- PRJ-014, Régua de retenção (Growth): a tabela diária por cliente". É pelo
  código que a conferência acha o outro lado.
- **Datas não entram no texto do projeto:** marco, data de entrega, "até março", "no 2º trimestre" vão para a lista do
  acompanhamento. Podem ficar: o `ate` da contribuição, a linha `> Fonte:`, a data da decisão em "Fora do escopo" e a
  data de uma fonte citada (a ata de 01/12/2026, por exemplo).

### Código dos projetos e dos marcos

- O código do projeto é `PRJ-001`, `PRJ-002`… É uma sequência única da empresa e nunca é reaproveitado. Não leva
  área nem ano.
- O código do marco é `PRJ-001/M01`, `PRJ-001/M02`…, numerado dentro do projeto.
- Quem dá o código é a responsável pela lista de códigos do acompanhamento. A skill **nunca inventa código**.
- **A lista vence.** Código do material que diverge da lista vai para o arquivo do acompanhamento. Código que, na
  lista, é de outro projeto não vale: o projeto fica sem código.
- **Projeto sem código não vai na proposta:** o rascunho fica no arquivo da diretoria, conferido como os outros, e o
  projeto entra na lista "pedir código". O diretor publica quando o código existir.

## 3. Captura (time central, semana de 07/12)

**Quem roda:** alguém do time central, que não precisa ser owner de nenhuma área. Das regras do `SKILL.md`, não se
aplicam aqui a 1 (só owner; a proibição das ferramentas de admin continua) e a 3 (publicar com ok), porque a captura
**não publica nada**, nem a 11, porque a captura
não monta a forma da área (só traz as visões gerais das pastas reservadas, seção 1). As outras valem: não manda
mensagem, cita a fonte, não preenche lacuna com suposição, corta o sensível, pergunta só o que muda o texto (sem a regra de uma pergunta por mensagem: a captura tem uma parada só), diz o
efeito antes de enviar e não chama ferramenta de admin. A regra 6 vale assim: sistema citado vira link quando o
documento dele existe no que você lê; se não, vai o nome em texto. A captura não cria documento de sistema da área
(isso é da carga da área).

**Fonte:** o material do retreat é a fonte citada nos documentos da estratégia (na linha `> Fonte:`), mesmo que
não esteja aberto para toda a área; a regra 4 do `SKILL.md` vale para o resto.

**Entrada:** o material do retreat como saiu (slides, documento, planilha, ata) e a lista de códigos. Sem a lista de
códigos, siga e ponha todos os projetos em "pedir código".

Para as propostas chegarem aos diretores, quem roda não pode ser admin do LivupOS nem owner ou substituto das
diretorias; se for, a entrega é por arquivo (C1), e isso basta.

### C1. Para onde cada coisa pode subir

1. `contexto_liv_up_minhas_permissoes`. Para cada área do material (`liv-up`, cada diretoria e cada subárea que
   recebe projeto):
   - **`propor: true` e `publicar_direto: false`:** sobe como proposta. Nada fica no ar; quem decide a área vê na lista
     de pendências.
   - **`publicar_direto: true`** (quem roda é owner, substituto ou admin do LivupOS): **não chame
     `propor_mudanca` nessa área**, porque a chamada publicaria na hora, sem o diretor ver. Os rascunhos dessa área
     ficam no arquivo da diretoria, e o diretor publica na sessão dele. Diga isso na parada C.
   - **Se a resposta traz `admin_livupos`** (quem roda é admin do LivupOS), nenhuma área vai por proposta, qualquer
     que seja a marca de cada uma: admin publica direto em todas. Tudo vai nos arquivos das diretorias, e essa é a
     entrega aceita.
   - **sem `propor` ou sem `ler`:** os rascunhos ficam no arquivo da diretoria, e o diretor confere e publica na
     sessão dele. Não sugira pedir acesso: o arquivo basta.
2. `contexto_liv_up_listar` em `liv-up/estrategia`, `liv-up/indicadores` e, em cada área que você lê,
   `<area>/estrategia`, `<area>/projetos` e `<area>/indicadores`, e `<subárea>/projetos` e `<subárea>/indicadores` das
   subáreas das diretorias do material. Guarde os caminhos que existem: a conferência usa.
   Se `liv-up/estrategia/2027` já está publicado, leia: os objetivos e as metas de lá valem sobre o rascunho. Leia
   também o documento de cada indicador que o material cita, nas áreas que você lê: o valor medido e o mês dele
   servem para o `de` e o `de_em` (seção C2).
3. O id de cada área sai do `listar` da raiz ou de `minhas_permissoes` (os dois valem como confirmados). Área que
   não aparece em nenhum dos dois: use o nome que o material dá, em minúsculas e com hífen, e diga no arquivo dela que
   o id é a confirmar.
4. Meça o material de cada diretoria e escolha o caminho, sequência ou paralelo (a régua está na C2). Diga a quem roda,
   com a frase de `references/conducao.md`, "Captura".

### C2. Montar os rascunhos

Monte, no molde da seção 2, `liv-up/estrategia/2027`, `<area>/estrategia/2027` de cada diretoria e um
`<area>/projetos/<projeto>/visao-geral` por projeto. Com material grande, numa conversa só, a conversa pode encher
antes da leitura cruzada, que é de onde vêm os achados mais úteis. Por isso o trabalho se divide em três passos, e o
do meio segue o caminho que a régua (abaixo) escolhe:

1. **Você, antes (a conversa principal).** Faça a C1 inteira: as ferramentas do LivupOS só são chamadas por você
   (fora o envio no caminho em paralelo, parada C). Além do que a C1 lista, leia o documento de cada indicador das
   áreas com material que você lê, e busque a lista oficial do que não abre para a empresa
   (`references/fora-da-empresa.md`, "Categorias"). Separe o material: o que é da empresa toda (o documento de
   objetivos, a ata, a planilha consolidada, a lista de códigos, e todo documento datado depois da ata ou vindo da
   diretoria executiva, mesmo que esteja no material de uma diretoria: uma busca rápida por "meta", "decid", "revis"
   e por datas depois da ata ajuda a achar) e o que é de cada diretoria. **Diretoria é a que tem meta ou projeto em
   qualquer material**, inclusive só na planilha. Subárea não é diretoria: os projetos dela vão com os da
   diretoria-pai (seção 1). Leia o material da empresa, e monte você o rascunho de
   `liv-up/estrategia/2027`: as diretorias apontam para os ids dele. O `de` e o `de_em` de uma meta da empresa entram
   já aqui quando as leituras da C1 dão o número (o indicador dela, ou a conta das diretorias que bate com o
   material); os outros você completa na C3. Crie a pasta de trabalho `estrategia-2027-trabalho/` (seção 5) e salve
   nela:
   - o rascunho da empresa e as visões gerais das pastas reservadas (seção 1, texto fixo), que são suas;
   - `existentes.txt` (os caminhos que existem), `codigos.csv` (a lista de códigos) e uma cópia da planilha;
   - `leituras.md`: o que a C1 leu de cada indicador (caminho, revisão, valor, mês) e a lista do que não abre;
   - `projetos.csv`: código, nome, diretoria dona e pasta de cada projeto do material (a dona é uma só: a que o
     material diz, ou a da lista de códigos), para ninguém escrever o mesmo arquivo nem errar o caminho de outro;
   - `areas.txt`: os ids das áreas, marcando as que quem roda não lê, e uma linha `subárea → diretoria-pai` para
     cada subárea que existe (do `listar` da raiz); é dela que sai o `--subareas` da conferência (seção 5).

   **Antes de escrever a primeira diretoria (ou de chamar os subagentes), tire das cópias da planilha e da lista de
   códigos toda linha marcada como confidencial ou sigilosa**, com pessoa identificável ou não. Se a ata tiver um item
   assim, salve também uma cópia da ata sem ele. **O tema de uma decisão sigilosa não vai a arquivo nenhum da pasta de
   trabalho, em nenhum caminho** (nem plano, nem anotação, nem pedido, nem resumo): fica só na conversa.
2. **Cada diretoria, pelo caminho que a régua escolhe:** em sequência (o padrão), uma por vez, por você; ou em
   paralelo, um subagente por diretoria com o pedido abaixo. Em qualquer caminho, cada diretoria termina com os
   rascunhos em `docs/<area>/` e um resumo com os itens do pedido. Diretoria só citada por outra, sem meta nem
   projeto, não ganha rascunho: você mesmo anota o que há dela.
3. **Você, depois: a passada final (C3)**, que cruza as diretorias pelos resumos e pela conferência automática, sem
   reler os rascunhos inteiros.

**A régua: o tamanho do material, não o número de diretorias.** O padrão é em sequência. Meça na C1 (passo 4) o
material de cada diretoria, sem o material da empresa (a ata, a planilha consolidada, o documento de objetivos):
- texto, com `wc -m` (caracteres, não bytes), depois de converter com o que houver (`pdftotext`, Python);
- PDF escaneado, slide só com imagem ou sem conversor: conte páginas ou slides vezes ~2.500 caracteres;
- deck único do retreat com todas as diretorias: meça as páginas de cada uma; planilha: só as linhas dela.

Use o **paralelo** só quando, além de haver subagente, o material das diretorias somado passar de ~200 mil
caracteres, ou uma diretoria sozinha passar de ~50 mil. Por quê: nos ensaios de 24/11, com material pequeno
(~2 mil caracteres por diretoria), a sequência deu a mesma qualidade e custou muito menos (com 3 diretorias, ~251 mil
tokens contra ~915 mil; com 10, ~300 mil contra ~2,26 milhões, em menos tempo). A conversa principal dos dois
caminhos fica do mesmo tamanho perto de ~20 mil caracteres por diretoria, mas o paralelo custa bem mais no total e só
se paga quando a conversa da sequência arrisca encher: daí o corte acima desse ponto. **Os limites saíram de conta,
não de medida:** o maior material ensaiado tinha ~23 mil caracteres no total, numa janela de contexto em que as
conversas passaram de 300 mil tokens. Acima disso é território sem ensaio: diga isso a quem roda e não encurte a
passada final. Sem subagente e com material acima da régua (no Claude do navegador ou do desktop, ou dentro de um
subagente), siga em sequência e diga a quem roda que o material é grande para uma conversa só e que o Claude Code é
o lugar mais seguro. A frase a quem roda está em `references/conducao.md`, "Captura".

**Em sequência:**
- a ordem: primeiro as decisões que mudam a empresa ou outra diretoria (a ata, ou um e-mail ou documento da
  diretoria executiva que muda uma meta da empresa) e a diretoria dona de uma decisão sigilosa; depois as outras.
  Assim a regra do sigilo e o número da empresa já valem quando cada diretoria é escrita;
- uma diretoria por vez, com o pedido abaixo como roteiro e as mesmas regras;
- ao terminar cada uma, grave os rascunhos em `docs/<area>/` (e os projetos das subáreas dela em
  `docs/<subárea>/projetos/`) e o resumo em `estrategia-2027-trabalho/resumos/<area>.md`
  antes de começar a próxima; o item 1 do resumo (sigilo) fica só na conversa, e nenhum outro item do arquivo leva o
  tema sigiloso;
- não traga o texto dos rascunhos de volta para a conversa: na passada final, leia os resumos do disco e use a
  conferência automática;
- as regras de sigilo (C2) valem já ao escrever cada diretoria, porque aqui quem escreve já leu a decisão;
- **as últimas diretorias:** a pressa não se nota de dentro. Na passada final, confira de novo contra o material as
  duas ou três últimas diretorias escritas, e qualquer uma com menos metas ou projetos no resumo do que linhas na
  planilha, ou com mais seções "O material do retreat não traz." que a média. No ensaio de 10 diretorias, foi isso
  que pegou o que a pressa deixou passar.

**Em paralelo:** um subagente por diretoria, todos ao mesmo tempo, com o pedido abaixo. Roda numa conversa principal
do Claude Code (um subagente não abre outro). Avise só o subagente da diretoria dona de um item confidencial, no
texto do pedido dele, nunca num arquivo.

**Onde fica a pasta de trabalho.** No Claude Code, na pasta da conversa. No Claude do navegador e do desktop, é a pasta
do ambiente de execução de código da conversa (o mesmo que roda o script): vale até o fim da conversa, e os arquivos
para baixar saem dela. O hash sai de `sha256sum`, `shasum -a 256` ou do `hashlib` do Python, o que houver. Sem
execução de código, não há pasta nem script: estime o material por páginas e use a mesma régua; abaixo de ~20 mil
caracteres, siga numa conversa só, com a conferência à mão (seção 5) e o envio sem hash; acima, diga a quem roda que
a captura não cabe e que precisa do Claude Code ou da execução de código ligada.

**O pedido a cada subagente** (troque o que está entre `< >`):

```text
Você monta os rascunhos da estratégia 2027 da diretoria <Área> (id <area>), a partir do material do retreat. Não
acione nenhuma skill: leia só os arquivos indicados aqui. Da skill (em <caminho absoluto da pasta da skill>), leia
references/estrategia.md, seção 2 (o molde) e seção 3, C2 (as regras de leitura); references/separar.md, seção 5;
e references/fora-da-empresa.md. A lista oficial do que não abre está em leituras.md: não busque no LivupOS.

Pasta de trabalho: <caminho absoluto de estrategia-2027-trabalho>. Material: <caminhos absolutos dos arquivos da
diretoria>, a ata (<caminho; a cópia, se houver>), o documento de objetivos da empresa (<caminho>; ele diz a que
objetivo cada número da planilha corresponde) e a cópia da planilha consolidada (<pasta de trabalho>/<arquivo>), só
nas linhas de <Área> e nas que citam <Área>. Na pasta de trabalho: codigos.csv (lista de códigos), projetos.csv
(projetos de todas as diretorias, com a pasta de cada um: use-a no depende_de), areas.txt (ids das áreas), a
estratégia da empresa em docs/liv-up/estrategia/2027.md, existentes.txt (o que existe no LivupOS) e leituras.md
(valores medidos dos indicadores). Quem roda <lê | não lê> <Área>: <se não lê, escreva o caminho provável do
indicador; a conferência diz "não conferido">. <Se houver: "O item <tema> do seu material é confidencial: trate
pelas regras de sigilo da C2 e devolva no item 1.">

Escreva só a estratégia da diretoria e os projetos de que ela é dona (projetos.csv), em <pasta de
trabalho>/docs/<area>/..., no caminho do LivupOS; o projeto de um time que é subárea vai na pasta que projetos.csv dá
(docs/<subárea>/projetos/...). Não altere nada fora dessas pastas, nem as visões gerais das
pastas reservadas que estão dentro dela (docs/<area>/estrategia/visao-geral.md e docs/<area>/projetos/visao-geral.md):
elas, a lista de códigos e as cópias são da conversa principal. Forma igual à das outras diretorias:
- toda seção do molde aparece; a que o material não preenche diz "O material do retreat não traz." ("Em aberto"
  vazio sai);
- "Quem espera algo deste projeto" leva sempre a frase "Quem depende deste projeto entra aqui quando a diretoria dona
  confirma.";
- dependência de área é `area:` e `espera`, sem `marco`;
- se alguma meta compõe uma da empresa, uma vez, logo depois da tabela, a frase "O fechamento com as metas da Liv Up
  está na estratégia da Liv Up."; a conta entre diretorias não é sua.
Não chame ferramenta do LivupOS nem de mensagem; não invente código. O que é sensível com pessoa identificável não
vai a arquivo nenhum nem aos itens 2 a 9 do resumo (nem o nome, nem o código, nem marco ou data dele); decisão
sigilosa vai só no item 1, nunca no 9. A regra do "outro projeto que esbarra na decisão sigilosa" é da conversa
principal, que vê todas as diretorias: se você suspeitar de algo assim, não mude o texto; aponte no item 1. Exceção:
se este pedido avisa que a sua diretoria é dona de um item confidencial, aplique você a regra do "projeto ou meta da
própria diretoria dona" (C2) e liste no item 1 o que deixou neutro.

Devolva, em até 60 linhas, sem repetir os rascunhos. Os itens 1, 6 e 9 nunca se cortam:
1. sigilo, só aqui e só na conversa: o que ficou fora por ser sensível (nome do projeto e código, ou "sem código";
   o tema da decisão, sem nome nem número de pessoas; a pergunta pronta ao diretor dono da decisão); o sigiloso sem
   pessoa identificável (tema e pergunta ao diretor); e o projeto desta diretoria que parece esbarrar numa decisão
   sigilosa, qual e por quê (com os termos que tocam a decisão), sem mudar o texto;
2. os documentos escritos (caminho e título);
3. as metas: id, compoe ou objetivo, indicador, de, de_em, para, prazo;
4. os projetos: código (ou "sem código"), título, objetivo (ou objetivos), dono (papel), a meta que move (`meta`),
   se é projeto-chave (está na coluna "Projetos-chave" da A2 ou não) e a prioridade que o material dá, o pai, se
   houver, contribuições (indicador e
   efeito) e depende_de (de quem, o que espera, marco);
5. o que falta, pela sua leitura, com quem responde (papel);
6. o que o material de <Área> cita sobre outras diretorias, em qualquer seção: o que ela promete entregar e o que ela
   pede, com o trecho curto;
7. marcos e datas para o acompanhamento, e códigos do material que divergem da lista;
8. divergências entre fontes que você não decidiu; e indicadores que você precisou e não estavam em leituras.md;
9. decisões no material de <Área> que mudam a empresa ou outra diretoria (uma meta da empresa, um prazo de que outra
   depende), com o trecho curto e a fonte.
```

Com todas as diretorias prontas (de volta dos subagentes ou gravadas por você), confira pelos resumos que cada uma
tem o que o resumo diz. Depois, antes de rodar a conferência
e de novo antes de montar os arquivos, procure com `grep` em todo `docs/` os nomes, códigos e termos que tocam cada
decisão sigilosa do item 1 (o tema e os termos apontados). O que achar, corrija pela C2. O item 1
fica só na conversa; tire a linha do código sensível da cópia `codigos.csv` se ainda estiver lá. Duas ou mais
perguntas sigilosas ao mesmo diretor viram uma só. Indicador que faltou (item 8): leia na passada final e corrija.

**Regras de leitura** (valem para você e, no que é escrever os rascunhos, para cada subagente; o que mexe na lista
de códigos, nas cópias e nos arquivos das diretorias é seu):

- **Fonte de cada campo:** todo material do retreat vale igual (a planilha consolidada, os slides, as notas, a ata).
  Onde só a planilha dá o objetivo de um projeto, use e ponha no "Em aberto" para o diretor confirmar.
- **Objetivo do projeto:** o material liga a um objetivo da empresa (use o id), ou diz que é só da área
  (`proprio-da-area`), ou não diz (`"a confirmar"` e a pergunta com as duas saídas, seção 2). Não deduza
  `proprio-da-area` do silêncio do material nem de o projeto ser de um time.
- **Onde mora o projeto de um time:** na subárea, se ela existe (está em `areas.txt` ou no `listar` da raiz); se não, na
  diretoria (seção 1). Nunca em `projetos/` dentro de `geral/` ou de uma frente.
- **A decisão mais nova vale.** Uma ata ou decisão datada depois dos slides vale sobre eles: projeto cortado não sobe,
  e meta revisada entra com o valor novo. Diga a fonte da mudança no "Em aberto" do documento.
- **Número da empresa que é a soma ou a média dos das diretorias** não é divergência: confira a conta antes de
  chamar de divergência (R$ 60 mi + R$ 51 mi = R$ 111 mi fecha).
- **Dois números para a mesma coisa, sem decisão que escolha** (slides × planilha, por exemplo): não escolha. O campo
  fica `"a confirmar"`, e a divergência vai para a lista do diretor, com os dois valores e as fontes.
- **O valor medido decide o `de` e o `de_em`.** O documento do indicador é medição, não decisão. Se o material não dá
  o mês do valor de hoje, ou diverge do documento do indicador, use o documento, cite caminho e revisão, e registre a
  divergência no "Em aberto". **Sem documento do indicador,** na área que você lê ou na que não lê, é igual: use o
  número do material, com o mês se ele der (sem mês, `de_em: "a confirmar"`), e ponha no "Em aberto" que o valor de
  hoje se confirma quando o indicador existir.
- **O que falta não se preenche:** campo sem fonte fica vazio ou `"a confirmar"`, e vira linha do que falta.
- **Projeto sem código:** o rascunho vai no arquivo da diretoria, não na proposta (seção 2), e o projeto vai para
  "pedir código", com nome, diretoria e dono, se o material diz.
- **Projeto que só aparece na lista de códigos**, sem material do retreat, não ganha rascunho: vira linha no arquivo da
  diretoria dona. **Projeto apresentado e não decidido** (a ata diz que ficou para depois) ganha rascunho, com o
  "Em aberto" citando a ata.
- **Marcos e datas** vão para a lista do acompanhamento (projeto, marco, data, fonte). O rascunho do projeto só
  cita o código do marco quando uma dependência precisa dele.
- **Sensível:** valem as regras de `references/separar.md`, seção 5. Corte de vaga ou demissão com pessoa
  identificável, salário de alguém, caso de pessoa: fica fora de todo arquivo. Isso vence o "documento à parte
  fechado" da seção 1: com pessoa identificável, nada do projeto vai a documento nenhum. Se o projeto já tem código na
  lista, ele sai também:
  - do arquivo da diretoria, inclusive das linhas da lista de códigos copiadas nele;
  - do arquivo do acompanhamento (nem como cortado, nem como código divergente);
  - da cópia da lista de códigos que vai para a conferência: tire a linha antes de rodar o script (seção 5).

  No arquivo da diretoria, só "1 item ficou fora por ser sensível; fale com o time central". A pergunta ao diretor
  dono da decisão fica só na conversa, sem nome nem número de pessoas, com o texto pronto para quem roda levar
  pessoalmente.
- **Projeto ou meta da própria diretoria dona da decisão sigilosa** que a decisão muda (a obra que a decisão adia, o
  custo que ela reduz): o texto (cabeçalho, tese, riscos, "Em aberto") fica neutro, sem o que revela a decisão; o
  número que depende dela fica `"a confirmar"`, sem comentário. Esse `"a confirmar"` não gera linha no que falta da
  dona nem na lista de `liv-up` (nem a da soma com parte aberta), e não entra no acompanhamento: a pergunta fica só
  na conversa, ao diretor dono, junto com a da decisão. No caminho em paralelo, quem aplica é o subagente da dona,
  avisado no pedido.
- **Outro projeto que esbarra na decisão sigilosa** (conta com um turno, uma equipe ou uma vaga que a decisão muda;
  usar o mesmo recurso sem depender do que a decisão muda não é esbarrar: as geladeiras que dependem da linha em um
  turno seguem normais, e os marcos do próprio projeto da linha também, se a descrição não revela a decisão):
  qualquer pergunta escrita pode antecipar o que ainda não foi comunicado. A dependência fica no rascunho, mas sem o
  termo que toca a decisão, no cabeçalho (`espera`) e no texto ("Depende de", riscos): escreva o que se espera de
  forma neutra ("capacidade da Linha 3") e, se o `marco` não está na lista, `"a confirmar"`, para não ir ao ar um
  código que não existe. No arquivo da diretoria que depende, só a linha "Uma dependência espera resposta do time
  central". Tudo o que levaria alguém a perguntar sobre ela fica fora dos arquivos: a linha
  no que falta dos dois diretores, o pedido em "O que outras diretorias esperam de você", e, no acompanhamento, o
  marco que não está na lista, a data e a divergência de código. A pergunta vai na mesma conversa, para quem roda
  levar ao diretor dono da decisão, que decide o que responder e o que entra depois. Quando ele responder, quem roda
  leva a linha do marco à responsável pela lista de códigos.
- Meta ou projeto que o material marca como sigiloso, sem pessoa identificável, segue a seção 1.
- **O que não abre para a empresa:** as pastas são lidas pela empresa toda. Aplique `references/fora-da-empresa.md`:
  tire do texto o valor de verba, orçamento, capex, contrato, comissão e alçada. Se a frase não se entende sem ele,
  vira pergunta ao diretor.

### C3. Conferir: a passada final

A passada final é sua, na conversa principal, e cruza as diretorias. Use os resumos (dos subagentes, ou de `resumos/` na sequência) e a saída da
conferência; abra um rascunho só quando precisar corrigir ou tirar uma dúvida.

Rode a conferência (seção 5) em `estrategia-2027-trabalho/docs`, com todas as diretorias juntas, os caminhos que
existem, a lista de códigos como veio (sem as linhas do projeto sensível) e as áreas que você não lê. Depois, uma
leitura, com quatro perguntas:
- as metas que compõem uma da empresa fecham com cada versão do número, quando há mais de uma?
- algum projeto cortado ou adiado ainda conta numa meta (a receita de uma diretoria contava com ele)?
- as contribuições dos projetos para um mesmo indicador passam da meta, ou não chegam perto dela?
- alguma dependência aparece no texto (perguntas da sala, riscos) sem estar em `depende_de`?

Complete o `de` e o `de_em` das metas da empresa que abrem nas diretorias, com os resumos (seção 2, "Valor de hoje
da meta que abre nas diretorias").

Pelos itens 9 dos resumos, atualize o rascunho da empresa com as decisões que a mudam e corrija as diretorias
afetadas (antes de rodar a conferência).

Passe também pelos itens 1 dos resumos: se algum projeto de outra diretoria esbarra numa decisão sigilosa (um turno,
uma equipe, uma vaga que ela muda), aplique a regra da C2 a ele (no paralelo, o subagente dele não sabia da decisão).
Confira também os projetos e metas da própria diretoria dona: o que a decisão muda está neutro, e o `"a confirmar"`
dele não gerou linha em lista nenhuma.

E, para cada pedido de outra diretoria (a parte "Para confirmar" da conferência), veja no item 6 do resumo da
diretoria de quem se espera (ou no material dela, se precisar) se ela cita o pedido, em qualquer seção (não só na de
pedidos): **já citado** ("a sua área citou
este pedido no material: `<como cita>`") ou **não citado** ("a sua área não citou este pedido"). Citar não quer dizer
combinar (pode ser um risco); o diretor precisa ver qual é o caso. O que esbarra numa decisão sigilosa fica fora
(C2).

**O que entra na lista do que falta, e como se conta.** A lista é por diretoria, e a contagem é o número de linhas
dela. Para duas pessoas que rodam a captura chegarem ao mesmo número:
- **uma linha por coisa que a diretoria precisa decidir ou fornecer**, citando nela a meta ou o projeto (valor e mês
  de hoje da mesma meta são uma coisa só; os indicadores não conferidos da mesma diretoria, uma linha com a lista
  deles, porque a pergunta é uma só, "existem?", enquanto o indicador que não existe pede quem o cria, uma linha
  cada; contribuições que não chegam perto da meta, ou que passam dela, uma linha por meta, com os projetos). "Não
  chega perto" tem critério: com a mesma unidade, os efeitos somados ficam abaixo de metade do caminho entre o `de` e
  o `para`; "passa" é quando somados passam do `para`; meta sem nenhum projeto contribuindo também é "não chega
  perto", mas o projeto que aponta a meta pelo `meta` conta como projeto da meta, mesmo sem `contribuicao`. Com unidade diferente ou efeito `"a confirmar"`, não conta. As linhas que o script marca "(informativo)"
  não contam.
  Meta da empresa vai para a lista de `liv-up`. Entra o que
  responde o diretor ou um dono de projeto da diretoria; a linha juntada responde a diretoria;
- **o mesmo pedido repetido em vários projetos ou metas vira uma linha só**, com a lista deles;
- **fora da contagem:** o que se pede a outra diretoria (seção "para confirmar" dela, como já é); o que é de quem
  montou os rascunhos (corrigido antes de mostrar); e o que é da lista de códigos (projeto sem código, código
  divergente), que vai para "os projetos que esperam código" e para o acompanhamento;
- **a soma com uma parte "a confirmar"** conta uma vez, na lista de `liv-up`; na diretoria com a parte aberta, a
  linha "falta o valor de chegada" já leva o número que fecha a conta, sem virar linha a mais. Na lista de `liv-up`,
  "falta o valor de chegada" e a conta da mesma meta também são uma linha só.

Exemplo, Growth. Três projetos ligados a um objetivo só pela planilha, o mesmo indicador de ticket médio que não
existe em dois projetos, e a Assinatura sem dono:

> - Confirmar o objetivo de Régua de recompra, Kits da semana e Assinatura Liv Up Mais (só a planilha diz). Responde:
>   diretoria de Growth.
> - Quem cria o indicador de ticket médio (Kits da semana e Assinatura Liv Up Mais apontam para ele)? Responde:
>   diretoria de Growth.
> - Dono da Assinatura Liv Up Mais: uma pessoa, pelo e-mail (o material diz "Time CRM"). Responde: diretoria de
>   Growth.

E dois casos das regras de juntar: dois indicadores que quem roda não lê, e a recompra, de 31% para 38%, com
projetos que somam +2 p.p.:

> - Os indicadores de sessões do app e de cupom usado existem? Não deu para conferir. Responde: diretoria de Growth.
> - Recompra em 90 dias: os projetos (Régua de recompra, Kits da semana) somam +2 p.p. para uma meta de +7 p.p.; o
>   que leva o resto? Responde: diretoria de Growth.

São 5 linhas, não 10. A saída do script vem uma linha por documento: junte antes de contar.

A contagem, na parada C, no arquivo e na justificativa, é a depois da leitura: a saída do script sem o
que a leitura mostrou que não é problema, mais os achados da leitura (soma que não fecha, contribuição que passa da
meta ou não chega perto), cada um na lista da diretoria a que ele pertence. Tire também da saída do script as linhas
que esbarram numa decisão sigilosa (C2): marco fora da lista, pedido ou divergência ligados a ela.

Junte, por diretoria:
- o que falta (sem os pedidos de outras diretorias: eles não contam como falta, porque "Quem espera algo deste
  projeto" só se preenche na conferência com o diretor);
- o que outras diretorias esperam dela, separado em já citado e não citado;
- o que ela espera de outras diretorias (os `depende_de` dos projetos dela);
- as divergências entre fontes;
- o que ficou fora por ser sensível, só com o motivo.

### ⏸ Parada C

Numa mensagem, mostre:

- **por área:** quantos documentos vão como proposta, quantos ficam no arquivo da diretoria e por quê;
- **o que falta,** contado por diretoria (a lista inteira vai no arquivo), sem os pedidos de outras diretorias, que
  são contados à parte, para confirmar;
- **a lista para o acompanhamento:** projetos sem código, códigos do material que divergem da lista, projetos
  cortados que a lista ainda tem, marcos com data e dependências com data.

Diga o efeito de enviar, numa mensagem só, com o parágrafo de cada caso que existe:

> Em `<áreas>`, vou abrir uma proposta por área com os rascunhos. Nada fica no ar: quem decide cada área vê a proposta
> na lista de pendências e decide na sessão dele (de 14 a 18/12). Proposta parada há 14 dias expira; se a sessão
> passar disso, os rascunhos continuam no arquivo da diretoria. O LivupOS mostra a proposta a quem decide a área no
> resumo diário dele; eu não mando mensagem. Para desfazer antes da decisão, eu cancelo a proposta.
>
> Em `<áreas>`, nada sobe agora; os rascunhos vão no arquivo da diretoria, porque `<motivo>`.
>
> `<Áreas>` não apresentaram metas nem projetos; o arquivo delas leva só o que outras diretorias esperam delas.
>
> No fim, apago a pasta de trabalho da conferência (`estrategia-2027-trabalho/`), que tem as cópias do material e da
> lista de códigos e os rascunhos soltos; os arquivos das diretorias ficam, com os rascunhos dentro.
>
> Posso enviar?

(O parágrafo da pasta só se ela existe; sem execução de código, não há pasta.) Para cancelar uma proposta depois, se
pedirem: diga antes que os rascunhos continuam no arquivo da diretoria e que o diretor deixa de ver a proposta; com o
ok, `contexto_liv_up_atualizar_proposta` com `cancelar`.

Antes de mostrar a parada C, registre em `estrategia-2027-trabalho/envio.txt` uma linha por documento que vai em
proposta: área, caminho no LivupOS, tamanho em bytes e o hash do arquivo (`shasum -a 256`). É a lista do que a parada
C mostrou; nada fora dela é enviado.

Com o ok, uma proposta por área. **Quem envia** (vale só quando quem roda não é admin do LivupOS: admin não propõe,
os rascunhos vão nos arquivos, C1):
- **No caminho em paralelo:** um subagente por área, todos ao mesmo tempo, para a conversa principal não reler os
  rascunhos.
  O pedido diz: a área; os caminhos e os hashes daquela área, de `envio.txt`; a justificativa e a `origem` prontas;
  e as travas abaixo. Ele devolve, por documento, o caminho, o número da proposta e o hash que enviou.
- **Na sequência (o padrão), ou sem subagentes:** você mesmo, área por área. Copie o texto do arquivo para a chamada,
  nunca de memória: leia o arquivo imediatamente antes de cada envio e confira o hash dele contra `envio.txt`. Se a
  ferramenta devolver o tamanho ou o hash do que recebeu, confira também contra `envio.txt`. Um subagente de envio
  custa por si mais do que o material pequeno que justifica a sequência.

Quando quem roda é admin do LivupOS (o caso provável na semana de 07/12), não há envio nenhum, em nenhum caminho:
os rascunhos vão só nos arquivos das diretorias (C1).

O pedido ao subagente de envio (troque o que está entre `< >`):

```text
Você envia ao LivupOS a proposta da estratégia 2027 da área <area>, que quem roda aprovou ("pode enviar"). Não acione
nenhuma skill. Arquivos e hashes (sha256) que podem ir, e só eles:
<linhas de envio.txt desta área: caminho no LivupOS, arquivo na pasta de trabalho, tamanho, hash>
1. Calcule o hash de cada arquivo. Se algum não bate com a lista, não envie nada desta área e devolva qual mudou.
2. Chame contexto_liv_up_propor_mudanca uma vez (ou mais, se passar de 20 documentos), com uma mudança "criar" por
   arquivo, o conteúdo exatamente como está no arquivo, a justificativa abaixo, sem mudar uma letra, e a origem
   { tipo: "mcp", ref: "estrategia-2027/captura/<area>" }.
   Justificativa: <texto pronto>
3. Não chame nenhuma outra ferramenta de escrita, não publique direto e não mande mensagem. Se o LivupOS recusar,
   não tente de outro jeito: devolva a recusa como veio.
Devolva, por arquivo: caminho no LivupOS, número da proposta e hash enviado.
<Em ensaio: "Não chame o LivupOS: confira os hashes e devolva a lista do que enviaria.">
```

**As travas do envio:**
- O texto vai exatamente como está no arquivo da pasta de trabalho, sem reescrever nada. Antes de enviar, confira o
  hash de cada arquivo contra `envio.txt`; se mudou, não envie aquela área e devolva o motivo.
- Só as áreas e os documentos de `envio.txt`, só depois do "pode enviar", e só `propor_mudanca` (nunca publicação
  direta nem outra ferramenta de escrita).
- Recusa do LivupOS não se contorna: o subagente devolve a recusa como veio, e você decide (abaixo).
- Quando todos voltarem, confira a lista inteira (caminho, número, hash) contra `envio.txt`. O que faltar ou não
  bater, diga a quem roda.
- Em ensaio ou teste, ninguém chama o LivupOS: quem envia (você ou o subagente) confere os hashes e devolve a lista
  do que enviaria.

O que cada proposta leva:

1. `contexto_liv_up_propor_mudanca`: com até 20 mudanças (se passar de 20, divida em mais de uma). Inclua as visões gerais das pastas reservadas que a seção 1 pede (a carga da área não cria
   essas pastas: `forma-comum.md`, seção 4). A justificativa no formato de `references/moldes.md`, com o primeiro item "Propõe a
   estratégia 2027 de `<Área>`: `<N>` metas e `<M>` projetos para conferir" (em `liv-up`: "Propõe a estratégia 2027
   da Liv Up: `<K>` objetivos e `<N>` metas para conferir") e, depois do Resumo, a fonte (material do retreat) e
   quantas linhas tem a lista do que falta. `origem`: `{ tipo: "mcp", ref: "estrategia-2027/captura/<area>" }`.
2. Anote o número de cada proposta no arquivo da diretoria.

Recusa ao enviar: siga "Quando travar" no `SKILL.md`. Se a recusa for por causa dos campos novos do cabeçalho, não
tire os campos: os rascunhos ficam no arquivo da diretoria, e diga isso ao time central.

### C4. Entregar os arquivos

Os arquivos locais seguem "Onde ficam os arquivos locais" do `SKILL.md`. São:

- **`estrategia-2027-<area>-AAAA-MM-DD.md`, um por diretoria citada** (e um para `liv-up`): a que tem meta ou
  projeto e a de quem outra diretoria espera algo, mesmo sem rascunho. É o que o diretor anexa na sessão dele, que
  costuma ter 40 minutos. Nesta ordem:
  1. **"O que precisa de você"**, no topo, em até 10 linhas: quantas metas e projetos, o número da proposta (ou o
     motivo de não ter), as perguntas que mais pesam (as que mudam um número ou um projeto; o resto fica na lista),
     quantas linhas tem cada lista abaixo, os projetos marcados como só da área (fora da contagem, para ele ver a
     escolha) e, se houve, "1 item ficou fora por ser sensível; fale com o time central";
  2. a lista do que falta para aquele diretor;
  3. sempre a seção "O que outras diretorias esperam de você" (com "nenhuma", se for o caso, e a data do
     levantamento), em duas partes: "já citado no material da sua área" e "não citado no material da sua área";
  4. "O que você espera de outras diretorias": os `depende_de` dos projetos dela;
  5. os projetos que esperam código;
  6. as linhas da lista de códigos dos projetos da diretoria e dos projetos de que eles dependem;
  7. os objetivos da empresa e as metas da empresa que a diretoria compõe (do rascunho da empresa, para a conferência
     do diretor ter contra o que comparar enquanto a da empresa não é publicada);
  8. por último, os rascunhos completos, com as visões gerais das pastas reservadas que vão na proposta (em área que
     quem roda não lê, marcadas "só se a área ainda não tiver"). As listas vêm antes, para o diretor achar o que precisa dele sem passar pelos rascunhos.

  Diretoria sem rascunho (só citada por outras): o arquivo leva os itens 1, 3, 5, 6 (se houver linha na lista de
  códigos) e 7; os outros saem. Não leva o que foi cortado por ser sensível (C2).

  Monte cada arquivo sem trazer os rascunhos para a conversa: escreva os itens 1 a 7 e junte o item 8 com um laço no
  terminal sobre a lista dos documentos que você conferiu (o item 2 dos resumos e as visões gerais), que escreve
  `### <caminho no LivupOS>` antes de cada um (e "só se a área ainda não tiver" nas visões gerais de área que quem
  roda não lê). Confira a lista contra os arquivos de `docs/<area>/` (`find`): arquivo que não está na lista não
  entra sem você conferir. Antes, faça a busca do sigilo (C2) e confira que a passada final corrigiu na pasta de
  trabalho os rascunhos que precisou corrigir.
- **`estrategia-2027-acompanhamento-AAAA-MM-DD.md`:** para a responsável pela ferramenta de acompanhamento. Leva os
  projetos que esperam código, os códigos do material que divergem da lista, os projetos cortados que a lista ainda
  tem, os marcos com data e as dependências com data, cada um com a fonte. Também não leva o projeto sensível (C2),
  mesmo que ele tenha código na lista.

Depois de entregar os arquivos, apague a pasta de trabalho da conferência (`estrategia-2027-trabalho/`, seção 5), e
só ela: ela guarda as cópias do material e da lista de códigos, e os rascunhos já estão nos arquivos das diretorias. O efeito foi
dito na parada C; diga na mensagem final que apagou.

A captura não registra resultado no LivupOS: o registro de carga é da área. Termine com a lista dos arquivos.

A skill não manda esses arquivos a ninguém: quem roda é quem entrega.

## 4. Conferência (etapa de estratégia, owner da diretoria, 14 a 18/12)

Vale a regra 1 do `SKILL.md`: só owner ou substituto, conferido na etapa 1.

### E1. Achar o que chegou

- `contexto_liv_up_pendencias`: as propostas abertas da área com documento em `<area>/estrategia/` ou
  `<area>/projetos/`, e as das subáreas dela em `<subárea>/projetos/`. Abra cada uma com `contexto_liv_up_ver_proposta`. Só entra na etapa de estratégia a proposta da captura:
  a que tem o número anotado no arquivo da diretoria ou, sem arquivo, a que abre com "Propõe a estratégia 2027" e
  o nome da área. Qualquer outra proposta nessas pastas fica fora: diga numa linha que ela existe e que a decisão é com a
  curadoria, não aqui.
- O arquivo `estrategia-2027-<area>-…` que a pessoa anexar (peça na abertura da etapa, se não veio).
- `contexto_liv_up_listar` em `<area>/estrategia` e `<area>/projetos`: o que já está publicado.
- `contexto_liv_up_ler` de `liv-up/estrategia/2027` (para objetivos e metas da empresa). Se ainda não está publicado,
  confira contra o rascunho da empresa que vem no arquivo, e diga isso.

Nem proposta nem arquivo: diga numa frase que a estratégia da diretoria ainda não chegou (o time central monta a
partir do retreat) e encerre a etapa.

Se o arquivo não traz os objetivos da empresa ou a lista de códigos, e a estratégia da empresa não está publicada,
diga numa linha o que não deu para conferir (objetivos, metas da empresa, códigos), siga com o resto e deixe como
pendência "conferir de novo quando a estratégia da Liv Up for publicada".

Se a visão geral de `estrategia/` ou de `projetos/` da área não é o texto fixo (`references/forma-comum.md`, seção 4),
por exemplo com metas ou projetos do ano anterior, ofereça trocar pelo texto fixo, com o efeito e o ok. A troca é um
`alterar` com o `revisao_base_id` lido agora, na chamada de `propor_mudanca` da versão dele; se a proposta do time
central foi aprovada sem mudança, numa chamada à parte, depois. O conteúdo antigo, se ele quiser guardar, vira
`estrategia/<ano anterior>` (criar), com o mesmo texto.

### E2. Conferir de novo e perguntar

Rode a conferência (seção 5) com o estado de hoje: o que estava faltando pode ter sido publicado nesse meio tempo.
Mostre ao diretor, numa mensagem:

- os documentos, com o resumo e a tabela de metas;
- o que falta, por documento;
- o que outras diretorias esperam dos projetos dele: o "já citado" aparece com o que o material da área dele diz,
  para ele só corrigir se mudou; pergunta mesmo só o "não citado" (o que a pessoa já disse não se pergunta);
- os projetos marcados como só da área, numa linha, para ele confirmar a escolha;
- os projetos das subáreas dele, que ele confere junto (E1 também procura propostas em `<subárea>/projetos/`).

Se o plano da carga está à mão (na sessão só de estratégia, peça para anexar; sem ele, pule) e tem itens em "espera
a estratégia", compare com o que chegou e mostre, numa linha cada, o que
está no plano e não está nos rascunhos. O diretor decide se entra (com fonte) ou se fica de fora.

As perguntas seguem a exceção da regra 12 para a estratégia: junte as do mesmo documento e não pergunte o que ele já respondeu. Pergunta sobre um
número dá as opções ("a meta fica em R$ 111 mi ou passa a R$ 105 mi, sem o projeto cortado?"). Nome de quem decidiu no
retreat vira papel ("a CEO", "o diretor de Operações").

O que ele não souber vira "Em aberto" no documento, com dono e data. Se ele não diz quem nem quando, use o padrão e
diga que é o padrão, para ele trocar na parada 7: o dono é quem o rascunho ou a lista do que falta indicou; a data é o
fim da semana de conferência, ou a revisão de fevereiro de 2027 quando depende de outra diretoria.

Se um "Em aberto" pode mudar o `para` de uma meta, pergunte numa linha: publica o número agora (e, se mudar, entra
como revisão) ou publica `"a confirmar"`?

A dependência que ele confirma entra em "Quem espera algo deste projeto", no lugar da frase "Quem depende deste projeto entra aqui quando a diretoria dona confirma." (que fica se ele
não confirma nenhuma). A dependência que o arquivo marca como "espera resposta do time central" não vira pergunta:
fica como está, com `"a confirmar"`, e o "Em aberto" diz que o time central responde. A que ele não reconhece vai para a lista do
diretor da outra área, como pergunta.

Projeto com `objetivo: "a confirmar"`: pergunte a que objetivo da Liv Up ele serve, ou se é só da área. Só com a
resposta explícita "só da área" grave `objetivo: proprio-da-area`; resposta em dúvida ("acho que é mais da área")
fica `"a confirmar"`, com o diretor no "Em aberto". O `ate` de uma contribuição que o material não data fica
`"a confirmar"`.

### ⏸ Parada 7

Mostre a versão final de cada documento (o texto inteiro dos que ele pedir) e o efeito, com o texto de
`references/conducao.md`, parada 7.

A decisão sobre a proposta é dela inteira: aprovar publica todos os documentos dela. O "pode publicar" da parada 7
não basta para decidir a proposta: a ferramenta exige o pedido explícito do diretor para aquela proposta, depois de
ver o diff. Então:

1. **Rode a conferência de novo na versão final**, antes de tudo: link fora do formato ou para documento não publicado
   não vai ao ar.
2. **Veio em proposta e nenhum documento mudou nem saiu:** chame `contexto_liv_up_ver_proposta`, mostre o diff em
   resumo e faça a pergunta literal de aprovação (`references/conducao.md`, parada 7). Só um "sim" ou "aprova" a essa
   pergunta, dentro de 30 minutos do diff, é o pedido: então `contexto_liv_up_decidir_proposta` com `aprovar` e o
   `diff_hash` mostrado. Qualquer outra resposta: não decida.
3. **Veio em proposta e algum documento mudou ou saiu:** chame `ver_proposta`, mostre o diff e faça a pergunta literal
   de recusa (`conducao.md`, parada 7). Só com o "sim" a essa pergunta, dentro de 30 minutos do diff:
   `decidir_proposta` com `rejeitar`, o `diff_hash` mostrado e o comentário "Substituída pela versão conferida pelo diretor em AAAA-MM-DD; fora desta
   versão: `<documentos que saíram e por quê>`". Depois, `contexto_liv_up_propor_mudanca` com `criar` e a versão
   conferida; como owner, ele publica direto. Se essa publicação falhar, nada fica no ar: a versão conferida fica no
   arquivo `estrategia-2027-<area>-conferida-…`, e "Quando travar" vale.
4. **Veio só no arquivo:** `contexto_liv_up_propor_mudanca` com `criar`, com o "pode publicar"; publica direto.

`origem` das chamadas da etapa de estratégia: `{ tipo: "mcp", ref: "estrategia-2027/conferencia/<area>" }`. Projeto sem código
continua fora: o diretor publica quando o código existir.

Até 20 mudanças por chamada. Se a área ainda não tem a visão geral de `estrategia/` ou de `projetos/`, ela entra na
mesma chamada (também quando a proposta da captura, que a trazia, foi recusada). Recusas: as mesmas regras de `SKILL.md`, "Recusas na publicação", com uma exceção: se a recusa for por causa dos campos do
cabeçalho da estratégia (`metas`, `objetivos`, `contribuicao`, `depende_de`…), não tire os campos para passar. A
versão conferida fica no arquivo, a pendência vai ao admin do LivupOS, e o diretor publica quando a plataforma
aceitar. O que ficou pendente vai para o plano local e para a lista de perguntas por pessoa, com dono e data.

### E3. Fechar a sessão só de estratégia

Quando a sessão foi só de estratégia (a área já teve carga), o fechamento é curto. Confira você mesmo e mostre só o
que falhou: cada documento publicado aparece com título e caminho; nenhum link quebrado; toda pendência tem dono e
data; o que ficou de fora (projeto sem código, não decidido, cortado) está dito. Entregue o arquivo
`estrategia-2027-<area>-conferida-AAAA-MM-DD.md` (o que foi publicado, as pendências por pessoa, prontas para copiar,
e o que ficou de fora). Não refaça o plano nem a lista do que não abre da carga, não pergunte da próxima leva e não
registre resultado de carga.

Na trilha da carga, a etapa aparece como `◆  Estratégia de <Área>`, sem número; na sessão só de estratégia, a
trilha tem três passos (`references/conducao.md`, "Só a estratégia"). Quando feita, aparece como
`◇  Estratégia: <N> metas, <M> projetos` ou `◇  Estratégia: ainda não chegou`.

## 5. Conferência automática

`scripts/conferir_estrategia.py` faz a conta. Monte a pasta de trabalho `estrategia-2027-trabalho/`: dentro dela,
`docs/` com um `.md` por documento, no caminho do LivupOS (`docs/growth/estrategia/2027.md`), incluindo a estratégia
da empresa (publicada ou rascunho); os caminhos que existem (do `listar`) em `existentes.txt`; a lista de códigos
em `codigos.csv`; e, na captura, a cópia da planilha, `leituras.md`, `projetos.csv` e `areas.txt`, para os
subagentes (C2). Depois rode:

```
python3 scripts/conferir_estrategia.py estrategia-2027-trabalho/docs \
  --existentes estrategia-2027-trabalho/existentes.txt --codigos estrategia-2027-trabalho/codigos.csv \
  --areas-sem-leitura people,tech --subareas producao=operacoes,last-mile=logistica
```

A lista de códigos entra como veio (uma linha por marco, dono pelo nome ou pelo e-mail), **menos as linhas do
projeto sensível (C2)**, que você tira antes de salvar. Na captura, a pasta é apagada no fim (C4). Mostre ao diretor
a lista depois da leitura (C3), não a saída bruta: tire o que a leitura mostrou que não é problema.

Antes de mostrar ou copiar a saída para um arquivo, tire as linhas que esbarram numa decisão sigilosa (C2): o script
não sabe qual é. A saída tem duas partes: o que falta, por área, com quem responde (papel, não e-mail); e, à parte, "Para confirmar
com quem se espera", os pedidos de outras diretorias, que não contam como falta. É material de trabalho: para o diretor, traduza em
linguagem simples, sem caminho, id nem nome de campo, e o que é "de quem montou os rascunhos" você mesmo corrige
antes de mostrar. Sem execução de código no ambiente, ou sem PyYAML, faça a
mesma lista à mão, item por item:

1. Objetivo citado (por meta da empresa, meta da diretoria ou projeto) que não está entre os objetivos da empresa.
   `proprio-da-area` num projeto não é falta.
2. Indicador citado (em meta ou contribuição) que não existe no LivupOS nem nos rascunhos ("não conferido", se é de
   área que quem roda não lê).
3. Meta sem `de`, `de_em`, `para` ou `prazo`, ou com `"a confirmar"` (valor e mês de hoje numa linha só). Aspiração
   na entrega, ou aquém do comprometido. Id de meta repetido. `de` ou `para` escritos sem aspas (aponte com
   todas as letras: sem aspas, `1.750` vira 1,75; não faça a conta nem compare a tabela com esse número). Metas da
   empresa sem indicador viram uma linha só, para quem decide `liv-up`.
4. Meta da empresa sem `abre_em`. Meta da diretoria que não diz o que compõe nem a que objetivo serve. `compoe` que
   aponta meta que não existe, ou que não é um id (ou lista de ids) em texto. `limite_projetos_chave` que não é inteiro
   positivo (a área fica sem limite).
5. Metas da diretoria que não fecham a da empresa: some (`soma`) ou tire a média simples (`media`) do `para` das metas
   que dizem compor. Se a média tem peso, peça o peso, sem chamar de erro. Unidade diferente: confira à mão. Com uma
   parte "a confirmar", faça a conta com as conhecidas e diga quanto a parte aberta precisa dar para fechar (na
   soma, ou quanto as conhecidas já passam da meta; na média, pela média simples), e ponha o número também na linha
   da diretoria com a parte aberta.
6. Projeto sem código, com código fora do formato, com código repetido, ou que não está na lista. Nome ou dono que
   não batem com a lista.
7. Projeto sem dono, com mais de um dono, ou com dono sem e-mail. Projeto sem objetivo, ou sem `meta` e sem
   contribuição. `meta` que não existe. `objetivos` que não é lista. `chave` que não é true nem false. `pai` que não
   existe, que tem pai ou que é o próprio projeto. Projeto
   numa pasta `projetos/` dentro de `geral/` ou de uma frente (não abre para a empresa). `efeito` da
   contribuição escrito sem aspas.
8. `depende_de` que aponta projeto que não existe. Marco fora do formato, de outro projeto, ou que não está na lista.
9. Dependência que só um lado declarou: o projeto do qual se depende não tem quem depende dele em "Quem espera algo
   deste projeto". Dependência de área (`area:`) e de projeto de área que quem roda não lê vão para a lista da área de
   quem se espera, como pergunta. Estes vão à parte, "para confirmar", fora da contagem do que falta.
10. Tabela do texto que não bate com o cabeçalho.
11. Data de marco ou entrega no texto do projeto (fora da linha de Fonte, de "Fora do escopo", de "Em aberto" e de
    data de fonte anterior ao ano da estratégia).
12. Objetivo da empresa sem nenhuma meta nem projeto (informativo).
13. D160, informativos (não contam): projetos-chave acima do `limite_projetos_chave` que a área declarou (sem a
    declaração não há limite, D166); objetivo da área sem nenhum resultado-chave (a árvore pede pelo menos uma meta por objetivo);
    meta que nenhum projeto-chave move (só na área que marcou algum; a subárea conta à parte da diretoria);
    objetivo com mais de 5 metas da mesma área. A aspiração na entrega ou aquém do comprometido não é informativa:
    é falta, no item 3.
14. Campo do sistema no cabeçalho (`camada`, `autoridade`, `status`, `owner`, `owner_id`, `revisar_em`): o LivupOS
    recusa.

A conta não julga. O que só lendo se acha fica para a leitura do diretor na parada 7: projeto que promete algo que o
indicador não mede, escopo que a ata cortou e o texto ainda promete, risco sem dono.
