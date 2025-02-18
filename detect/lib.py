import easyocr
from PIL import Image
import io
import numpy as np


def detect(image_bytes):
    # 创建一个 reader 对象，指定要识别的语言，这里以英文为例
    reader = easyocr.Reader(['ch_sim', 'en'])

    # 将字节数据转换为 PIL 图像对象
    image = Image.open(io.BytesIO(image_bytes))

    # 将 PIL 图像对象转换为 numpy 数组
    image_np = np.array(image)

    # 使用 EasyOCR 进行 OCR 识别
    result = reader.readtext(image_np)

    return result
