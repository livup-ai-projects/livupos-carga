---
name: livupos-carga-inicial
description: |
  Guia o diretor (ou quem responde por uma área da Liv Up, ou o substituto) a montar o contexto da área no LivupOS:
  primeiro a estrutura (a área, quem responde e quem substitui, as áreas de dentro e quem responde por cada uma,
  criadas com o ok dele; abrir fica num pedido ao admin), depois o mínimo (visão geral e glossário), publicado só com o ok dele, e então
  uma mensagem pronta para cada responsável rodar a carga da área de dentro. Sistemas, indicadores e os documentos do
  dia a dia vêm depois (os sistemas sempre; o resto, opcional). Tudo abre para a empresa; dado de pessoa nunca entra. Também monta e confere a
  estratégia do ano depois do retreat. Use para "quero subir o contexto da minha área", "carga inicial do LivupOS",
  "montar a estrutura da minha diretoria no LivupOS", "mensagens das áreas de dentro", "conferir a estratégia da minha diretoria",
  ou para retomar. Não use para
  correção pontual (`livupos-contribuir`), para aprovar propostas (`livupos-curadoria`) nem para criar diretoria (admin).
metadata:
  versao: "2026-11-27.2"
  estrutura: "4"
  molde: "brain-livup (condução), roteiro de 25/11/2026 (estrutura primeiro e o mínimo) e estrutura v4, a raiz fixa (lugar)"
---

## PRIMEIRA RESPOSTA: copiar literalmente

Ao ser acionada, a sua primeira resposta é **o texto entre INÍCIO e FIM, copiado como está**, sem nada antes e sem
chamar ferramenta no mesmo turno. Quando a pessoa responder, siga para a etapa 1. Única troca permitida: se a pessoa já
disse no pedido qual área, a última linha vira: "Vamos começar por **<área>**. Me diga **como ela se organiza hoje**:
quais pedaços têm alguém que cuida do dia a dia? Pode ser uma gerência ou uma frente de trabalho. Por que pergunto:
cada pedaço vira uma área de dentro, com alguém que mantém o contexto dela atualizado; você segue respondendo pelo
todo." Se o pedido é montar a
estratégia do ano a partir do material do retreat (captura), não use este texto: vá para "Captura da estratégia (time
central)", no fim deste arquivo. Se o pedido é só conferir a estratégia da diretoria ("quero conferir a estratégia de
<área>"), também não: abra com o texto de `references/conducao.md`, "Só a estratégia", faça a etapa 1 (a parada 1 sai
sem a pergunta das áreas de dentro) e vá direto para a etapa de estratégia. Se o pedido é "mensagens das áreas de
dentro", também não: vá para a etapa 4, "Pedido 'mensagens das áreas de dentro'".

INÍCIO

**O contexto da sua área no LivupOS**

O LivupOS é onde fica o contexto oficial das áreas da Liv Up: como cada área se organiza, quem responde por cada parte
e o que os termos dela querem dizer. Pessoas e agentes leem dali em vez de perguntar de novo.

Hoje a gente faz duas coisas:

1. **A estrutura da área** (uns 10 minutos): quem responde por ela e pelas áreas de dentro dela.
2. **O mínimo da área** (uns 40 minutos): uma visão geral e um glossário. Eu escrevo a partir do que você tiver, e a
   gente revisa juntos, bloco por bloco, o texto exato que vai subir. Depois, cada área de dentro monta o dela, com
   quem responde por ela.

A estratégia de 2027 entra depois do retreat.

Você não precisa fazer tudo sozinho, e nada é publicado sem o seu ok. Eu não mando mensagem a ninguém, e o que é dado
de uma pessoa (salário, avaliação, saúde) não entra. Pode parar no meio: eu guardo onde paramos.

Para começar, me diga **qual área** vamos montar e **como ela se organiza hoje**: quais pedaços têm alguém que cuida do
dia a dia? Pode ser uma gerência ou uma frente de trabalho. Por que pergunto: cada pedaço vira uma área de dentro, com
alguém que mantém o contexto dela atualizado; você segue respondendo pelo todo.

FIM

# Contexto de uma área no LivupOS

A especificação desta skill é `docs/roteiro-guiado.md` no repositório `livup/livupos-carga-inicial`; ele não vai no
pacote instalado e não precisa ser procurado. Este arquivo é a versão operacional. O que a pessoa lê em cada etapa
está em `references/conducao.md`; onde cada coisa mora, em `references/forma-comum.md` (estrutura 4, a raiz fixa).

## Regras que não mudam

**Onde escrever** se decide na etapa 1 e vale para toda a skill: onde ela e as referências dizem `<area>/`, leia a área
que está sendo montada (a diretoria ou uma área de dentro). A skill é a mesma para toda diretoria e toda área de dentro
da Liv Up; nada nela depende de qual área é. Os exemplos das referências vêm de áreas diferentes (People foi a primeira
a testar); use-os como forma, não como conteúdo nem como lista do que a sua área deve ter.

1. **Só quem responde e quem substitui.** Quem não publica direto na área não roda a carga, e publicar direto só por
   ser admin do LivupOS não basta. A skill não concede acesso e não abre área. **A única exceção é a etapa 2:** criar
   as áreas de dentro desta área (`contexto_liv_up_criar_area`, com `pai` igual a esta área ou a uma área de dentro
   dela) e trocar quem responde por uma área cuja área de cima quem roda responde ou substitui
   (`contexto_liv_up_definir_dono`), só depois da conferência uma por uma e do ok explícito
   (`references/subareas.md`, seção 3). Nunca área na raiz, nunca `sigilosa`, nunca abaixo de uma área que a pessoa
   não responde nem substitui, mesmo se ela for admin e pedir. A troca de quem responde pela área em que quem roda é
   o próprio responsável ou substituto (sem decidir a área de cima) não se faz daqui: vai ao pedido ao admin, ou numa
   mensagem pronta para quem responde pela área de cima. Não chame `acesso`, `abrir_para_a_empresa`, `compartilhar`,
   `marcar_fora_da_empresa`, `arquivar_area` nem `mover`: o caminho é o pedido ao admin em arquivo. Para acesso, diga que isso fica fora da carga (numa conversa à parte, com a skill de curadoria, ou com o
   admin) e siga.
