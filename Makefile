-include .env # В .env надо экранировать спец символы Make #,$
export

PROJECTNAME=$(shell basename "$(PWD)")

#Make пишет работу в консоль Linux. Сделаем его silent.
MAKEFLAGS += --silent

## run-dev: Run developer server
run-dev:
	@poetry run python manage.py runserver

## install: Install dependencies
install:
	@poetry install

## selfcheck: Checks the validity of the pyproject.toml file
selfcheck:
	@poetry check

## lint: Run linter
lint: selfcheck
	@poetry run flake8 task_manager tests

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

.PHONY: help
all: help
help: Makefile
	@echo
	@echo " Choose a command run in "$(PROJECTNAME)":"
	@echo
	@sed -n 's/^##//p' $< | column -t -s ':' |  sed -e 's/^/ /'
	@echo
