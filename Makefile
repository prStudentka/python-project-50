install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

gendiff-install:
	python3 -m pip install . gendiff

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

gendiff:
	poetry run python -m gendiff.scripts.gendiff --help