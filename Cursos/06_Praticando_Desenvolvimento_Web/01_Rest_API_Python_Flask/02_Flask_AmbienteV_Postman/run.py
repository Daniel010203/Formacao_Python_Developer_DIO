from flask import Flask
app = Flask(__name__)

@app.route("/<numero>", methods=('POST'))
def ola(numero):
    return 'Ola mundo! {}'.format(numero)

if __name__=="__main__":
    app.run(debug=True)