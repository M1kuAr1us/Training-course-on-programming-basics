from unittest.mock import Mock, patch
import math


# Example 1: Basic Mock usage
print("Example 1: Basic Mock usage")
mock_obj = Mock()
mock_obj.return_value = 10
result = mock_obj()
print(f"mock_obj() returned: {result}")
mock_obj.some_method(5, key='value')
print(f"Called some_method with: {mock_obj.some_method.call_args}\n")


# Example 2: Using patch to replace a function
print("Example 2: Using patch to replace a function")
def external_api_call():
    raise RuntimeError("Real API call")

def get_data():
    return external_api_call()

with patch('__main__.external_api_call', return_value={'data': 123}):
    print(f"get_data() returned: {get_data()}\n")


# Example 3: side_effect in Mock (inspired by Toptal)
print("Example 3: side_effect in Mock")
mock_div = Mock(side_effect=lambda x, y: x / y if y != 0 else (_ for _ in ()).throw(ZeroDivisionError("division by zero")))
print(f"mock_div(10, 2): {mock_div(10, 2)}")
try:
    mock_div(10, 0)
except ZeroDivisionError as e:
    print(f"Caught ZeroDivisionError: {e}\n")


# Example 4: autospec with patch
print("Example 4: autospec with patch")
with patch('math.sqrt', autospec=True) as mock_sqrt:
    mock_sqrt.return_value = 5
    print(f"math.sqrt(16) returned: {math.sqrt(16)}")
    mock_sqrt.assert_called_with(16)