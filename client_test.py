import unittest
from unittest.mock import patch

from python_script import query


class TestPythonScript(unittest.TestCase):
    @patch('python_script.requests.post')
    def test_query(self, mock_post):
        # Set the mock response from the chatgpt API
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

        # Set the command line arguments
        args = {
            'start_line': 4,
            'end_line': 20,
            'filename': 'foo.py',
            'query': 'How do I refactor this?',
            'api_key': 'chatgpt-api-key',
            'model': 'text-davinci-002'
        }

        # Run the query function
        result = query(args)

        # Assert that the correct response is returned
        expected_result = {
            'code_suggs': [
                {
                    'text': 'def foo(x, y):\n    return x + y\n',
                    'explanation': 'This code defines a function called `foo` that takes two arguments `x` and `y` and returns their sum.'
                }
            ]
        }
        self.assertEqual(result, expected_result)

