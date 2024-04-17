import os
from config import app
from post.index import posts
from alunos.alunos_routes import alunos_blueprint

app.register_blueprint(posts)
app.register_blueprint(alunos_blueprint)

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port = app.config['PORT'], debug=app.config['DEBUG'])