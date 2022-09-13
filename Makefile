default: run
.PHONY: install

I=install

ENV=pipenv
RUN=run python
MAIN=src/main.py

install:
	pip $(I) $(ENV)
	$(ENV) $(I)

run:
	$(ENV) $(RUN) $(MAIN)