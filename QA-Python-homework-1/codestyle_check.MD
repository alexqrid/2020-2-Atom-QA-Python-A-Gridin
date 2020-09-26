### pylint --confidence INFERENCE_FAILURE
```sh
~/PycharmProjects/atom/2020-2-Atom-QA-Python-A-Gridin $ pylint --confidence INFERENCE_FAILURE QA-Python-homework-1/

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

```
### flake8 
Старался подвести структуру проекта под шаблонную, но в `conftest.py` не было необходимости в чём-то ещё
```
QA-Python-homework-1/conftest.py:1:1: F403 'from fixtures.fixtures import *' used; unable to detect undefined names
QA-Python-homework-1/conftest.py:1:1: F401 'fixtures.fixtures.*' imported but unused
```
```shell script
~/PycharmProjects/atom/2020-2-Atom-QA-Python-A-Gridin $ flake8 --ignore=F403,F401 QA-Python-homework-1/

~/PycharmProjects/atom/2020-2-Atom-QA-Python-A-Gridin $
```

### pycodestyle
```sh
~/PycharmProjects/atom/2020-2-Atom-QA-Python-A-Gridin $ pycodestyle QA-Python-homework-1/
~/PycharmProjects/atom/2020-2-Atom-QA-Python-A-Gridin $ 
```
