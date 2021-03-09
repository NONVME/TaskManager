-include .env # В .env надо экранировать спец символы Make #,$
export

PROJECTNAME=$(shell basename "$(PWD)")

#Make пишет работу в консоль Linux. Сделаем его silent.
MAKEFLAGS += --silent

## run: Run production server
run:
	gunicorn task_manager.wsgi --log-file -

## run-dev: Run developer server
run-dev:
	@poetry run python manage.py runserver

## install: Install dependencies
install:
	@poetry install

## lint: Run Flake8 linter
lint:
	@poetry check
	@poetry run flake8 task_manager tests

## migrate: makemigrations -> migrate
migrate:
	@poetry run python3 manage.py makemigrations
	@poetry run python3 manage.py migrate

## test: Run tests
test: lint
	@poetry run pytest --cov .

## test-cov: Prepare coverage report for Codeclimate and tests
test-cov:
	@poetry run coverage run --source=page_loader -m pytest
	@poetry run coverage xml

## build: Check, lint and build package
build: install test
	rm -rf ./dist/*
	@poetry build

## package-install: Install package localy
package-install: build
	@pip install --user --upgrade dist/*.whl

heroku_release:
	python manage.py migrate

.PHONY: help
all: help
help: Makefile
	@echo
	@echo " Choose a command run in "$(PROJECTNAME)":"
	@echo
	@sed -n 's/^##//p' $< | column -t -s ':' |  sed -e 's/^/ /'
	@echo
