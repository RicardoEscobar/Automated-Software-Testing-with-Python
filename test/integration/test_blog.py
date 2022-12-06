"""Integration testing for blog.py"""
import unittest
from blog import Blog


class BlogTest(unittest.TestCase):
    """Integration test case for blog.py"""

    def setUp(self) -> None:
        self.title = 'Test title.'
        self.author = 'Test author.'
        self.posts = [{
            'title': 'Test post title.',
            'content': 'Test post content.'
        }]
        return super().setUp()

    def test_create_post_in_blog(self):
        """Validate creating a post from a blog."""
        blog = Blog(title=self.title, author=self.author)
        blog.create_post(title='Test post title.',
                         content='Test post content.')

        self.assertEqual(len(blog.posts), 1)
        self.assertEqual(blog.posts[0].title, 'Test post title.')
        self.assertEqual(blog.posts[0].content, 'Test post content.')

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
