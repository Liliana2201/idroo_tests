import unittest
import uuid
import pyperclip
from main import Rate, User, Board, save_board_img, Figure, Text


class UsingBoardTests(unittest.TestCase):
    # создаем пользователя, доску, текст и фигуру на доске
    def setUp(self):
        user_id = str(uuid.uuid4())
        rate_id = str(uuid.uuid4())
        self.rate = Rate(rate_id, "free", 0)
        self.user = User(
            user_id, self.rate, "Name_user", "test@example.com", "password"
        )
        board_id = str(uuid.uuid4())
        board_background = "Adaptive grid"
        board_link = "https://app.idroo.com/boards/" + str(uuid.uuid4()).split("-")[0]
        self.user.boards.append(Board(board_id, self.user, "test_name", board_link, board_background))
        figure_id = str(uuid.uuid4())
        self.user.boards[0].figures.append(Figure(figure_id, self.user.boards[0], "pencil", "line", "black", 3, "none"))
        text_id = str(uuid.uuid4())
        self.user.boards[0].texts.append(Text(text_id, self.user.boards[0], "none", 0, "none", "black", "none", 16, "Open Sans"))
    def test_change_background(self):
        new_board_background = "squares"
        self.user.boards[0].change_background(new_board_background)  # меняем фон
        self.assertEqual(self.user.boards[0].background, new_board_background)  # проверяем, что фон созданной доски совпадает с заданным

    def test_share(self):
        self.user.boards[0].share()
        self.assertEqual(self.user.boards[0].link, pyperclip.paste())  # проверяем что ссылка скопирована в буфер обмена

    def test_save_board_as_img(self):
        path = save_board_img(self.user.boards[0])
        self.assertEqual(path, f'"C:/Users/Лилиана Шубина/Downloads/{self.user.boards[0].name}.png"')

    def test_change_color_figure(self):
        new_color = "red"
        self.user.boards[0].figures[0].change_color(new_color)
        self.assertEqual(self.user.boards[0].figures[0].color, new_color)  # проверяем, что цвет созданной фигуры совпадает с заданным

    def test_change_font_text(self):
        new_font = "wrong_font"
        self.user.boards[0].texts[0].change_font(new_font)
        self.assertEqual(self.user.boards[0].texts[0].font, new_font)  # проверяем, что шрифт созданного текста совпадает с заданным


if __name__ == '__main__':
    unittest.main()
