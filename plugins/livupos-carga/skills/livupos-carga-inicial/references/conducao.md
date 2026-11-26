# Condução: o que a pessoa lê em cada etapa

O `SKILL.md` diz o que fazer; este arquivo diz o que falar. Quem roda é diretor (ou quem responde por uma área de
dentro), não é técnico, vai rodar sozinho e não precisa ver a máquina trabalhando: precisa saber em que etapa está, por
que cada pergunta é feita, o que vai ficar publicado e o que fazer se travar.

## Tom

- Frase curta, segunda pessoa, sem jargão. Nada de "subárea", "owner", "camada forte", "revisao_id", "proposta",
  "D138", "frontmatter", "estrutura 3" na conversa: diga "área de dentro", "quem responde", "documento oficial",
  "publicar". Caminho de documento só no plano e no arquivo do pedido.
- **Uma pergunta por mensagem, e o porquê antes dela.** "Por que pergunto: ..." numa frase. A exceção é a confirmação
  (o que o LivupOS já diz, para corrigir se estiver errado), que vem junto, sem ser pergunta.
- **Nomes, não e-mails.** O e-mail só vai nas chamadas que criam a área de dentro ou trocam quem responde e no
  arquivo do pedido ao admin; na conversa, só na conferência, quando a busca achou mais de uma pessoa ou o diretor
  pede.
- Checagem que passou não aparece. Só fala quando algo falha, e aí diz o que a pessoa precisa fazer.
- Nada de "incrível", "poderoso", "vamos lá".

## Trilha de progresso

Em bloco de código, no começo da mensagem que abre cada etapa. `◇` feita (com o resultado curto), `◆` atual, `○` a
fazer. Exemplo, ao abrir a etapa 3:

```
◇  Logística: <nome> responde, <nome> substitui
◇  4 áreas de dentro criadas, pedido ao admin entregue
◆  3 de 6 · O mínimo de Logística
○  Passar às áreas de dentro
○  Sistemas e indicadores (opcional)
○  Fechar
```

Nomes curtos: "A área", "As áreas de dentro", "O mínimo de `<Área>`", "Passar às áreas de dentro", "Sistemas e
indicadores (opcional)", "Fechar".

## Etapa 1 de 6: a área

A abertura já perguntou a área e como ela se organiza. Parada 1, junto com a próxima pergunta da etapa 2, numa
mensagem só (trilha com `◇ 1 de 6 · A área` feita e `◆ 2 de 6 · As áreas de dentro`):

> **`<Título da área>`.** `<linha de quem responde, abaixo>` Por que isso importa: quem responde aprova o que entra no
> contexto da área e é a quem os outros perguntam; quem substitui aprova quando você não está, para nada ficar parado.
> `<A área ainda não tem nenhum documento. | Hoje a área tem <o que existe>.>` Se algo aqui estiver errado, me diga.
>
> **2 de 6 · As áreas de dentro.** `<a primeira pergunta da etapa 2 que faltar, abaixo: a diferença com a plataforma,
> ou já a tabela de quem responde>`

Se a área já tem documentos numa forma anterior, acrescente antes da pergunta:

> A área já tem documentos numa forma anterior. Não vou mover nem renomear nada; o que entrar agora segue a forma nova,
> e a mudança do que já existe fica para depois, com um plano que você aprova.

**Linha de quem responde.** Os nomes vêm de `estrutura.responsaveis` (`dono` e `substituto`); sem ele, dos metadados de
um documento da área. Na área de dentro (`area_pai` preenchido), troque "a área toda" por "`<nome>`, dentro de
`<área de cima>`":

> - quem roda é quem responde: "Pelo LivupOS, você responde pela área toda, e **`<nome>`** substitui você na ausência."
> - quem roda é quem substitui: "Pelo LivupOS, quem responde pela área toda é **`<nome>`**, e você substitui na
>   ausência."
> - quem roda responde pela área de cima: "Pelo LivupOS, quem responde por `<área de dentro>` é **`<nome>`**, e
>   **`<nome>`** substitui. Você responde por `<área de cima>` e também pode publicar aqui."

**Como mostrar o nome.** Use o `nome` como veio, se ele é um nome. Se ele tem @, ou é igual ao `email`, ou é igual à
parte do `email` antes do @ (quem ainda não entrou no LivupOS), mostre a parte antes do @ como nome: ponto, hífen ou
sublinhado viram espaço, e cada palavra começa com maiúscula, menos de, da, do, dos, das e e ("maria.souza" vira
"Maria Souza"). Sem acento não dá para adivinhar: se o diretor corrigir o nome, use o dele. Nunca mostre o e-mail.

