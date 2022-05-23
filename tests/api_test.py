from run import app


class TestApi:
    def test_app_all_posts_status_code(self):
        response = app.test_client().get('/api/posts', follow_redirects=True)
        assert response.status_code == 200, "Статус код запроса постов неверный"
        assert response.mimetype == "application/json", "Получен не JSON"

    def test_app_all_posts_type_count_content(self):
        response = app.test_client().get('/api/posts', follow_redirects=True)
        assert type(response.json) == list, "Получен не список"
        assert len(response.json) == 8, "Получено неверное количество элементов в списке"

    def test_app_all_posts_type_check_keys(self):
        keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
        response = app.test_client().get('/api/posts', follow_redirects=True)
        first_keys = set(response.json[0].keys())
        assert keys == first_keys, "Полученные ключи не совпадают"
