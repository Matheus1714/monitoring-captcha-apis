from dotenv import dotenv_values

config = dotenv_values(".env.prod")

API_KEY_ANTI_CAPTCHA = config.get('API_KEY_ANTI_CAPTCHA', '')
API_KEY_CAP_SOLVER = config.get('API_KEY_CAP_SOLVER', '')
API_KEY_TWO_CAPCHA = config.get('API_KEY_TWO_CAPCHA', '')

# import os

# API_KEY_ANTI_CAPTCHA = os.environ.get('API_KEY_ANTI_CAPTCHA', '')
# API_KEY_CAP_SOLVER = os.environ.get('API_KEY_CAP_SOLVER', '')
# API_KEY_TWO_CAPCHA = os.environ.get('API_KEY_TWO_CAPCHA', '')