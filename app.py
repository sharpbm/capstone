from flask import Flask
app = Flask(__name__)


@app.route('/<name>')
def hello_name(name):
    return "<h1 style='text-align: center;'>Hello %s !!</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)