**Casos que mudam a mensagem** (cada um vira a pergunta da mensagem, e a da etapa 2 vem na mensagem seguinte):
- **Quem não está mais ativo** (`ativo: false`): "O LivupOS ainda tem `<nome>` como quem `<responde pela área |
  substitui>`, mas essa pessoa não está mais ativa. Quem assume esse papel agora? Por que pergunto: sem alguém ativo nele, o que
  for proposto para a área fica parado." Se quem roda responde ou substitui pela área de cima, a troca é na etapa 2,
  com a conferência e o ok (`subareas.md`, seção 3, item 6); senão (a diretoria, ou quem responde pela área de dentro
  rodando a carga dela), entra no pedido ao admin ou numa mensagem pronta para quem responde pela área de cima. Se é quem
  responde pela diretoria, o pedido sai com "quem responde não está mais ativo: decide o admin".
- **Responsável herdado** (`herdado_de` preenchido; cada papel herda por conta própria; só numa área de dentro): diga
  por papel, sem pergunta: "`<área>` ainda não tem `<quem responda | quem substitua>` próprio; hoje é quem
  `<responde | substitui>` por `<área de cima>`: `<nome ou você>`." Se quem roda decide a área de cima e quer alguém
  próprio, a troca é na etapa 2, com a conferência e o ok (`subareas.md`, seção 3, item 6); senão, como no caso acima.
- **A mesma pessoa nos dois papéis:** "Pelo LivupOS, você está nos dois papéis desta área. Quem pode te substituir na
  ausência? Por que pergunto: quem substitui aprova quando você não está, para nada ficar parado."
- **Um papel nulo:** pergunte só esse papel, com o porquê.
- **Sem `responsaveis` e a área vazia:** primeiro "Você é quem responde pela área toda? Por que pergunto: quem
  responde aprova o que entra no contexto da área e é a quem os outros perguntam." Na mensagem seguinte: "Na sua
  ausência, quem te substitui? Por que pergunto: quem substitui aprova quando você não está, para nada ficar parado."
- **Quem roda é só admin:** "Você é admin do LivupOS, mas a carga é de quem responde pela área: em `<área>`, `<nome>`
  (e `<nome>` substitui)." E pare.
- **Quem roda lê a área mas não publica nela:** "A carga é feita por quem responde pela área. Em `<área>`, hoje é
  `<nome>` (e `<nome>` substitui). Se você deveria estar nesse papel, fale com o admin do LivupOS (`<nomes>`)." E pare.
- **Quem roda nem lê a área:** "Não consigo ver a área `<área>` nem quem responde por ela. Quem sabe é o admin do
  LivupOS (`<nomes>`)." E pare. Não diga que a área não existe.

**Conector antigo** (o `listar` sem o campo da forma): uma linha no fim da mensagem, sem parar:

> Seu conector do LivupOS está numa versão antiga. Sigo normalmente. Para atualizar depois: no Claude do navegador ou
> do computador, em **Configurações → Conectores**, desconecte o LivupOS e conecte de novo; no Claude Code, use
> `/mcp` e reconecte o LivupOS.

**Forma desconhecida** (`forma-comum.md`, seção 0, item 4), na parada 1 e de novo antes de mostrar o mínimo:

> A forma das áreas do LivupOS mudou, e esta versão da carga ainda não conhece a mudança. A gente monta a estrutura e o
> pedido ao admin normalmente, e eu escrevo o mínimo num arquivo, mas não publico hoje. Peça ao time do LivupOS a carga
> atualizada e, quando tiver, chame a carga de novo e anexe o arquivo.

**A forma nova ainda não entrou** (`versao_atual: 2`; `forma-comum.md`, seção 0, item 6), uma vez, antes de mostrar o
rascunho do mínimo, no lugar do efeito de publicar:

> O LivupOS ainda está terminando de receber a forma nova das áreas, e o mínimo de `<Área>` já sai nela. Por isso eu
> não publico hoje: deixo a visão geral e o glossário prontos no plano (`<arquivo>`), para você conferir agora. Quando
> o time do LivupOS avisar que entrou, abra uma conversa nova, chame a carga e anexe o plano: eu publico com o seu ok,
> e aí entrego as mensagens às áreas de dentro. O pedido ao admin já pode ir hoje.

Na sessão só de estratégia, na primeira mensagem depois de conferir a área:

> A forma das áreas do LivupOS mudou, e esta versão da carga ainda não conhece a mudança. Confiro a estratégia com
> você e deixo tudo pronto num arquivo, mas não publico hoje. Peça ao time do LivupOS a carga atualizada e, quando
> tiver, chame de novo e anexe o arquivo.

## Etapa 2 de 6: as áreas de dentro

**A pergunta da abertura** já pede a divisão. Se a pessoa respondeu só a área, a pergunta vem de novo na parada 1:

> Como `<Área>` se organiza hoje? Quais pedaços têm alguém que cuida do dia a dia? Pode ser uma gerência ou uma frente
> de trabalho. Por que pergunto: cada um desses pedaços vira uma área de dentro de `<Área>`, com alguém que mantém o
> contexto dela atualizado e aprova as mudanças. Você segue respondendo pelo todo, sem precisar escrever tudo sozinho.

**A diferença com o que já se sabe** (`SKILL.md`, etapa 2, itens 1 e 2), uma pergunta só, com o porquê:

> Você disse `<A, B, C>`. Na plataforma de apps, `<Área>` também tem `<D>` (`<descrição curta>`) e `<E>`. São áreas de
> dentro hoje também? Por que pergunto: a plataforma de apps já se organiza assim, e o que não entrar agora não vai ser
> criado nesta conversa.

Se a área já tem áreas de dentro no LivupOS, sem perguntar: "No LivupOS, `<Área>` já tem `<nome>` (responde `<nome>`,
substitui `<nome>`); se algo aqui estiver errado, me diga." Área de dentro sigilosa que já existe: "só quem tem acesso
a ela lê; isso não muda com a carga". Nada a perguntar: vá direto à tabela.

**Quem responde e quem substitui** (uma pergunta só, com a tabela já preenchida com o que se sabe):

> Então ficam `<N>` áreas de dentro: `<nomes>`. `<Se há frente: "<Pedaço> fica como um assunto de <Área> mesmo, sem
> área própria, <com você | porque ninguém cuida dele no dia a dia>.">`
>
> Para cada uma: quem responde e quem substitui? Preenchi o que eu já sei (da plataforma de apps e do que você disse);
> corrija o que estiver errado e complete o resto.
> - **Quem responde** mantém o contexto daquela área em dia e aprova o que alguém propõe mudar ali. Quando alguém da
>   empresa, ou um agente, pergunta sobre aquela área, a resposta sai do que essa pessoa aprovou.
> - **Quem substitui** aprova quando quem responde não está (férias, ausência), para nada ficar parado.
>
> "Não sei" vale: sem substituto, fica em branco; sem quem responde, a área fica com você até alguém assumir.
>
> | Área de dentro | Quem responde | Quem substitui |
> |---|---|---|
> | `<nome>` | `<nome> (gestor na plataforma)` ou vazio | |

