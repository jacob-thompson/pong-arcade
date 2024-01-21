.PHONY: clean build install run test pushtest push
DEFAULT: run

clean:
	rm -rf dist .tox
build: clean
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