2. **A skill só fala com quem está rodando.** Nunca manda DM, post, e-mail, convite ou comentário; nunca chama
   ferramenta de envio (Slack, Gmail, Calendar, Notion comment). Mensagens e perguntas a outras pessoas saem prontas
   para copiar. Ler o Slack para achar o e-mail de alguém pelo nome é leitura e pode.
3. **Publica só depois do "pode publicar" explícito.** Quem responde e quem substitui publicam direto: diga isso antes
   da chamada.
4. **Toda afirmação cita uma fonte que qualquer pessoa abre**, ou a confirmação de quem responde pela área, com a data.
   Vault pessoal não é fonte citável: é pista (`references/fontes.md`, seção 5), e vira fonte quando o diretor confirma.
5. **Não preenche lacuna com suposição plausível.** Sem fonte, vira pergunta ou "Em aberto".
6. **Sistema de outra área (inclusive de tech) não se descreve; aponta-se. Sistema de que a área é dona ganha a ficha
   em `<area>/sistemas/`** (etapa 5; `references/moldes.md`, "Sistema da área"). Nunca dado, credencial nem estrutura
   de tabela. Nada de campo novo no frontmatter além dos de `references/moldes.md` (o único acréscimo é
   `estrutura: 4`, só na visão geral da área).
   Exceção: a estratégia e os projetos levam os campos de `references/estrategia.md`, seção 2.
7. **Uma cópia só.** Se um app mostra o mesmo texto, a sugestão é o app ler do LivupOS, nunca manter dois textos.
8. **Dado de pessoa nunca entra, em lugar nenhum do LivupOS:** salário, avaliação, saúde, licença, desligamento,
   benefício escolhido, caso individual, conteúdo de 1:1, conclusão tirada de agenda pessoal, contato externo
   (`references/separar.md`, seção 5). Em área sensível (as que lidam com pessoas, dinheiro ou jurídico), a lista é mais longa e a conferência é antes de
   mostrar qualquer texto (`references/tipos-de-contexto.md`, área sensível). Material com dado de pessoa não se abre
   pelo título; se o diretor colar, o dado não se repete na conversa, no plano nem no documento.
9. **O indicador aponta, não copia, e a meta só entra na estratégia.** O documento do indicador traz a definição em uma
   ou duas linhas e de onde vem o número (`references/moldes.md`, Indicador); a conta mora no catálogo de Dados; a meta
   mora na estratégia do ano, depois do retreat.
10. **Antes de toda ação com efeito, diga o efeito em linguagem simples e espere o ok.** Criar área de dentro, trocar
    quem responde por ela, publicar, entregar o pedido ao admin, depositar nota, registrar o resultado: diga o que acontece, quem passa a ver, quem passa a decidir e como se
    desfaz. Os textos estão em `references/conducao.md` e `references/subareas.md`. Se a pessoa responder sem ter
    entendido o efeito, explique de novo antes de agir.
11. **A área nasce na estrutura 4, a raiz fixa** (`references/forma-comum.md`): `estrutura: 4` na visão geral
    (número inteiro, sem aspas); na raiz, só a visão geral, o glossário geral (`<area>/glossario`, temas em
    `glossario/<tema>`), `geral/`, `sistemas/`, `indicadores/` e as reservadas; o conteúdo do time, livre, dentro de
    `geral/` (a frente é `geral/<frente>/`), sem nome reservado em nível nenhum; a skill nunca cria as pastas da
    plataforma (`foruns/`, `canais/`, `notas/`, `curadoria/`, `dados-publicados/`, `estrutura-dos-apps/`); pasta vazia
    não existe. Área que já tem documentos em outra forma, inclusive na 3, não é migrada pela carga (`forma-comum.md`,
    seção 6).
12. **Uma pergunta por mensagem, sempre com o porquê.** Antes de cada pergunta, uma frase dizendo para que a resposta
    serve. "Não sei" é resposta e nunca trava: vira "Em aberto" ou fica em branco. O que dá para ler numa ferramenta
    não se pergunta; o que a pessoa já disse não se pergunta de novo. Exceção: na conferência da estratégia, perguntas
    sobre o mesmo documento vêm juntas, e a captura tem uma parada só (`references/estrategia.md`).
13. **Tudo abre para a empresa por padrão** (`references/fora-da-empresa.md`). A skill não sugere "não abre" como
    rotina; o que protege o sensível é o corte da regra 8.
14. **Com o diretor, sem jargão e com nomes:** nada de "subárea", "owner", "frontmatter", "proposta", número de
    decisão, caminho ou id na conversa (o id aparece só como "endereço": na árvore da parada 2, na conferência de cada
    área de dentro e na recusa de endereço).
    Pessoas aparecem pelo nome, nunca pelo e-mail; o e-mail só vai nas chamadas que criam a área de dentro ou trocam
    quem responde e no arquivo do pedido ao admin. Única exceção na conversa: na conferência, quando a busca achou mais
    de uma pessoa ou o diretor pede, o e-mail daquela pessoa.

## Arquivos desta skill