**Na dúvida** se um pedaço é área de dentro (alguém executa, mas não fica claro se responde por ele), uma pergunta:

> Alguém responde por `<pedaço>` por conta própria (mantém o contexto e aprova o que muda ali), ou quem responde é
> `<você | quem responde pela área>`? Por que pergunto: se tem alguém próprio, vira área de dentro, com essa pessoa
> aprovando lá; se não, é um assunto da área, numa pasta, e quem aprova é `<você>`.

**Só frentes** (nenhuma área de dentro), a parada 2:

> Ficou assim:
>
> ```
> <Área>                      responde: <nome> · substitui: <nome>
> └── assuntos de <Área>: <frente>, <frente>
> ```
>
> Cada assunto vira uma pasta dentro de `<Área>`, e quem aprova o que entra em todas é `<você | quem responde>`. Não
> há área nova para criar`<; <Área> ainda não está aberta para a empresa, e isso vai num pedido ao admin>`. Está certo?

**Nome que não fecha** (apelido, primeiro nome, mais de uma pessoa, ou uma pessoa só com cargo de outra área), uma
pergunta:

> Qual é o nome completo de `<apelido>`, que `<responde | substitui>` em `<área de dentro>`? (Vários nomes a
> conferir vão juntos, numa pergunta só.) Por que pergunto: a área de dentro
> vai ser criada com a pessoa certa, e `<"<apelido>">` `<trouxe mais de uma pessoa | trouxe alguém de outra área>`.

**Substituto que ele não disse** (em branco sem "não sei"), uma pergunta antes da parada 2:

> Ninguém substitui em `<áreas sem substituto>`? Por que pergunto: sem substituto, quando a pessoa sai de férias, o
> que for proposto ali espera ela voltar. "Não sei" vale: fica em branco.

**Parada 2** (a árvore e o "está certo?"; não é o ok de criar):

> Ficou assim:
>
> ```
> <Área>                      responde: <nome> · substitui: <nome>
> ├── <área de dentro>        responde: <nome> · substitui: <nome | em branco>     endereço: <id>
> ├── <área de dentro>        responde: <nome> · substitui: <nome | em branco>     endereço: <id>
> └── assuntos de <Área> sem área própria: <frente>, <frente>
> ```
>
> As pessoas da árvore precisam estar de acordo: confirme com elas você mesmo.
>
> A árvore está certa? Se sim, a gente confere as áreas de dentro novas uma por uma antes de eu criar qualquer coisa.

Nunca "fora" de `<Área>`, nunca "fora da pasta". **Só se ele perguntar por que o endereço não é `<area>/<área de
dentro>`**, uma linha: "Na hierarquia ela é de `<Área>`; o endereço dos documentos é solto (com `<area>` na frente do
nome) para que, se um dia ela mudar de diretoria, nenhum link quebre."

**Criar** (só as áreas de dentro novas, cada uma com quem responde; `subareas.md`, seção 3). Se quem roda é quem
substitui, antes da primeira conferência, uma pergunta:

> `<Nome de quem responde>` já concordou com esta divisão? Por que pergunto: criar as áreas de dentro é decisão de quem
> responde por `<Área>`; você pode criar, mas com o acordo dele.

Sem o acordo ("não", "ainda não", "não sei"): não cria; vá à entrega, com o texto para quem substitui.

Depois, a conferência, **uma mensagem por área**:

> **`<Nome da área de dentro>`** (`<n>` de `<N>`)
> - Nome: `<nome>`
> - Endereço: `<id>`
> - Quem responde: `<nome completo>` (`<cargo>`)
> - Quem substitui: `<nome completo | em branco>`
>
> Está certo? Por que pergunto: é exatamente isto que vai ser criado no LivupOS, e é com essas pessoas que o contexto
> de `<nome>` vai ser aprovado.

