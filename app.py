from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sobre.html')
def sobre():
    return render_template('sobre.html')

@app.route('/contacto.html')
def contacto():
    return render_template('contacto.html')


if __name__ == '__main__':
    app.run(debug=True)
