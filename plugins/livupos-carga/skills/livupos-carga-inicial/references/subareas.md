# Áreas de dentro: quando, como explicar, criar com o diretor e o pedido ao admin

Na conversa com o diretor, "área de dentro"; na plataforma, subárea. A carga começa pela estrutura: a área, quem
responde por ela e as áreas de dentro, cada uma com quem responde e quem substitui (`SKILL.md`, etapa 2). Desde
26/11/2026 (D164), quem responde por uma área (ou quem substitui) cria as áreas de dentro dela: a skill confere com o
diretor, uma por uma, explica o que muda e **só cria com o ok explícito dele** (seção 3). O que a plataforma recusa, e o
que só o admin faz (abrir para a empresa, a área na raiz, a marca sigilosa, trocar quem responde pela diretoria), vai
no pedido ao admin em arquivo (seção 4). A skill nunca abre área.

## 1. Quando um pedaço vira área de dentro

**Quando tem alguém que cuida do dia a dia** (`forma-comum.md`, seção 2). Pode ser uma gerência ou uma frente de
trabalho. Pedaço sem ninguém que cuide é frente (pasta dentro da área). O critério antigo ("só quando muda quem decide
ou quem lê") não vale mais.

Se a área já tem áreas de dentro, a carga respeita a divisão que existe e confirma quem responde e quem substitui em
cada uma. Uma área de dentro que já existe e é sigilosa segue como está (quem muda isso é o admin do LivupOS, não a
carga). Área de dentro nova de uma área sigilosa (marcada pelo admin: People, Financeiro) nasce sigilosa e fechada para
a empresa; a skill nunca pede `sigilosa` na criação e põe "abrir" no pedido ao admin, como as outras.

A skill não supõe nenhuma área de dentro, em área nenhuma: quem diz quais existem é o diretor. Toda área de dentro que
ele disser abre para a empresa como as outras, também em área sensível: o que é dado de uma pessoa nunca entra, em
lugar nenhum (`tipos-de-contexto.md`, área sensível), e é esse corte que protege, não o sigilo da pasta.

## 2. O que dizer e o que perguntar

**O porquê vem antes da pergunta,** sempre (`conducao.md`, etapa 2). Os textos-base:

- **Área de dentro:** "Cada área de dentro terá alguém que mantém o contexto dela atualizado e aprova as mudanças;
  você segue respondendo pelo todo."
- **Quem responde:** "É quem mantém o contexto daquela área em dia e aprova o que alguém propõe mudar ali. Quando
  alguém da empresa (ou um agente) pergunta sobre aquela área, a resposta sai do que essa pessoa aprovou."
- **Quem substitui:** "Aprova quando quem responde não está (férias, ausência), para nada ficar parado."
- **"Não sei" é resposta:** sem substituto, fica em branco; sem quem responde, a área de dentro nova não é criada
  agora: o pedaço fica como assunto de `<Área>`, com você, até alguém assumir (então, a conferência e o ok dela).

**Efeito, para dizer antes de criar (regra 10),** uma vez para todas, depois da conferência uma por uma e antes do
ok (seção 3, item 3). É a explicação em linguagem simples do que é uma área de dentro e do que muda para quem responde:

> Antes de eu criar, o que isso muda. Uma área de dentro é um pedaço de `<Área>` com alguém que responde por ele no
> LivupOS. A partir de agora, cada pessoa que você confirmou como quem responde passa a aprovar o que entra na área
> dela, recebe os pedidos de mudança e as perguntas daquele pedaço, e quem substitui aprova quando quem responde não
> está. Você continua podendo aprovar lá e responde por `<Área>` como um todo. Elas `<abrem para a empresa toda, como <Área> | nascem fechadas, como toda área
> de dentro de <Área>; o admin abre quando você pedir>`; dado de pessoa não entra em nenhuma delas. Desfazer é com o
> admin: ele move os documentos e arquiva a área (arquivar desliga, não apaga).
>
> `<Com mais de 10 áreas: "O LivupOS cria até 10 áreas novas por dia por pessoa: crio as 10 primeiras da árvore
> hoje, e as outras ficam para amanhã ou vão ao admin, como você preferir.">`
>
> Posso criar as `<N>` áreas de dentro agora?

O "aberta ou fechada" sai da área de cima: `aberta_para_a_empresa` no `listar` com `estrutura: true`; se a área de cima
está fechada, ou é sensível marcada pelo admin (`sigilosa`), as áreas de dentro nascem fechadas. Na dúvida, diga
"o admin abre, se ainda não estiver aberta".

Os nomes vêm do diretor, conferidos nos gestores da plataforma de apps (`list_areas`) e no Slack
(`slack_search_users`, só leitura); um resultado só no Slack não basta sem o cargo e a área baterem com o pedaço
(`SKILL.md`, etapa 2, item 3). O e-mail sai de lá, ou do diretor quando nenhum dos dois acha. O e-mail não aparece na conversa (salvo na conferência,
quando a busca achou mais de uma pessoa ou o diretor pede): vai só nas chamadas que criam a área ou trocam quem
responde e no arquivo do pedido. As pessoas indicadas precisam concordar: diga ao diretor que confirme com elas ele mesmo (a
mensagem da etapa 4 já explica o papel a elas).

Se quem roda é quem substitui, a plataforma deixa criar, mas criar área de dentro é decisão de quem responde: antes da
primeira conferência, uma pergunta ("`<nome de quem responde>` já concordou com esta divisão? Por que pergunto: criar as áreas de dentro
é decisão de quem responde por `<Área>`; você cria, mas com o acordo dele"). Sim: segue para a conferência. Não ou não sabe: não
cria; o arquivo sai com tudo em "Criar e abrir" e "Confirmação de quem responde: pendente", e quem roda manda a quem
responde, que roda a carga ou confirma (o texto da entrega diz isso). Se quem responde não está mais ativo, não cria:
o pedido sai com "quem responde não está mais ativo: decide o admin".

## 3. Criar com o diretor

Depois do "está certo?" da árvore (parada 2), para as áreas de dentro **novas** (as que já existem não se criam):

1. **Quem pode, antes de tudo.** Só quem responde ou substitui pela área que está sendo montada (etapa 1, item 1), e
   só abaixo dela. Ser admin do LivupOS não basta e não muda o caminho: a skill nunca cria área na raiz, nunca numa
   área que a pessoa não responde nem substitui, nunca com `sigilosa`. Se `contexto_liv_up_criar_area` não aparece
   entre as ferramentas, a plataforma ainda não deixa: tudo vai no pedido ao admin (seção 4), sem tentar. Área de
   dentro nova **sem quem responde** não se cria: o pedaço fica como assunto de `<Área>` até alguém assumir.
2. **Conferência, uma por uma.** Uma mensagem por área de dentro nova, com o que vai ser gravado:

   > **`<Nome da área de dentro>`** (`<n>` de `<N>`)
   > - Nome: `<nome>`
   > - Endereço: `<id>`
   > - Quem responde: `<nome completo>` (`<cargo, se veio do Slack ou da plataforma>`)
   > - Quem substitui: `<nome completo | em branco>`
   >
   > Está certo? Por que pergunto: é exatamente isto que vai ser criado no LivupOS, e é com essas pessoas que o
   > contexto de `<nome>` vai ser aprovado.

   O e-mail não aparece; se a busca achou mais de uma pessoa ou o diretor pedir, mostre o e-mail só daquela. Corrigiu
   algo: refaça só aquela área. "Essa não": ela sai da criação e, se for pedaço de `<Área>`, vira frente.
3. **O efeito e o ok** (seção 2, "Efeito, para dizer antes de criar"), numa mensagem só, depois da última conferência.
   Só um sim claro vale ("pode", "cria", "sim"); resposta sem ter entendido o efeito: explique de novo (regra 10).
   Se quem roda é quem substitui, a pergunta do acordo de quem responde vem antes da primeira conferência (seção 2).
4. **Criar.** Com o ok, `contexto_liv_up_criar_area` uma vez por área, na ordem da árvore (a de cima antes da de dentro
   dela): `id`, `nome`, `pai` = a área de cima (`<area>`, ou a área de dentro recém-criada, no nível 2), `owner` e
   `substituto` (os e-mails conferidos; pessoas diferentes), `motivo` "Carga inicial: área de dentro de `<Área>`,
   conferida com quem responde em `<AAAA-MM-DD>`" (sem nome nem motivo pessoal), `intencao` "Criar a área de dentro
   conferida com quem responde na carga inicial" (sem dado de pessoa), sem `sigilosa`. A ferramenta exige `intencao`:
   erro de validação por campo faltando não é recusa, corrija e chame de novo. Diga antes da primeira chamada: "Criando
   as `<N>` áreas de dentro." Uma por vez; uma recusa não para as outras.
5. **O resultado, numa mensagem:** a árvore de novo com "criada" em cada uma, e o que veio de volta:
   - `aberta_para_a_empresa: false`: "nasceu fechada (como `<Área>` | por ser área de dentro de uma área sensível):
     vai no pedido ao admin para abrir";
   - `provisorias` com a pessoa: "`<nome>` ainda não entrou no LivupOS: o papel vale no primeiro login dela";
   - recusada: o motivo em linguagem simples (tabela abaixo), e ela vai no pedido ao admin, em "Criar e abrir".
6. **Troca de quem responde numa área de dentro que já existe** (pessoa que não está mais ativa, a mesma pessoa nos
   dois papéis, responsável herdado que o diretor quer próprio), só quando quem roda responde ou substitui pela área
   de cima dela (por exemplo, o diretor rodando a carga da diretoria ou da área de dentro): a mesma conferência (só
   aquela área), o efeito ("a partir de agora, quem aprova em `<área de dentro>` é `<nome>`; `<nome de antes>` deixa
   de aprovar lá") e o ok; então `contexto_liv_up_definir_dono` com `area`, `owner`, `substituto` (repita o atual
   para mantê-lo: omitir deixa sem substituto), o `motivo` e a `intencao`, sem dado de pessoa. Quando quem roda é o
   próprio responsável ou substituto da área que está sendo montada, sem decidir a de cima (a diretoria, ou quem
   responde por uma área de dentro rodando a carga dela), não troca daqui: vai ao pedido ao admin (seção 4) ou, numa
   área de dentro, numa mensagem pronta para quem responde pela área de cima.

**Quando a plataforma recusa** (a mensagem diz o que fazer; diga em linguagem simples e siga com as outras):

| A recusa diz | O que dizer ao diretor | O que fazer |
|---|---|---|
| "você não responde pela área" ou "só um admin" | "O LivupOS não deixou você criar `<nome>` daqui." | Vai ao pedido ao admin |
| "o líder cria até o nível 2" | "`<nome>` ficaria fundo demais na árvore: o LivupOS para na área de dentro da área de dentro." | Pergunte se ela fica um nível acima; se sim, refaça a conferência dela (outro lugar, outro endereço) e peça o ok de novo; senão, pedido ao admin |
| "você já criou 10 áreas nas últimas 24 horas" | "O LivupOS limita a 10 áreas novas por dia, para evitar erro em lote." | As que faltam vão ao pedido ao admin ou ficam para outra conversa, amanhã (o diretor escolhe); amanhã, mostre de novo a conferência delas e peça o ok antes de criar |
| "id da área de dentro" ou "a área ... já existe" | "O endereço `<id>` não serve (`<já existe | precisa começar por <area>->`)." | Sugira outro endereço, refaça a conferência daquela área e peça o ok de novo antes de criar |
| "o sigilo é um só para todas as áreas" (só em área sensível marcada pelo admin) | "O LivupOS não deixa `<nome>` responder por `<área de dentro>` agora: `<nome>` tem um acesso temporário a outra área, e ele valeria aqui também." (sem dizer qual área nem qual acesso) | O diretor escolhe outra pessoa (refaça a conferência e o ok) ou a área vai ao pedido ao admin, com "quem responde tem acesso temporário em outra área" |
| "começa pelo de outra área" | "O endereço `<id>` parece de outra área que já existe." | Sugira outro endereço, refaça a conferência e peça o ok de novo |
| "a marca sigilosa só o admin" | (não acontece: a skill nunca pede) | — |

## 4. O pedido ao admin (o que sobra)

Entregue o arquivo `areas-de-dentro-<area>-AAAA-MM-DD.md` no fim da etapa 2 (depois de criar, se criou), no mesmo lugar
do plano ou, no Claude sem pasta, como arquivo para baixar, sempre que sobrar pelo menos um destes: área de dentro que
a plataforma recusou ou que não foi criada (quem substitui sem o acordo de quem responde, ferramenta ausente); área de
dentro criada que nasceu fechada; a diretoria ainda não aberta para a empresa; troca de quem responde ou de quem
substitui **na área que está sendo montada**, quando quem roda não decide a área de cima (item 6 da seção 3). Sem
nada disso, não há arquivo: diga numa linha que nada depende do admin. Se depois aparecer outra área de dentro, ela
passa pela conferência, pelo efeito e pelo ok (seção 3) e é criada; só o que a plataforma recusar ou que nascer
fechado entra no mesmo arquivo, na seção "Atualização de AAAA-MM-DD" com só o que mudou, entregue de novo ("é um
complemento ao pedido que você já mandou: o admin faz só o que está na atualização"). Repita a entrega no fechamento.

**O id.** Na hierarquia, a área de dentro é da diretoria (a área de cima, com quem responde por ela aprovando lá).
Só o endereço dos documentos começa pelo id dela (`logistica-last-mile/visao-geral`), porque no LivupOS todo caminho começa pelo
id da área e o id não tem barra; assim, se a área mudar de diretoria, nenhum link quebra. Por isso o id é único na
empresa e **sempre leva o id da diretoria na frente**, para mostrar a quem ela pertence:
- `<id da diretoria>-<nome curto>`: minúsculas, sem acento, com hífen (`logistica-last-mile`,
  `operacoes-qualidade`, `people-dp`). O nome curto é o que o diretor usa, numa ou duas palavras; o nome da plataforma de apps só
  quando já é curto e é o mesmo (`last_mile`, `qualidade`, `dp`; sublinhado vira hífen e a diretoria não se repete:
  `people_performance` vira `people-performance`). Nome longo da plataforma não entra: o diretor diz "Recrutamento" e a
  plataforma tem `recrutamento_selecao`, o id é `people-recrutamento`;
- confira que ele não existe no `listar` da raiz (vazio = as áreas que quem roda lê). Área sigilosa que quem roda não
  lê não aparece ali: diga no arquivo "conferido no que o diretor lê; o admin confere o resto".
Na conversa, o id aparece como "endereço" só na árvore da parada 2, na conferência de cada área e na recusa de
endereço. Nunca diga que a área fica "fora" da diretoria.

Modelo do arquivo (seções vazias saem):

```markdown
# Pedido ao admin do LivupOS: áreas de dentro de <Área> (<AAAA-MM-DD>)

Pedido feito por <nome e e-mail de quem rodou a carga>, que <responde por | substitui em> `<area>`, durante a carga.
Quem responde por `<area>`: <nome e e-mail>.

Já criadas na carga, por <nome>: <ids, ou "nenhuma">.

## Abrir para a empresa (áreas de dentro já criadas, que nasceram fechadas)

| Id | Nome | Por que nasceu fechada |
|---|---|---|
| `<id>` | <nome> | <"a área de cima está fechada" ou "área de dentro de área sensível"> |

## Criar e abrir para a empresa (a plataforma recusou ou não foi criada)

Cada área abaixo: criar como área de dentro de `<area>`, definir quem responde e quem substitui, e **abrir para a
empresa**. Motivo de não ter sido criada na carga: <a recusa em linguagem simples | "quem substitui, sem o acordo de
quem responde" | "a ferramenta não estava disponível">.

| Id (único na empresa) | Nome | Área de cima | Quem responde (e-mail) | Quem substitui (e-mail) | O que cuida |
|---|---|---|---|---|---|
| `<id>` | <nome> | `<area>` | <e-mail, ou "fica com quem responde por <area> até alguém assumir"> | <e-mail ou "em branco"> | <uma linha> |

Ids conferidos no que <nome> lê no LivupOS; o admin confere as áreas que não aparecem para ele.

## A diretoria para a empresa

- `<area>` hoje: <aberta / fechada / não sei>. Pedido: <abrir para a empresa / já está aberta>.

## Troca de quem responde (só a que a carga não faz: na área que está sendo montada, sem decidir a de cima)

| Área | Quem responde hoje | Quem passa a responder (e-mail) | Quem passa a substituir (e-mail) | Por quê (só: "não está mais ativo", "herdado da área de cima", "a mesma pessoa nos dois papéis", "pedido do diretor") |
|---|---|---|---|---|

(vazio se nada muda)

## Confirmação

<Nome> confirmou em <AAAA-MM-DD>, nesta carga, que entendeu: cada área de dentro passa a ter quem responde e quem
substitui, que aprovam o que entra nela; que ele continua podendo aprovar lá; que tudo abre para a empresa (as que
nasceram fechadas, com este pedido); e que desfazer é com o admin. As pessoas indicadas: <concordaram, segundo ele | ele ainda vai confirmar com elas>.
<Se quem rodou é quem substitui e quem responde ainda não concordou: "Confirmação de quem responde por <area>: pendente.">
```

Antes, o arquivo se chamava `subareas-<area>-AAAA-MM-DD.md`; na retomada, aceite os dois nomes.

O "por quê" nunca traz o motivo pessoal (licença, desligamento, saúde): é dado de pessoa. Se o diretor contar, não
repita no arquivo nem no plano.

## 5. Desfazer

Uma área de dentro criada por engano (na carga ou pelo admin) se desfaz assim, pelo admin: mover os documentos dela para a diretoria (simulando
antes quem ganha ou perde acesso), corrigir os links e arquivar a área (arquivar desliga, não apaga). O que não volta
sozinho é o hábito das pessoas, que já mandavam pedido de mudança a quem responde por ela.
