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

  ```python
  from machination.stringbuild import StringMachination
  mach = StringMachination(states, st_one)
  ```
3. Run the Machination on given data. Here we are running it on a single piece
of data where the 'one_name' state gets the argument of 'cats.' An optional
argument was passed where if we were to visit another state, we would
concatenate the strings with a space instead of nothing at all.
  ```python
  mach.run({
    'one_name': 'cats'
  }, " ")
  ```

## Testing
Testing requires mock, nose and (optional) coverage libraries. nosetests
should work just fine.
