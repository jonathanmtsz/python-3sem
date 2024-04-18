from flask import Blueprint, jsonify, request
from .alunos_model import aluno_por_id, aluno_existe, AlunoNaoEncontrado, edita_aluno, lista_alunos, apaga_aluno, adiciona_aluno

alunos_blueprint = Blueprint('alunos', __name__)

@alunos_blueprint.route('/alunos',methods=['GET'])
def get_alunos():
    return jsonify(lista_alunos())


@alunos_blueprint.route('/alunos',methods=['POST'])
def add_alunos():
    data = request.json
    if 'nome' not in data:
        return jsonify({'erro': 'aluno sem nome'}), 400
    id_enviado = data['id']
    if aluno_existe(id_enviado):
        return jsonify({'erro': 'id já utilizada'}), 400
    else:
        adiciona_aluno(data)
        return lista_alunos()
    return jsonify(lista_alunos())

@alunos_blueprint.route('/alunos/<int:nAluno>',methods=['DELETE'])
def remove_alunos(nAluno):
    apaga_aluno(nAluno)
    return "removido"

@alunos_blueprint.route('/alunos/<int:nAluno>',methods=['PUT'])
def edit_alunos(nAluno):
    data = request.json
    if 'nome' not in data:
        return jsonify({'erro': 'aluno sem nome'}), 400
    else:
        edita_aluno(nAluno,data['nome'])
        return jsonify({'ok':f'nome alterado para {data['nome']}'})
    
@alunos_blueprint.route('/alunos/<int:nAluno>',methods=['DELETE'])
def delete_alunos(nAluno):
    apaga_aluno(nAluno)
    return "aluno excluido"

