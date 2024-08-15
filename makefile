.PHONY: clean build install run test
DEFAULT: run

clean:
	rm -rf dist .tox
build: clean
	python -m build
install: build
	pipx install dist/*.tar.gz --force
run: install
	pong
test: build
	twine check dist/*
	tox