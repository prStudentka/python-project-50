install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

gendiff-install:
	python3 -m pip install . gendiff

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff

gendiff:
	poetry run python -m gendiff.scripts.gendiff --help

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

test:
	poetry run pytest -vv

example:
	poetry run gendiff tests/fixtures/file1.yml tests/fixtures/file2.yaml

tree:
	poetry run gendiff tests/fixtures/tree1.json tests/fixtures/tree2.json
