import os
from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask.ext.mail import Message, Mail


mail = Mail()
app = Flask(__name__)

app.secret_key = os.environ['SECRET_KEY']

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = os.environ['MAIL_USERNAME']
app.config["MAIL_PASSWORD"] = os.environ['MAIL_PASSWORD']

mail.init_app(app)


#Create our index or root / route
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            msg = Message("Mail sent from Memorious website",
                          sender=form.email.data,
                          recipients=[os.environ['CONTACT_EMAIL']])

            msg.body = """
                From: %s <%s>

                %s
                """ % (form.name.data, form.email.data, form.message.data)

            mail.send(msg)

            return render_template('contact.html', success=True)
        else:
            return render_template('contact.html', form=form)

    elif request.method == 'GET':
        return render_template('contact.html', form=form)


if __name__ == "__main__":
    app.run(debug="True")