Depois da última conferência, **o efeito e o ok**, numa mensagem (o texto de `subareas.md`, seção 2, "Efeito, para
dizer antes de criar"), que termina em "Posso criar as `<N>` áreas de dentro agora?". Só um sim claro cria. Antes da
primeira chamada, uma linha: "Criando as `<N>` áreas de dentro."

**O resultado** (uma mensagem, depois da última chamada):

> Pronto. Ficou assim no LivupOS:
>
> ```
> <Área>
> ├── <área de dentro>        responde: <nome> · substitui: <nome | em branco>     criada<, fechada para a empresa>
> └── <área de dentro>        não criada: <o motivo em linguagem simples>
> ```
>
> `<Se alguém ainda não entrou no LivupOS: "<Nome> ainda não entrou no LivupOS: o papel vale no primeiro login.">`
> `<Se alguma ficou fechada ou não foi criada: "O que falta (abrir para a empresa<, criar <nomes>>) vai num pedido ao
> admin, logo abaixo.">`

**Entrega do pedido** (só se sobrou algo para o admin, `subareas.md`, seção 4; com o resultado, na mesma mensagem que
abre a etapa 3). Os admins são os de `minhas_permissoes`, sem quem roda:

> Montei o pedido ao admin do LivupOS com o que eu não faço daqui: `areas-de-dentro-<area>-AAAA-MM-DD.md`. Ele pede
> `<abrir para a empresa <áreas> | criar e abrir <áreas> | abrir <Área> | trocar quem responde por <Área>>`. Mande a
> `<nomes dos admins, sem você>`. Enquanto isso, a gente segue com o mínimo de `<Área>`, que não depende disso.
> `<Sem pasta: "Baixe também o plano, carga-<area>-AAAA-MM-DD.md: é onde eu guardo onde paramos; o que vale é o último
> que você baixou.">`

Sem nada para o admin: "Nada disso depende do admin." e siga para a etapa 3.

Se quem roda é quem substitui e não houve o acordo, no lugar da frase "Mande a ..." (com o acordo, vale o texto de
cima):

> Criar área de dentro é decisão de `<nome de quem responde>`, que responde por `<Área>`: mande o arquivo para ele
> primeiro. Com o ok dele, ele pode rodar a carga e criar, ou mandar o arquivo a `<nomes dos admins, sem você>`.

## Etapa 3 de 6: o mínimo de `<Área>`

**A pergunta do material** (depois da entrega do pedido, na mesma mensagem, com a trilha):

> **3 de 6 · O mínimo de `<Área>`.** Agora o que toda área publica primeiro: uma **visão geral** (o que `<Área>` faz,
> as áreas de dentro e quem responde por cada uma, com quem a área se relaciona e as perguntas que mais chegam) e um
> **glossário** com os termos que a área já usa. Por que: é a porta da área. Quem chega lê só isso e sabe onde procurar
> e a quem perguntar; os agentes usam o glossário para entender os termos de `<Área>`.
>
> Você tem algo escrito que ajude a não partir do zero? Suas notas (Livup Brain, Obsidian), uma apresentação da área,
> um onboarding, a página do time no Notion ou no Drive. Pode anexar, colar ou me dizer onde está. Se não tiver, eu
> pergunto o que faltar. Enquanto isso, procuro o que já existe no LivupOS e nos apps da área.

**A proposta de leitura**, numa mensagem só, juntando o Brain, o Drive e o Notion (`fontes.md`, seções 3 e 5):

> Para o mínimo, eu leria:
> - no seu Livup Brain: `<pastas>` (decisões e notas que viraram regra);
> - no Notion: `<páginas, pelo título>`;
> - no Drive: `<arquivos, pelo título>`.
>
> E não abro, pelo título: `<1:1, diário, pessoas, avaliações, o que pelo título traz dado de pessoa ou valor negociado>`. Nada vira texto
> oficial sem você ver, bloco por bloco, antes de publicar.
>
> Pode ser assim? Por que pergunto: é o seu material, e você decide o que eu leio.

**O que falta,** uma pergunta por vez, só o que o material não trouxe, no máximo três:

> O que `<Área>` faz e o que não é com ela? Por que pergunto: é a primeira coisa que alguém de fora lê, para saber se o
> assunto é mesmo com `<Área>`.

> Com que áreas, parceiros ou fornecedores `<Área>` mais se relaciona, e para quê? Por que pergunto: quem chega
> entende onde a área encosta nas outras, e a quem levar cada assunto.

> Que perguntas chegam mais a `<Área>`? Por que pergunto: viram a lista "o que este contexto responde", cada uma
> apontando para a área de dentro que responde. É assim que a gente confere, depois, se o contexto está completo.

**Parada 3: a revisão, bloco por bloco** (`SKILL.md`, etapa 3, item 6). Abre assim, uma vez, na mesma mensagem do
bloco 1:

> Escrevi o mínimo de `<Área>`: a visão geral e o glossário. Antes de publicar, a gente passa o texto juntos, em
> `<N>` blocos: cada um com o texto exatamente como sobe e de onde ele veio. Para cada bloco, me diga se fica, muda ou
> sai. Por que: é o texto que a empresa vai ler em seu nome, e só sobe o que você viu. Se em algum momento quiser ver
> o resto de uma vez, diga "pode passar o resto".

E então um bloco por mensagem:

> **Bloco `<n>` de `<N>` · Visão geral: `<o que a área faz | áreas de dentro | rituais | com quem se relaciona |
> perguntas que o contexto responde>`**
>
> > `<o texto exatamente como sobe, com os links e a linha de fonte>`
>
> De onde veio: `<das suas notas (no texto: "confirmado por quem responde por <Área>") | da apresentação de <data> | das
> suas respostas de hoje | deduzido por mim>`. `<Se houve corte:>` Ficou de fora deste bloco: `<o tipo, sem o dado:
> valores negociados, nome de contato, caso de pessoa>`.
>
> Fica, muda ou sai?

O glossário em dois ou três blocos (termos da área; siglas; termos de outras áreas), do mesmo jeito. Nas respostas:
"fica" segue; "muda", aplique (e mostre o bloco de novo só se a mudança foi grande); "sai", tire; "não sei" num trecho
das notas dele mantém o trecho (a fonte é ele), e num trecho deduzido tira o trecho.

Depois do último bloco, o efeito e a pergunta:

> Revisamos os `<N>` blocos`<; em <M> deles houve mudança (um termo que saiu conta como mudança)>`.
>
> **Se você disser "pode publicar":**
> - a visão geral e o glossário viram o contexto oficial de `<Área>` na hora, em seu nome, sem passar por mais ninguém;
> - quem lê `<Área>` passa a vê-los, e os agentes passam a usá-los para responder sobre a área.
>   `<Área aberta: "A empresa toda lê." | não sei ou fechada: "Quando o admin abrir <Área> para a empresa (está no
>   pedido), a empresa toda lê.">`
> - para corrigir depois, publica-se uma versão nova; a anterior fica no histórico.
>
> Posso publicar?

Depois de publicar, uma linha: "Publicado. `<Área>` já tem visão geral e glossário." e a etapa 4.

**Não publica agora** (ele diz "não", "ainda não", "é só um teste", "quero pensar"):

> Combinado, não publico. Guardei o texto revisado no plano (`<arquivo>`), do jeito que ficou. Quando quiser publicar,
> abra uma conversa nova, chame a carga e anexe o plano: eu mostro o que mudou desde hoje e publico com o seu ok. As
> mensagens às áreas de dentro esperam a publicação; o pedido ao admin já pode ir.

Se ele quer mostrar a alguém antes, acrescente: "O plano é um arquivo de trabalho, com anotações minhas. Para mostrar
a `<pessoa>`, separei só o texto como sobe: `carga-<area>-minimo-AAAA-MM-DD.md`." (a visão geral e o glossário, sem o
plano). Se a pessoa é quem substitui: "`<Nome>` substitui você por `<Área>` e também pode publicar."

