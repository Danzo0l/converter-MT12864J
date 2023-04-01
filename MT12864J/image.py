from PIL import Image


def open_image(path: str) -> Image:
    image = Image.open(path)
    return image


def save_image(image: Image, filename: str) -> str:
    image.save(filename)
    return str(filename)


def show_image(image: Image):
    image.show()


def resize_image(image: Image, width: int, height: int) -> Image:
    image = image.resize((width, height))
    return image


def convert_image(image: Image) -> Image:
    image = image.convert('L')
    return image


def threshold_iamge(threshold: int, image: Image) -> Image:
    image = image.point(lambda p: 255 if p > threshold else 0)
    image = image.convert('1')
    return image
