all: test

env:
	virtualenv -p python2 env

install-test-deps: | env
	. env/bin/activate && \
		pip install -r requirements.txt

test: install-test-deps
	. env/bin/activate && \
		python -m unittest discover tests/

test-noenv:
	python -m unittest discover tests/

clean:
	rm -rf env
	rm -f tests/*.pyc

.PHONY: all clean test test-noenv install-test-deps
