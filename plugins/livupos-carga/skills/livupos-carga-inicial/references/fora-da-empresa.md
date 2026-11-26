# Aberto para a empresa por padrão

Desde 25/11/2026, **tudo o que a carga publica é aberto para a empresa por padrão**: a área de dentro criada na carga
herda a abertura da área de cima, e a que nasce fechada (área de cima fechada ou sensível marcada pelo admin) vai no
pedido ao admin para abrir, como a diretoria ainda fechada (`subareas.md`, seções 3 e 4); nenhum documento leva a marca
"não abre" por rotina. A skill
**não sugere** "abre para a empresa: não" documento a documento, nem pergunta isso na parada de publicar. Áreas
sigilosas que já existem não mudam (quem decide é o admin do LivupOS).

O que segura o sensível não é a marca, é o **corte**: o que é de uma pessoa nunca entra, em área aberta ou fechada
(`separar.md`, seção 5). O que é dado de negócio sensível sai do texto e fica onde já mora; o documento aponta.

## A ordem de decisão

1. **Tire do documento o dado** (o número, o valor, o nome do cofre, a alçada, o valor da faixa salarial). Quase sempre
   o documento continua útil sem ele: "o contrato define o modelo de cobrança", "as faixas por cargo estão na planilha
   de remuneração, que só o time de remuneração abre". Sem o dado, o documento abre.
2. **Se a regra não se entende sem o dado,** deixe o dado fora mesmo assim e escreva onde ele está e quem pergunta a
   quem. Não sugira a marca.
3. **Duas exceções, em que o texto todo é o dado** (não dá para tirar um número e abrir): mecanismo de defesa (como se
   detecta fraude, regra antifraude) e apuração ou investigação (como uma denúncia é apurada). Aí pergunte ao diretor,
   uma vez, com o porquê: "Este documento descreve como `<a apuração é feita | a fraude é detectada>`; aberto, ajuda
   quem quer contornar. Prefere que só quem lê `<área>` veja? Se sim, ele leva a marca 'não abre'." Na dúvida dele,
   o documento fica para a leva seguinte, não sobe com a marca sem o "sim".
4. **O diretor pode pedir a marca** num documento. Diga o efeito e registre (abaixo).

**Efeito da marca, para dizer (regra 10):** "Com a marca, só quem lê `<área>` vê este documento; a empresa não. Tirar a
marca depois é publicar uma versão nova sem ela." O admin também pode marcar, e a marca dele só ele tira.

As visões gerais de `estrategia/` e `projetos/` nunca levam a marca.

## Onde fica a decisão, quando há marca

1. No frontmatter do documento (`fora_da_empresa: true`), que é o que fecha de fato.
2. Na justificativa da publicação (um item do Resumo).
3. No plano local, seção "O que não abre", com documento, motivo e data.

## Categorias: o dado que sai do texto

A lista oficial é mantida pelo admin do LivupOS; antes de usar a tabela abaixo, procure-a (`contexto_liv_up_buscar`
"o que não abre para a empresa"); se existir, ela vale. A tabela diz o que **sai do texto** (passo 1), não o que leva a
marca. A estratégia usa a mesma tabela (`estrategia.md`).

| Categoria | Exemplos |
|---|---|
| Preço ou condição negociada | preço por km, por entrega, diária; taxa extra |
| Contrato e valor de fornecedor | valor por parceiro, contrato, reajuste e negociação em curso |
| Comissão | comissão de venda ou de parceiro |
| Verba e número financeiro | orçamento, capex, meta anual que não será atingida, número comercial de outra área (as metas do ano em `estrategia/` são abertas por desenho) |
| Margem e P&L | margem por canal, P&L de produto ou de canal |
| Remuneração | faixa salarial por cargo, tabela de bônus, valor de benefício (a regra entra; o valor fica onde mora) |
| Condição com plataforma ou parceiro | campanha negociada, taxa, cofinanciamento |
| Teste comercial em andamento | grupo de teste, lojas e preços do teste |
| Onde ficam credenciais | qual cofre, qual conta de serviço |
| Alçadas | quem aprova até quanto (o papel entra; o valor, não) |
| Mecanismo de defesa, apuração e investigação | ver o passo 3 |

## O que já é público

Não fecha: o preço ao consumidor está no site e abre. A política por trás dele (margem, regra de reajuste) entra como
regra, sem o número.
