from flask import Flask, render_template, abort, g
from jinja2 import Environment
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, FormField, SubmitField
import os

app = Flask("ModularOne", template_folder='templates')
app.secret_key = 'modularone'

login_accepted: bool = True #bypass na razie

jinja_food: dict[str,str] = { 
    "app": "Scaffold",
    "ver": "0.0.1",
    "about": "Opis aplikiacji w skrócie.<br> Tu warto wspomnieć o czymś co jest ważne lub nie.<br> Albo nie wspominać. <strong>Można użyć</strong> <a href='#'>formatowań</a> html"
}

######################## ROUTING ##################################
#sprawdzić czy ten dekorator spełni warunki
@app.before_request
def is_logged():
    """Sprawdzenie czy jest aktywna sesja dla użytkownika
    
    Keyword arguments:
    argument -- na ten moment brak
    Return: Zwraca formularz logowania o ile niezalogowany
    """
    
    if login_accepted == False:
        return render_template('pages/login.html.j2', data=jinja_food)

@app.route('/')
def index():
    return render_template('pages/index.html.j2', data=jinja_food)

@app.route('/test')
def test():
    return render_template('pages/test.html.j2', data=jinja_food)

@app.route('/static/img')
def static_img():
    return 

@app.route('/admin')
def admin():
    return render_template('admin/templates/index.html.j2', data=jinja_food)


@app.route('/steps/<int:step>')
def steps(step):
    """Routing dla parametrów przekazywanych przez url. 

    
    Keyword arguments:
    argument -- step nr kroku 
    Return: formularz i wartość przekazaną w url
    """
    
    return render_template('pages/step.html.j2', step=step, data=jinja_food)

@app.errorhandler(404)
def page_not_found(e):
    """przechywcenie błędu 404 i przekierowanie do customowej strony
    dodaatkowo ma rzucić błędem który zostanie zapisany w loggerze

    Keyword arguments:
    argument -- error
    Return: -- przekierowanie do template 404
    """
    
    # error_throw(kto, kiedy, wywołany url + info że 404) taka funkcja rzucająca do loogera (via databus?)
    return render_template('errors/404.html.j2')

@app.errorhandler(500)
def server_error(e):
    """przechywcenie błędu 500 i przekierowanie do customowej strony 
    dodatkowo ma rzucić błędem który zostanie zapisany w loggerze
     
    Keyword arguments:
    argument -- error
    Return: -- przekierowanie do template 404
    """
    # error_throw(kto, kiedy, opis: wywołany url + info że 500) taka funkcja rzucająca do loogera (via databus?)
    return render_template('errors/500.html.j2')


##################### FRONTEND ##################################################
# login form under constr.....
class LoginForm(FlaskForm):
    uname = StringField('uname')
    passwd = PasswordField('password')

######################## SERWER START ###########################################
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
  
    