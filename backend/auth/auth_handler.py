import time
from typing import Dict

import jwt
from decouple import config

JWT_SECRET = config("SECRET")
JWT_ALGORITHM = config("ALGORITHM")


def generateJWT(user_id: str, roles : str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "roles": roles,
        "expires": time.time() + 600
    }

    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token

def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}