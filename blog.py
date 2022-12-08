from typing import Optional, Dict, List
from post import Post


class Blog:
    def __init__(self, title: Optional[str] = None, author: Optional[str] = None) -> None:
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self) -> str:
        separator = ', '
        result = 'Blog('
        param = list()

        if self.title is not None:
            param.append(f'title={repr(self.title)}')
        if self.author is not None:
            param.append(f'author={repr(self.author)}')

        result += separator.join(param) + ')'
        return result

    def __str__(self):
        return f'{self.title} by {self.author} ({len(self.posts)} post{"s" if len(self.posts) != 1 else None})'

    def create_post(self, title: Optional[str] = None, content: Optional[str] = None) -> None:
        """Add a new post into the blog lists"""
        post = Post(title, content)
        self.posts.append(post)

    def json(self) -> Dict[Optional[str], Optional[str] | Optional[List[Post]]]:
        """Returns a dict with the attributes."""
        json = dict()
        if self.title is not None:
            json['title'] = self.title
        if self.author is not None:
            json['author'] = self.author
        if len(self.posts) > 0:
            json['posts'] = [post.json() for post in self.posts]

        return json
