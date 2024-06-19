from . import db 
from flask import Blueprint, render_template

bp = Blueprint('actor', __name__,url_prefix="/actores/")

@bp.route("/")
def actor():
    consulta = """
        SELECT first_name, last_name, actor_id FROM actor
        ORDER BY last_name;
        """
    con = db.get_db()
    res = con.execute(consulta)
    lista_actor = res.fetchall()
    pagina = render_template("actores.html", actores = lista_actor)

    return pagina 


@bp.route('/<int:id>')
def detalles(id):
    consulta1 = """
        SELECT first_name, last_name, actor_id FROM actor
        ORDER BY last_name;
        """

    consulta2 = """
        SELECT name, category_id AS CategoriaId FROM category
        WHERE category_id = ?
        ORDER BY name;
        """
    
    con = db.get_db()
    res = con.execute(consulta1,(id,))
    lista_pelis = res.fetchall()

     
    resul = con.execute(consulta2,(id,))
    lista_pelis = res.fetchone()

    pagina = render_template("actores.html", pelis = lista_pelis, act = lista_actores)

    return pagina 
