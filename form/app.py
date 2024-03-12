from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
@app.route('/index')

def index():

    con = sql.connect("form_db.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur = con.execute("select * from discos")
    data = cur.fetchall()

    return render_template("index.html", datas=data)

@app.route("/add_disco", methods=["POST", "GET"])
def add_disco():

    if request.method == "POST":
        artista = request.form["artista"]
        titulo = request.form["titulo"]
        ano = request.form["ano"]
        gravadora = request.form["gravadora"]
        con = sql.connect("form_db.db")
        cur = con.cursor()
        cur.execute("insert into discos(ARTISTA,TITULO,ANO,GRAVADORA) values (?,?,?,?)", (artista, titulo, ano, gravadora))
        con.commit()
        flash("Dados cadastrados", "success")

        return redirect(url_for("index"))
    return render_template("add_disco.html")

@app.route("/edit_disco/<string:id>", methods=["POST","GET"])
def edit_disco(id):
    if request.method == "POST":
        artista = request.form["artista"]
        titulo = request.form["titulo"]
        ano = request.form["ano"]
        gravadora = request.form["gravadora"]
        con = sql.connect("form_db.db")
        cur = con.cursor()
        cur.execute("update disco set ARTISTA=?, TITULO=?, ANO=?, GRAVADORA=? where ID=?", (artista, titulo, ano, gravadora))
        con.commit()
        flash("Dados atualizados", "success")

        return redirect(url_for("index"))
    con=sql.connect("form_db.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from discos where ID=?", (id, ))
    data = cur.fetchone()
    return render_template("edit_disco.html", datas = data)

@app.route("/delete_disco/<string:id>", methods=["GET"])
def delete_disco(id):
    con = sql.connect("form_db.db")
    cur = con.cursor()
    cur.execute("delete from discos where ID=?", (id,))
    con.commit()
    flash("Dados deletados", "warning")

    return redirect(url_for("index"))


if __name__=='__main__':
    app.secret_key="1234"
    app.run(debug=True)
