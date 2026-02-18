.PHONY: serve-backend
serve-backend:
	uvicorn main:app --reload

.PHONY: browse
browse:
	xdg-open http://localhost:8000

.PHONY: serve
serve: serve-backend
#	make -j 2 serve-backend browse


.PHONY: install
install:
	pip install fastapi
	pip install "uvicorn[standard]"
	pip install mysql-connector-python
	pip install pydantic_settings
	pip install sqlalchemy
	pip install pymysql
	pip install PyJWT
	pip install pydantic
	pip install python-decouple
	pip install "python-jose[cryptography]"
	pip install "passlib[bcrypt]"


