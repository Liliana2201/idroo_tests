import uuid
import os
import pyperclip
from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class Rate:
    rate_id: str
    name: str
    price: float


class User:
    def __init__(self,
                 user_id: str,
                 rate: Rate,
                 name: str,
                 email: str,
                 password: str, ):
        self.user_id = user_id
        self.rate = rate
        self.name = name
        self.email = email
        self.password = password
        self.boards: List[Board] = []
        self.images: List[Image] = []
        self.documents: List[Document] = []

    def __eq__(self, other):
        if isinstance(other, User):
            return self.user_id == other.user_id
        else:
            return False

    # сменить тариф
    def change_rate(self, new_rate: Rate):
        self.rate = new_rate

    # добавить изображение
    def add_image(self, image_name: str):
        image_id = str(uuid.uuid4())
        image = Image(image_id, self, image_name)
        self.images.append(image)

    # добавить документ
    def add_document(self, document_name: str):
        document_id = str(uuid.uuid4())
        document = Document(document_id, self, document_name)
        self.documents.append(document)

    # создать доску
    def create_board(self, board_name: str):
        board_id = str(uuid.uuid4())
        board_background = "Adaptive grid"
        board_link = "https://app.idroo.com/boards/" + str(uuid.uuid4()).split("-")[0]
        board = Board(board_id, self, board_name, board_link, board_background)
        self.boards.append(board)


class Image:
    def __init__(self,
                 image_id: str,
                 user: User,
                 name: str,
                 participants: List[User] = ()):
        self.image_id = image_id
        self.user = user
        self.name = name
        self.participants = participants

    def __eq__(self, other):
        if isinstance(other, Image):
            return self.image_id == other.image_id
        else:
            return False


class Document:
    def __init__(self,
                 document_id: str,
                 user: User,
                 name: str,
                 participants: List[User] = ()):
        self.document_id = document_id
        self.user = user
        self.name = name
        self.participants = participants

    def __eq__(self, other):
        if isinstance(other, Document):
            return self.document_id == other.document_id
        else:
            return False


class Board:
    def __init__(self,
                 board_id: str,
                 user: User,
                 name: str,
                 link: str,
                 background: str,
                 participants: List[User] = ()):
        self.board_id = board_id
        self.user = user
        self.name = name
        self.link = link
        self.background = background
        self.participants = participants
        self.figures: List[Figure] = []
        self.texts: List[Text] = []

    def __eq__(self, other):
        if isinstance(other, Board):
            return self.board_id == other.board_id
        else:
            return False

    # создать фигуру
    def create_figure(self, shape: str, line_stile: str, color_pen: str, size_pen: int, color_fill: str):
        figure_id = str(uuid.uuid4())
        figure = Figure(figure_id, self, shape, line_stile, color_pen, size_pen, color_fill)
        self.figures.append(figure)

    # создать текст
    def create_text(self, color_stroke: str, width_stroke: int, line_stile: str, color_text: str, color_fill: str,
                    text_size: int, font: str):
        text_id = str(uuid.uuid4())
        text = Text(text_id, self, color_stroke, width_stroke, line_stile, color_text, color_fill, text_size, font)
        self.texts.append(text)

    # изменить фон доски
    def change_background(self, new_board_background: str):
        self.background = new_board_background

    # поделиться доступом
    def share(self):
        pyperclip.copy(self.link)


class Figure:
    def __init__(self,
                 figure_id: str,
                 board: Board,
                 shape: str,
                 line_stile: str,
                 color: str,
                 size: int,
                 fill: str):
        self.figure_id = figure_id
        self.board = board
        self.shape = shape
        self.line_stile = line_stile
        self.color = color
        self.size = size
        self.fill = fill

    def __eq__(self, other):
        if isinstance(other, Figure):
            return self.figure_id == other.figure_id
        else:
            return False

    # изменить цвет пера
    def change_color(self, new_color: str):
        self.color = new_color


class Text:
    def __init__(self,
                 text_id: str,
                 board: Board,
                 color_stroke: str,
                 width_stroke: int,
                 line_stile: str,
                 color_text: str,
                 color_fill: str,
                 text_size: int,
                 font: str):
        self.text_id = text_id
        self.board = board
        self.color_stroke = color_stroke
        self.width_stroke = width_stroke
        self.line_stile = line_stile
        self.color_text = color_text
        self.color_fill = color_fill
        self.text_size = text_size
        self.font = font

    def __eq__(self, other):
        if isinstance(other, Text):
            return self.text_id == other.text_id
        else:
            return False

    # изменить шрифт
    def change_font(self, new_font: str):
        self.font = new_font


# регистрация пользователя
def reg_user(name: str, rate: Rate, email: str, password: str) -> User:
    user_id = str(uuid.uuid4())
    user = User(user_id, rate, name, email, password)
    return user


# регистрация пользователя через google
def reg_user_with_google(rate: Rate, email: str) -> User:
    user_id = str(uuid.uuid4())
    name = "Гость" + user_id
    password = str(uuid.uuid4()).split("-")[0]
    user = User(user_id, rate, name, email, password)
    return user


# авторизация пользователя
def login_user(user: User, email: str, password: str) -> Optional[User]:
    if email == user.email and password == user.password:
        return user
    return None


# авторизация пользователя через google
def login_user_with_google(user: User, email: str) -> Optional[User]:
    if email == user.email:
        return user
    return None


# вход на доску по ссылке
def login_board(user: User, board: Board, link: str, user_id: str) -> Optional[Board]:
    if link == board.link and user_id == user.user_id:
        user.boards.append(board)
        board.participants.append(user)
        return board
    return None


# удалить доску
def delete_board(user: User, board: Board) -> Optional[User]:
    if board.user == user:
        user.boards.remove(board)
        return user
    return None


# сохранить доску как картинку
def save_board_img(board: Board):
    stroka = f'"C:/Users/Лилиана Шубина/Downloads/{board.name}.png"'
    return stroka
