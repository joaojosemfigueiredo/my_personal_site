from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Configurações do Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'figueiredojoaojose.sci@gmail.com'
app.config['MAIL_PASSWORD'] = ''  # Substitua pela senha de app gerada
app.config['MAIL_DEFAULT_SENDER'] = 'figueiredojoaojose.sci@gmail.com'

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html', active_page='home')

@app.route('/sobre-mim')
def sobre_mim():
    return render_template('sobre-mim.html', active_page='sobre-mim')

@app.route('/projetos')
def projetos():
    return render_template('projetos.html', active_page='projetos')

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        nome = request.form['name']
        email = request.form['email']
        mensagem = request.form['message']
        
        msg = Message("Mensagem do Site Pessoal",
                      recipients=['figueiredojoaojose.sci@gmail.com'])
        msg.body = f"Nome: {nome}\nE-mail: {email}\nMensagem: {mensagem}"
        mail.send(msg)
        
        return redirect(url_for('home'))
    return render_template('contato.html', active_page='contato')

if __name__ == '__main__':
    app.run(debug=True)
