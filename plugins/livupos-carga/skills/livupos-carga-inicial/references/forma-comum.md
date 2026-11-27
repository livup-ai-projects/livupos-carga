# A forma comum das áreas (estrutura 4: a raiz fixa)

Toda área do LivupOS (diretoria, área de dentro, a área de dentro dela e `liv-up`) tem a **mesma raiz**, com os mesmos
nomes. A versão 4 foi decidida pelo dono do LivupOS em 27/11/2026 (a raiz fixa) e substitui a 3 (25/11/2026) para toda
área nova: a liberdade de organização fica **dentro** de `geral/`, e `sistemas/` é base de toda área. A carga monta a
área nela desde o mínimo. A forma é dado, não invenção desta skill: a definição mora no contrato da plataforma (versão
4), e este arquivo a resume. As regras do `SKILL.md` (ok para publicar, dado de pessoa fora, nenhuma mensagem) não
dependem dela.

**Depende da v4 no ar.** Enquanto a plataforma devolver `versao_atual` menor que 4, a carga monta a estrutura e o
rascunho do mínimo, mas não publica (seção 0, item 6).

## 0. De onde vem a forma

O `contexto_liv_up_listar` com `estrutura: true` devolve a forma das áreas:

- `estrutura.versao_atual`: a versão da forma (4 com a v4 no ar; 3 ou 2 antes);
- `estrutura.versao_da_area`: a versão em que a área está, ou nulo, se ela não tem versão;
- `estrutura.definicao`: os documentos básicos (nome, tipo, se é coleção, se é obrigatório; na 4, com `sistemas/`),
  as pastas reservadas, as regras (cada uma com o nível e o modo), `minimo_d0` (o que nasce no mínimo), `niveis` (na
  4, só o da área), `pastas_da_plataforma` (as pastas que a plataforma grava por caminho fixo) e, da 4 em diante,
  `raiz_permitida` (tudo o que pode estar na raiz: "/" no fim é pasta, sem "/" é documento; inclui as pastas da
  plataforma, que a skill não cria) e `nomes_reservados_em_geral` (os nomes que nenhum segmento abaixo de `geral/`
  pode ter);
- `pastas_abertas_para_a_empresa`: as pastas que a empresa toda lê, mesmo numa área fechada;
- `responsaveis`: quem responde e quem substitui na área, a área de cima e as áreas de dentro (`SKILL.md`, etapa 1).

`toda_area` diz se a regra vale para a área inteira; `nao_e_regra` lista o que a forma descreve sem ser regra: não
aplique como regra. Campo da definição que este arquivo não cita: leia e siga, se ele só detalha o que está aqui (um
nome a mais na lista dos reservados, uma descrição); se ele pede o que a skill não sabe fazer, é forma desconhecida
(item 4).

Regras para usar:

1. **Com o campo e a versão 4, a definição vale** onde divergir deste arquivo, só para a forma (onde cada coisa mora,
   o que pode ficar na raiz, `raiz_permitida`, os nomes reservados, `nomes_reservados_em_geral`, e o tipo dos
   documentos básicos que a carga cria). Fora isso, os
   moldes e o resto da skill não mudam.
2. **Forma anterior** se decide por `versao_da_area` abaixo de 4 (nulo, 2 ou 3), numa área que já tem documentos,
   **a menos que a visão geral da raiz já declare `estrutura: 4`** (a área que a carga montou com a plataforma ainda
   abaixo da 4): essa é estrutura 4, qualquer que seja o `versao_da_area`. A área na 3 tem um caso próprio (seção 6,
   "Área na estrutura 3").
   **Documentos** aqui são os da área, fora `agentes/`, as pastas da plataforma (`foruns/`, `canais/`, `notas/`,
   `curadoria/`, `dados-publicados/`, `estrutura-dos-apps/`, `ontologia/` e `ontologia.yaml`), os pedidos que a
   plataforma grava em `sistemas/<app>/pedidos` e as pastas reservadas que só têm a visão geral de texto fixo: eles
   não fazem uma área vazia virar antiga.
