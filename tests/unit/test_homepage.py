from roasts_and_recipies.site import home_page


def test_root_url_resolves_to_home_page(client):
    response = client.get("/")
    assert response.data == home_page


def test_home_page_returns_correct_html(client):
    response = client.get("/")

    assert response.html.startswith("<html>")
    assert "<title>To-Do lists</title>" in response.html
    assert "<title>To-Do lists</title>" in response.html
    assert response.html.endswith("</html>")
