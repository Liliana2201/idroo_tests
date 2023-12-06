import unittest
import uuid
from main import Rate, User


class CreateBoardTests(unittest.TestCase):
    # создаем пользователя
    def setUp(self):
        user_id = str(uuid.uuid4())
        rate_id = str(uuid.uuid4())
        self.rate = Rate(rate_id, "free", 0)
        self.user = User(
            user_id, self.rate, "Name_user", "test@example.com", "password"
        )

    def test_create_board(self):
        board_name = "test_board"
        self.user.create_board(board_name)
        self.assertEqual(len(self.user.boards), 1)  # проверяем, что количество досок соответствует 1
        self.assertEqual(self.user.boards[0].name,
                         board_name)  # проверяем, что имя созданной доски совпадает с введенным


if __name__ == '__main__':
    unittest.main()
