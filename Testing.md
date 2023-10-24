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

