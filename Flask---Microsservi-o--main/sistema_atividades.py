from flask import Flask,abort
from flask import make_response, request, url_for
import acesso
import model_atividades

app = Flask(__name__)

app.url_map.strict_slashes = False
#para poder aceitar a url professores/1 e professores/1/ do mesmo jeito

@app.route('/')
def index():
    return "Sistema de entrega de atividades"

@app.route('/atividades/all/', methods=['GET'])
def get_all():
    return model_atividades.atividades

@app.route("/atividade/<int:id_atividade>/")
def rota_atividade(id_atividade):
    try:
        d = model_atividades.localiza_atividade(id_atividade)
        print(d)
        copy = d.copy()
        copy['url'] = f"/atividade/{id_atividade}/"
        return {'isok': True, 'atividade': copy}
    except model_atividades.AtividadeNotFound:
        return {'isok': False, 
                'erro': 'atividade nao encontrada'} , 404           

@app.route("/atividade/<int:id_a>/professor/<int:id_p>")
def rota_atividade2(id_a,id_p):
    try:
        d = model_atividades.localiza_atividade(id_a)
        copy = d.copy()
        if not acesso.leciona(id_professor=id_p,id_disciplina=d['id_disciplina']):
            del copy['respostas']
        copy['url'] = f"/atividade/{id_a}/"
        return {'isok': True, 'atividade': copy}
    except model_atividades.AtividadeNotFound:
        return {'isok': False, 
                'erro': 'atividade nao encontrada'} , 404      

if __name__ == '__main__':
   app.run(debug=True, host='localhost', port=5050)