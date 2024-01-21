.PHONY: build install run test pushtest push clean
DEFAULT: run

build:
	python3 -m build
install: build
	pipx install dist/*.tar.gz --force
run: install
	pong
test: build
	twine check dist/*
	tox
pushtest: build
	twine upload --repository testpypi dist/*
push: build
	twine upload dist/*
clean:
	rm -rf dist .tox