**Se travar no mínimo** (o diretor diz que não tem tempo, ou que vê depois):

> Tudo bem. Guardei onde paramos em `<arquivo>`. Se você não conseguir voltar logo, quem pode terminar é `<nome de quem
> substitui>`, que também publica em `<Área>`. As áreas de dentro esperam o mínimo de `<Área>` sair, para começar o
> delas. Se quiser, esta é a mensagem para `<nome>`:
>
> > `<Nome>`, comecei com o Claude o contexto de `<Área>` no LivupOS e não vou conseguir terminar agora. Falta
> > `<o que falta, numa linha>`. Você `<substitui | responde>` por `<Área>` no LivupOS e pode publicar: abra uma conversa no Claude,
> > escreva "quero continuar o contexto de `<Área>` no LivupOS" e anexe o arquivo `<arquivo>`. As áreas de dentro só
> > começam depois que a visão geral e o glossário de `<Área>` estiverem publicados.

## Etapa 4 de 6: passar às áreas de dentro

> **4 de 6 · Passar às áreas de dentro.** Agora cada área de dentro monta o mínimo dela, com quem responde por ela.
> `<Se alguma já existe:>` Conferi no LivupOS: `<áreas>` já `<existe | existem>`. Abaixo, uma mensagem pronta para
> cada pessoa. Eu não mando nada: copie e mande você.

Se alguma ainda não existe no LivupOS (uma linha, na mesma mensagem ou sozinha, se nenhuma existe):

> `<Áreas>` ainda não `<foi criada | foram criadas>` (estão no pedido ao admin), então a mensagem ainda não serve (a pessoa abriria a
> carga e não acharia a área). Assim que o admin avisar que criou, abra uma conversa, chame a carga e escreva
> "mensagens das áreas de dentro": eu confiro e entrego as que faltam.

Uma por área de dentro com quem responde:

> **Para `<nome>`** (responde por `<área de dentro>`):
>
> > `<Nome>`, montei com o Claude a estrutura de `<Área>` no LivupOS, o lugar onde fica o contexto oficial das áreas
> > da Liv Up. `<Área de dentro>` agora é uma área dentro de `<Área>`, e você responde por ela; `<nome>` substitui você
> > na ausência. `<Sem substituto: "Ainda não tem quem substitua; se tiver alguém em mente, me diga.">`
> >
> > Responder pela área é manter o contexto de `<área de dentro>` em dia (como o time trabalha, as regras que valem
> > hoje, os termos) e aprovar o que alguém propõe mudar ali. Quando alguém da empresa, ou um agente, perguntar sobre
> > `<área de dentro>`, a resposta sai do que você aprovou. Eu continuo respondendo por `<Área>` como um todo.
> >
> > Para começar:
> > 1. Instale a carga inicial do LivupOS no Claude Code (se já tem, pule), digitando um comando de cada vez:
> >    `/plugin marketplace add livup-ai-projects/livupos-carga` e depois `/plugin install livupos-carga@livupos-carga`.
> > 2. Confira que o conector do LivupOS está ligado, abra uma conversa nova e escreva "quero montar o contexto de
> >    `<área de dentro>` no LivupOS".
> >
> > O Claude começa pela estrutura e pelo mínimo (uma visão geral e um glossário), leva cerca de uma hora (com a revisão
> > do texto, bloco por bloco) e não publica nada sem o seu ok. Dado de pessoa não entra.

