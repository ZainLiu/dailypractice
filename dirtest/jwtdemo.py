import jwt
import datetime
from jwt import exceptions

SALT = 'apple'
def create_token():
    # 构造header
    headers = {
        'typ': 'jwt',
        'alg': 'HS256',
    }
    # 构造payload
    payload = {
        'user_id': 1,
        'username': 'pig',
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=5)
    }
    result = jwt.encode(payload=payload,key=SALT,algorithm='HS256',headers=headers)
    return result

def parse_payload(token):
    result = {'status':False,'data':None,'error':None}
    try:
        ver_str = jwt.decode(token,SALT,True)
        result["status"] = True
        result['data'] = ver_str
    except exceptions.ExpiredSignatureError:
        result['error'] = 'token已经失效'
    except exceptions.DecodeError:
        result['error'] = 'token认证失败'
    except exceptions.InvalidTokenError:
        result['error'] = '非法的token'
    return result

if __name__ == '__main__':
    token = create_token()
    print(token)
    a = parse_payload(token)
    print(a)
    print(dir())