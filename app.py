from flask import Flask

from src.routes.captcha import captcha
from src.routes.home import home

app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(captcha)

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')