import os
import json
from django.core.exceptions import ImproperlyConfigured

def secret_key(BASE_DIR):
    secret_file = os.path.join(BASE_DIR, 'secrets.json')

    with open(secret_file) as f:
        secrets = json.loads(f.read())
        
    def get_keys(setting, secrets=secrets):
        try:
            return secrets[setting]
        except KeyError:
            error_msg = "Set the {0} enviroment variable".format(setting)
            raise ImproperlyConfigured(error_msg)
        
    SECRET_KEY = get_keys("SECRET_KEY")
    MAIN_DOMAIN = get_keys("MAIN_DOMAIN")
    NAVER_CLIENT_ID = get_keys("NAVER_CLIENT_ID")
    NAVER_SECRET_KEY = get_keys("NAVER_SECRET_KEY")
    KAKAO_REST_API_KEY = get_keys("KAKAO_REST_API_KEY")
    KAKAO_SECRET_KEY = get_keys("KAKAO_SECRET_KEY")
    STATE = get_keys("STATE")
    
    return SECRET_KEY, MAIN_DOMAIN, NAVER_CLIENT_ID, NAVER_SECRET_KEY, KAKAO_REST_API_KEY, KAKAO_SECRET_KEY, STATE