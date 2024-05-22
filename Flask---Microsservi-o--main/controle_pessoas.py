from flask import Flask,abort
from flask import make_response, request, url_for
import model_pessoa

app = Flask(__name__)
app.url_map.strict_slashes = False #  /alunos /alunos/

@app.route('/')
def index():
    return "Sistema de controle de pessoas"

@app.route('/pessoas/ver_tudo/', methods=['GET'])
def get_all():
    return model_pessoa

@app.route("/leciona/<int:id_professor>/<int:id_disciplina>", methods=["GET"])
def rota_leciona(id_professor,id_disciplina):
    try:
        if model_pessoa.leciona(id_professor,id_disciplina):
            return {'isok':True, 'leciona':True}
        else:
            return {'isok':True, 'leciona':False}
    except model_pessoa.DisciplinaNaoEncontrada:
        return {'isok':False, 'erro':'disciplina nao encontrada'},404
    

if __name__ == '__main__':
   app.run(debug=True, host='localhost', port=5000)