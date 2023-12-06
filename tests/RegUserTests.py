import unittest
import uuid
from main import Rate, User, reg_user


class RegUserTests(unittest.TestCase):
    # добавляем бесплатный тариф
    def setUp(self):
        rate_id = uuid.uuid4()
        self.rate = Rate(str(rate_id), "free", 0)

    def test_reg_user(self):
        user_name = "test_name"
        self.user = reg_user(user_name, self.rate, "test@example.com", "password")  # регистрируем пользователя
        self.assertEqual(self.user.name, user_name)  # проверяем, что имя созданного пользователя совпадает с введенным


if __name__ == '__main__':
    unittest.main()
