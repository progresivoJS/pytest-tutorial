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
    blog.posts.assert_called_with()
    blog.posts.assert_called_once_with()
    blog.reset_mock()
    blog.posts.assert_not_called()
