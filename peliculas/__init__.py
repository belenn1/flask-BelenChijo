from flask import Flask

app = Flask(__name__)

with app.app_context():
    from . import db
    db.init_app(app)

    

@app.route('/hello')
def hello():
    return 'Hello, World!'

from . import categoria,actores,lenguaje
app.register_blueprint(categoria.bp)
app.register_blueprint(actores.bp)
app.register_blueprint(lenguaje.bp)








     
     