import unittest
from blog import Blog


class BlogTest(unittest.TestCase):
    def setUp(self) -> None:
        self.title = 'Test title'
        self.author = 'Test author'
        return super().setUp()

    def test_create_blog(self):
        """Validate create blog."""
        expected = dict()
        expected['title'] = 'Test title'
        expected['author'] = 'Test author'

        blog = Blog(title=self.title, author=self.author)
        self.assertEqual(expected['title'], blog.title)
        self.assertEqual(expected['author'], blog.author)


if __name__ == '__main__':
    unittest.main()
