# Ler e separar

O trabalho mais longo da carga, e o que a pessoa não vê. Faça nesta ordem, ficha por ficha.

## 1. Classificar cada ficha ou documento de origem

Cada pedaço recebe uma classe (abaixo) e, se vira documento, um lugar: a área de dentro que é dona dele, ou uma pasta
dentro de `geral/` (a frente, ou a pasta que o time procura), ou `sistemas/` e `indicadores/` na raiz
(`forma-comum.md`, seções 2 e 3). Sai de quem procura: "quem cuida disso aqui?". O mesmo documento de origem pode se
dividir entre frentes.

| Classe | Sinais | Destino |
|---|---|---|
| Processo ou regra | passo a passo, "quem faz", "quando", regras vigentes, exceções | documento oficial (tipo `processo`) |
| Indicador | fórmula, meta, fonte do dado, frequência | um documento por indicador em `indicadores/`, sem a fórmula e sem a meta |
| Ritual | daily, semanal, comitê, checkpoint: objetivo, participantes, cadência | uma linha na seção Rituais da visão geral da área; documento em `geral/` (na frente dele) só se tem regra própria |
| De outra área | o dono é de outra área (expansão, comercial de varejo) | uma linha na visão geral ou termo na seção de outras áreas do glossário; não vira documento |
| Acompanhamento de projetos | status de projeto, "roda?", candidatos, colunas de acompanhamento de agente ou app | sai; fica no app |
| Projeto, meta ou plano do ano | tese de projeto, meta de indicador para o ano, plano de ação, OKR | não sobe na carga: vai para o plano como "espera a estratégia" (`forma-comum.md`, seção 4) |
| Histórico | "decisões recentes", versões antigas, linha do tempo | sai do forte; a regra vigente diz "vale desde" |
| Política, valores, regra de cálculo | benefício, elegibilidade, valores da empresa, classificação de verba | documento oficial pelo molde de `tipos-de-contexto.md` |

## 2. Classificar cada afirmação de regra

Para cada regra, uma de quatro: **vigente**, **substituída**, **em teste**, **proposta**. Pistas:

- a mesma regra aparece com datas diferentes na seção de decisões: a mais recente que foi aplicada é a vigente;
- "a partir de", "passou a", "agora" com data: vigente desde essa data, se nada posterior a muda;
- "vamos testar", "piloto", "até tal dia": em teste, com a data de fim;
- "ficou de", "proposta", "seria bom": proposta. Não vai para o forte.

Só a vigente vai para o documento oficial, com "vale desde". Em teste entra marcada como teste, com até quando. A data
que importa é a em que passou a valer, não a da reunião em que se falou dela.

## 3. Confirmações que invalidam lacunas

