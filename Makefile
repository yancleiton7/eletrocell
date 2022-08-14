env:
	source venv/bin/activate

env-drop:
	deactivate

run:
	uvicorn app:app --reload
	
model:
	sqlacodegen sqlite:///eletrocell.db

migration:
	alembic revision --autogenerate
