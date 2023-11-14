import uuid
from typing import List, Optional


class Rate:
    def __init__(self,
                 rate_id: str,
                 name: str,
                 price: float):
        self.rate_id = rate_id
        self.name = name
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Rate):
            return self.rate_id == other.rate_id
        else:
            return False


class RepImage:
    def __init__(self, rep_image_id: str):
        self.rep_image_id = rep_image_id
        self.images: List[Image] = []

    def __eq__(self, other):
        if isinstance(other, RepImage):
            return self.rep_image_id == other.rep_image_id
        else:
            return False

    # добавить изображение
    def add_image(self, image_name: str):
        image_id = str(uuid.uuid4())
        image = Image(image_id, image_name)
        self.images.append(image)


class RepDocument:
    def __init__(self, rep_document_id: str):
        self.rep_document_id = rep_document_id
        self.documents: List[Document] = []

    def __eq__(self, other):
        if isinstance(other, RepDocument):
            return self.rep_document_id == other.rep_document_id
        else:
            return False

    # добавить документ
    def add_image(self, document_name: str):
        document_id = str(uuid.uuid4())
        document = Document(document_id, document_name)
        self.documents.append(document)


class RepBoard:
    def __init__(self, rep_board_id: str):
        self.rep_board_id = rep_board_id
        self.boards: List[Board] = []

    def __eq__(self, other):
        if isinstance(other, RepBoard):
            return self.rep_board_id == other.rep_board_id
        else:
            return False

    # создать доску
    def create_board(self, board_name: str):
        board_id = str(uuid.uuid4())
        board_background = "Adaptive grid"
        board = Board(board_id, board_name, board_background)
        self.boards.append(board)


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
        self.repBoard: RepBoard
        self.repImage: RepImage
        self.repDocument: RepDocument

    def __eq__(self, other):
        if isinstance(other, User):
            return self.user_id == other.user_id
        else:
            return False

    # сменить тариф
    def change_rate(self, new_rate: Rate):
        self.rate = new_rate


class Image:
    def __init__(self,
                 image_id: str,
                 name: str,
                 participants: List[User] = ()):
        self.image_id = image_id
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
                 name: str,
                 participants: List[User] = ()):
        self.document_id = document_id
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
                 name: str,
                 background: str,
                 participants: List[User] = ()):
        self.board_id = board_id
        self.name = name
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


# авторизация пользователя
def login_user(user: User, email: str, password: str) -> Optional[User]:
    if email == user.email and password == user.password:
        return user
    return None


# поделиться правами доступа
# def share_rights(name_board: Board, permissions: str, user: User):

# сохранить доску как картинку
# def save_board_img(board: Board):
