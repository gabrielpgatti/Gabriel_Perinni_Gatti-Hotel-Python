Nearly empty Python3 project with a failing test!
===

**Ensure that you have Python 3 installed and that your PIP installation points to it**

Create a virtualenv

```
$ virtualenv -p python3 venv
# source venv/bin/activate
```

To install the required modules:

```
$ pip install -r requirements.txt
```
or
```
$ pip3 install -r requirements.txt
```


To run the (failing) test:

```
$  pytest -v
```
