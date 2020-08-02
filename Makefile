# Put any command that doesn't create a file here (almost all of the commands)
.PHONY: \
	help \
	manage \
	migrate \
	migrations \
	server \
	shell \
	test \

usage:
	@echo "Available commands:"
	@echo "help             Display available commands"
	@echo "manage           Run a Django management command"
	@echo "migrate          Run Django migrations"
	@echo "migrations       Create Django migrations"
	@echo "server	        Start development server"
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

shell:
	$(MAKE) manage ARGS="shell_plus ${ARGS}"

test:
	$(MAKE) manage ARGS="test octopus${ARGS}"
