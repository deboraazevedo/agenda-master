from flask import Flask, render_template, request, redirect, url_for

from flask.ext.pymongo import PyMongo
from bson.objectid import ObjectId

from forms import AgendaForm

app = Flask(__name__)
app.config.from_object('configs')
mongo = PyMongo(app)

@app.route("/")
def index():
    agendas = mongo.db.agendas.find().sort([('nome', 1)])
    return render_template("index.html", agendas=agendas)


@app.route("/agendas/add/", methods=['GET', 'POST'])
def add():
    form = AgendaForm()
    if request.method == 'POST':
        mongo.db.agendas.insert(form.data)
        return redirect(url_for("index"))

    return render_template("add.html", form=form)


@app.route("/agendas/<agenda_id>/edit/", methods=['GET', 'POST'])
def edit(agenda_id):
    agenda = mongo.db.agendas.find_one({'_id': ObjectId(agenda_id)})
    form = AgendaForm(**agenda)
    if request.method == 'POST':
        agenda.update(form.data)
	mongo.db.agendas.save(agenda)
	return redirect(url_for("index"))

    return render_template("edit.html", form=form, agenda=agenda, agenda_id=agenda_id)


@app.route("/agendas/<agenda_id>/delete/", methods=['GET'])
def delete(agenda_id):
    mongo.db.agendas.remove({'_id': ObjectId(agenda_id)})
    return redirect(url_for('index'))




if __name__ == "__main__":
    app.run(debug=True)
