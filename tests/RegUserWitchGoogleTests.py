import unittest
import uuid
from main import Rate, User, reg_user_with_google


class RegUserWitchGoogleTests(unittest.TestCase):
    # добавляем бесплатный тариф
    def setUp(self):
        rate_id = uuid.uuid4()
        self.rate = Rate(str(rate_id), "free", 0)

    def test_reg__user(self):
        user_email = "test@example.com"
        self.user = reg_user_with_google(self.rate, user_email)  # регистрируем пользователя
        self.assertEqual(self.user.email, user_email)  # проверяем, что email созданного пользователя совпадает с введенным


if __name__ == '__main__':
    unittest.main()
