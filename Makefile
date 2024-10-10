run:
	@echo "Starting dev server..."
	python src/manage.py runserver

migrate:
	@echo "Migrating database..."
	python src/manage.py migrate