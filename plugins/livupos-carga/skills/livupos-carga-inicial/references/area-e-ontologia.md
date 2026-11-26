# O que é da área e o que é da ontologia da empresa

O contexto da área é o que pessoas **decidem** e como trabalham. A ontologia é o que **existe** com identidade estável
nos sistemas e nos dados. A carga escreve só o primeiro e aponta o segundo.

| Da ontologia da empresa (a carga aponta) | Da área (a carga escreve) |
|---|---|
| entidades: entrega, rota, pedido, palete, parceiro, lote | regras: escada de chamadas, critério de quebra de rota |
| dimensões: canal, modal, motivo de contato (a lista de valores) | o que a área decide sobre uma métrica: que unidades entram no CPO, o que conta como atraso (a meta do ano vai para `estrategia/`, não para a carga) |
| sistemas de tech e tabelas: Abbiamo, Protheus, `delivery_lastmile_points` | processos: fechamento, carregamento, gestão de parceiros; o uso dos sistemas da área (para que serve, quem usa, quem cuida) |
| fluxos entre sistemas | vocabulário e referências do time |
| a conta das métricas: fica na camada semântica do BigQuery, não na ontologia nem na área | |

Critério de entrada na ontologia: ter identidade estável e morar em algum lugar (sistema, tabela, consulta, planilha,
pasta do Drive).

## Quando o termo tem as duas partes

É o caso mais comum. A entidade fica na ontologia e a decisão fica na área:

- **Regra sobre entidade:** "venda válida" é regra da área; o pedido de venda é entidade. O documento da área diz a regra
  e aponta a entidade.
- **Atributo cujo valor alguém decide:** "taxa por degrau" é atributo da chamada de parceiro, e o valor é regra da área.
- **Dimensão cuja lista a área decide:** "motivo de impacto": a lista mora no sistema, quem decide o que cada motivo
  significa é a área. O documento da área tem o significado; a ontologia, quando existir, aponta para ele.
- **Fonte que vale:** se o mesmo número está em dois lugares (o custo planejado em dois apps), quem decide qual vale é a
  regra da área.

## Na carga

1. Para cada sistema, tabela ou entidade citada, primeiro separe pela ordem de `moldes.md`, "Sistema da área":
   **sistema da área** ganha documento da área na lista `sistemas/` (da área ou da frente que o usa) e sai desta lista; **sistema de outra área**
   vira link para o documento da área dona (ou nome e área em texto) e também sai desta lista; **ferramenta de uso
   geral** não entra. Para o resto (sistema de tech, tabela, entidade), procure o documento que já existe
   (`tech/sistemas/*` ou o espaço `ontologia`, com `contexto_liv_up_buscar`).
2. **Existe:** no documento da área, só link. No glossário, definição curta, onde mora e o link.
   **Existe só em parte** (há documento da integração com o sistema, como o envio de pedidos à Abbiamo, mas não do
   sistema em si): link para o que existe e o sistema vai para a lista do item 3.
3. **Não existe:** vai para a lista "o que falta fora da área": nome, definição curta, onde mora (sistema,
   tabela ou planilha), de que documento da área veio, quem conhece (papel). Métrica que não está na camada semântica
   do BigQuery entra na mesma lista, marcada "métrica, para o catálogo de Dados".
   A lista entra sempre como **uma nota da área** (`origem.ref`: `carga-inicial/<area>/o-que-falta-fora-da-area`),
   mostrada antes de publicar a leva. A skill não propõe nada noutro espaço: uma proposta lá chega a outro owner, e a carga só fala
   com quem está rodando. No fechamento, sugere ao owner levar a lista a quem cuida da ontologia e do catálogo de Dados.
4. Nunca escreva `<area>/ontologia.yaml`, nem um documento que descreva sistema de tech, tabela ou integração. Sistema
   da área tem documento, mas só a parte humana (para que serve, quem usa, quem cuida), nunca a estrutura.
