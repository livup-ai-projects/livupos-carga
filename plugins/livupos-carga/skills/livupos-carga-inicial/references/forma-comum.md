# A forma comum das áreas (estrutura 3)

Toda área do LivupOS (diretoria, área de dentro e `liv-up`) tem a mesma forma. A versão 3 foi decidida pelo dono do LivupOS em
25/11/2026 (D144) e substitui a 2 (23/11/2026) para toda área nova. A carga monta a área nela desde o mínimo. A forma é
dado, não invenção desta skill: a definição mora no contrato da plataforma (versão 3), e este arquivo a resume. As
regras do `SKILL.md` (ok para publicar, dado de pessoa fora, nenhuma mensagem) não dependem dela.

**Depende da v3 no ar.** Enquanto a plataforma devolver `versao_atual: 2`, a carga monta a estrutura e o rascunho do
mínimo, mas não publica (seção 0, item 6).

## 0. De onde vem a forma

O `contexto_liv_up_listar` com `estrutura: true` devolve a forma das áreas:

- `estrutura.versao_atual`: a versão da forma (3 com a v3 no ar; 2 antes);
- `estrutura.versao_da_area`: a versão em que a área está, ou nulo, se ela não tem versão;
- `estrutura.definicao`: os documentos básicos (nome, tipo, se é coleção, se é obrigatório), as pastas reservadas, as
  regras (cada uma com o nível e o modo) e, da v3 em diante, `minimo_d0` (o que nasce no mínimo), `niveis` (o que pode
  ficar na raiz da área e na raiz de uma frente) e `listas` (as listas combinadas, como `incidentes/`, com
  `sugerida_em`);
- `pastas_abertas_para_a_empresa`: as pastas que a empresa toda lê, mesmo numa área fechada;
- `responsaveis`: quem responde e quem substitui na área, a área de cima e as áreas de dentro (`SKILL.md`, etapa 1).

`toda_area` diz se a regra vale para a área inteira; `nao_e_regra` lista o que a forma descreve sem ser regra: não
aplique como regra.

Regras para usar:

1. **Com o campo e a versão 3, a definição vale** onde divergir deste arquivo, só para a forma (onde cada coisa mora e
   o tipo dos documentos básicos que a carga cria). Fora esse tipo, os moldes e o resto da skill não mudam.
2. **Forma anterior** se decide por `versao_da_area` diferente de 3 (nulo ou 2), numa área que já tem documentos,
   **a menos que a visão geral da raiz já declare `estrutura: 3`** (a área que a carga montou com a plataforma ainda
   na 2): essa é estrutura 3, qualquer que seja o `versao_da_area`.
   **Documentos** aqui são os da área, fora `agentes/`, `notas/`, as pastas que a plataforma escreve (`foruns/`,
   `canais/`, `curadoria/`, `dados-publicados/`, `estrutura-dos-apps/`, `ontologia/`) e as pastas reservadas que só
   têm a visão geral de texto fixo: elas não fazem uma área vazia virar antiga.
3. **A skill garante sozinha** (a plataforma começa só observando):
   - o `estrutura: 3` gravado como número inteiro, sem aspas, na visão geral da raiz;
   - o glossário geral em `<area>/glossario` (documento), os temas, quando houver, em `<area>/glossario/<tema>`, e os
     indicadores em `<area>/indicadores/`, nunca dentro de frente;
   - nada solto: na raiz da área só a visão geral e pastas; na raiz de uma frente, só a visão geral dela;
   - o tipo dos documentos básicos que a carga **cria**: o de `documentos_basicos[].tipo`, com o campo; o de
     `moldes.md`, sem ele. Esse tipo vence o "copie o tipo dos vizinhos". Documento que já existe mantém o tipo que tem.
4. **Forma que a skill não conhece:** `versao_atual` maior que 3, ou `pastas_abertas_para_a_empresa` diferente de
   `["estrategia", "projetos"]`. Uma forma nova pode pedir documento básico sem molde aqui, ou abrir para a empresa
   uma pasta que a skill não avisaria.
   - Na carga: faça a etapa 1 e a 2 (a estrutura e o pedido ao admin não dependem da forma dos documentos) e monte o
     mínimo como rascunho, sem publicar. Diga o texto de `references/conducao.md`, "Forma desconhecida", na parada 1 e
     de novo antes de mostrar o rascunho.
   - Na sessão só de estratégia: confira e mostre o que falta (etapa de estratégia, até antes da parada 7), sem
     publicar, e entregue `estrategia-2027-<area>-conferida-AAAA-MM-DD.md`.
   - Não publique nada. Registre no plano a forma "desconhecida, não publicar", a versão que veio e o que a definição
     traz de novo. Entregue o plano e o rascunho e encerre, sem checklist e sem registrar resultado.
