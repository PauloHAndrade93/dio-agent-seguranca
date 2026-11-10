# Laboratorio: codigo vulneravel para testar a skill

Esta pasta contem o codigo usado para exercitar a skill
[`vulnerability-analysis`](../skills/vulnerability-analysis/SKILL.md) do DIO Agent.

> ⚠️ Codigo **propositalmente vulneravel**, apenas para estudo em ambiente de
> laboratorio proprio. Nao use estes padroes em producao.

## Arquivos

| Arquivo | O que e |
|---------|---------|
| `app.py` | Login **vulneravel** a SQL Injection (CWE-89). Monta o SQL concatenando a entrada do usuario. |
| `app_corrigido.py` | Versao **segura**: usa consulta parametrizada (placeholders `?`). |

## Como rodar

```bash
python app.py            # mostra a falha
python app_corrigido.py  # mostra a correcao
```

Nao precisa instalar nada: usa `sqlite3`, que ja vem com o Python, e um banco
em memoria.

## O que observar

No `app.py`, a entrada maliciosa no campo de usuario:

```
' OR '1'='1' --
```

transforma a consulta em algo sempre verdadeiro e **burla a autenticacao**
(`Acesso: True` sem saber a senha). No `app_corrigido.py`, a mesma entrada
nao tem efeito (`Acesso: False`), porque o banco trata o valor como dado,
nunca como codigo SQL.

## Como usar com o agente

Abra o harness na pasta do projeto e peca uma analise, por exemplo:

> Atue como especialista em AppSec. Analise o arquivo `lab/app.py`, explique a
> falha, a tecnica do MITRE ATT&CK envolvida e como corrigir — sem reescrever
> tudo por mim.

O agente deve seguir a skill `vulnerability-analysis`: pedir contexto quando
faltar, classificar impacto, probabilidade e severidade, apontar a correcao
(consulta parametrizada) e so entao mostrar o caminho seguro.
