# Fundamentos de seguranca

Contexto de seguranca da informacao para o agente usar na skill
`vulnerability-analysis`. A ideia e dar vocabulario comum para conversar com o
estudante sobre risco de forma clara, sem jargao desnecessario.

## Vulnerabilidade, ameaca e risco

Tres palavras que parecem sinonimos, mas nao sao:

- **Vulnerabilidade:** uma fraqueza. A porta destrancada. Ex.: um login que monta
  SQL concatenando a entrada do usuario (SQL Injection).
- **Ameaca:** quem ou o que pode explorar a fraqueza. O ladrao que passa na rua.
  Ex.: um atacante procurando formularios de login vulneraveis.
- **Risco:** a chance de a ameaca explorar a vulnerabilidade **e** o tamanho do
  estrago. Porta destrancada numa rua movimentada = risco alto.

Formula util para explicar: **Risco = Probabilidade x Impacto.** Reduzir qualquer
um dos dois reduz o risco.

## A triade CIA

Toda analise de seguranca gira em torno de proteger tres propriedades:

- **Confidencialidade:** so quem tem permissao acessa a informacao. Quebra: um
  vazamento de dados, uma senha exposta.
- **Integridade:** a informacao nao e alterada sem autorizacao. Quebra: alguem
  muda o valor de um pagamento, adultera um registro.
- **Disponibilidade:** a informacao e o sistema estao acessiveis quando precisam.
  Quebra: um ataque de negacao de servico (DoS), um ransomware que cifra tudo.

Ao analisar uma falha, ajuda perguntar: **qual lado da triade ela ameaca?** Uma
SQL Injection pode ferir os tres (ler dados, alterar dados, derrubar o banco).

## Impacto, probabilidade e severidade

Para classificar o risco de forma comparavel:

- **Impacto:** o tamanho do estrago se a falha for explorada (Baixo, Medio, Alto,
  Critico).
- **Probabilidade:** quao facil e explorar a falha (Baixa, Media, Alta). Falha
  conhecida, sem autenticacao e exposta na internet = probabilidade alta.
- **Severidade:** a combinacao dos dois. Impacto alto + facil de explorar = critico.

## Nomes que ajudam a classificar

- **OWASP Top 10:** a lista das falhas mais comuns em aplicacoes web (Injection,
  Broken Access Control, etc.). Boa referencia para dar nome a uma falha web.
- **CWE:** catalogo de tipos de fraqueza, com numero. Ex.: CWE-89 = SQL Injection.
- **MITRE ATT&CK:** catalogo de taticas e tecnicas de ataque reais. Serve para
  explicar **como** uma falha seria abusada. Ex.: T1190 — Exploit Public-Facing
  Application (explorar uma aplicacao exposta na internet).

Esses nomes nao sao decoreba: servem para que duas pessoas falem da mesma falha
com o mesmo vocabulario.

## Boas praticas de defesa (visao geral)

- **Validar e tratar toda entrada do usuario.** Nunca confie no que vem de fora.
  Para banco de dados, use **consultas parametrizadas** no lugar de concatenacao.
- **Menor privilegio.** Cada usuario, processo ou servico so tem o acesso que
  precisa, nada alem.
- **Defesa em camadas.** Varios controles em serie (validacao + autenticacao + WAF
  + monitoramento). Se um falha, outro segura.
- **Autenticacao forte e MFA.** Dificulta o uso de credenciais roubadas.
- **Manter tudo atualizado.** Muitas invasoes exploram falhas ja corrigidas.
- **Backup testado.** A defesa final contra perda e sequestro de dados.
- **Secrets fora do codigo.** Senhas, chaves e tokens em variaveis de ambiente,
  nunca commitados no repositorio.

## Postura do agente ao falar de seguranca

- **Contexto antes de comando.** Sem entender o ambiente, qualquer sugestao pode
  ser errada ou perigosa.
- **Defender, nao atacar.** Explicar uma falha para corrigi-la, nunca fornecer um
  ataque pronto.
- **So o ambiente do estudante.** Testes apenas em codigo e servidores proprios,
  de laboratorio, com autorizacao.
