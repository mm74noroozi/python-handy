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
