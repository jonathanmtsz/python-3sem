from flask import Blueprint, jsonify
from .alunos_model import aluno_por_id, aluno_existe, AlunoNaoEncontrado, edita_aluno, lista_alunos, apaga_aluno, adiciona_aluno

alunos_blueprint = Blueprint('alunos', __name__)

@alunos_blueprint.route('/alunos',methods=['GET'])
def get_alunos():
    return jsonify(lista_alunos())