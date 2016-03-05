BUILDDIR ?= _build
PORT ?= 9999
HOST ?= 127.0.0.1
PYGAME_URL = http://pygame.org/ftp/
PYGAME_RELEASE ?= pygame-1.9.1release


.PHONY: help clean develop install install-pygame server

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  clean                    to remove all build, test, coverage and Python artifacts"
	@echo "  develop                  to install all dependencies, required for development."
	@echo "  install                  to install all dependencies, required to run."
	@echo "  install-pygame           to download and install pygame"
	@echo "  server                   to start the gameserver individualy for multiplayer."

clean:
	python setup.py clean -a
	rm -fr dist/
	rm -fr *.egg-info
	find . -name '.DS_Store' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '*.orig' -exec rm -f {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

server:
	python burningkingdoms/server/main.py --port=$(PORT)

install-pygame:
	@echo "Installing pygame..."
	cd /tmp/; wget $(PYGAME_URL)$(PYGAME_RELEASE).tar.gz; tar xzf $(PYGAME_RELEASE).tar.gz;
	cd /tmp/$(PYGAME_RELEASE)/; ./configure; python setup.py install
	@echo "Cleaning up pygame tempfiles..."
	cd /tmp/; rm $(PYGAME_RELEASE).tar.gz; rm -rf $(PYGAME_RELEASE)
	@echo "Successfully installed pygame."

develop: install-pygame
	python setup.py develop

install: install-pygame
	python setup.py install