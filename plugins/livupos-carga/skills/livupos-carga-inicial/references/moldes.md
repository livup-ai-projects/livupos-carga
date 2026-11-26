# Moldes de documento e a justificativa da publicação

Antes de escrever, leia um ou dois documentos vizinhos já publicados (`contexto_liv_up_listar` na pasta e
`contexto_liv_up_ler`) e copie o `tipo` e o jeito de citar fonte. Exceção: nos documentos básicos que a carga cria,
o tipo vem da forma (`forma-comum.md`, seção 0). Se a área está vazia, use os de `compras-ic/compras/`
como referência de estilo.

## Frontmatter

`titulo` e `resumo` vão sempre entre aspas duplas (um ": " no meio quebra o YAML sem elas). Só estes campos: `tipo`,
`titulo` (3 a 200 caracteres), `resumo` (20 a 300), `tags` (opcional), `estrutura: 3` (só
na visão geral da raiz da área ou da área de dentro, `forma-comum.md`) e, só quando o diretor pediu a marca,
`fora_da_empresa: true` (`fora-da-empresa.md`; não é rotina). No indicador, também `definicao`, `fonte`,
`catalogo` e `tipo_indicador` (abaixo). Nunca `camada`, `autoridade`, `status`, `owner`,
`owner_id`, `revisar_em`, nem campo novo. O LivupOS preenche o resto. Exceção: a estratégia do ano e os projetos
levam os campos de `references/estrategia.md`, seção 2.

Tipos usados na carga: `processo` (processo e regra), `glossario`, `referencia` (visões gerais, indicadores, política,
valores). Se a área já tem documentos de processo com outro tipo, siga a área; numa área nova ou vazia, use estes.

Caminho: minúsculas, sem acento, com hífen. Glossário: `<area>/glossario` (o geral) e `<area>/glossario/<tema>` (um tema); indicador:
`<area>/indicadores/<indicador>`; documento que vale para a área inteira: `<area>/geral/<documento>`; de frente:
`<area>/<frente>/geral/<documento>` ou `<area>/<frente>/<lista>/<item>`. Nada solto ao lado de pastas
(`forma-comum.md`).

## Regras de texto que valem para todos

- Primeira linha depois do título: `> Fonte: ...` com as fontes do documento (ficha do app e data, documento oficial,
  respostas de quem responde pela área, com data, atas). Cada afirmação que não é óbvia tem a fonte no fim da frase ou da seção.
- Sistema de tech, tabela e entidade: link para o documento de `tech/sistemas` ou da ontologia, com o nome que as pessoas usam
  (`[Abbiamo](../../tech/sistemas/abbiamo.md)`, link relativo com `.md`, como os documentos publicados fazem; conte os
  `../` pela profundidade real do documento: `logistica/visao-geral` usa um, `logistica/glossario/rotas` e `logistica/expedicao/visao-geral`
  usam dois, `logistica/expedicao/geral/x` usa três). Nunca descreva o sistema de tech. Sistema da área (app do time, planilha que
  funciona como sistema, sistema externo que o time opera): link para o documento dele na lista `sistemas/`
  ("Sistema da área", abaixo). Entre documentos da própria área, o mesmo formato
  (`[Absenteísmo](../indicadores/absenteismo.md)` a partir de uma frente).
- Papel no lugar de nome, também em "confirmado por" e na linha de fonte ("respostas da coordenação de 16/11"). Se o
  papel de quem roda não tem fonte, use o papel na área: "confirmado por quem responde por People", "pela substituição de Tech". Nome
  só em "quem decide" e em quem responde pelas áreas de dentro, confirmado pelo diretor.
- Valor que mora noutro lugar: diga onde e qual vale ("o custo planejado por unidade e mês está no app de custos do Last Mile, que
  é a fonte oficial"). Não copie a tabela se ela muda todo mês.
- "Em aberto" no fim, só com o que tem dono e vai ser respondido, uma linha por item: o que falta e quem responde.
- 1 a 3 mil tokens.

## Processo e regra

```markdown
# <Nome do processo>

> Fonte: <fontes e datas>.

<Duas a quatro frases: o que é, onde começa e termina, o que vem antes e depois.>

Quem decide as regras deste processo: <papel ou dono>, salvo onde a regra diz outro.

## Quem faz o quê
<tabela papel | o que faz>

## Passo a passo
1. ...

## Regras
- **<Nome da regra>.** <o que é>. Vale desde: <data>. Onde está o valor: <lugar e qual fonte vale, se houver mais de
  um>. <Quem decide: só se for diferente do documento.> <Sigilo: só se for sensível, e até quando.> <Quem de fora vê
  ou depende: e o que se pode dizer a ele.>

## Exceções
- <situação>: <o que se faz> (fonte).

## Em aberto
- <o que falta>. Responde: <papel>.
```

Os seis rótulos (o que é, quem decide, vale desde, onde está o valor, sigilo, quem de fora vê) são as seis perguntas
do modelo v7. "Quem decide" fica no topo do documento e só se repete na regra que tem outro dono. Sigilo e "quem de
fora" só aparecem quando têm resposta; o que é, vale desde e onde está o valor, sempre (com ⚠️ se faltar, e a pergunta
vai para a lista).

