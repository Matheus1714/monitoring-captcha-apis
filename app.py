from flask import Flask
from src.routes.home import home
from src.routes.captcha import captcha

app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

app.register_blueprint(home)
app.register_blueprint(captcha)


if __name__ == '__main__':
    app.run(debug=True)