from flask import Flask

app = Flask(__name__)

with app.app_context():
    from . import db
    db.init_app(app)

    

@app.route('/hello')
def hello():
    return 'Hello, World!'

from . import categoria
app.register_blueprint(categoria.bp)

from . import lenguaje
app.register_blueprint(lenguaje.bp)






     
     