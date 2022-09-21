.PHONY: install build winbuild clean run
default: run

MAIN = pong.py
REQ = requirements.txt

NAME = Pong

install:
	pip install -r $(REQ)
build:
	pyinstaller $(MAIN) --add-data data:data --name $(NAME)
winbuild:
	wine C:/Python310/Scripts/pyinstaller.exe $(MAIN) --add-data "data;data" --name $(NAME)
clean:
	rm Pong.spec
	rm -rf dist
	rm -rf build
run:
	python3 $(MAIN)