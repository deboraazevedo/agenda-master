from flask_wtf import Form
from wtforms import TextField, TextAreaField, StringField

class AgendaForm(Form):
	nome = StringField('Nome')
	telefone = StringField('Numero telefone')
        email = TextAreaField('Endereco de email')


#name = StringField(u'Nome', [validators.required(), validators.length(max=100)])
#telefone = StringField(u'Numero telefone', [validators.optional(), validators.length(max=14)])
#email = TextAreaField(u'Endereco de email', [validators.optional(), validators.length(max=200)])
	

