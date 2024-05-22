atividades = [
    {
        'id_atividade':1,
        'id_disciplina':1,
        'enunciado': 'crie um app de todo em flask',
        'respostas': [
            {'id_aluno': 1, 'resposta':'todo.py', 'nota':9},
            {'id_aluno': 2, 'resposta':'todo.zip.rar'},
            {'id_aluno': 4, 'resposta':'todo.zip', 'nota':10}
            ]
    },

    {
        'id_atividade':2,
        'id_disciplina':1,
        'enunciado': 'crie um servidor que envia email em Flask',
        'respostas': [
            {'id_aluno': 4, 'resposta':'email.zip', 'nota':10}
            ]
    },

    ]

class AtividadeNotFound(Exception):
    pass

def localiza_atividade(id_atividade):
    for d_atividade in atividades:
        if d_atividade['id_atividade'] == id_atividade:
            return d_atividade
    raise AtividadeNotFound

