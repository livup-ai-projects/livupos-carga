# livupos-carga

Distribuição temporária da carga inicial do LivupOS para os diretores da Liv Up. Arquivado depois da carga.

## Instalar

Cole o link deste repositório no Claude Code (a aba Code do app do Claude serve; não precisa de git nem do terminal) e
peça: "instala essa skill".

Instruções para o Claude:

1. Baixar o zip https://github.com/livup-ai-projects/livupos-carga/archive/refs/heads/main.zip e extrair só a pasta
   `livupos-carga-main/plugins/livupos-carga/skills/livupos-carga-inicial/` em `~/.claude/skills/livupos-carga-inicial/`
   (no Windows, `$env:USERPROFILE\.claude\skills\livupos-carga-inicial\`). Se a pasta já existir, apagar e extrair de novo.
2. Conferir que existe `~/.claude/skills/livupos-carga-inicial/SKILL.md` e que a linha `versao:` dele é 2026-11-27.5.
3. Avisar a pessoa para reiniciar o app do Claude, conferir que o conector do LivupOS está ligado e, numa conversa
   nova, escrever "quero montar o contexto de <área> no LivupOS".

Quem já instalou pelo `/plugin` (Claude Code no terminal) não precisa instalar de novo: as duas formas trazem a
mesma skill. Não instale das duas formas.

## Atualizar

Peça de novo "instala essa skill" com o link deste repositório: o Claude troca a pasta pela versão nova.

## No terminal (opcional)

```
/plugin marketplace add livup-ai-projects/livupos-carga
/plugin install livupos-carga@livupos-carga
```

Gerado de livup/livupos-carga-inicial, commit b39d070, versão 2026-11-27.5.
