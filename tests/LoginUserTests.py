import unittest
import uuid
from main import Rate, User, login_user


class LoginUserTests(unittest.TestCase):
    # создаем аутентифицированного пользователя
    def setUp(self):
        user_id = str(uuid.uuid4())
        rate_id = str(uuid.uuid4())
        self.rate = Rate(rate_id, "free", 0)
        self.authenticated_user = User(
            user_id, self.rate, "Name_user", "test@example.com", "password"
        )

    # если данные совпадают, возвращаем аутентифицированного пользователя
    def test_login_user_valid_data(self):
        self.assertEqual(
            login_user(
                self.authenticated_user, "test@example.com", "password"
            ),
            self.authenticated_user
        )

    # если данные не совпадают, возвращаем сообщение об ошибке
    def test_login_user_invalid_data(self):
        self.assertIsNone(
            login_user(
                self.authenticated_user, "test@example.com", "wrongPassword"
            ),
            "Неверный пароль"
        )


if __name__ == '__main__':
    unittest.main()