3. **A skill garante sozinha** (a plataforma começa só observando):
   - o `estrutura: 4` gravado como número inteiro, sem aspas, na visão geral da raiz;
   - **na raiz, só os nomes da raiz fixa** (seção 1): nenhum documento solto, nenhuma pasta de frente, de tipo ou de
     lista ao lado de `geral/`;
   - o glossário geral em `<area>/glossario`, os temas, quando houver, em `<area>/glossario/<tema>`, os indicadores
     em `<area>/indicadores/` e os sistemas em `<area>/sistemas/`, nunca dentro de `geral/`;
   - **dentro de `geral/`, nenhum nome reservado**, em nível nenhum (seção 3);
   - **nunca cria as pastas da plataforma** (`foruns/`, `canais/`, `notas/`, `curadoria/`, `dados-publicados/`,
     `estrutura-dos-apps/`) nem `agentes/`, `ontologia/`, `ontologia.yaml` ou `sistemas/<app>/pedidos`: quem escreve
     nelas é a plataforma;
   - o tipo dos documentos básicos que a carga **cria**: o de `documentos_basicos[].tipo`, com o campo; o de
     `moldes.md`, sem ele. Esse tipo vence o "copie o tipo dos vizinhos". Documento que já existe mantém o tipo que tem.
4. **Forma que a skill não conhece:** `versao_atual` maior que 4, ou `pastas_abertas_para_a_empresa` diferente de
   `["estrategia", "projetos"]`. Uma forma nova pode pedir documento básico sem molde aqui, ou abrir para a empresa
   uma pasta que a skill não avisaria.
   - Na carga: faça a etapa 1 e a 2 (criar as áreas de dentro e o pedido ao admin não dependem da forma dos documentos) e monte o
     mínimo como rascunho, sem publicar. Diga o texto de `references/conducao.md`, "Forma desconhecida", na parada 1 e
     de novo antes de mostrar o rascunho.
   - Na sessão só de estratégia: confira e mostre o que falta (etapa de estratégia, até antes da parada 7), sem
     publicar, e entregue `estrategia-2027-<area>-conferida-AAAA-MM-DD.md`.
   - Não publique nada. Registre no plano a forma "desconhecida, não publicar", a versão que veio e o que a definição
     traz de novo. Entregue o plano e o rascunho e encerre, sem checklist e sem registrar resultado.
5. **Sem o campo no schema** (conector antigo): use este arquivo e siga, sem travar. Diga na parada 1 como reconectar
   (`conducao.md`, etapa 1). **Com o campo, mas a chamada falhou** ou voltou sem `estrutura`: tente uma vez de novo; se
   não vier, use este arquivo e siga, sem falar em conector antigo.
6. **`versao_atual` menor que 4 (a v4 ainda não está no ar; decisão de 27/11: a carga e a v4 entram no mesmo dia).**
   Faça a etapa 1 e a 2 (criar as áreas de dentro e o pedido ao admin não dependem da versão) e monte o mínimo como
   rascunho, já na forma 4, **sem publicar**: publicar antes deixaria uma marca de versão que a plataforma ainda não
   conhece. Diga o texto de `references/conducao.md`, "A forma nova ainda não entrou", antes de mostrar o rascunho.
   Registre no plano "mínimo pronto, espera a v4" e entregue o rascunho no plano, para publicar na retomada. As
   mensagens às áreas de dentro esperam a publicação, como sempre. Não há fechamento com registro de resultado.
   **Vale para toda publicação da carga**, não só o mínimo: com `versao_atual` abaixo de 4, nenhuma leva sai
   (sistemas, indicadores, documentos do dia a dia ficam em rascunho no plano), nada leva `estrutura: 4` e nenhuma
   visão geral troca `estrutura: 3` por `4`. A etapa de estratégia segue as regras dela (`estrategia.md`).

## 1. A árvore (a raiz fixa)

A mesma em toda área e em toda área de dentro. **Na raiz, só estes nomes:**

```
<area>/
├── visao-geral          estrutura: 4 no frontmatter. O mapa da área: o que ela faz, as áreas de dentro (com quem
│                        responde por cada uma), quem é quem, os sistemas, onde fica cada coisa de geral/, as
│                        perguntas que mais chegam
├── glossario            o glossário geral (documento): os termos que valem para a área inteira; é o do mínimo
├── glossario/           os temas, quando um assunto crescer: um documento do tipo glossario por tema
│   └── <tema>
├── geral/               o conteúdo do time, LIVRE por dentro (seção 3): qualquer subpasta, qualquer profundidade
│   ├── <documento>      o que vale para a área inteira (uma política, um ritual com regra própria)
│   └── <frente>/        um pedaço do trabalho sem responsável próprio (seção 2), ou uma pasta por tipo
│       └── ...          (geral/fornecedores/, geral/contratos/, geral/processos/)
├── sistemas/            um documento por sistema de que a área é dona: a ficha (seção 3). Base de toda área
│   └── <sistema>
├── indicadores/         um documento por indicador (opcional, depois do mínimo)
│   └── <indicador>
├── estrategia/          reservada: entra depois do retreat (seção 4)
└── projetos/            reservada: entra depois do retreat (seção 4)
```

