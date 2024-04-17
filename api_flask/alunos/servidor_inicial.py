from flask import Flask, jsonify, request

import model_aluno_professor as model

app = Flask(__name__) 
		
@app.route("/alunos", methods=["GET"])
def alunos():
    print("lista de todos os alunos")
    return model.lista_alunos()

@app.route("/prof", methods=["GET"])
def prof():
    print("lista de todos os professores")
    return model.lista_profs()


'''atende em /alunos, verbo POST'''
@app.route("/alunos", methods=["POST"])
def cria_aluno():
    dict = request.json
    if 'nome' not in request.json.keys():
        return ({'erro':'aluno sem nome'},400)
    id_enviado = dict['id']
    if model.aluno_existe(id_enviado):
        return ({'erro':'id ja utilizada'},400)
    else:
        model.adiciona_aluno(dict)
        return model.lista_alunos()

@app.route("/prof", methods=["POST"])
def cria_prof():
    dict = request.json
    if 'nome' not in request.json.keys():
        return ({'erro':'professor sem nome'}, 400)
    id_enviado = dict['id']
    if model.aluno_existe(id_enviado):
        return ({'erro':'id ja utilizado'}, 400)
    else:
        model.adiciona_prof(dict)
        return model.lista_profs()

@app.route("/alunos/<int:nAluno>", methods=["GET"]) 
def alunoPorId(nAluno):
    try:
        #return "<h1>ola meu caro</h1><p>tudo bao?</p>"
        return model.aluno_por_id(nAluno)
    except model.AlunoNaoEncontrado:
        return ( {"erro":'aluno nao encontrado'}, 400)

@app.route("/prof/<int:nProf>", methods=["GET"]) 
def profPorId(nProf):
    try:
        #return "<h1>ola meu caro</h1><p>tudo bao?</p>"
        return model.prof_por_id(nProf)
    except model.ProfNaoEncontrado:
        return ( {"erro":'prof nao encontrado'}, 400)


@app.route("/alunos/<int:nAluno>", methods=["PUT"]) 
def editaPorIdAluno(nAluno):
    if 'nome' not in request.json.keys():
        return ({'erro':'aluno sem nome'},400)
    novo_nome = request.json['nome']
    try:
        model.edita_aluno(nAluno,novo_nome)
        return model.aluno_por_id(nAluno)
    except model.AlunoNaoEncontrado:
        return ( {"erro":'aluno nao encontrado'}, 400)

@app.route("/prof/<int:nProf>", methods=["PUT"]) 
def editaPorIdProf(nProf):
    if 'nome' not in request.json.keys():
        return ({'erro':'prof sem nome'},400)
    novo_nome = request.json['nome']
    try:
        model.edita_prof(nProf,novo_nome)
        return model.prof_por_id(nProf)
    except model.ProfNaoEncontrado:
        return ( {"erro":'prof nao encontrado'}, 400)

# 1) /alunos/<int:nAluno>  e0 passa nAluno no def  para pegar o nro na URL    
# 2)  methods=["PUT"] para definir o verbo
# 3)  return ({'erro':'aluno sem nome'},400) diz qual o arquivo retornado (o dicionario)
#     e tb o codigo de status (400)
# 4) Se vc nao disser o cod status, vai "200 OK" por padrao, como em         
# return model.aluno_por_id(nAluno)
# 5) request.json representa o dicionario que o usuario enviou (nao necessariamente
# um dicionario, na real, poderia ser outra coisa)
        


@app.route("/alunos/<int:nAluno>", methods=["DELETE"])
def deletePorIdAluno(nAluno):
    try:
         model.apaga_aluno(nAluno)
    except model.AlunoNaoEncontrado:
        return ( {"erro":'aluno nao encontrado'}, 400)


@app.route("/prof/<int:nProf>", methods=["DELETE"])
def deletePorIdProf(nProf):
    try:
        model.apaga_prof(nProf)
    except model.ProfNaoEncontrado:
        return({"erro":'professor nao encontrado'}, 400)
    


#Na URL /reseta, apagaremos a lista de alunos e professores (essa URL só atende o verbo POST).
@app.route("/reseta", methods=["POST"])
def reseta():
    model.apaga_tudo()
    return "resetado" #poderia ser return dados
    #tive que retornar ALGUMA COISA, pro usuario receber algo
    #o flask nao deixa uma funcao de URL nao ter retorno

if __name__ == '__main__':
        app.run(host = 'localhost', port = 5002, debug = True)