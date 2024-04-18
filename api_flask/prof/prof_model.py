dados = {
        "professores":
        [ {"nome": "prof", "id" : 0} ]
        }

class ProfNaoEncontrado(Exception):
    pass

def prof_por_id(id_prof):
    lista_profs = dados['professores']
    for dicionario in lista_profs:
        if dicionario['id'] == id_prof:
            return dicionario
    raise ProfNaoEncontrado

def prof_existe(id_prof):
    try:
        prof_por_id(id_prof)
        return True
    except ProfNaoEncontrado:
        return False

def adiciona_prof(dict):
    dados['professores'].append(dict)

def lista_profs():
    return dados["professores"]

def apaga_tudo():
    dados['professores'] = []

def apaga_prof(id_prof):
    dici_prof = prof_por_id(id_prof)
    dados['professores'].remove(dici_prof)

def edita_prof(id_prof,novo_nome):
    dici_prof = prof_por_id(id_prof)
    dici_prof['nome'] = novo_nome