Também podem estar na raiz, mas **a skill nunca cria nem mexe:** `agentes/` (reservada, da plataforma de agentes) e as
pastas da plataforma, `foruns/`, `canais/`, `notas/`, `curadoria/`, `dados-publicados/`, `estrutura-dos-apps/`,
`ontologia/` e `ontologia.yaml` (o que a definição devolver em `pastas_da_plataforma`). Elas guardam o que a plataforma
grava por caminho fixo (atas, canais, notas, critérios da curadoria, a estrutura e os dados publicados dos apps) e não
mudam de lugar (a tela do LivupOS pode vir a agrupá-las, mas o caminho é este; não fale disso ao diretor).

A área de dentro é da diretoria na hierarquia (a área de cima), mas os documentos dela começam pelo id dela, que leva
o da diretoria na frente (`logistica-last-mile/...`), com a mesma raiz fixa (seção 7).

**O mínimo** (`minimo_d0` da definição) é o que toda área publica antes de qualquer outra coisa: a visão geral, as
áreas de dentro (criadas na carga com o ok de quem responde, ou pelo admin, com quem responde por cada uma, e listadas
na visão geral) e o glossário geral, em `<area>/glossario`. Pasta vazia não existe: `geral/`, `sistemas/`,
`indicadores/`, `estrategia/` e `projetos/` só nascem quando têm o primeiro documento. `sistemas/` é base porque toda
área tem sistemas, não porque nasce vazia: a ficha de cada um entra na etapa 5 (`SKILL.md`).

**Documentos básicos** são `visao-geral`, `glossario` (com a pasta `glossario/` dos temas), `sistemas/` e
`indicadores/`, sempre na raiz da área. O documento `glossario` e a pasta `glossario/` convivem, como um sistema e a
pasta dele em `tech/sistemas`.
- Glossário, `sistemas/` e `indicadores/` nunca vão dentro de `geral/`. O indicador que uma frente acompanha mora em
  `<area>/indicadores/`, e o sistema que só uma frente usa, em `<area>/sistemas/`; o documento da frente aponta.
- A visão geral da área é o único documento com `estrutura: 4` no frontmatter. É ela que diz em que versão a área está.
- `sistemas/` e `indicadores/` não têm visão geral: a lista é gerada pelo LivupOS. As pastas reservadas
  (`estrategia/`, `projetos/`) têm a visão geral de texto fixo (seção 4).
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
- **Não tem** (um assunto estável que o próprio diretor ou o time todo cuida): é **frente**, uma pasta dentro de
  `geral/` (`<area>/geral/<frente>/`), sem responsável na plataforma; quem aprova o que entra é quem responde pela
  área. Na dúvida, pergunte ao diretor se há alguém que cuida daquilo no dia a dia; se não há, é frente.
- **Não é área de dentro:** tipo de documento (`processos/`, `politicas/`: pode virar pasta dentro de `geral/`, se o
  time procura assim), projeto (vai em `projetos/`, depois do retreat), pessoa, parceiro ou fornecedor (pasta dentro de
  `geral/`) e sistema (`sistemas/`, na raiz).
- Um pedaço de uma frente que tem responsável próprio vira área de dentro, com a raiz dela.
- Nome de frente e de pasta: substantivo, minúsculas, sem acento, com hífen, e nunca um nome reservado (seção 3).

## 3. `geral/` e `sistemas/`

**`geral/` é livre por dentro.** O time organiza como procura: documento solto em `geral/` (o que vale para a área
inteira), pasta por frente (`geral/expedicao/`), pasta por tipo (`geral/processos/`, `geral/contratos/`), pasta por
parceiro ou fornecedor (`geral/fornecedores/`), em qualquer profundidade. Não há mais "lista" na raiz nem a regra de
"três do mesmo tipo viram lista": a skill não sugere reorganizar `geral/`.

