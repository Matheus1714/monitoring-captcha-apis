from dotenv import dotenv_values

config = dotenv_values(".dev.env")

API_KEY_ANTI_CAPTCHA = config.get('API_KEY_ANTI_CAPTCHA', '')
API_KEY_CAP_SOLVER = config.get('API_KEY_CAP_SOLVER', '')
API_KEY_TWO_CAPCHA = config.get('API_KEY_TWO_CAPCHA', '')
