default: run

MAIN=pong.py

install:
	pip install pygame

build:
	pyinstaller $(MAIN) --add-data data:data --name Pong

clean:
	rm pong.spec
	rm -rf dist
	rm -rf build

run:
	python3 $(MAIN)