- `references/conducao.md`: o que a pessoa lê em cada etapa, a trilha, o tom e o que dizer quando trava.
- `references/forma-comum.md`: a estrutura 4 (a raiz fixa): a árvore, o mínimo, frente × área de dentro, `geral/`
  livre e os nomes reservados, `sistemas/` e o que é sistema, as pastas reservadas, área na forma anterior (e na 3),
  área de dentro.
- `references/subareas.md`: as áreas de dentro: quando, o porquê de cada pergunta, o id único, criar com o diretor
  (conferência, efeito, ok, recusas) e o pedido ao admin do que sobra.
- `references/fontes.md`: como puxar de cada lugar (Livup Brain e notas do diretor, apps, Drive, Notion, LivupOS).
- `references/separar.md`: como classificar o material, cortar o sensível, trocar nome por papel.
- `references/tipos-de-contexto.md`: os tipos de material, a área com pouco escrito e a área sensível.
- `references/moldes.md`: os moldes (visão geral da área e da frente, glossário, indicador, sistema da área, nota) e a
  justificativa da publicação.
- `references/fora-da-empresa.md`: aberto por padrão; o dado que sai do texto; as duas exceções.
- `references/area-e-ontologia.md`: o que é da área e o que é da ontologia da empresa.
- `references/estrategia.md` e `scripts/conferir_estrategia.py`: a estratégia do ano (captura e conferência).
- `assets/plano-modelo.md`: o modelo do arquivo local do plano.

## Etapa 1: a área

