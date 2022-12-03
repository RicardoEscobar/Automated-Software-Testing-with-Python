from typing import Optional, Dict


class Blog:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self) -> str:
        pass

    def create_post(self, title, content):
        pass

    def json(self):
        pass