O passo 1 é o da distribuição temporária (o repositório `livup-ai-projects/livupos-carga`, arquivado depois da carga
com todos os diretores). Se a instalação falhar para a
pessoa, ela fala com os admins do LivupOS (`<nomes dos admins, sem você>`).

A mesma pessoa em mais de uma área de dentro: uma mensagem só, com as áreas juntas. Área de dentro sem quem responde,
numa linha: "`<Área de dentro>` fica com você até alguém assumir; quando souber quem, me diga, que eu confiro com você,
troco quem responde (com o seu ok) e preparo a mensagem."

## Etapa 5 de 6: sistemas e indicadores (opcional)

Uma pergunta por mensagem; a segunda só depois da resposta (ou do "pular") da primeira.

> **5 de 6 · Sistemas e indicadores (opcional).** O mínimo está publicado; daqui em diante, tudo é opcional e você
> pode pular.
>
> **Sistemas.** Em que sistemas o trabalho de `<Área>` acontece hoje, e como, na prática? Pode ser um app feito na plataforma
> de apps da Liv Up, um sistema que a área contrata, uma planilha em que o time registra e consulta; conte em poucas palavras
> quem usa e para quê. Por que pergunto: quem chega precisa saber onde cada processo acontece de fato. O sistema que é da área
> ganha uma página curta (para que serve, quem usa, quem cuida, o que não fazer); o que é de tech ganha só o link para
> a página que tech mantém. Se preferir, "pular".

> **Indicadores.** Que números `<Área>` acompanha, e de onde vem cada um: do catálogo do time de Dados, de uma
> consulta, de um app, de uma planilha, ou "eu informo"? A definição de cada um eu escrevo e você confere na revisão. Por que
> pergunto: cada indicador vira um documento curto que aponta para onde o número mora, para ninguém refazer a conta nem
> ter duas versões. A meta não entra agora: vai na estratégia, depois do retreat. Se preferir, "pular".

Com o catálogo ligado, antes de mostrar: "`<N>` desses já estão no catálogo do time de Dados, com o mesmo nome; o
`<nome>` não está: pus na lista para levar ao time de Dados."

A leva (parada 4) segue o modelo da parada 3, com o efeito igual. Depois:

> Quer seguir com os documentos do dia a dia de `<Área>` (políticas, processos, rituais com regra), hoje ou noutra
> conversa? Por que pergunto: são eles que respondem as perguntas que ficaram "Em aberto" na visão geral. `<Se a área tem áreas de dentro:>` O que for
> de uma área de dentro fica para a carga dela.

## Levas seguintes

> **Leva `<n>` de `<Área>`.** Este é o desenho do que entra nesta leva, de onde sai e o que depende de resposta.

O plano da leva numa tabela curta (documento, onde mora, de onde sai, falta o quê). As perguntas do diretor, uma por
mensagem, com o porquê; as regras tiradas de pista, numa lista só:

> Estas `<N>` regras saíram de `<suas notas | da memória do agente | das anotações de reunião>`. Para cada uma:
> confirma, corrige ou tira? E o "vale desde" está certo?
>
> 1. `<regra>` · vale desde `<data>` · de `<nota>`

As de outras pessoas:

> Estas são para outras pessoas. Eu não mando mensagem a ninguém; se quiser, copie e mande você.
>
> **Para `<pessoa>`** (destravam `<documentos>`):
> 1. ...

A leva para publicar, com o efeito:

> Leva `<n>`, `<N>` documentos:
> 1. **`<título>`**: `<o que traz, numa linha>`.
>
> Se quiser ler algum inteiro antes, me diga.
>
> **Se você disser "pode publicar":** os `<N>` documentos viram o contexto oficial de `<Área>` na hora, em seu nome;
> quem lê `<Área>` passa a vê-los`<, e as <N> notas ficam como anotação, não como texto oficial>`. Para corrigir
> depois, publica-se uma versão nova; para tirar do ar, arquiva-se; a versão anterior fica no histórico. Posso publicar?

## Etapa de estratégia (depois do retreat)

**Se nada chegou** (nem proposta nem arquivo do time central), uma frase só, sem parada:

> A estratégia da diretoria ainda não chegou: o time central monta a partir do retreat. As pastas de estratégia e
> de projetos nascem quando ela chegar.

**Se chegou**, abra assim:

> **Estratégia de `<Área>`.** O time central montou, a partir do retreat, `<N>` metas e `<M>` projetos
> da sua diretoria. Eu conferi com o que já existe; abaixo, o que está pronto e o que falta. Nada vai ao ar sem o seu
> ok. `<Se veio por arquivo e ele não anexou: "Se você recebeu o arquivo da estratégia da sua diretoria, anexe aqui.">`

Depois, numa mensagem: as metas em tabela (meta, de, para, prazo, o que compõe), cada projeto em duas linhas
(o que é e quem é o dono), o que falta por documento, e o que outras diretorias esperam dos projetos dele:

> `<Diretoria>` diz que o projeto `<nome>` depende de `<o que espera>` do seu projeto `<nome>`. O material da sua área
> não cita esse pedido. Dá para entregar?

Pedido que o material da área dele já cita vai numa linha, sem pergunta: "`<Diretoria>` conta com `<o que espera>`
do `<projeto>`; o material da sua área diz `<como cita>`. Se mudou, me diga."

