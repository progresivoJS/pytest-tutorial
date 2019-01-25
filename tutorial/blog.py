import requests


class Blog:
    def __init__(self, name):
        self.name = name

    def posts(self):
        response = requests.get("https://blog.naver.com/inja0391")
        return response.json()

    def __repr__(self):
        return f'Blog({self.name})'
