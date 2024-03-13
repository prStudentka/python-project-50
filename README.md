### Hexlet tests and linter status:
[![Actions Status](https://github.com/prStudentka/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/prStudentka/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/a9ba16b365ab9dae50b6/maintainability)](https://codeclimate.com/github/prStudentka/python-project-50/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/a9ba16b365ab9dae50b6/test_coverage)](https://codeclimate.com/github/prStudentka/python-project-50/test_coverage)

### You can get the actions badge by navigating to the required workflow on your repo on GitHub.com, clicking on the settings button on the right (the one with 3 dots beside the workflow search) and clicking on the Create status badge button.
[![Hello-world](https://github.com/prStudentka/python-project-50/actions/workflows/hello-world.yml/badge.svg)](https://github.com/prStudentka/python-project-50/actions/workflows/hello-world.yml)

## Installation: ##
###### for debian 12+: ######
pip install + [Repository github](https://github.com/prStudentka/python-project-50)
###### for else: ######
Make sure you are running at least Python 3.10.0 \
To install this package from GitHub on Your PC use command \
git clone [Repository github](https://github.com/prStudentka/python-project-50)
- install: make install
- build: make build
- gendiff: make gendiff-install

## How to use: ##
gendiff -h \
gendiff path/file1 path/file2

###### Use format output stylish, plain or json: ######
gendiff -f plain path/file1 path/file2

#### Сравнение плоских файлов. Рекурсивное сравнение ####
![Example 1](https://github.com/prStudentka/hexlet-git/blob/main/pr50/gendiff_stylish.jpg?raw=true)

#### Плоский формат ####
![Example 2](https://github.com/prStudentka/hexlet-git/blob/main/pr50/gendiff_plain.jpg?raw=true)

