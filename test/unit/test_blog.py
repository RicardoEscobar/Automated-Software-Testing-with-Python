"""Unit testing for blog.py"""
import unittest
from blog import Blog


class BlogTest(unittest.TestCase):
    """Unit test case for blog.py"""

    def setUp(self) -> None:
        self.title = 'Test title.'
        self.author = 'Test author.'
        self.posts = [{
            'title': 'Test post title.',
            'content': 'Test post content.'
        }]
        return super().setUp()

    def test_create_blog(self):
        """Validate create blog."""
        expected = dict()
        expected['title'] = 'Test title.'
        expected['author'] = 'Test author.'

        blog = Blog(title=self.title, author=self.author)
        self.assertEqual(expected['title'], blog.title)
        self.assertEqual(expected['author'], blog.author)

    def test_repr(self):
        """Validate the repr method."""
        blog = Blog(title=self.title, author=self.author)
        expected = f'Blog(title={repr(self.title)}, author={repr(self.author)})'
        self.assertEqual(repr(blog), expected)

        blog = Blog()
        expected = 'Blog()'
        self.assertEqual(repr(blog), expected)

        blog = Blog(author=self.author)
        expected = f'Blog(author={repr(self.author)})'
        self.assertEqual(repr(blog), expected)

        blog = Blog(title=self.title)
        expected = f'Blog(title={repr(self.title)})'
        self.assertEqual(repr(blog), expected)

        empty_string = ''
        blog = Blog(empty_string)  # first positional title argument
        expected = f'Blog(title={repr(empty_string)})'
        self.assertEqual(repr(blog), expected)

        blog = Blog(None, empty_string)  # second positional title argument
        expected = f'Blog(author={repr(empty_string)})'
        self.assertEqual(repr(blog), expected)

    def test_json(self):
        """Validating the json method."""
        # Using posts in blog object
        blog = Blog(title=self.title, author=self.author)
        blog.create_post('Test post title.', 'Test post content.')
        expected = {
            'title': 'Test title.',
            'author': 'Test author.',
            'posts': [
                {'title': 'Test post title.',
                 'content': 'Test post content.'},
            ]
        }
        self.assertEqual(blog.json(), expected)

        # Test using empty post list
        blog = Blog(title=self.title, author=self.author)
        expected = {
            'title': 'Test title.',
            'author': 'Test author.',
        }
        self.assertEqual(blog.json(), expected)


if __name__ == '__main__':
    unittest.main()