Fichas montadas à mão costumam ter uma confirmação nova no topo ("Confirmado pela supervisão em 13/11: teto da taxa da Saúde R$
11,50") e o corpo com o ⚠️ antigo. Para cada confirmação:

1. procure no mesmo documento todo ⚠️, ❗ e pergunta sobre o mesmo assunto;
2. troque o ⚠️ pelo valor confirmado, com "confirmado por <papel ou nome de quem decide> em <data>";
3. tire a pergunta da lista.

Faça o mesmo com as respostas que a pessoa der.

Confirmação de um valor não é decisão da regra: "confirmado pela supervisão em 13/11" diz que o número está certo, não
quem decide mudá-lo. Ela serve de fonte e de data. O "quem decide" sai da pergunta ao diretor (ver seção 6).

Quando a confirmação mais nova, dada por quem decide, diverge da fonte que o material chama de "a que vale" (o teto
confirmado pela supervisão em 13/11 contra o Google Doc da escada), a mais nova fica no texto com a data, a divergência
vira nota da área e pergunta ao owner, e o documento diz qual vale até o owner decidir. Se nenhuma das duas versões vem
de quem decide, ou o owner diz que não sabe qual vale, é divergência aberta (seção 4), e a seção 4 vence.

## 4. Divergência e lacuna

- **❗ divergência aberta** (duas fontes dizem coisas diferentes e ninguém decidiu): nenhuma das versões vai para o
  forte, em nenhum documento (nem na visão geral, nem no glossário). No lugar, uma linha de "Em aberto" com quem
  responde. Vira nota da área, com as duas versões e as fontes, e pergunta ao dono.
- **⚠️ lacuna:** vira pergunta ao dono. Se não tem dono claro ou a resposta não vai chegar logo, uma linha na seção "Em
  aberto" no fim do documento, dizendo quem responde.
- **💭 hipótese ou sugestão** de quem escreveu a ficha: sai do forte. Se for útil, nota da área.

## 5. Sensível

**Corte, em qualquer lugar do LivupOS:**

- conteúdo de 1:1;
- conclusão tirada de agenda pessoal (vira pergunta, nunca afirmação);
- nota de pessoa de um vault;
- caso com pessoa identificável: fraude, acidente, reincidência, cliente ou parceiro que reclamou (em Logística, o
  motorista que sumiu; em Produção, o operador acidentado);
- mudança de lotação de alguém;
- avaliação ou crítica a pessoa ou time, clima de reunião;
- contato de cliente ou de parceiro B2B, e comentário de cliente final identificável;
- nome de contato externo (pessoa de fornecedor ou parceiro); a empresa parceira pode aparecer, a pessoa não.
  Parceiro com nome de pessoa conta como pessoa até alguém confirmar que é empresa ("dois outros parceiros");
- dado de pessoa: salário, desconto, falta, atestado, saúde, licença, avaliação, promoção, desligamento, benefício
  escolhido, dependente, matrícula, mesmo em exemplo ou amostra, e número pequeno que identifica alguém (em área
  sensível, a lista completa está em `tipos-de-contexto.md`, área sensível);
- CPF, cartão, conta, senha, token (o LivupOS bloqueia o depósito).

Ao cortar um caso, guarde a **regra** que ele ensinou, se houver: "fraude com baixa feita de casa" vira "baixa só com
o motorista no local; suspeita vai para <papel>", sem o caso.

**Dado de negócio sensível** (valor de contrato, margem, faixa salarial): sai do texto e o documento aponta onde mora
(`fora-da-empresa.md`). Tudo o que a carga publica abre para a empresa: o corte é o que protege.

## 6. Pessoa → papel

1. Liste as pessoas que entram em "quem faz o quê" e "quem decide". As outras não entram no texto e não precisam de
   busca.
2. **Papel no texto = a função que o material descreve** ("o roteirizador da noite", "a gestão de parceiros"). Vários
   do time podem ter o mesmo cargo com funções diferentes. O cargo do Slack (`slack_search_users`) só desempata ou
   confirma; se o cargo contradiz o material, vira pergunta. Apelido ambíguo ("Duda", três pessoas no Slack): não
   escolha, pergunte.
3. **Quem decide:** uma pergunta ao owner por documento, não por regra ("quem decide as regras da escada?"), feita no
   plano da leva. A resposta vale para todas as regras do documento, salvo exceção que ele disser. Enquanto não há
   resposta, o documento traz "Quem decide: ⚠️" uma vez, na abertura, e não em cada regra. O nome pode aparecer em
   "quem decide" (é o dono) se o owner confirmar; senão, o papel.
4. "Quem escreveu a ficha" não é "quem decide a regra".

## 7. Nomes de transcrição

Atas e fichas tiradas de transcrição trazem nomes errados. Junte os que têm grafia ou som parecido com um sistema,
parceiro, termo ou pessoa já conhecidos ("Biamo", "Bia", "Aviamo" → Abbiamo; "Proteus" → Protheus; "Maiara" → Mayara).

- certo e de termo ou sistema: sinônimo no glossário, para as atas resolverem o termo;
- certo e de pessoa: só na tabela pessoa → papel do plano (pessoa não vai para o glossário);
- duvidoso ("Avião"): pergunta, nunca sinônimo.

## 8. Tamanho: dividir e juntar

Alvo: 1 a 3 mil tokens por documento (conte ~4 caracteres por token).

- Ficha acima de ~3 mil tokens: divida por assunto, cada parte com sentido sozinha (roteirização → alocação e montagem;
  escada e taxas; falhas, quebra e resgate).
- Fichas ralas que se repetem: junte numa só, sem repetir o que já está noutro documento (entrega + acompanhamento).
- Indicadores espalhados por várias fichas: junte por família (pontualidade e impacto; custo).
