# machination [![BuildStatus](https://travis-ci.org/emersonn/machination.svg?branch=master)](https://travis-ci.org/emersonn/machination)
A finite state machine modeler that allows you to generate output for procedures
such as text generation.

## Installation
Install using the provided setup.py.

```sh
$ cd path/to/main/folder
$ pip install .
```

## Basic Usage
1. Create a list of States that you will use in your Machination. All your
States should be uniquely named. Return None if your State has no State
to go to, or if there is a condition that cannot be satisfied.

  ```python
  from machination.stringbuild import StringState
  st_one = StringState("one_name", one_function, "one text")
 ```
2. Create a Machination from the List of States, along with the starting State.

## Testing
Testing requires mock, nose and (optional) coverage libraries. nosetests
should work just fine.
