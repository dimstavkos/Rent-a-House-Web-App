from fastapi.middleware.cors import CORSMiddleware

cors_origins = [
    "*"
]

cors_methods = ["*"]
cors_headers = ["*"]
cors_allow_credentials = True