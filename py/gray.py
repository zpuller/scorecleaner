import numpy as np
import sys

from PIL import Image


def adjust_levels(image_path, output_path, thresh):
    image = Image.open(image_path).convert('L')

    np_image = np.array(image)
    np_image = np.where(np_image > thresh, 255, np_image)

    result_image = Image.fromarray(np_image)
    result_image.save(output_path)


input_path, output_path = sys.argv[1:]

adjust_levels(input_path, output_path, 192)
