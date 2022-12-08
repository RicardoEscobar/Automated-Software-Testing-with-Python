"""Starting point. Run this to initiate the app."""
MENU_PROMPT = 'Enter (c) to create blog, (l) to list blogs, (r) to read one, (p) to create apost, (q) to quit.'

blogs = dict()


def menu():
    """Show user available blogs"""
    print_blogs()
    selection = input(MENU_PROMPT)


def print_blogs():
    """Prints blogs"""
    for key, blog in blogs.items():
        print('- {}'.format(blog))