5. **Sem o campo no schema** (conector antigo): use este arquivo e siga, sem travar. Diga na parada 1 como reconectar
   (`conducao.md`, etapa 1). **Com o campo, mas a chamada falhou** ou voltou sem `estrutura`: tente uma vez de novo; se
   não vier, use este arquivo e siga, sem falar em conector antigo.
6. **`versao_atual: 2` (a v3 ainda não está no ar; decisão de 25/11: esperar a v3).** Faça a etapa 1 e a 2 (a
   estrutura e o pedido ao admin não dependem da versão) e monte o mínimo como rascunho, **sem publicar**. Diga o texto
   de `references/conducao.md`, "A forma nova ainda não entrou", antes de mostrar o rascunho. Registre no plano "mínimo
   pronto, espera a v3" e entregue o rascunho no plano, para publicar na retomada. As mensagens às áreas de dentro
   esperam a publicação, como sempre. Não há fechamento com registro de resultado.

## 1. A árvore

```
<area>/
├── visao-geral          estrutura: 3 no frontmatter. O que a área faz, as áreas de dentro (com quem responde
│                        por cada uma), as frentes, rituais, com quem se relaciona, perguntas que mais chegam
├── glossario           o glossário geral (documento): os termos que valem para a área inteira; é o do mínimo
├── glossario/           os temas, quando um assunto crescer: um documento do tipo glossario por tema
│   └── <tema>
├── indicadores/         lista: um documento por indicador (opcional, depois do mínimo)
│   └── <indicador>
├── geral/               o que vale para a área inteira (uma política, um ritual com regra própria)
├── <lista>/             itens do mesmo tipo, nome no plural (sistemas/, fornecedores/), sem visão geral
├── <frente>/            pedaço estável do trabalho sem responsável próprio (seção 2)
│   ├── visao-geral      o propósito da frente; a lista dos documentos é gerada pelo LivupOS
│   ├── geral/           o que vale para a frente inteira
│   └── <lista>/         itens do mesmo tipo dentro da frente
├── estrategia/          reservada: entra depois do retreat (seção 4)
└── projetos/            reservada: entra depois do retreat (seção 4)
```

A área de dentro é da diretoria na hierarquia (a área de cima), mas os documentos dela começam pelo id dela, que leva
o da diretoria na frente (`logistica-last-mile/...`), com a mesma forma (seção 7). A carga não cria
`agentes/` nem `notas/` (são da plataforma).

**O mínimo** (`minimo_d0` da definição) é o que toda área publica antes de qualquer outra coisa: a visão geral, as
áreas de dentro (criadas pelo admin, com quem responde por cada uma, e listadas na visão geral) e o
glossário geral, em `<area>/glossario`. Pasta vazia não existe: `geral/`, listas, `indicadores/`, `estrategia/` e `projetos/` só nascem
quando têm o primeiro documento.

**Documentos básicos** são `visao-geral`, `glossario` (com a pasta `glossario/` dos temas) e `indicadores/`, sempre na
raiz da área. O documento `glossario` e a pasta `glossario/` convivem, como um sistema e a pasta dele em `tech/sistemas`.
- Glossário e `indicadores/` nunca vão dentro de frente nem de `geral/`. O indicador que uma frente acompanha mora em
  `<area>/indicadores/` e a visão geral da frente aponta para ele.
- A visão geral da área é o único documento com `estrutura: 3` no frontmatter. É ela que diz em que versão a área está.
- Listas (`indicadores/`, `sistemas/` e as outras) não têm visão geral: a lista é gerada pelo LivupOS. As pastas
  reservadas (`estrategia/`, `projetos/`) não são listas: têm a visão geral de texto fixo (seção 4).
- Moldes: `moldes.md` (visão geral da área e da frente, indicador, glossário, sistema da área).

## 2. O que é frente, e o que é área de dentro

