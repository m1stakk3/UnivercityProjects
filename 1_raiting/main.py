import cv2 as cv
from os import path
from datetime import datetime


def write_initials_on_image(
        image_path: str = "victor.jpeg",
        initials_value: str = "Kirin Daniel Alexandrovich",
        result_filename: str or None = None
) -> str:
    """
    Функция наносит надпись на новое изображение и сохраняет его
    :param image_path: путь к изображению, которое лежит в основе
    :param initials_value: строка с инициалами (на английском языке)
    :param result_filename: строка с именем файла
    :return: путь к файлу
    """

    # считывание изображения
    image = cv.imread(path.abspath(image_path))

    # получения параметров ширины, высоты и каналов
    height, width, channels = image.shape

    # заданние параметров текста
    font: int = cv.FONT_HERSHEY_DUPLEX
    text_coordinates: tuple = (width // 4, height // 2)
    font_scale: int = 2
    font_color: tuple = (0, 152, 255)
    thickness: int = 3
    line_type: int = 2

    # нанесение текста на картинку
    cv.putText(
        image,
        initials_value,
        text_coordinates,
        font,
        font_scale,
        font_color,
        thickness,
        line_type
    )

    # сохранение новой картинки
    result_path: str = datetime.now().strftime("%H-%M-%ST%d-%m-%Y") if result_filename is None else result_filename
    result_path += ".jpg"
    cv.imwrite(result_path, image)
    return result_path


assert path.exists(write_initials_on_image())
assert path.exists(write_initials_on_image(result_filename="test"))
