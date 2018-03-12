from flask import Flask, render_template, request, redirect, url_for
from static.Forms.forms import TickerForm

app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))


@app.route('/', methods=('GET', 'POST'))
def submit():
    form = TickerForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('showform.html', form=form)


@app.route('/index.html')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()