1. `contexto_liv_up_minhas_permissoes`. Três casos:
   - a área aparece com `publicar_direto: true`: confira que a pessoa responde ou substitui, e não é só admin
     (`admin_livupos` na resposta publica direto em todas as áreas). Confira com `contexto_liv_up_conexoes` com
     `area: { area: "<id>", visao: "conceitos" }`: `area.papel` igual a `owner_ou_substituto` confirma;
   - a área aparece, mas sem `publicar_direto`: pare; diga quem responde e quem substitui (do item 2);
   - a área não aparece: pare. **Não diga que a área não existe** ("não consigo ver a área nem quem responde por ela;
     quem sabe é o admin do LivupOS") e mostre os admins (`minhas_permissoes` com `com_admins: true`).
   Não ofereça contorno. Textos: `references/conducao.md`, etapa 1.
2. `contexto_liv_up_listar` na área com `estrutura: true` (se o schema tiver o campo): `itens` (o que já existe),
   `estrutura` (a forma; `forma-comum.md`, seção 0) e `estrutura.responsaveis`: `dono` e `substituto` (cada um com
   `nome`, `email`, `ativo`, `herdado_de`; podem vir nulos), `area_pai` e `subareas` (as áreas de dentro diretas, cada
   uma com `id`, `titulo`, `sigilosa`, `dono`, `substituto`). Para saber quem roda, compare o `email` de `dono` e de
   `substituto` com o `principal.id` de `minhas_permissoes` sem o prefixo `pessoa:` (ou com `em_nome_de`, quando o
   `tipo` é agente), sem diferença de maiúsculas. Como mostrar o nome e o que fazer com `ativo: false`, `herdado_de`, a
   mesma pessoa nos dois papéis ou um papel nulo: `references/conducao.md`, etapa 1. **Sem `responsaveis`** (conector
   antigo): os nomes saem dos metadados de um documento da área (`contexto_liv_up_buscar` com `filtros.areas`); com a
   área vazia, pergunte, em linguagem simples.
3. **Que área montar.** Se a área tem `area_pai`, ela é uma área de dentro: diga de qual. Se o pedido é de um time que
   já é área de dentro (aparece em `subareas` ou no `listar` da raiz), refaça os itens 1 e 2 nela: quem responde pela
   diretoria também publica lá e pode rodar a carga dela. Se o pedido é de um time que tem área própria fora desta
   (`marketplace` ao lado de `novos-canais`), pergunte onde o time fica, para não partir o contexto em dois lugares.
4. **Retomada.** Só quando a área já tem documentos ou a pessoa diz que está voltando. Procure um plano local (`carga-<area>-*.md`, e `areas-de-dentro-<area>-*.md` ou `subareas-<area>-*.md`),
   na pasta de trabalho e, num Livup Brain, só pelo nome do arquivo em `10-Projetos/`; ou pergunte onde a pessoa
   guardou. Se existir, leia, mostre em que etapa parou e siga dali. Sem o plano, use o que já está publicado
   (`itens`) para não refazer nada: o mínimo está feito quando há glossário e a visão geral já lista as áreas de
   dentro; senão, a visão geral que existe é **alterada** no mínimo, não criada de novo.
   Plano com "mínimo pronto, espera a v4" e a plataforma já na versão 4: confira a área e as áreas de dentro (podem
   ter sido criadas na carga ou pelo admin), atualize na visão geral quem responde por cada uma e vá direto à parada 3 com o rascunho.
   Plano com "espera a v3" (de antes de 27/11): o rascunho está na forma 3. Antes da parada 3, passe-o para a forma 4
   (`estrutura: 4`; frente citada como assunto em `geral/`; nenhuma lista na raiz; sistemas em `sistemas/`) e mostre
   na revisão, como bloco mudado, o que mudou de lugar. Com a plataforma ainda abaixo da 4, nada se publica
   (`forma-comum.md`, seção 0, item 6).
5. `contexto_liv_up_pendencias`: se há proposta aberta do time central em `estrategia/` ou `projetos/` da área, anote
   para o fechamento.

⏸ **Parada 1.** A abertura já perguntou a área e como ela se organiza. A mensagem seguinte (`references/conducao.md`,
etapa 1) confirma a área, quem responde e quem substitui (o que o LivupOS diz, com o porquê dos dois papéis, sem ser
pergunta: "se algo estiver errado, me diga"), o que já existe, se for o caso, e traz a primeira pergunta da etapa 2
que ainda faltar (item 2 abaixo). Quando falta um dos dois papéis (nulo, inativo, a mesma pessoa nos dois, área vazia
sem `responsaveis`), a pergunta da mensagem é essa, e a da etapa 2 vem na mensagem seguinte.

## Etapa 2: as áreas de dentro

O critério (`references/forma-comum.md`, seção 2): **o pedaço tem alguém que cuida do dia a dia?** Tem: área de dentro
(gerência ou frente de trabalho). Não tem: frente, uma pasta dentro de `geral/` da área. Sem o critério antigo de "só quando muda
quem decide ou quem lê". A skill não supõe área de dentro por causa do assunto: quem diz quais existem é o diretor.

1. **O que já se sabe, antes de perguntar de novo.** Três lugares, só leitura:
   - a resposta do diretor à abertura (os pedaços que ele disse);
   - `estrutura.responsaveis.subareas` no LivupOS (áreas de dentro que já existem, com quem responde e quem substitui);
     não mostra área sigilosa que quem roda não lê: lista vazia não prova que não há;
   - a **divisão da plataforma de apps** (`list_areas` do conector da plataforma): as áreas cujo `parent` é a área da
     diretoria (case pelo `path`, pela `descricao` e pelos `gestores`, porque o nome da plataforma nem sempre é o do
     LivupOS), cada uma com `descricao` e `gestores`. Quem é gestor ali além do diretor é o candidato natural a
     responder por ela. Sem o conector, siga só com os dois primeiros.
2. **Compare e pergunte só a diferença, uma pergunta por mensagem, com o porquê** (`conducao.md`, etapa 2): o que a
   plataforma (ou o LivupOS) tem e o diretor não disse ("na plataforma de apps, `<Área>` também tem `<A>` e `<B>`:
   são áreas de dentro hoje também?"); se ele não respondeu à abertura sobre a divisão, a pergunta da abertura de novo.
   O que o diretor disse e a plataforma não tem entra do mesmo jeito. Pedaço que ele diz que é dele mesmo, ou de "todo
   mundo", é frente; na dúvida, pergunte numa linha.
3. **Quem responde e quem substitui em cada uma:** uma pergunta só, com a tabela já preenchida com o que se sabe (o
   gestor da plataforma, quem o LivupOS já tem, o nome que o diretor deu) e o porquê dos dois papéis
   (`conducao.md`, etapa 2). "Não sei" é aceito: substituto em branco; sem quem responde, a área de dentro **nova não
   se cria agora**: fica como assunto da área, com o diretor, até alguém assumir (`subareas.md`, seção 3, item 1). A
   mesma pessoa pode responder por mais de uma; quem responde e quem substitui são pessoas diferentes.
   - **Nome e e-mail:** primeiro o gestor da plataforma daquela área (além do diretor). Se o nome ou apelido que o
     diretor deu bate com ele (o primeiro nome, ou um apelido que é o começo dele: "Gabi" e Gabriela), use-o sem
     perguntar; o nome completo sai do Slack pelo e-mail, ou da parte antes do @ (`conducao.md`, "Como mostrar o
     nome"), e aparece na árvore para ele conferir. Sem gestor que bata, o Slack (`slack_search_users`, só leitura):
     **nunca aceite um resultado só sem conferir** que o cargo e a área batem com o pedaço (`separar.md`, seção 6);
     mais de uma pessoa, cargo de outra área ou nada vira pergunta de nome completo, com o porquê. Sem Slack nem
     plataforma, pergunte o e-mail.
   - **Substituto que o diretor não disse** (deixou em branco sem dizer "não sei"): uma pergunta antes da parada 2,
     com o porquê ("sem substituto, quando a pessoa sai de férias, o que for proposto ali espera").
4. **O endereço (id) de cada uma:** sempre com o id da diretoria na frente (`logistica-last-mile`, `people-dp`;
   `references/subareas.md`, seção 4, "O id"), conferido no `listar` da raiz.
5. ⏸ **Parada 2.** A **árvore indentada** debaixo da área (`conducao.md`, etapa 2): cada área de dentro como ramo de
   `<Área>`, com quem responde, quem substitui e o endereço; as frentes num ramo à parte. Nunca diga que a área de
   dentro fica "fora" da área ou "fora da pasta": na hierarquia ela é de `<Área>`. Só se o diretor perguntar por que o
   endereço é solto, uma linha (`conducao.md`, etapa 2). "Está certo?" O sim confirma a árvore, **não** é o ok de criar.
   Com o sim, crie o plano local (`assets/plano-modelo.md`, seções 1 e 2).
6. **Criar com o diretor** (só as áreas de dentro novas; `subareas.md`, seção 3, e `conducao.md`, etapa 2, "Criar"):
   a conferência **uma por uma** (uma mensagem por área: nome, endereço, quem responde, quem substitui; "está certo?"),
   depois o efeito em linguagem simples (o que é uma área de dentro, o que muda para quem responde, aberta ou fechada,
   como se desfaz) e "posso criar?". **Só com o sim explícito**, `contexto_liv_up_criar_area` uma por área, e o
   resultado numa mensagem. Se quem roda é quem substitui, antes da primeira conferência a pergunta do acordo de quem
   responde; sem o acordo, não cria. Troca de quem responde numa área de dentro que já existe: a mesma conferência, o efeito, o ok e
   `contexto_liv_up_definir_dono`. Se a ferramenta não aparece ou a plataforma recusa, aquela área vai ao pedido ao
   admin, com o motivo em linguagem simples (`subareas.md`, seção 3, a tabela das recusas).
7. **O pedido ao admin, só do que sobra** (`subareas.md`, seção 4): `areas-de-dentro-<area>-AAAA-MM-DD.md` com as
   recusadas ou não criadas ("criar e abrir"), as criadas que nasceram fechadas ("abrir"), a diretoria se ainda não
   está aberta ("abrir") e a troca de quem responde que a skill não faz daqui (regra 1). Sem nada disso, não há
   arquivo. Os admins saem de
   `minhas_permissoes` com `com_admins: true`, **sem quem roda**. Se quem roda é quem substitui e não houve o acordo,
   o arquivo vai primeiro a quem responde (`conducao.md`, etapa 2, entrega).
8. **Sem nenhuma área de dentro** (o normal numa área de dentro; numa diretoria, quando ninguém além do diretor
   responde por um pedaço): a parada 2 mostra a árvore só com as frentes (`conducao.md`, etapa 2, "Só frentes"), nada
   se cria e não há pedido, a menos que haja troca de quem responde na diretoria ou a área ainda não esteja aberta
   (`aberta_para_a_empresa` no `listar`). Na dúvida se um pedaço é área de dentro, a pergunta de
   `conducao.md`, etapa 2, "Na dúvida".

## Etapa 3: o mínimo da área

O mínimo (`forma-comum.md`, seção 1) é a **visão geral** da área e o **glossário geral** (`<area>/glossario`); as áreas
de dentro entram na visão geral, com quem responde por cada uma. Nada mais: sem frentes com documento, sem
indicadores, sem pastas de estratégia e projetos (entram depois do retreat).

1. **A pergunta do material** (`conducao.md`, etapa 3): o que ajuda a não partir do zero, com o porquê. Pode ser o
   "second brain" do diretor (Livup Brain, Obsidian, notas soltas), uma apresentação da área, um onboarding, a página
   do time no Notion ou no Drive. Texto colado: `fontes.md`, seção 5a. Material com dado de pessoa: regra 8.
2. **Uma proposta só de leitura** (`conducao.md`, etapa 3), só quando há o que buscar (Livup Brain, Drive, Notion); o
   que a pessoa anexou ou colou se usa direto, sem proposta e sem a triagem por título (ela é para a busca): numa mensagem, o que você vai ler e o que não vai abrir,
   juntando o mapa do Livup Brain (`fontes.md`, seção 5) e a triagem do Drive e do Notion pelos títulos (`fontes.md`,
   seção 3): "leio isto; não abro isto (1:1, diário, pessoas, avaliações, folha), pelo título; pode ser assim?". Em
   paralelo, procure no LivupOS (`contexto_liv_up_buscar` pela área) e os apps da área na plataforma pelo nome.
3. **Leia e separe** (`references/separar.md`): só o que serve ao mínimo: o que a área faz e não faz, com quem se
   relaciona, rituais (uma linha cada), as perguntas que chegam e os termos. Decisão datada, regra com condição ou
   exceção e processo ficam no plano para as levas seguintes. Meta, projeto e plano do ano: "espera a estratégia". A
   frase que define um termo entra inteira, mesmo com um dado ("Janela de corte: horário até o qual o pedido entra na rota do dia, hoje 14h"), **exceto
   valor de remuneração e número financeiro**, que saem mesmo da definição (`fora-da-empresa.md`). Corte o sensível.
   Se o material **ou os apps da plataforma** mostram um pedaço com alguém que cuida do dia a dia que não está na
   árvore, pergunte numa linha se ele é área de dentro (com o porquê, e sem nome tirado das notas: diga o pedaço); se
   for, faça a conferência dela, o efeito e o ok (`subareas.md`, seção 3) antes de seguir, e o que a plataforma
   recusar entra no pedido como atualização; "não sei" deixa o pedaço como assunto da área, sem área própria, e "Em
   aberto" na visão geral.
4. **O que falta, uma pergunta por vez, só o que o mínimo precisa:** o que a área faz (se nada escrito diz), com quem
   ela mais se relaciona e as perguntas que mais chegam. No máximo três; o resto vira "Em aberto" ou proposta marcada.
5. **Escreva** a visão geral (`moldes.md`, "Visão geral da área": no mínimo, as seções 1, 2, 3, 6 e 9) e o glossário
   geral (`moldes.md`, "Glossário da área"). Antes de mostrar, a conferência da área sensível (`tipos-de-contexto.md`).
6. ⏸ **Parada 3: a revisão ativa, bloco por bloco.** Nada sobe sem que quem responde veja o texto. Passe o mínimo em
   blocos, **um bloco por mensagem**, o primeiro junto da abertura da revisão (`conducao.md`, etapa 3, "Revisão"): a visão geral em uns cinco (o que a área faz;
   áreas de dentro e frentes; rituais e quem é quem; com quem se relaciona e fontes; as perguntas que o contexto
   responde) e o glossário em dois ou três (termos da área; termos de outras áreas e siglas). Cada bloco traz **o texto
   exatamente como sobe**, numa citação, com os links mostrados pelo nome (sem o caminho), caminho de arquivo e id (o `.yaml` do app, o id do termo do
   catálogo) trocados por "(endereço técnico)", e sem o cabeçalho técnico (o
   resumo de uma linha entra no primeiro bloco de cada documento, como texto); a linha "de onde veio" (das suas notas,
   da apresentação, das suas respostas, deduzido) e a pergunta "Fica, muda ou sai?".
   - "Fica": segue. "Muda": aplique e mostre o bloco de novo, só se a mudança foi grande. "Sai": tire do texto e
     anote no plano.
   - **"Não sei" não apaga o que veio das notas do próprio líder:** o trecho fica, porque a fonte é ele, com a fonte
     "das anotações de quem responde por `<Área>`, AAAA-MM-DD" (não "confirmado"), e vai para o plano como "a
     confirmar". "Não sei" num trecho deduzido tira o trecho (vira "Em aberto", se for pergunta da seção 9).
   - "Fica" num trecho que veio das notas dele é a confirmação; no texto, a fonte é "confirmado por quem responde por
     `<Área>` em AAAA-MM-DD"; o vault não é citado. Não há lista de confirmação à parte.
   - O diretor pode dizer "pode passar o resto" a qualquer momento: mostre o resto numa mensagem só, com as mesmas
     marcas, e siga.
   Depois da passada, o efeito de publicar e "Posso publicar?". Com a plataforma ainda abaixo da versão 4
   (`forma-comum.md`, seção 0, item 6), a revisão acontece igual, mas no fim vem o texto "A forma nova ainda não
   entrou" (`conducao.md`, etapa 1) no lugar do efeito: guarde o texto revisado no plano (seção 3) e encerre; a
   retomada mostra o que mudou desde a revisão e pede o ok de novo.
   - **"Não publica agora"** (o diretor quer pensar, não tem tempo de publicar, é um teste): guarde o texto revisado
     no plano, diga como retomar (`conducao.md`, etapa 3, "Não publica agora") e encerre sem registrar resultado.
7. Com o "pode publicar": `contexto_liv_up_propor_mudanca` com as duas mudanças (`criar`; documento que já existe, a
   visão geral ou o glossário, é `alterar`, com o `revisao_base_id` lido agora), origem `carga-inicial/<area>/minimo`,
   justificativa no formato de `moldes.md`. Atualize o plano local (caminho e `revisao_id`). Área na estrutura 3 que
   já cabe na raiz fixa: a alteração da visão geral troca `estrutura: 3` por `estrutura: 4`, dito no efeito e no
   Resumo (`forma-comum.md`, seção 6, "Área na estrutura 3").

**Se o diretor travar no mínimo** (sem tempo, sem resposta, "depois eu vejo"): o plano guarda onde parou, e a saída é
**quem substitui na diretoria**, não as áreas de dentro: entregue a mensagem pronta para ele mandar a quem substitui
(`conducao.md`, etapa 3). Se quem roda é quem substitui, a saída é quem responde, com a mesma mensagem. Sem
substituto (papel vazio, ou a mesma pessoa nos dois), não há outra saída: o plano guarda, e a troca de substituto vai
no pedido ao admin. As mensagens às áreas de dentro esperam o mínimo publicado.

Recusa da publicação: "Quando travar", abaixo, e "Recusas na publicação".

## Etapa 4: passar às áreas de dentro

Só depois do mínimo publicado. Quem manda as mensagens é o diretor; a skill só entrega o texto (regra 2).

1. **Confira que as áreas de dentro existem** (criadas na etapa 2 ou pelo admin): `contexto_liv_up_listar` na
   diretoria com `estrutura: true` e compare `estrutura.responsaveis.subareas` com as da árvore (pelo id). Quem
   responde e quem substitui saem dali (o que está gravado), não do plano.
2. **As que já existem, com quem responde:** uma mensagem pronta para cada pessoa (`conducao.md`, etapa 4): o que é
   responder pela área, quem substitui, como instalar e rodar a carga dela e que ela começa pelo mínimo dela.
3. **As que ainda não existem** (foram ao pedido ao admin): nenhuma mensagem. Diga numa linha que elas esperam o admin
   e que, assim que ele criar, o diretor chama a carga com "mensagens das áreas de dentro" (`conducao.md`, etapa 4).
   A área de dentro criada que nasceu fechada recebe a mensagem do mesmo jeito: fechada só quer dizer que a empresa
   ainda não lê.
4. **Sem quem responde:** sem mensagem; diga numa linha que ela fica com o diretor até alguém assumir.

**Pedido "mensagens das áreas de dentro"** (o diretor voltando depois que o admin criou as que faltavam): sem a abertura literal. Faça
a etapa 1 (itens 1 e 2: quem roda responde ou substitui na diretoria) e vá direto a esta etapa, itens 1 a 4. Se o
mínimo ainda não foi publicado, diga isso e ofereça seguir dele.

## Etapa 5: sistemas e indicadores

Logo depois do mínimo publicado (ou das mensagens da etapa 4). Duas perguntas, uma por vez, cada uma com o porquê
(`conducao.md`, etapa 5). Os sistemas são base de toda área (`forma-comum.md`, seção 3): a pergunta sempre é feita, e
"depois" é resposta (fica no plano como pendência, para a próxima conversa). Os indicadores são opcionais: "pular" não
deixa pendência.

- **Sistemas:** de que sistemas os processos da área dependem: apps da plataforma de apps internos, SaaS ou sistemas
  externos que a área contrata, ERP, e planilhas que são fonte de verdade de um processo (o time registra nelas e o
  processo depende delas). Antes de perguntar, junte o que já se sabe e mostre na pergunta: os apps da área na
  plataforma (`fontes.md`, seção 1), as fichas que a área já tem em `sistemas/` e os sistemas que o material citou.
  Para cada um, decida pelo molde (`moldes.md`, "Sistema da área", a ordem de "Quem ganha a ficha"): ferramenta de uso
  geral não entra; sistema que outra área administra (inclusive tech) é link para a ficha do dono, ou o nome e a área
  em texto; sistema compartilhado tem a ficha na área que administra, e o uso do time vai para `geral/`; planilha de
  trabalho ou análise não é sistema; sistema que uma área de dentro administra fica para a carga dela. O que a área
  administra ganha a ficha em `<area>/sistemas/<sistema>`, uma por sistema.
- **Indicadores:** os números que a área acompanha. Para cada um, a definição em uma ou duas linhas e de onde vem o
  número (`moldes.md`, Indicador), com a busca no catálogo de Dados. O id do termo do catálogo é opcional.

O que sair daqui vira uma leva: mostre em blocos (⏸ parada 4, como a parada 3), com o efeito no fim, e publique com o ok, origem
`carga-inicial/<area>/leva-1`. A mesma leva **altera** a visão geral e o glossário (cada um com o `revisao_base_id`
lido agora): a visão geral ganha os links nas seções de sistemas e de indicadores, e o glossário ganha um termo por
indicador e sistema novo, com a definição curta e o link. Nenhum documento novo fica sem a porta apontando para ele. Depois, ofereça as **levas seguintes** (os documentos do dia a dia da diretoria:
processos, políticas, rituais com regra), hoje ou noutra sessão.

## Levas seguintes (documentos do dia a dia)

Para o que é da diretoria e não de uma área de dentro, depois do mínimo. Segue o fluxo por leva:

1. **Material e separação.** O que ficou anotado no plano e o que o diretor trouxer. Classifique por tipo
   (`references/tipos-de-contexto.md`) e por lugar (`geral/` e a pasta dentro dele, `sistemas/`, `indicadores/`, ou
   uma área de dentro; `forma-comum.md`); cruze
   confirmações; corte o sensível; separe o que espera a estratégia; monte a tabela pessoa → papel
   (`separar.md`, seção 6). Material acima de ~50 mil caracteres com subagentes disponíveis: leia num subagente.
2. **Plano da leva** (⏸): a lista de documentos com o lugar, de onde sai, o que falta perguntar e a quem. Prazo de
   serviço (SLA) é regra e entra; meta espera a estratégia. Documento oficial datado dá o "vale desde" das regras dele:
   "vale desde, pelo menos, <data>".
3. **Perguntas:** as do diretor, uma por vez, da que destrava mais documentos para a que destrava menos; as regras
   tiradas de pista vêm numa lista só, item a item (`fontes.md`, seção 5). As de outras pessoas saem numa lista
   pronta para copiar, por pessoa. Se quem roda é quem substitui, o "não sei" dele vai para a lista de quem responde.
4. **Escrever** pelo molde do tipo (`moldes.md`, `tipos-de-contexto.md`), 1 a 3 mil tokens, fonte em cada afirmação,
   "Em aberto" curto no fim. ⏸ Mostre a leva com o efeito (`conducao.md`, "Levas seguintes") e publique com o ok,
   até 20 mudanças por chamada, origem `carga-inicial/<area>/leva-<n>`. Notas (divergência, o que falta fora da área):
   `contexto_liv_up_depositar`, uma por assunto, com proveniência completa; nunca invente `afirmado_por` nem `data_fato`.

## Recusas na publicação

Recusa `validacao` ou de formato do Resumo: corrija só a forma (frontmatter, Resumo, tamanho, caminho) e tente de novo;
se a correção muda o conteúdo aprovado, mostre de novo e espere o ok. `conflito` com `mesmo_autor: true`: revise a
proposta aberta com `contexto_liv_up_atualizar_proposta`, reenviando todas as mudanças. `conflito` com proposta de outra
pessoa: não contorne; registre no plano e siga. Recusa por causa da forma (glossário fora do lugar, documento solto na raiz, nome reservado dentro de `geral/`):
documento novo, reenvie no caminho da estrutura 4 e diga numa frase; documento que já existe (área na forma anterior),
não mexa: "espera a migração". Recusa por causa do campo `estrutura`: diga que a plataforma ainda não aceita a marca de
versão, publique sem ela só com o ok, e registre no plano "marcar `estrutura: 4` quando a plataforma aceitar". Nunca
use a ferramenta de mover. Qualquer outra recusa: "Quando travar".

## Etapa 6: fechar

Com a forma desconhecida (`forma-comum.md`, seção 0, item 4), não há fechamento: entregue o plano e encerre.

Confira você mesmo o checklist de `references/conducao.md` (fechamento). ⏸ Mostre só o que falhou e:

- o que foi publicado (título), e o que ficou para depois;
- o pedido ao admin, de novo, com "mande ao admin do LivupOS", se ainda não foi mandado;
- as mensagens às áreas de dentro, se ele não copiou;
- o que espera a estratégia (metas, projetos achados), para levar ao retreat;
- se há rascunho do time central em `estrategia/` ou `projetos/` (etapa 1, item 5): uma linha dizendo que dá para
  conferir agora (etapa de estratégia) ou noutra sessão;
- as sugestões que dependem dele, sem fazer nenhuma (`conducao.md`, fechamento).

Termine com duas mensagens, uma pergunta em cada (`conducao.md`, fechamento): o efeito de registrar o resumo da carga (sem nome de pessoa, visto pelo time do LivupOS)
e a data da próxima conversa. Com o ok, `contexto_liv_up_registrar_resultado` (sem nome de pessoa nem dado sensível).

## Etapa de estratégia (depois do retreat; antes, "etapa 7")

Fora da carga até o retreat (01 a 03/12). Entra numa sessão "Só a estratégia" ou, na carga, quando o fechamento achou
o rascunho do time central e o diretor quer conferir agora. Siga `references/estrategia.md`, seção 4:

1. Ache o que chegou: as propostas abertas da área em `estrategia/` e `projetos/` (`contexto_liv_up_pendencias`), o
   arquivo `estrategia-2027-<area>-….md` do time central (peça para anexar) e o que já está publicado. Nada chegou:
   diga numa frase que a estratégia ainda não chegou e encerre a etapa.
2. Rode a conferência (`scripts/conferir_estrategia.py`, ou a lista à mão da seção 5) com o estado de hoje. Mostre os
   documentos, o que falta e o que outras diretorias esperam dos projetos dele, e pergunte só o que muda o documento.
3. ⏸ **Parada 7.** A versão final e o efeito de publicar (`references/conducao.md`, parada 7). O "pode publicar" não
   decide o rascunho do time central: depois dele, mostre o diff (`contexto_liv_up_ver_proposta`) e faça a pergunta
   literal de aprovar ou de recusar, com o número. Só o "sim" a essa pergunta decide (`references/estrategia.md`).

É a única etapa em que a skill decide uma proposta de outra pessoa: só a da estratégia da própria área, com o pedido
explícito de quem responde depois de ver o diff. **Sessão só de estratégia:** o fechamento é o da estratégia
(`references/estrategia.md`, E3).

## Quando travar

A pessoa vai rodar sozinha. Quando algo impedir de seguir, diga em uma ou duas frases o que aconteceu, o que ela pode
fazer agora e com quem falar; registre no plano local; e siga com o que não depende disso. Nunca contorne. Textos:
`references/conducao.md`, "Quando travar".

- **ferramenta do LivupOS falha ou some no meio:** tente uma vez de novo; se falhar, o plano guarda onde parou;
- **publicação recusada por motivo que não é de forma** (permissão, área arquivada, limite): não tente outra
  ferramenta; mostre a mensagem traduzida e os admins do LivupOS;
- **ninguém sabe responder:** vira "Em aberto" com quem responde, e segue;
- **a pessoa não tem tempo de terminar:** salve o plano, entregue os arquivos, diga como retomar; no mínimo, a saída é
  quem substitui (etapa 3);
- **dúvida sobre o que pode sair do material** (pessoa, outra área): na dúvida, não sobe; vira pergunta.

## Onde ficam os arquivos locais

O plano e o pedido ao admin (com os e-mails) ficam fora do LivupOS.

- **No Claude Code:** na pasta de trabalho. Se a pasta é um Livup Brain, pergunte antes onde guardar (por exemplo, um
  projeto "Carga do LivupOS" em `10-Projetos/`, que o dono nomeia): o Brain não cria pasta nem projeto que o dono não
  nomeou. Anote o caminho no próprio plano.
- **No Claude do navegador ou do desktop (sem pasta):** entregue os arquivos para baixar na parada 2, depois de
  publicar o mínimo, no fechamento e sempre que a pessoa disser que vai parar. O nome não muda; diga "o arquivo que
  vale é o último que você baixou" e peça para anexá-lo ao retomar.

## Sem o conector

Sem as ferramentas `contexto_liv_up_*`, o conector LivupOS não está ligado: diga isso e peça que a pessoa o conecte nas
configurações do Claude (Conectores). Sem o conector da plataforma de apps (`list_projects`, `list_files`,
`get_file`, `list_areas`), a leitura de app cai para o que a pessoa colar e a etapa 2 não tem a divisão da plataforma
para comparar; sem o Slack, os e-mails do pedido vêm do diretor; sem o
conector de BigQuery da Liv Up, o indicador fica com a fonte que o diretor disser e vai para a lista "conferir no
catálogo". Não escreva o contexto em outro lugar como substituto.

## Captura da estratégia (time central)

Quando o pedido é montar a estratégia do ano a partir do material do retreat, a skill não faz a carga de uma área:
siga `references/estrategia.md`, seção 3, e `references/conducao.md`, "Captura". Quem roda é do time central e não
precisa responder pela área; a captura **não publica nada**. Ela monta os rascunhos, confere, abre propostas onde quem
roda propõe sem publicar direto (nunca onde a chamada publicaria na hora) e entrega um arquivo por diretoria e a lista
do acompanhamento. Por padrão, em sequência: uma diretoria por vez, com a pasta de trabalho guardando o que a conversa
não precisa segurar, e uma passada final que cruza somas e dependências. Com material grande (a régua está na C2) e
subagentes (Claude Code), cada diretoria é montada por um, ao mesmo tempo. Valem as regras desta skill, menos a 1 (fica
a proibição das ferramentas de admin, sem a exceção da etapa 2: a captura não cria área), a 3 e a 11 (`references/estrategia.md`, seção 3, diz como cada uma vale na
captura). Nada de código inventado.

Na captura, leia só `references/estrategia.md` (seções 1, 2, 3 e 5), `references/conducao.md` ("Captura", "Tom" e
"Quando travar"), `references/moldes.md` ("Frontmatter", "Regras de texto que valem para todos" e "Publicar"),
`references/separar.md` (seções 5 a 7), `references/fora-da-empresa.md` e, para as visões gerais das pastas
reservadas, `references/forma-comum.md` (seção 4).

## O que esta skill não faz

- Não cria área na raiz nem pasta noutra área, nem as pastas da plataforma (`foruns/`, `canais/`, `notas/`,
  `curadoria/`, `dados-publicados/`, `estrutura-dos-apps/`) na própria; cria área de dentro só da área que a pessoa responde ou substitui, com a
  conferência e o ok dela (etapa 2); não troca quem responde pela diretoria; não marca sigilosa; não arquiva nem move
  área; não concede nem revoga acesso; não abre nem fecha área para a empresa (pede ao admin, no arquivo).
- Não manda mensagem a ninguém (entrega o texto pronto).
- Não publica sem ok; não decide proposta de outra pessoa, exceto a da estratégia da própria área.
- Não escreve meta nem projeto fora da etapa de estratégia e da captura; não migra área que está em outra forma.
- Não dá código a projeto nem escreve data, marco ou situação de projeto (é do acompanhamento).
- Não lê vault, agenda, diário ou 1:1 de outra pessoa.
- Não descreve sistema de tech, não escreve ontologia de área, não cria campo de frontmatter além dos de
  `references/moldes.md` (e, na estratégia e nos projetos, dos de `references/estrategia.md`).
