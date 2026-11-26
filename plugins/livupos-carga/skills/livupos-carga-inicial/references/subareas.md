# Áreas de dentro: quando, como explicar e o pedido ao admin

Na conversa com o diretor, "área de dentro"; na plataforma, subárea. A carga começa pela estrutura: a área, quem
responde por ela e as áreas de dentro, cada uma com quem responde e quem substitui (`SKILL.md`, etapa 2). A skill não
cria área nem abre área: ela monta o pedido, o diretor decide e manda, e o admin cria a partir do arquivo.

## 1. Quando um pedaço vira área de dentro

**Quando tem alguém que cuida do dia a dia** (`forma-comum.md`, seção 2). Pode ser uma gerência ou uma frente de
trabalho. Pedaço sem ninguém que cuide é frente (pasta dentro da área). O critério antigo ("só quando muda quem decide
ou quem lê") não vale mais.

Se a área já tem áreas de dentro, a carga respeita a divisão que existe e confirma quem responde e quem substitui em
cada uma. Uma área de dentro que já existe e é sigilosa segue como está (quem muda isso é o dono do LivupOS, não a carga).

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
- **"Não sei" é resposta:** sem substituto, fica em branco; sem quem responde, a área de dentro fica com você até
  alguém assumir.

**Efeito, para dizer antes do pedido (regra 10),** uma vez para todas, na parada 2, junto da árvore (a mensagem que
entrega o arquivo não repete):

> Quando o admin criar: cada área de dentro passa a ter quem responde e quem substitui, que aprovam o que entra nela;
> você continua podendo aprovar lá, como quem responde por `<área>`. Elas abrem para a empresa toda, como o resto do
> contexto da Liv Up. Desfazer é com o admin: ele move os documentos e arquiva a área (arquivar desliga, não apaga).

Os nomes vêm do diretor, conferidos nos gestores da plataforma de apps (`list_areas`) e no Slack
(`slack_search_users`, só leitura); um resultado só no Slack não basta sem o cargo e a área baterem com o pedaço
(`SKILL.md`, etapa 2, item 3). O e-mail sai de lá, ou do diretor quando nenhum dos dois acha. O e-mail não aparece na conversa, só no arquivo, que o diretor
confere antes de mandar. As pessoas indicadas precisam concordar: diga ao diretor que confirme com elas ele mesmo (a
mensagem da etapa 4 já explica o papel a elas).

Se quem roda é quem substitui, criar área de dentro é decisão de quem responde: o pedido sai com "Confirmação de quem
responde: pendente", e quem roda manda a quem responde, que confirma e manda ao admin (o texto da entrega diz isso). Se quem responde não está mais ativo,
o pedido sai com "quem responde não está mais ativo: decide o admin".

## 3. O pedido ao admin (entrega obrigatória)

Sempre que houver pelo menos uma área de dentro nova, troca de quem responde ou de quem substitui (pessoa que não está
mais ativa, a mesma pessoa nos dois papéis, responsável herdado que o diretor quer próprio), ou a diretoria ainda não
aberta para a empresa, entregue o arquivo `areas-de-dentro-<area>-AAAA-MM-DD.md` no fim da etapa 2, no mesmo lugar do
plano ou, no Claude sem pasta, como arquivo para baixar. Se depois aparecer outra área de dentro, acrescente ao mesmo
arquivo a seção "Atualização de AAAA-MM-DD" com só o que mudou e entregue de novo ("é um complemento ao pedido que
você já mandou: o admin cria só o que está na atualização"). Repita a entrega no fechamento.

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
Na conversa, o id aparece como "endereço" só na árvore da parada 2. Nunca diga que a área fica "fora" da diretoria.

Modelo do arquivo:

```markdown
# Pedido ao admin do LivupOS: áreas de dentro de <Área> (<AAAA-MM-DD>)

Pedido feito por <nome e e-mail de quem rodou a carga>, que <responde por | substitui em> `<area>`, durante a carga.
Quem responde por `<area>`: <nome e e-mail>.

## Criar e abrir para a empresa

Cada área abaixo: criar como área de dentro de `<area>`, definir quem responde e quem substitui, e **abrir para a
empresa** (a abertura não vem da diretoria: cada área se abre).

| Id (único na empresa) | Nome | Área de cima | Quem responde (e-mail) | Quem substitui (e-mail) | O que cuida |
|---|---|---|---|---|---|
| `<id>` | <nome> | `<area>` | <e-mail, ou "fica com quem responde por <area> até alguém assumir"> | <e-mail ou "em branco"> | <uma linha> |

Ids conferidos no que <nome> lê no LivupOS; o admin confere as áreas que não aparecem para ele.

## A diretoria para a empresa

- `<area>` hoje: <aberta / fechada / não sei>. Pedido: <abrir para a empresa / já está aberta>.

## Troca de quem responde (na diretoria ou numa área de dentro que já existe)

| Área | Quem responde hoje | Quem passa a responder (e-mail) | Quem passa a substituir (e-mail) | Por quê (só: "não está mais ativo", "herdado da área de cima", "a mesma pessoa nos dois papéis", "pedido do diretor") |
|---|---|---|---|---|

(vazio se nada muda)

## Confirmação

<Nome> confirmou em <AAAA-MM-DD>, nesta carga, que entendeu: cada área de dentro passa a ter quem responde e quem
substitui, que aprovam o que entra nela; que ele continua podendo aprovar lá; que tudo abre para a empresa; e que
desfazer é com o admin. As pessoas indicadas: <concordaram, segundo ele | ele ainda vai confirmar com elas>.
<Se quem rodou é quem substitui: "Confirmação de quem responde por <area>: pendente.">
```

Antes, o arquivo se chamava `subareas-<area>-AAAA-MM-DD.md`; na retomada, aceite os dois nomes.

O "por quê" nunca traz o motivo pessoal (licença, desligamento, saúde): é dado de pessoa. Se o diretor contar, não
repita no arquivo nem no plano.

## 4. Desfazer

Uma área de dentro criada por engano se desfaz assim, pelo admin: mover os documentos dela para a diretoria (simulando
antes quem ganha ou perde acesso), corrigir os links e arquivar a área (arquivar desliga, não apaga). O que não volta
sozinho é o hábito das pessoas, que já mandavam pedido de mudança a quem responde por ela.
