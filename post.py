from typing import Optional, Dict


class Post:
    def __init__(self, title: Optional[str] = None, content: Optional[str] = None) -> None:
        self.title = title
        self.content = content

    def json(self) -> Dict[Optional[str], Optional[str]]:
        """Returns a dict with the attributes."""
        json = dict()
        if self.title is not None:
            json["title"] = self.title
        if self.content is not None:
            json["content"] = self.content
        return json

    def __repr__(self) -> str:
        separator = ', '
        result = 'Post('
        param = list()

        if self.title is not None:
            param.append(f'title="{self.title}"')
        if self.content is not None:
            param.append(f'content="{self.content}"')

        result += separator.join(param) + ')'
        return result
