from flask import Flask, render_template

app = Flask(__name__)

with app.app_context():
    from . import db
    db.init_app(app)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/inventory2')
def inventory_id():
    consulta = """SELECT name FROM genres ORDER BY name;
    """
    con = db.get_db()
    res = con.execute(consulta)
    lista_lenguajes = res.fetchall()
    pagina = render_template('inventory.html', lenguajes=lista_lenguajes)
    return pagina


@app.route('/inventory')
def inventory():
    consulta = """SELECT last_update FROM inventory ORDER BY name;
    """
    con = db.get_db()
    res = con.execute(consulta)
    lista_inventory = res.fetchall()
    pagina = render_template('inventory.html')
    return pagina



     
     