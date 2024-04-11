import cv2
from os import path


# Загрузка видео
def write_initials_on_video(video_path: str = path.join(path.abspath(path.dirname(__file__)), "input_video.mp4")   ):

    cap = cv2.VideoCapture(video_path)

    # Получение информации о видео
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Цикл для обработки каждого кадра видео
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Добавление текста на кадр
        text = "Daniel Kirin"  # Замените на ваш текст
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        font_color = (255, 255, 255)  # Белый цвет текста
        thickness = 2
        text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
        text_x = int((width - text_size[0]) / 2)
        text_y = int((height - text_size[1]) / 2)
        cv2.putText(frame, text, (text_x, text_y), font, font_scale, font_color, thickness, cv2.LINE_AA)

        # Отображение обработанного кадра
        cv2.imshow('Daniel Kirin 2 course magister', frame)

        # Прерывание цикла при нажатии клавиши 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Освобождение ресурсов
    cap.release()
    cv2.destroyAllWindows()


write_initials_on_video()