O teste é a pergunta da etapa 2: **o pedaço tem alguém que cuida do dia a dia?** "Cuidar" aqui é responder pelo
contexto daquele pedaço (manter em dia e aprovar o que muda), não só executar o trabalho: num time pequeno, cada
analista faz um pedaço, mas quem responde por todos é a mesma pessoa, e os pedaços são frentes. Na área de dentro, o
normal é tudo frente; área de dentro dela só quando um pedaço tem quem responda por ele, diferente de quem responde pela
área.

- **Tem:** é **área de dentro** (subárea, no vocabulário da plataforma). Pode ser uma gerência ou uma frente de
  trabalho. Tem quem responde e quem substitui, mantém o próprio contexto e aprova as mudanças dele; o diretor segue
  respondendo pelo todo. O critério antigo ("só quando muda quem decide ou quem lê") não vale mais.
- **Não tem** (um assunto estável que o próprio diretor ou o time todo cuida): é **frente**, uma pasta dentro da área,
  sem responsável na plataforma; quem aprova o que entra é quem responde pela área. Na dúvida, pergunte ao diretor se
  há alguém que cuida daquilo no dia a dia; se não há, é frente.
- **Não é frente nem área de dentro:** tipo de documento (`processos/`, `politicas/`: tipo é metadado, não pasta),
  projeto (vai em `projetos/`, depois do retreat), pessoa, sistema ou parceiro (viram lista).
- **Sem frente dentro de frente.** Um pedaço de uma frente que tem responsável próprio vira área de dentro.
- Nome de frente: substantivo, minúsculas, sem acento, com hífen.

## 3. `geral/` e listas

Em cada nível (a raiz da área e a raiz de cada frente), ou o documento vale para o nível inteiro e vai em `geral/`, ou
é item de um conjunto e vai numa lista (pasta no plural). Nada solto ao lado das pastas.

- `geral/` não vira depósito: com três ou mais documentos do mesmo tipo em `geral/`, sugira uma lista.
- Lista: nome do item no plural, sem visão geral. Item é um documento ou, quando tem vários documentos, uma pasta.
- Lista que cresce no tempo começa o nome do item pela data (`2026-11-03-queda-do-checkout`).
- `sistemas/` (os sistemas da área, `moldes.md`, "Sistema da área") mora na raiz da área quando mais de uma frente usa
  o sistema, e dentro da frente quando só ela usa. Nasce com um item só.
- `incidentes/` é lista opcional combinada na definição, mas **piloto só com Tech**: a carga não a sugere a outras
  áreas (`listas[].sugerida_em`).
- Área na forma anterior que já tem uma pasta `sistemas/`: ela vence; o sistema novo vai para ela, e a carga não move
  as fichas que já existem.

## 4. As pastas reservadas: `estrategia/` e `projetos/`

Ficam fora do mínimo e fora das levas da carga: a estratégia (objetivos e metas do ano) e os projetos saem do retreat
de 01 a 03/12, montados pelo time central, e entram pela etapa de estratégia, conferidos por quem responde pela área
(`references/estrategia.md`). A pasta nasce com o primeiro documento dela, junto com a visão geral de texto fixo abaixo.
Meta, projeto ou plano do ano achados no material da carga vão para o plano local como "espera a estratégia"
(`assets/plano-modelo.md`), sem publicar.

As duas pastas são abertas para a empresa toda por regra da Liv Up, mesmo numa área fechada. Por isso o texto é fixo,
genérico e sem nada da área além do nome. Se a lista `pastas_abertas_para_a_empresa` vier diferente desse par, a forma é
desconhecida (seção 0, item 4).

Se a pasta já existe na área, não crie de novo nem altere. Exceção: na etapa de estratégia, se a visão geral não é o
texto fixo, a skill oferece trocar, com o ok de quem responde (`references/estrategia.md`, seção 4).

**`<area>/estrategia/visao-geral`** (troque só `<Área>`; estas visões gerais não têm a linha `> Fonte:`):

```markdown
---
tipo: referencia
titulo: "Estratégia de <Área>"
resumo: "Onde ficam os objetivos e as metas de <Área> para cada ano, ligados à estratégia da Liv Up."
---

# Estratégia de <Área>

Esta pasta guarda a estratégia de <Área>: os objetivos e as metas de cada ano, num documento por ano, ligados aos
objetivos da Liv Up. A meta fica aqui; o número medido fica na fonte que o documento de cada indicador aponta.

A pasta é preenchida com a estratégia de cada ano.
```

