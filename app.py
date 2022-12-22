"""Starting point. Run this to initiate the app."""
from blog import Blog

MENU_PROMPT = 'Enter (c) to create blog, (l) to list blogs, (r) to read one, (p) to create apost, (q) to quit.'
POST_TEMPLATE = """--- {} ---

{}

"""

blogs = dict()


def menu():
    """Show user available blogs"""
    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)


def print_blogs():
    """Prints blogs"""
    for key, blog in blogs.items():
        print('- {}'.format(blog))


def ask_create_blog():
    title = input('Enter your blog title: ')
    author = input('Enter your name: ')

    blogs[title] = Blog(title=title, author=author)


def ask_read_blog():
    title = input('Enter the blog title you want to read: ')

    print_posts(blogs[title])


def print_posts(blog):
    for post in blog.posts:
        print_post(post)


def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))


def ask_create_post():
    blog_name = input('Blog name: ')
    post_title = input('Post title: ')
    post_content = input('Post content: ')

    blogs[blog_name].create_post(post_title, post_content)
