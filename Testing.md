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
