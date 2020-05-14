from tests.setup import client

# Do these tests need to be this repetitive in order to
# be as clear as possible?


class TestCssFiles:

    def test_main_css(self):
        response = client.get('/static/main.css')
        assert response.status_code == 200
        assert 'text/css' in response.headers.get('Content-Type')

    def test_index_css(self):
        response = client.get('/static/index.css')
        assert response.status_code == 200
        assert 'text/css' in response.headers.get('Content-Type')

    def test_dashboard_css(self):
        response = client.get('/static/dashboard.css')
        assert response.status_code == 200
        assert 'text/css' in response.headers.get('Content-Type')

    def test_404_css(self):
        response = client.get('/static/404.css')
        assert response.status_code == 200
        assert 'text/css' in response.headers.get('Content-Type')


class TestJSFiles:
    """
    More .js files will probably be added to this test class,
    since they can get very long and complex.
    """

    def test_main_js(self):
        response = client.get('/static/main.js')
        assert response.status_code == 200
        assert 'application/javascript' in response.headers.get('Content-Type')

    def test_index_js(self):
        response = client.get('/static/index.js')
        assert response.status_code == 200
        assert 'application/javascript' in response.headers.get('Content-Type')

    def test_dashboard_js(self):
        response = client.get('/static/dashboard.js')
        assert response.status_code == 200
        assert 'application/javascript' in response.headers.get('Content-Type')

    def test_404_js(self):
        response = client.get('/static/404.js')
        assert response.status_code == 200
        assert 'application/javascript' in response.headers.get('Content-Type')
