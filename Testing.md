# Testing notes for python
## pytest
### Test Outcomes
- PASSED 
- FAILED
- SKIPPED: using either the @pytest.mark.skip() or @pytest.mark.skipif()
- XFAIL: not supposed to pass. using the @pytest.mark.xfail()
- XPASS: The test was marked with xfail, but it ran and passed
- ERROR: An exception happened either during the execution of a fixture
or hook function, and not during the execution of a test function
### pytest.fail
equals assert False
### \_\_tracebackhide\_\_
\_\_tracebackhide\_\_ = True hides the details on `lower` modules
### testing on error message!
```python
def test_raises_with_info():
  match_regex = "missing 1 .* positional argument"
  with pytest.raises(TypeError, match=match_regex):
    cards.CardsDB()

def test_raises_with_info_alt():
  with pytest.raises(TypeError) as exc_info:
    cards.CardsDB()
  expected = "missing 1 required positional argument"
  assert expected in str(exc_info.value)
```
### Scopes
- `scope='function'` : Run once per test function. The setup portion is run before each test using
the fixture. The teardown portion is run after each test using the fixture.
This is the default scope used when no scope parameter is specified.
- `scope='class'` : Run once per test class
- `scope='module'` : Run once per module
- `scope='package'` : Run once per package, or test directory
- `scope='session'` : Run once per session. All test methods and functions using a fixture of
session scope share one setup and teardown call.
#### dynamic scope
```python
# /path/to/conftest.py
@pytest.fixture(scope=db_scope)
def db():
  """CardsDB object connected to a temporary database"""
  with TemporaryDirectory() as db_dir:
    db_path = Path(db_dir)
    db_ = cards.CardsDB(db_path)
    yield db_
    db_.close()
```
```python
# /path/to/conftest.py
def db_scope(fixture_name, config):
  if config.getoption("--func-db", None):
    return "function"
  return "session"
```
```python
# /path/to/conftest.py
def pytest_addoption(parser):
  parser.addoption(
  "--func-db",
  action="store_true",
  default=False,
  help="new db for each test",
  )
```
```bash
pytest --func-db --setup-show test_count.py
```
### autouse
```python
import pytest
import time
@pytest.fixture(autouse=True, scope="session")
def footer_session_scope():
  """Report the time at the end of a session."""
  yield
  now = time.time()
  print("--")
  print(
  "finished : {}".format(
      time.strftime("%d %b %X", time.localtime(now))
    )
  )
  print("-----------------")

@pytest.fixture(autouse=True)
def footer_function_scope():
  """Report test durations after each function."""
  start = time.time()
  yield
  stop = time.time()
  delta = stop - start
  print("\ntest duration : {:0.3} seconds".format(delta))

def test_1():
  """Simulate long-ish running test."""
  time.sleep(1)

def test_2():
  """Simulate slightly longer test."""
  time.sleep(1.23)
```
### parameterize fixtures
```python
import pytest 
from cards import Card

@pytest.fixture(params=["done", "in prog", "todo"])
def start_state(request):
    return request.param

def test_finish(cards_db, start_state):
    c = Card("write a book", state=start_state)
    index = cards_db.add_card(c)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"
```
or
```python
from cards import Card
def pytest_generate_tests(metafunc):
    if "start_state" in metafunc.fixturenames:
        metafunc.parametrize("start_state", ["done", "in prog", "todo"])

def test_finish(cards_db, start_state):
    c = Card("write a book", state=start_state)
    index = cards_db.add_card(c)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"
```
### why pytest.mark.skip ?
Ex. : skip backward compatibilities 
@pytest.mark.skip(reason="Card doesn't support < comparison yet")
#### skipif
```python
import cards, pytest
from packaging.version import parse

@pytest.mark.skipif(
    parse(cards.__version__).major < 2,
    reason="Card < comparison not supported in 1.x",
    )
def test_less_than():
    c1 = Card("a task")
    c2 = Card("b task")
    assert c1 < c2
```
## unittest
### tox
tox is used to test on multiple environments
### type of assert
assertAlmostEqual: check the floating point

## mock
Here are some scenarios where mocking is commonly used in testing:

External Dependencies: When a unit of code interacts with external systems such as databases, web services, or third-party libraries, mocking can be used to simulate these interactions. This ensures that tests run quickly and consistently without relying on external resources.

Complex Collaborators: In object-oriented programming, objects often collaborate with each other to perform tasks. Mocking can be used to isolate the behavior of one object from its collaborators, making it easier to test the object's functionality in isolation.

State Verification: Mock objects can be configured to verify that certain methods are called with specific parameters or in a particular sequence. This allows developers to assert that the code under test interacts with its dependencies correctly.

Behavior Simulation: Mocking frameworks allow developers to define the behavior of mock objects, such as returning specific values or throwing exceptions when certain methods are called. This makes it possible to simulate different scenarios and edge cases during testing.

Performance Testing: In some cases, mocking can be used to simulate the behavior of high-latency or resource-intensive components, allowing developers to test how the system behaves under different performance conditions.
Here's a Python code snippet demonstrating this:
```python
# external_service.py
import requests

def get_data_from_external_service(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
```
Now, let's write a test for the get_data_from_external_service function using mocking to simulate the external API call:
```python
# test_external_service.py
import unittest
from unittest.mock import patch, Mock
from external_service import get_data_from_external_service

class TestExternalService(unittest.TestCase):

    @patch('external_service.requests.get')  # Mock the requests.get method
    def test_get_data_from_external_service_success(self, mock_get):
        # Prepare the mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'key': 'value'}
        
        # Configure the mock object to return the mock response
        mock_get.return_value = mock_response
        
        # Call the function under test
        result = get_data_from_external_service('http://example.com/api/data')
        
        # Assertions
        self.assertEqual(result, {'key': 'value'})
        mock_get.assert_called_once_with('http://example.com/api/data')

    @patch('external_service.requests.get')
    def test_get_data_from_external_service_failure(self, mock_get):
        # Prepare the mock response
        mock_response = Mock()
        mock_response.status_code = 404  # Simulate a failure status code
        
        # Configure the mock object to return the mock response
        mock_get.return_value = mock_response
        
        # Call the function under test
        result = get_data_from_external_service('http://example.com/api/data')
        
        # Assertions
        self.assertIsNone(result)
        mock_get.assert_called_once_with('http://example.com/api/data')

if __name__ == '__main__':
    unittest.main()
```

