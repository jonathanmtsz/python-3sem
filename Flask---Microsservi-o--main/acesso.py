import requests

def leciona(id_professor, id_disciplina):
    r = requests.get(f"http://localhost:5000/leciona/{id_professor}/{id_disciplina}")
    dic = r.json()
    if r.status_code == 404:
        return (False,'disciplina inexistente')
    return dic['leciona']