- **A única regra dentro de `geral/`:** nenhuma pasta nem documento, em nível nenhum, com um nome reservado:
  `foruns`, `canais`, `notas`, `curadoria`, `estrategia`, `projetos`, `indicadores`, `agentes`, `glossario`,
  `sistemas`, `dados-publicados`, `estrutura-dos-apps` (e o que a definição acrescentar). A plataforma reconhece essas
  pastas pelo nome em qualquer profundidade: `geral/x/notas/` fecharia para a empresa sem ninguém saber, e
  `geral/x/foruns/` viraria ata. Se o time chama uma pasta assim, troque o nome (`geral/expedicao/reunioes-do-time/`,
  não `foruns/`) e diga numa linha.
- Sugestão, não regra: área → `geral/` → frente → (subpasta) → documento já cobre quase tudo; mais fundo que isso
  costuma esconder o documento de quem procura.
- Pasta que cresce no tempo começa o nome do item pela data (`geral/fechamentos/2026-11-03-fechamento-de-outubro`).
- A visão geral da área diz onde fica cada coisa de `geral/` (uma linha por pasta, não a lista dos documentos).

**`sistemas/` é base de toda área.** Um documento por sistema de que a área é dona, sempre em `<area>/sistemas/<sistema>`
(nunca dentro de `geral/` nem de uma frente; molde em `moldes.md`, "Sistema da área").

- **Sistema** é aquilo de que um processo da área depende e que tem dono: app da plataforma de apps internos, SaaS ou
  sistema externo que a área contrata, ERP, ou **planilha que é fonte de verdade de um processo** (o time registra nela
  e o processo depende dela: cadastro, controle, fila). Planilha de trabalho ou de análise não é sistema: vai para
  `geral/` (ou não sobe). Ferramenta de uso geral da empresa (Slack, Google Workspace, Notion, Claude) não é sistema
  da área.
- **De quem é a ficha:** da área que administra o sistema (o contrato, a configuração, o acesso; no app da plataforma,
  a área do `owner_area`). **Sistema compartilhado** (o ERP que Compras, Financeiro e Fiscal usam): a ficha mora numa
  área só, a que administra, e as outras leem dali; **o uso de cada área** (como o time usa, a regra do time sobre ele)
  fica no `geral/` dela, com o link para a ficha.
- **Sistema de outra área** (inclusive de tech): não duplica. A visão geral e o documento de uso apontam para a ficha
  do dono, ou dizem o nome e a área em texto, se ela ainda não tem ficha ou se quem roda não a abre (área fechada ou
  sigilosa, como Financeiro). A ficha de um sistema compartilhado não leva `fora_da_empresa`: as áreas que usam
  precisam ler.
- **App da plataforma:** o nome da ficha é o id do app na plataforma (`<area>/sistemas/<id-do-app>`), porque a
  plataforma já grava `sistemas/<id-do-app>/pedidos` ao lado; outro nome deixaria dois itens para o mesmo app.
- Área na forma anterior que já tem uma pasta `sistemas/` dentro de uma frente (`<area>/<frente>/sistemas/`): o
  sistema novo vai para `<area>/sistemas/`, e a carga não move as fichas que já existem.
- `incidentes/` é piloto só com Tech (na 4, dentro de `geral/`: `geral/incidentes/<data>-<assunto>`, `listas[].dentro_de`;
  hoje na raiz de Tech, na forma anterior): a carga não a sugere a outras áreas (`listas[].sugerida_em`).

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

- Cada coisa mora na área **mais específica** que é dona dela (a área de dentro antes da diretoria); a área de cima
  aponta, não duplica (sistemas, documentos de `geral/`, termos).
- Processo que cruza áreas mora na área que conduz o ritual; se nenhuma conduz, é de `liv-up` (a carga não escreve
  lá: vira pergunta a quem responde pela área).
- O que é dado (relatório mensal) ou artefato (slides, modelos, vídeos de treinamento) não entra: o documento aponta
  para onde está.
- O que é entidade de sistema (produto, loja, canal) mora na ontologia; a área guarda só a regra
  (`area-e-ontologia.md`).
- Tipo é metadado no frontmatter; a pasta, dentro de `geral/`, é a que o time procura (pode ser por tipo).

## 6. Área que já tem documentos em outra forma