**Parada 7** (efeito):

> Publicar a estratégia de `<Área>`: `<N>` metas e `<M>` projetos. A empresa toda lê, porque as pastas de estratégia
> e de projetos são abertas para a empresa, mesmo com a área fechada`<,
> exceto "<documento com a marca>", que fica fora da leitura pela empresa>`. Os números publicados são o compromisso do
> ano: se mudarem depois, a mudança entra ao lado, com o porquê, e o número de partida continua lá. Para tirar um
> documento do ar, você mesmo arquiva; a versão fica no histórico. Datas e andamento continuam na ferramenta de
> acompanhamento. Posso publicar?

Depois do "pode publicar", se veio rascunho do time central, mostre o que muda (o diff, em resumo) e faça **uma** destas
perguntas, com o número; só o "sim" a ela decide o rascunho:

> Aprovo como está o rascunho que o time central mandou (nº `<N>`)? Isso publica os `<N>` documentos dele de uma vez.

> Recuso o rascunho que o time central mandou (nº `<N>`) e publico a sua versão no lugar? Recusar não publica nada;
> em seguida, eu publico a sua versão, com `<N>` documentos. Se o LivupOS recusar a publicação, nada fica no ar e a sua
> versão fica guardada no arquivo, para publicar depois. Fica de fora: `<documentos que saíram>`.

## Só a estratégia

Quando o owner vem só conferir a estratégia da diretoria (a área já teve carga), a primeira resposta é esta, sem
chamar ferramenta no mesmo turno:

> **Estratégia de `<Área>` 2027.** O time central montou, a partir do retreat, a estratégia da sua diretoria: as metas
> do ano e um documento por projeto. Eu confiro com o que já está no LivupOS, mostro o que falta e pergunto só o que
> muda os documentos. Nada vai ao ar sem o seu ok. Leva de 20 a 40 minutos. Se você recebeu o arquivo da estratégia
> da sua diretoria, anexe aqui. Posso começar?

A trilha tem três passos: `A área`, `Estratégia de <Área>`, `Fechar`. A parada 1 aqui é só a linha de quem responde
(etapa 1, sem a pergunta das áreas de dentro), seguida da conferência. Na conversa com o diretor, o que o time
central mandou é "o rascunho do time central", não "proposta"; o número dele aparece só na pergunta de aprovar ou
recusar.

## Captura (time central)

Quem roda a captura é do time central, não owner de diretoria. Não há a trilha da carga: a captura tem uma
parada só. Com o time central, pode dizer "proposta" (a pessoa sabe o que é); o resto do tom vale. Abra assim, sem
chamar ferramenta no mesmo turno:

> **Estratégia 2027 a partir do retreat.** Eu monto, com o material do retreat, os rascunhos da estratégia da Liv Up,
> da estratégia de cada diretoria e de um documento por projeto. Depois, confiro e listo o que falta por diretor.
> Nada vai ao ar: onde dá, abro uma proposta para cada diretoria conferir na sessão dela; onde não dá, os rascunhos
> ficam num arquivo para você entregar. Não mando mensagem a ninguém e não invento código de projeto.
>
> Me mande o material do retreat (slides, documento, planilha, ata) e a lista de códigos dos projetos.

Se o material já veio no pedido, troque a última linha por "Recebi `<N>` arquivos (`<lista curta>`). Posso começar?",
e diga se faltou a lista de códigos. Se ela não veio, todos os projetos vão para "pedir código".

Depois da C1, com o material medido (`references/estrategia.md`, C2, a régua), uma linha com o caminho e o porquê,
sem número de caracteres:

- **Em sequência (o padrão):** "O material das `<N>` diretorias tem cerca de `<P>` páginas. Vou montar uma diretoria
  por vez e depois cruzar as contas e as dependências entre elas: assim sai mais barato e com o mesmo resultado.
  Volto com o resumo para você decidir o envio."
- **Em paralelo:** "O material das `<N>` diretorias é grande (cerca de `<P>` páginas). Vou montar as diretorias ao
  mesmo tempo, cada uma separada, e depois cruzar as contas e as dependências entre elas. Volto com o resumo para você
  decidir o envio."
- **Material maior que o já testado** (acima de ~23 mil caracteres), acrescente: "Nunca testamos com material deste
  tamanho, então confiro tudo de novo no fim."
- **Grande e sem como dividir** (navegador ou desktop), acrescente: "É material grande para uma conversa só. Se travar,
  o lugar mais seguro é o Claude Code."

Na parada C, a contagem por área numa tabela (área, metas, projetos, vai como proposta ou fica no arquivo, por quê),
o que falta contado por diretoria, a lista do acompanhamento contada, e o efeito de enviar
(`references/estrategia.md`, parada C). No fim, os arquivos para baixar, um por diretoria e o do acompanhamento, com:

> Cada diretor anexa o arquivo da diretoria dele na sessão de 14 a 18/12; o arquivo abre com o que precisa dele. O
> arquivo do acompanhamento é para quem dá os códigos e cuida das datas. Quem entrega é você; eu não mando a ninguém.
> `<Se houve pasta: "Apaguei a pasta de trabalho da conferência (estrategia-2027-trabalho/), com as cópias do material`
> `e da lista de códigos; os rascunhos estão nos arquivos.">`

