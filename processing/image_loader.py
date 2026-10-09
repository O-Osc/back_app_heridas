import cv2


def load_image(image_path: str):
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(
            f"No se pudo leer la imagen: {image_path}"
        )

    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)