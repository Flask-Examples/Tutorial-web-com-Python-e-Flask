from flask_admin import Admin
from flask_admin.contrib.pymongo import ModelView
from wtforms import fields, form


class MessageForm(form.Form):
    name = fields.StringField()
    message = fields.TextAreaField()


class MessageView(ModelView):
    form = MessageForm
    # como é uma tupla tem que ter a virgula
    # column_list = ('name',)
    # Tupla
    column_list = ['name']


def configure(app):
    app.admin = Admin(app, name='Live de Python Admin')
    app.admin.add_view(MessageView(app.db.messages, 'Messages'))
