from flask import Blueprint, jsonify, request
from .prof_model import prof_existe,prof_por_id,ProfNaoEncontrado,apaga_prof,edita_prof,lista_profs,adiciona_prof

prof_blueprint = Blueprint('prof',__name__)

@prof_blueprint.route('/prof',methods=['GET'])
def get_prof():
    return jsonify(lista_profs())

@prof_blueprint.route('/prof',methods=['POST'])
def add_prof():
    data = request.json
    if 'nome' not in data:
        return jsonify({'erro': 'professor sem nome'}), 400
    id_enviado = data['id']
    if prof_existe(id_enviado):
        return jsonify({'erro': 'id já utilizado'}), 400
    else:
        adiciona_prof(data)
        return lista_profs()

@prof_blueprint.route('/prof/<int:nProf>',methods=['PUT'])
def edit_prof(nProf):
    data = request.json
    if 'nome' not in data:
        return jsonify({'erro': 'prof sem nome'}), 400
    novo_nome = data['nome']
    try:
        edita_prof(nProf, novo_nome)
        return prof_por_id(nProf)
    except ProfNaoEncontrado:
        return jsonify({"erro": 'prof não encontrado'}), 400
    
@prof_blueprint.route('/prof/<int:nProf>',methods=['DELETE'])
def delete_prof(nProf):
    apaga_prof(nProf)
    return "professor apagado"