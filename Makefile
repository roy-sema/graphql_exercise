# Put any command that doesn't create a file here (almost all of the commands)
.PHONY: \
	help \
	manage \
	migrate \
	migrations \
	server \
	setup_local \
	shell \
	test \

usage:
	@echo "Available commands:"
	@echo "help             Display available commands"
	@echo "manage           Run a Django management command"
	@echo "migrate          Run Django migrations"
	@echo "migrations       Create Django migrations"
	@echo "server	        Start development server"
	@echo "setup_local	    Set up virtual env, install requirements, run migrations and ingest data"
	@echo "shell            Run Django command line"
	@echo "test             Run Django tests"
	@echo "usage            Display available commands"

help:
	$(MAKE) usage

manage:
	@python3 ${PYTHON_ARGS} octopus/manage.py ${ARGS}

migrate:
	$(MAKE) manage ARGS="migrate ${ARGS}"

migrations:
	$(MAKE) manage ARGS="makemigrations ${ARGS}"

server:
	$(MAKE) manage ARGS="runserver ${ARGS}"

setup_local:
	@echo "Installing requirements ..."
	@pip install -r requirements.txt
	@echo "Running migrations ..."
	$(MAKE) migrate
	@echo "Importing 2019 season data ..."
	$(MAKE) manage ARGS="import_premier_league_season_matches 2019"
	$(MAKE) manage ARGS="import_nba_season_matches 2019"
	@echo "Setup complete. Use 'make server' command to start the development server at http://localhost:8000/"

shell:
	$(MAKE) manage ARGS="shell_plus ${ARGS}"

test:
	$(MAKE) manage ARGS="test octopus${ARGS}"
