from tenacity import *

def return_last_value(retry_state):
    """return the result of the last call attempt"""
    return retry_state.outcome.result()

def is_false(value):
    """Return True if value is False"""
    return value is False

# will return False after trying 3 times to get a different result
@retry(stop=stop_after_attempt(3),
       retry_error_callback=return_last_value,
       retry=retry_if_result(is_false))
 def eventually_return_false():
    return False
