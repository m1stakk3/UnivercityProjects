import cv2


def find_matches(image1, image2):
    # Загрузка изображений
    img1 = cv2.imread(image1, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(image2, cv2.IMREAD_GRAYSCALE)

    # Создание объекта SIFT
    sift = cv2.xfeatures2d.SIFT_create()

    # Нахождение ключевых точек и дескрипторов на обоих изображениях
    keypoints1, descriptors1 = sift.detectAndCompute(img1, None)
    keypoints2, descriptors2 = sift.detectAndCompute(img2, None)

    # Создание объекта BFMatcher
    bf = cv2.BFMatcher()

    # Сравнение дескрипторов и нахождение наилучших совпадений
    matches = bf.knnMatch(descriptors1, descriptors2, k=2)

    # Применение фильтра RANSAC для отсеивания неправильных совпадений
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    # Изменение размера изображений на 1920x1080 пикселей
    img1 = cv2.resize(img1, (1920, 1080))
    img2 = cv2.resize(img2, (1920, 1080))

    # Визуализация совпадений
    img_matches = cv2.drawMatches(img1, keypoints1, img2, keypoints2, good_matches, None,
                                  flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    # Отображение изображения с совпадениями
    cv2.imshow("Matches", img_matches)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Пример использования функции
find_matches("image1.jpg", "image2.jpg")
