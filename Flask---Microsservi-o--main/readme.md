# Introdução

Este projeto consiste em dois servidores Flask: `controle_pessoas` e `sistema_atividades`.

## O que cada serviço faz?

### controle_pessoas

Este é um serviço Flask que gerencia informações sobre pessoas, incluindo professores e alunos. Ele oferece a funcionalidade de verificar se um professor leciona uma disciplina específica.

- **Rota Importante:** `/leciona/<int:id_professor>/<int:id_disciplina>`
  - Esta rota verifica se um professor específico leciona uma determinada disciplina com base nos IDs fornecidos.

### sistema_atividades

Este é outro serviço Flask que gerencia atividades, incluindo a distribuição e correção de tarefas. Ele depende do serviço `controle_pessoas` para verificar se um professor tem permissão para corrigir uma atividade específica.

- **Rota Importante:** `/atividade/<int:id_a>/professor/<int:id_p>`
  - Esta rota verifica se um professor específico tem permissão para corrigir uma atividade com base nos IDs fornecidos.

# Como os serviços se relacionam?

## sistema_atividades.py e acesso.py:

- `sistema_atividades.py` usa `acesso.py` para verificar se um professor leciona uma disciplina antes de permitir o acesso a certas informações sobre atividades.

- Por exemplo, na rota `/atividade/<int:id_a>/professor/<int:id_p>`, `sistema_atividades.py` chama `acesso.leciona(id_professor=id_p, id_disciplina=d['id_disciplina'])` para verificar se o professor com `id_p` leciona a disciplina associada à atividade com `id_a`.

## acesso.py e controle_pessoa.py:

- `acesso.py` faz requisições HTTP para o servidor gerenciado por `controle_pessoa.py` para verificar se um professor leciona uma disciplina.

- A função `leciona` em `acesso.py` envia uma requisição para um endpoint como `/leciona/<int:id_professor>/<int:id_disciplina>` definido em `controle_pessoa.py`.

## sistema_atividades.py e controle_pessoa.py:

- Indiretamente conectados via `acesso.py`.

- `sistema_atividades.py` depende de `controle_pessoa.py` para obter informações de lecionamento através de `acesso.py`.

# Exemplo de Fluxo de Dados

### Usuário Acessa Atividade:

- O usuário acessa `/atividade/1/professor/2` em `sistema_atividades.py`.
- `sistema_atividades.py` chama `acesso.leciona(id_professor=2, id_disciplina=d['id_disciplina'])`.
- `acesso.py` envia uma requisição GET para `controle_pessoa.py` em `/leciona/2/101 `(onde 101 é o id_disciplina da atividade).
- `controle_pessoa.py` processa a requisição e retorna uma resposta indicando se o professor leciona a disciplina.
- `acesso.py` retorna o resultado para `sistema_atividades.py.`
- Com base no resultado, `sistema_atividades.py` decide se inclui ou exclui informações sobre as respostas na atividade antes de retornar os dados ao usuário.

# Resumo

- **sistema_atividades.py:** Gerencia atividades e verifica permissões.

- **acesso.py:** Faz requisições para verificar se professores lecionam disciplinas.

- **controle_pessoa.py:** Gerencia informações sobre pessoas e expõe endpoints usados por `acesso.py`.
