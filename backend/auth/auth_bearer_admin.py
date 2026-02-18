
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from .auth_handler import decodeJWT

class JWTBearerAdmin(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearerAdmin, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        return

        credentials: HTTPAuthorizationCredentials = await super(JWTBearerAdmin, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        isTokenValid: bool = False

        try:
            payload = decodeJWT(jwtoken)
        except:
            payload = None

        if payload:
            roles = payload["roles"].split(",")
            if "Administrator" in roles:
                isTokenValid = True
            else:
                isTokenValid = False
        return isTokenValid