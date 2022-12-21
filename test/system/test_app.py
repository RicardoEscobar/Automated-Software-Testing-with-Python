"""Integration testing for app.py"""
import unittest
from unittest.mock import patch
import app
from blog import Blog
from post import Post


class BlogTest(unittest.TestCase):
    """System test case for app.py"""

    def setUp(self) -> None:
        self.blog_title = 'Blog title.'
        self.blog_author = 'Blog author.'
        return super().setUp()

    def test_print_blogs(self):
        """Validate blog prints"""
        blog = Blog(title=self.blog_title, author=self.blog_author)
        app.blogs = {'test': blog}

        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with(
                '- Blog title. by Blog author. (0 posts)')

    def test_menu_print_prompt(self):
        """Validates that the menu prompt gets printed out."""
        with patch('builtins.input', return_value='q') as mocked_input:
            with patch('builtins.print') as mocked_print:
                app.menu()
                mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        """Validates that menu function calls the print_blogs function."""
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q') as mocked_input:
                app.menu()
                mocked_print_blogs.assert_called()

    def test_ask_create_blog(self):
        """Validates ask_create_blog function is called."""
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = (self.blog_title, self.blog_author)
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get(self.blog_title))

    def test_ask_read_blog(self):
        """Validate ask_read_blog is being called with Blog object."""
        blog = Blog(title='Test', author='Test author')
        app.blogs = {'Test': blog}
        with patch('builtins.input', return_value='Test'):
            with patch('app.print_posts') as mocked_print_posts:
                with patch('builtins.print'):
                    app.ask_read_blog()

                    mocked_print_posts.assert_called_with(blog)

    def test_print_posts(self):
        """Validate print_posts is being called with Blog object."""
        blog = Blog(title='Test', author='Test author')
        blog.create_post(title='Test post.', content='Test content.')
        app.blogs = {'Test': blog}

        with patch('app.print_post') as mocked_print_post:
            app.print_posts(blog)

            mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_post(self):
        """Validate print_post funtion works properly."""
        post = Post(title='Post title.', content='Post content.')
        expected_print = """--- Post title. ---

Post content.

"""
        with patch('builtins.print') as mocked_print:
            app.print_post(post)

            mocked_print.assert_called_with(expected_print)


if __name__ == '__main__':
    unittest.main()