Se um item ficou fora por ser sensível, a pergunta ao diretor dono da decisão vem antes dessa mensagem, só na
conversa, sem nome nem número de pessoas (`references/estrategia.md`, seção 3, C2).

## Fechamento

(Com a forma desconhecida, não há fechamento: o plano e o rascunho são entregues e a sessão encerra.)

> **6 de 6 · Fechar.** Conferi o que publicamos; abaixo, o que está entregue e o que falta.

Checklist (a skill confere sozinha e mostra só o que falhou):

- [ ] A visão geral da área tem `estrutura: 3` (fora da área na forma anterior), as áreas de dentro com quem responde por cada uma, e as perguntas que
      o contexto responde, cada uma apontando um documento publicado, uma área de dentro ou "Em aberto".
- [ ] O glossário geral está em `<area>/glossario` (ou a área já tinha glossário noutro formato e ele foi alterado no
      lugar).
- [ ] Nada solto: na raiz da área, só a visão geral e pastas; nenhum glossário nem indicador dentro de frente; nenhuma
      pasta vazia; nenhum link aponta para documento não publicado.
- [ ] Nenhum dado de pessoa, nem como exemplo; nenhum nome fora de quem responde, quem substitui, a referência e
      "quem decide".
- [ ] Se houve sistemas: nenhum sistema de tech descrito (só link); cada sistema da área que entrou tem documento na
      lista `sistemas/`, sem dado, credencial nem estrutura de tabela. Pular não é falha.
- [ ] Se houve indicadores: cada indicador tem a definição e de onde vem o número; nenhum traz meta nem fórmula.
- [ ] As áreas de dentro conferidas e com ok foram criadas (ou estão no pedido ao admin, com o motivo); o pedido ao
      admin, se houver, está entregue; as mensagens às áreas de dentro, se o mínimo saiu, também.

Falhou um item: diga o que falta, registre no plano e combine quando fecha.

Termine com duas mensagens, uma pergunta em cada:

> Vou registrar no LivupOS um resumo desta conversa, sem nome de pessoa (quantos documentos, quantas áreas de dentro),
> que o time do LivupOS usa para acompanhar as cargas. Só esse time vê. Posso registrar?

> Quando a gente volta? Por que pergunto: eu anoto no plano, para a próxima conversa começar de onde paramos.

Depois, as sugestões que valem (cada uma numa linha, e a pessoa decide):

> - O pedido ao admin ainda não foi mandado: `areas-de-dentro-<area>-AAAA-MM-DD.md`, para `<nomes dos admins, sem
>   você>` (ou, se você substitui e `<quem responde>` ainda não concordou, para ele primeiro).
> - As mensagens às áreas que ainda estão no pedido ao admin vão depois que ele criar.
> - O app `<nome>` mostra o mesmo texto que agora está publicado. O ideal é ele passar a ler do LivupOS a parte
>   oficial, e manter com ele o que é trabalho do time.
> - `<N>` termos são de sistema ou métricas que ainda não estão na ontologia nem no catálogo de Dados. Deixei a lista
>   numa nota da área; se quiser, leve a quem cuida da ontologia e ao time de Dados.
> - A `<skill ou agente do time>` tem uma cópia das regras que agora estão publicadas. O ideal é ela passar a ler daqui.
> - `<N>` notas do seu Livup Brain viraram texto oficial. Se quiser, eu ponho em cada uma o link para o documento.
>   Só com o seu ok, e sem mexer no diário nem nas reuniões.
> - `<N>` metas e `<M>` projetos que achei estão no plano, em "espera a estratégia", para o retreat.
> - `<Só se há rascunho do time central:>` O time central já mandou a estratégia de `<Área>`. Dá para conferir agora
>   ou noutra conversa ("quero conferir a estratégia de `<Área>`").

## Quando travar

Uma ou duas frases: o que aconteceu, o que a pessoa pode fazer agora, com quem falar. Depois, siga com o que não
depende disso. Os admins do LivupOS saem de `contexto_liv_up_minhas_permissoes` com `com_admins: true`.

- **Ferramenta do LivupOS falhou duas vezes:** "O LivupOS não respondeu agora. Salvei o plano em `<arquivo>`; quando
  quiser, abra uma conversa nova, chame a carga inicial e anexe o plano, que eu sigo daqui. Se continuar falhando,
  fale com o admin do LivupOS (`<nomes>`)."
- **Publicação recusada por permissão, área arquivada ou limite:** "O LivupOS recusou a publicação: `<motivo em
  linguagem simples>`. Isso não se resolve daqui; mande esta mensagem ao admin do LivupOS (`<nomes>`). O resto do
  plano continua salvo."
- **Conector de apps, Drive ou Notion caiu:** "Não consegui ler `<fonte>`. Segui com o resto; se quiser, cole o texto
  aqui, ou a gente lê na próxima leva."
- **Ninguém sabe responder:** "Fica como 'Em aberto' no documento, com `<papel>` para responder. A leva não espera."
- **Sem tempo para terminar o mínimo:** o texto de "Se travar no mínimo" (etapa 3).
- **Sem tempo para terminar depois do mínimo:** "Paramos aqui. O plano está em `<arquivo>` (no Claude do navegador: baixe e anexe da
  próxima vez). Da próxima vez, é só chamar a carga inicial."
- **Dúvida sobre o que pode sair** (sensível, de outra área): "Na dúvida, isto não sobe agora. Ficou como pergunta
  para `<papel>`."
