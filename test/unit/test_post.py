"""2022-11-29 16:04:27
Contains unit tests for the Post class.
"""
import unittest
from post import Post


class PostTest(unittest.TestCase):
    """Test case for Post class unit tests."""

    def setUp(self) -> None:
        self.title = "Test title."
        self.content = "Test content."

    def test_create_post(self):
        """Validate posts creation."""
        expected_title = "Test title."
        expected_content = "Test content."
        post = Post(title=self.title, content=self.content)
        self.assertEqual(post.title, expected_title)
        self.assertEqual(post.content, expected_content)

    def test_json(self):
        """Validates json method returns a dict containing title and content."""
        post = Post(title=self.title, content=self.content)
        expected = {'title': 'Test title.', 'content': 'Test content.'}
        self.assertEqual(post.json(), expected)

        post = Post()
        expected = dict()
        self.assertEqual(post.json(), expected)

        post = Post(title=self.title)
        expected = {'title': 'Test title.'}
        self.assertEqual(post.json(), expected)

        post = Post(content=self.content)
        expected = {'content': 'Test content.'}
        self.assertEqual(post.json(), expected)

    def test_repr(self):
        """Validate the repr method."""
        post = Post(title=self.title, content=self.content)
        expected = f'Post(title={repr(self.title)}, content={repr(self.content)})'
        self.assertEqual(repr(post), expected)

        post = Post()
        expected = 'Post()'
        self.assertEqual(repr(post), expected)

        post = Post(content=self.content)
        expected = f'Post(content={repr(self.content)})'
        self.assertEqual(repr(post), expected)

        post = Post(title=self.title)
        expected = f'Post(title={repr(self.title)})'
        self.assertEqual(repr(post), expected)

        # Validate with empty string
        empty_string = ''
        post = Post(empty_string)  # first positional title argument
        expected = f'Post(title={repr(empty_string)})'
        self.assertEqual(repr(post), expected)

        post = Post(None, empty_string)  # second positional title argument
        expected = f'Post(content={repr(empty_string)})'
        self.assertEqual(repr(post), expected)

        # Validate double quote (") character use in title
        quoted_title = 'This "is" a test.'
        post = Post(title=quoted_title)
        expected = f'Post(title={repr(quoted_title)})'
        self.assertEqual(repr(post), expected)


if __name__ == '__main__':
    unittest.main()
