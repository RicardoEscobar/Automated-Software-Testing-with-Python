"""Integration testing for app.py"""
import unittest
from unittest.mock import patch
import app
from blog import Blog


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
        with patch('builtins.input') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        """Validates that menu function calls the print_blogs function."""
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q') as mocked_input:
                print(
                    f'mocked_input.return_value = {mocked_input.return_value}')
                app.menu()
                mocked_print_blogs.assert_called()


if __name__ == '__main__':
    unittest.main()
