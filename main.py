import argparse
from pathlib import Path

from config import INPUT_DIR
from processing.image_loader import load_image


def main():

    # 1. Recibir la ruta de la imagen
    parser = argparse.ArgumentParser(
        description="Procesamiento de imágenes de heridas"
    )

    parser.add_argument(
        "image",
        nargs="?",
        help="Ruta de la imagen que se va a procesar"
    )

    args = parser.parse_args()

    # 2. Definir qué imagen se va a procesar
    if args.image:
        image_path = Path(args.image).expanduser().resolve()
    else:
        image_path = (INPUT_DIR / "herida_test_001.jpg").resolve()

    # 3. Comprobar que la imagen existe
    if not image_path.is_file():
        raise SystemExit(
            f"Error: no se encontró la imagen: {image_path}"
        )

    # 4. Cargar la imagen
    image = load_image(str(image_path))

    # 5. Mostrar información para verificar la entrada
    height, width, channels = image.shape

    print("Imagen cargada correctamente")
    print(f"Ruta: {image_path}")
    print(f"Ancho: {width} píxeles")
    print(f"Alto: {height} píxeles")
    print(f"Canales: {channels}")

    # Próximo paso:
    # En este punto conectaremos el pipeline de IA.


if __name__ == "__main__":
    main()
