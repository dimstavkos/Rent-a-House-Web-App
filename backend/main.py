from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from config.Settings import Settings
from middleware.CORS import cors_origins, cors_allow_credentials, cors_methods, cors_headers
from routes import api, auth_api, role_api, admin_api, user_api, location_api, property_api, review_api, propertyType_api, indoorSpace_api, propertyRuleList_api, userMessage_api, photo_api, booking_api, availableDate_api
import sys

settings = Settings()

app = FastAPI(debug=True)
app.include_router(api.router)
app.include_router(role_api.router)
app.include_router(user_api.router)
app.include_router(admin_api.router)
app.include_router(auth_api.router)
app.include_router(location_api.router)
app.include_router(property_api.router)
app.include_router(review_api.router)
app.include_router(propertyType_api.router)
app.include_router(indoorSpace_api.router)
app.include_router(propertyRuleList_api.router)
app.include_router(userMessage_api.router)
app.include_router(photo_api.router)
app.include_router(booking_api.router)
app.include_router(availableDate_api.router)







app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=cors_allow_credentials,
    allow_methods=cors_methods,
    allow_headers=cors_headers,
)

if __name__ == "__main__":
    import uvicorn

    n = len(sys.argv)

    if n >= 2 and sys.argv[1] == "--ssl":
        uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True, ssl_keyfile='snakeoil.key', ssl_certfile='snakeoil.pem')
    else:
        uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)
