from tests.setup import client


class TestTemplates:

    def test_index_template(self):
        response = client.get('/')
        assert response.status_code == 200
        assert 'text/html' in response.headers.get('Content-Type')
        assert response.template.name == 'index.html'

    def test_dashboard_template(self):
        response = client.get('/dashboard')
        assert response.status_code == 200
        assert 'text/html' in response.headers.get('Content-Type')
        assert response.template.name == 'dashboard.html'

    def test_404_template(self):
        response = client.get('/routethatdoesntexist')
        assert response.status_code == 404
        assert 'text/html' in response.headers.get('Content-Type')
        assert response.template.name == '404.html'