**`liv-up/estrategia/visao-geral`** (a da empresa: o texto acima ficaria circular em `liv-up`):

```markdown
---
tipo: referencia
titulo: "Estratégia da Liv Up"
resumo: "Onde ficam os objetivos e as metas da Liv Up para cada ano, que as diretorias desdobram nas metas delas."
---

# Estratégia da Liv Up

Esta pasta guarda a estratégia da Liv Up: os objetivos e as metas da empresa de cada ano, num documento por ano. Cada
diretoria desdobra essas metas nas metas dela, na pasta de estratégia da própria área. A meta fica aqui; o número medido
fica na fonte que o documento de cada indicador aponta.

A pasta é preenchida com a estratégia de cada ano.
```

`liv-up` só ganha `projetos/visao-geral` se tiver projeto, com o texto abaixo trocando "de `<Área>`" por "da Liv Up"
e "de que `<Área>` é dona" por "de que a Liv Up é dona".

**`<area>/projetos/visao-geral`**:

```markdown
---
tipo: referencia
titulo: "Projetos de <Área>"
resumo: "Onde ficam os projetos de que <Área> é dona, uma pasta por projeto."
---

# Projetos de <Área>

Esta pasta guarda os projetos de que <Área> é dona: uma pasta por projeto, com a visão geral dele (por que existe, a
que objetivo serve, quem responde, de que depende). Datas e andamento não ficam aqui. Quando um projeto acaba, o
que vale para sempre vai para a área.
```

## 5. Regras de lugar

- Tipo é metadado, não pasta.
- Processo que cruza áreas mora na área que conduz o ritual; se nenhuma conduz, é de `liv-up` (a carga não escreve
  lá: vira pergunta a quem responde pela área).
- O que é dado (relatório mensal) ou artefato (slides, modelos, vídeos de treinamento) não entra: o documento aponta
  para onde está.
- O que é entidade de sistema (produto, loja, canal) mora na ontologia; a área guarda só a regra
  (`area-e-ontologia.md`).
- O limite prático é área → frente → (`geral/` ou lista) → item.

## 6. Área que já tem documentos em outra forma

Se a área já tem documentos (seção 0, item 2) e não está na versão 3, ela está na forma anterior. **A carga não migra:**
a migração tem plano próprio, com prévia e aprovação de quem responde. Nesse caso, diga numa frase na parada 1 e siga
assim:

- o novo entra na forma 3 (tema novo de glossário em `glossario/<tema>`, indicador novo em `indicadores/`), sem mover,
  renomear nem arquivar o que existe; exceção: sistema da área novo vai para a pasta `sistemas/` que a área já tem;
- se a área já tem glossário em `<area>/glossario`, a carga **altera** esse glossário; se os termos dela estão noutro
  formato (`glossario-<tema>` na raiz, ou só temas em `glossario/`), a carga acrescenta onde ela já tem, sem mover;
- documento que já existe e trata do mesmo assunto é alterado no lugar dele, não duplicado;
- a visão geral existente não ganha `estrutura: 3` (quem marca é a migração).

## 7. Área de dentro

A área de dentro tem a mesma forma: visão geral com `estrutura: 3`, `glossario` e `indicadores/` próprios na raiz
dela, frentes, `geral/` e listas. **O caminho começa pelo id dela**, que leva o da diretoria na frente (`logistica-last-mile/visao-geral`,
`people-dp/glossario`; `subareas.md`, seção 3). Na hierarquia ela é da diretoria. Dos termos da diretoria, só os que a área de dentro
usa vão em "Termos de outras áreas" do glossário dela, cada um com uma linha e o link para o glossário da diretoria
(uma cópia só: a definição mora lá). A carga da área de dentro é feita por quem responde por ela,
com esta mesma skill, depois que a diretoria publicou o mínimo dela. Na etapa 2 dela, a pergunta é a mesma: um pedaço
com quem cuide do dia a dia vira área de dentro da área de dentro (a plataforma aceita três níveis: diretoria, área de
dentro e a de dentro dela). No terceiro nível, todo pedaço é frente.