Se a área já tem documentos (seção 0, item 2) e não está na versão 4, ela está na forma anterior. **A carga não migra:**
a migração tem plano próprio, com prévia e aprovação de quem responde (mover é do admin). Nesse caso, diga numa frase
na parada 1 e siga assim:

- o novo entra na forma 4 (documento novo de uma frente em `geral/<frente>/`, tema novo de glossário em
  `glossario/<tema>`, indicador novo em `indicadores/`, sistema novo em `sistemas/`, na raiz), sem mover, renomear nem
  arquivar o que existe; **exceção:** se a área já tem na raiz uma pasta do mesmo assunto ou do mesmo tipo (Tech:
  `processos/`, `runbooks/`, `incidentes/`; Compras: a pasta de fornecedores), o documento novo vai para ela até a
  migração, para o conteúdo não se partir em dois lugares (as ferramentas da plataforma de Tech ainda gravam ali); na
  dúvida, pergunte ao diretor onde o time procura;
- se a área já tem glossário em `<area>/glossario`, a carga **altera** esse glossário; se os termos dela estão noutro
  formato (`glossario-<tema>` na raiz, ou só temas em `glossario/`), a carga acrescenta onde ela já tem, sem mover;
- documento que já existe e trata do mesmo assunto é alterado no lugar dele, não duplicado, mesmo fora da raiz fixa;
- a visão geral existente não ganha `estrutura: 4` (quem marca é a migração), salvo a da área na 3 que já cabe na 4
  (abaixo);
- anote no plano, seção 1, o que está fora da raiz fixa (as pastas da raiz que não são da seção 1), para a migração.
  É o que a migração vai olhar (não fale de "fora da forma" ao diretor).

**Área na estrutura 3** (`versao_da_area: 3`, ou a visão geral com `estrutura: 3`; Tech e as áreas montadas pela carga
entre 25 e 27/11). Olhe o que ela tem na raiz:

- **Só nomes da raiz fixa** (seção 1), mais as pastas da plataforma e `agentes/`: ela já cabe na 4. Na primeira vez
  que a carga **altera** a visão geral (no mínimo ou numa leva), troque `estrutura: 3` por `estrutura: 4` no
  frontmatter, junto com o resto da mudança, e diga isso no efeito e num item do Resumo ("a visão geral passa a
  declarar a forma nova; nada muda de lugar"). Sem alteração da visão geral, a carga não abre uma só para trocar o
  número. Daí em diante, a área é estrutura 4.
- **Com frente ou lista na raiz** (`<area>/<frente>/` com visão geral, `fornecedores/`, `processos/`, `incidentes/`):
  é forma anterior, como acima. O documento novo vai para `geral/`; o que já existe fica onde está até a migração, com
  o diretor. A visão geral fica com `estrutura: 3`.

## 7. Área de dentro

A área de dentro tem **a mesma raiz fixa**: visão geral com `estrutura: 4`, `glossario`, `geral/` e `sistemas/` dela,
`indicadores/` próprios, se tiver. **O caminho começa pelo id dela**, que leva o da diretoria na frente
(`logistica-last-mile/visao-geral`, `people-dp/geral/folha/...`; `subareas.md`, seção 4, "O id"). Na hierarquia ela é
da diretoria.

- **Cada coisa mora na área mais específica que é dona dela.** O sistema que só a área de dentro administra tem a ficha
  em `<area-de-dentro>/sistemas/`; o processo que só ela conduz, no `geral/` dela. A diretoria **aponta** (uma linha
  na visão geral, com o link), não duplica. O que vale para a diretoria inteira fica na diretoria.
- Dos termos da diretoria, só os que a área de dentro usa vão em "Termos de outras áreas" do glossário dela, cada um
  com uma linha e o link para o glossário da diretoria (uma cópia só: a definição mora lá).
- A estratégia é da diretoria; a área de dentro pode ter projetos e indicadores próprios (`estrategia.md`).

A carga da área de dentro é feita por quem responde por ela, com esta mesma skill, depois que a diretoria publicou o
mínimo dela. Na etapa 2 dela, a pergunta é a mesma: um pedaço com quem cuide do dia a dia vira área de dentro da área de
dentro (a plataforma aceita três níveis: diretoria, área de dentro e a de dentro dela). No terceiro nível, todo pedaço
é frente, em `geral/`.
