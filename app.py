from flask import Flask
from src.routes.home import home

app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

app.register_blueprint(home)

if __name__ == '__main__':
    app.run(debug=True)