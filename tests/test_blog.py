from unittest.mock import patch
from tutorial.blog import Blog


@patch('tutorial.blog.Blog')
def test_blog_posts(MockBlog):
    blog = MockBlog()
    blog.posts.return_value = [
        {
            'userid': 1,
            'id': 1,
            'title': 'Test Title',
            'body': 'blahblah body'
        }
    ]

    response = blog.posts()
    assert response is not None
    assert isinstance(response[0], dict)

    assert MockBlog.called
    print(blog.posts.assert_called_with())