## Indicador

Opcional, depois do mínimo (`SKILL.md`, etapa 5). Um documento por indicador, em `<area>/indicadores/<indicador>`
(nunca dentro de frente), `tipo: referencia`. **Aponta, não copia:** a conta e a definição técnica moram no catálogo do
time de Dados (o glossário de negócio do BigQuery, que o Claude lê por `get_business_metrics`) ou numa tabela; o
documento guarda a definição nas palavras da área e de onde vem o número. **Não traz meta** (a meta mora na estratégia
do ano; a achada no material vai para o plano como "espera a estratégia") e **não traz a fórmula**.

`definicao` e `fonte` são obrigatórios no cabeçalho (D148; o painel avisa "indicador sem fonte" e "indicador sem
definição"); `catalogo` e `tipo_indicador` são opcionais:

```markdown
---
tipo: referencia
titulo: "<Nome do indicador> (<sigla>)"
resumo: "<o que mede e para que a área usa, numa frase>"
definicao: "<uma ou duas linhas, nas palavras da área: o que mede e o que conta>"
fonte: <catalogo | consulta | app | planilha | dono_informa>
catalogo: <id do termo no catálogo de Dados>      # opcional, só com fonte: catalogo e o id em mãos
tipo_indicador: <metrica | pesquisa>               # opcional: pesquisa é nota de questionário (eNPS, satisfação)
---

# <Nome do indicador> (<sigla>)

> Fonte: <fontes e datas>.

- **Definição:** <a mesma do cabeçalho>.
- **De onde vem o número:** <o catálogo de Dados (o nome da métrica) | a consulta salva (link) | o app da plataforma
  (link) | a planilha (onde mora) | "quem responde informa" (quem e onde)>.
- **Quem responde:** <papel ou área de dentro>, se não for quem responde pela área.
- **Frequência:** <com que frequência é olhado e em que ritual>, se o diretor disse.
- **Não confundir com:** <homônimo>, se houver.

## Em aberto
- <o que falta>. Responde: <papel>.
```

- **`fonte`:** `catalogo` (a métrica está no catálogo de Dados), `consulta` (uma consulta salva), `app` (um app da
  plataforma), `planilha`, ou `dono_informa` (o número não está em sistema nenhum: quem responde informa). Nem toda
  métrica está no catálogo, e isso não é falta: a fonte é a que existe hoje.
- **Catálogo:** se o conector de BigQuery da Liv Up está ligado, procure a métrica em `get_business_metrics` pelo nome
  e pelos sinônimos. Achou: `fonte: catalogo` e o id em `catalogo`. Não achou: a fonte que o diretor disser, e a
  métrica vai para a lista do que falta fora da área ("pedir ao time de Dados"). Sem o conector, a fonte que o diretor
  disser e a lista "conferir no catálogo".
- **A definição** a skill escreve (do catálogo, do material ou do que o diretor disse) e passa na revisão em blocos; não
  é pergunta à parte.
- **O glossário aponta para o indicador,** não redefine: o termo do indicador no glossário tem a definição curta e o link.

Indicador curto é normal (algumas centenas de tokens).

## Glossário da área

O mínimo é um documento `tipo: glossario` em `<area>/glossario`, com os termos que valem para a área inteira (o que a
área já sabe: siglas, nomes de rituais, de programas, de etapas, os termos que alguém de fora não entende). Se um tema
crescer, ele ganha `<area>/glossario/<tema>`, e o geral continua em `<area>/glossario`. Se a área já tem
glossário noutro lugar ou noutro formato (numa área na forma antiga, como Tech, uma pasta com documentos no formato
`## Termo`), altere o documento de termos que já existe (o geral da área, se houver vários) e acrescente no formato que
ele já usa, sem converter nem mover o que existe (`forma-comum.md`, seção 6). O formato abaixo é para a área que ainda não tem glossário. Se já existe, a carga
**altera** esse documento (`edicoes` ou documento inteiro com `revisao_base_id`), nunca cria um segundo.

Formato que o extrator lê, um item por termo:

```markdown
- **Termo (sinônimo, outro sinônimo):** definição curta. [documento da regra](caminho.md)
```

- Termo que é **entidade de sistema** (entrega, rota, pedido, parceiro): definição curta, onde mora e o link. Ver
  `area-e-ontologia.md`.
- Termo que é **regra ou indicador**: definição curta e link para o documento.
- **Homônimo:** um termo para cada sentido, cada um com "não confundir com".
- **Erro de transcrição** confirmado: sinônimo do termo certo.
- **Termo de outra área:** na seção de título fixo `## Termos de outras áreas`, com a versão local e a última frase
  `Área dona: <id da área>`.

## Visão geral da área

`<area>/visao-geral`, `tipo: referencia`, com `estrutura: 3` no frontmatter (fora da forma anterior,
`forma-comum.md`, seção 6). É a porta da área: quem chega lê só ela e sabe onde procurar e a quem perguntar.

```markdown
---
tipo: referencia
titulo: "<Área>: visão geral"
resumo: "<o que a área faz, numa frase>"
estrutura: 3
---
```

Seções, nesta ordem. **No mínimo** entram 1, 2, 3, 6 e 9; as outras entram se o material ou o diretor trouxeram, e
nunca viram pergunta só para preencher:

1. **O que a área faz:** escopo, onde o trabalho começa e termina, o que é de outra área. Numa área de dentro, a
   primeira frase diz de qual área ela é ("O Departamento Pessoal é uma área de dentro de People & Culture"), com o
   link para a visão geral dela.
2. **Áreas de dentro:** sem nenhuma, uma linha ("`<Área>` não tem áreas de dentro: quem responde por ela responde por
   todas as frentes"). Com elas, uma linha por área de dentro: o nome, o que cuida, quem responde e quem substitui (nome:
   é a estrutura da área, e o LivupOS já mostra esses nomes), com link para `../<id>/visao-geral.md` só se ela já
   existe com visão geral; senão, sem link. Área de dentro sem quem responde: "por enquanto, com quem responde por
   `<Área>`". Diga uma vez que cada área de dentro mantém o próprio contexto e que quem responde pela área responde
   pelo todo.
3. **Frentes:** só se houver (pedaço sem responsável próprio): uma linha por frente, o propósito e a referência
   (papel), com link para a visão geral dela só se ela já está publicada ou sai na mesma leva. No mínimo, sem link.
4. **Quem é quem:** os papéis que decidem e respondem na área, além dos de cima.
5. **Rituais:** uma linha por ritual: objetivo, quem participa (papéis), cadência, o que se decide nele.
6. **Com quem a área se relaciona:** outras áreas, parceiros e fornecedores (a empresa, nunca a pessoa de contato), e
   o que fica combinado, sem valores.
7. **Sistemas e apps:** sistemas de tech como link para `tech/sistemas`; sistemas da área com link para o documento
   na lista `sistemas/`, ou o nome sem link, "na próxima leva". **Fonte que guarda dado de pessoas** (a planilha de
   headcount, com salários; um controle de afastamentos; a lista de motoristas com documentos): aparece como fonte que existe, numa linha, com o assunto, quem
   cuida (o papel, ou o nome se é quem responde por uma área de dentro) e "para acesso, peça a `<quem cuida>`", sem
   link e sem nenhum número ou campo dela. Não ganha documento próprio.
8. **Indicadores:** uma linha por indicador publicado, com link. No mínimo, a seção não entra.
9. **O que este contexto responde:** 5 a 15 perguntas reais que alguém de fora faria à área, cada uma com o documento
   (ou a área de dentro) que responde. No mínimo, o normal é apontar a área de dentro ("Como abro uma vaga? →
   Recrutamento"). Pergunta sem resposta publicada aponta "Em aberto". Se as perguntas foram deduzidas, diga isso ao
   mostrar e marque-as como sugestão para o diretor trocar.

A estratégia e os projetos não têm seção até chegarem (depois do retreat): link para pasta que não existe não entra.
Se passar de 3 mil tokens, encurte os rituais e os apps antes de cortar perguntas.

## Visão geral da frente

`<area>/<frente>/visao-geral`, `tipo: referencia`. Curta: é o índice da pasta. **A lista dos documentos é gerada pelo
LivupOS na leitura; não escreva a lista.**

```markdown
---
tipo: referencia
titulo: "<Frente> (<Área>)"
resumo: "<o propósito da frente, numa frase>"
---

# <Frente>

> Fonte: <fontes e datas>.

<Duas a quatro frases: para que a frente existe, o que cobre e o que não cobre (e onde está o que não cobre).>

Referência: <papel> (a quem perguntar). Quem aprova o que entra aqui é quem responde por <Área>.

Indicadores que esta frente acompanha: <links para `../indicadores/<indicador>.md`, se houver>.

## Em aberto
- <o que falta>. Responde: <papel>.
```

## Sistema da área

`<area>/sistemas/<sistema>` (mais de uma frente usa) ou `<area>/<frente>/sistemas/<sistema>` (só uma frente usa),
`tipo: referencia`, `tags: [sistema]`. Opcional, depois do mínimo (`SKILL.md`, etapa 5). Este molde vence o "copie os vizinhos":
se a área já tem fichas de sistema mais longas (telas, o que o app grava, código), siga este molde no documento novo e
não mexa nas antigas.

**Quem ganha este documento.** Decida nesta ordem, e pare no primeiro que vale:
1. **Sistema de tech:** tem documento em `tech/sistemas/*` (inteiro ou só da integração), ou tech contratou ou
   mantém. Só link. Se o documento de tech é só da integração, o sistema vai para "o que falta fora da área"
   (`area-e-ontologia.md`). Exemplo: a Abbiamo, que o Last Mile opera todo dia, é de tech.
2. **Ferramenta de uso geral da empresa** (Slack, Google Workspace, Notion, Claude): não é sistema da área; no máximo
   uma linha na visão geral.
3. **Sistema de outra área** (o app de Compras que o time consulta): link para o documento da área dona, ou o nome e a
   área em texto. Não ganha documento aqui nem vai para "o que falta fora da área".
4. **Sistema da área:** o time é a referência no dia a dia e decide como ele é usado:
   - **app do App Builder** com `owner_area` da área (ou da subárea), em que o time registra, decide ou opera. Quem
     escreveu o código não importa, e rodar na plataforma de apps (de tech) não torna o app "de tech". Painel e
     relatório, que só mostram número, não ganham documento: uma linha na visão geral;
   - **planilha que funciona como sistema:** o time registra e consulta nela (cadastro, controle, fila); planilha só
     de análise não ganha documento;
   - **sistema externo que a área contrata e administra** (o time escolhe o fornecedor e dá o acesso).
5. **Na dúvida,** pergunte ao diretor, com as duas opções.

**Onde mora.** Na lista `sistemas/` da raiz da área, se mais de uma frente o usa, ou se a frente que o usa ainda não
tem visão geral publicada; na da frente, se só ela usa e ela já existe. Sistema
que é de uma área de dentro (o sistema que só ela opera) mora na área de dentro e entra pela carga dela. App do
App Builder mora na área do `owner_area` dele (a plataforma liga o documento ao app por ali), mesmo que uma área de
dentro o opere: diga isso em "Quem usa". Se a
área já tem uma pasta `sistemas/` (numa área na forma anterior), ela vence (`forma-comum.md`, seção 3).

Curto (meia página a uma página):

```markdown
---
tipo: referencia
titulo: "App de vagas"
resumo: "O app em que gestores pedem vaga e o time de atração acompanha cada uma até a contratação: para que serve, quem usa, quem cuida e o que não fazer nele."
tags: [sistema]
---

# App de vagas

> Fonte: <ficha do app e data, respostas de quem responde pela área, com data, material do time>.

## O que é e para que o time usa
<duas a quatro frases: o problema do dia a dia que ele resolve; não como funciona por dentro. App da plataforma:
cite-o como app `<id-na-plataforma>`, que é como o LivupOS liga o documento ao app>

## Quem usa
<os papéis e times; quem só consulta e quem registra>

## Quem cuida
<a referência (a quem perguntar) e quem administra o acesso, por papel>

## Onde fica
<o endereço do app ou do sistema (app da plataforma: `https://<app>.livup-ai.app`). App da plataforma: também, em texto, o caminho da estrutura que a plataforma gera
(`<area do owner_area>/estrutura-dos-apps/<app>.yaml`) e o dos dados publicados, se houver. Planilha: ver abaixo>

## Ligado a
<uma linha: de que sistema ou planilha ele recebe e para qual manda, com link (sistema de tech) ou nome; sem descrever
a integração, os campos nem a frequência técnica>

## O que não fazer
<os cuidados que o time combinou: o que não se apaga, o que não se edita à mão, o que não se compartilha>

## Em aberto
- <o que falta, com quem responde>
```

Por tipo de sistema:
- **App do App Builder:** a estrutura do banco e os dados publicados a plataforma já gera e mantém; o documento só
  aponta para eles e escreve a parte humana. Ponto de partida: a `description` do app e o que a pessoa confirmar.
  Quem administra o acesso de um app da plataforma: quem o criou e a gestão da área (eles concedem acesso
  individual); diga por papel.
- **Planilha:** o que ela guarda (o assunto, não o conteúdo), quem mantém e com que frequência é atualizada. O link
  só entra se a planilha não guarda dado de pessoa nem financeiro e não está compartilhada como "qualquer pessoa com
  o link"; senão, diga onde ela mora (a pasta ou o drive do time) sem o link. Planilha que guarda dado de pessoas não
  ganha documento: vai como fonte na visão geral (seção 7 da visão geral da área).
- **Sistema externo:** o fornecedor (a empresa, nunca a pessoa de contato), o que o time faz nele e quem administra
  o acesso (papel).

**Nunca entra:** dado do sistema (nem como exemplo), credencial, senha, token, login compartilhado, link com token,
estrutura de tabela ou de colunas copiada, print de tela, valor de contrato, nome de pessoa (papel no lugar). Em área
sensível, nem o assunto de cada aba ou campo que é sobre pessoas: o documento diz para que o time usa, e só.

**Se o material traz credencial, valor de contrato ou dado de pessoa** (uma planilha de ferramentas com a senha do
login do time, por exemplo): não repita o valor em lugar nenhum, nem na conversa. Diga ao owner, numa linha, que a
fonte guarda isso e que o lugar de credencial é o cofre de senhas do time, não a planilha; o resto da fonte pode ser
usado.

## Nota da área (camada fraca)

`contexto_liv_up_depositar`, uma nota por assunto, cada uma com `origem.ref` própria (`carga-inicial/<area>/<slug>`):

- **título:** o assunto em uma linha;
- **conteúdo:** o achado, para quem vai ler sem ter visto a conversa; se é divergência, as duas versões e as fontes; se
  pede mudança num documento, qual e o que muda;
- **proveniência:** fonte (tipo, descrição de ao menos 10 caracteres, link se houver), `afirmado_por` (quem disse, não
  quem registra), `data_fato` (AAAA-MM-DD ou AAAA-MM, nunca futura), `motivo`. Falta algo, pergunte.

`afirmado_por` de cada tipo de nota que a carga monta:

| Nota | `afirmado_por` | `data_fato` |
|---|---|---|
| Lista do que falta fora da área | quem roda a carga (owner ou substituto; confere a lista antes de publicar) | o dia da carga |
| Divergência entre fontes | quem escreveu ou confirmou a versão mais nova: o nome que a fonte dá, ou o papel, se a fonte só registra o papel ("coordenação de Tech, na Daily de 03/11") | a data dessa versão; se nenhuma tem data, a da leitura, e diga isso no conteúdo. Se nenhuma versão diz quem escreveu, quem roda a carga afirma a divergência (que as duas versões existem), na data da leitura |
| Análise de vault pessoal | o autor da análise, que mandou o texto | a data da análise |

Se a fonte não diz quem escreveu, pergunte ao owner; não deposite sem.

## Publicar: `contexto_liv_up_propor_mudanca`

- Até 20 mudanças por chamada; uma chamada por leva (ou duas, se passar de 20).
- `origem`: `{ "tipo": "mcp", "ref": "carga-inicial/<area>/minimo" }` no mínimo e `carga-inicial/<area>/leva-<n>` nas
  levas seguintes (área de dentro: o id dela no lugar de `<area>`).
- A justificativa (até 2.000 caracteres) abre com o Resumo, para o owner que lê no Slack:

```text
Resumo:
- Publica o mínimo de Logística: a visão geral, com as quatro áreas de dentro e quem responde por cada uma, e o glossário geral
- Sai da apresentação da área, das notas do diretor confirmadas por ele e das respostas dele de 26/11

Detalhes: fontes de cada documento, o que foi inferido, o que ficou para a próxima leva e por quê.
```

- 1º item até 160 caracteres, começando pelo efeito ("Publica", "Acrescenta", "Corrige"). Itens seguintes até 300.
- Sem número de decisão, caminho de documento, hash, id ou uuid no Resumo (cite o documento pelo título).
- Se o diretor pediu a marca "não abre" num documento (`fora-da-empresa.md`), um item do Resumo diz qual e por quê.
- Se a justificativa passar de 2.000 caracteres, parta a leva em duas chamadas.
