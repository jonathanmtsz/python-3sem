from config import db
class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(self, nome):
        self.nome = nome

    def to_dict(self):
        return {'id':self.id,'nome':self.nome}

class AlunoNaoEncontrado(Exception):
    pass

def aluno_por_id(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado
    return aluno.to_dict()

def lista_alunos():
    aluno = Aluno.query.all()
    return [aluno.to_dict() for aluno in alunos]

def aluno_existe(id_aluno):
    try:
        aluno_por_id(id_aluno)
        return True
    except AlunoNaoEncontrado:
        return False

def adiciona_aluno(dict):
    dados['alunos'].append(dict)

def apaga_tudo():
    dados['alunos'] = []

def apaga_aluno(id_aluno):
    dici_aluno = aluno_por_id(id_aluno)
    dados['alunos'].remove(dici_aluno)

def edita_aluno(id_aluno,novo_nome):
    dici_aluno = aluno_por_id(id_aluno)
    dici_aluno['nome'] = novo_nome