import unittest
from unittest.mock import patch

from python_script import run_python_script


class TestPythonScript(unittest.TestCase):
    @patch('python_script.requests.post')
    def test_run_python_script(self, mock_post):
        # Set the mock response from the OpenAI API
        mock_response = {
            'data': {
                'code_suggs': [
                    {
                        'text': 'def foo(x, y):\n    return x + y\n',
                        'explanation': 'This code defines a function called `foo` that takes two arguments `x` and `y` and returns their sum.'
                    }
                ]
            }
        }
        mock_post.return_value = mock_response

        # Run the Python script with the selected lines, filename, and query
        selected_lines = 'def foo(x, y):\n    return x * y\n'
        filename = 'foo.py'
        query = 'How do I rewrite this to return the sum instead of the product?'
        result = run_python_script(selected_lines, filename, query)

        # Assert that the correct code suggestions and explanation are returned
        expected_result = {
            'code_suggs': [
                {
                    'text': 'def foo(x, y):\n    return x + y\n',
                    'explanation': 'This code defines a function called `foo` that takes two arguments `x` and `y` and returns their sum.'
                }
            ]
        }
        self.assertEqual(result, expected_result)
