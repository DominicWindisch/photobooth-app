import logging
import math

from PIL import Image
from rectpack import newPacker

logger = logging.getLogger(__name__)


def merge_print_items_stage(print_items: list[Image.Image], page_width_mm: int, page_height_mm: int, dpi: int = 300) -> list[Image.Image]:
    """ """

    # fit images into a given page size
    # if necessary, return multiple pages to print

    # setup page canvas
    page_width_px = page_width_mm * dpi / 25.4
    page_height_px = page_height_mm * dpi / 25.4
    page_orientation_landscape = page_width_mm > page_height_mm

    # setup packer
    packer = newPacker()

    # allow infinite pages, i.e. take as many as necessary
    packer.add_bin(page_width_px, page_height_px, float("inf"))

    scaled_items: list[Image.Image] = []
    for index, item in enumerate(print_items):
        _image = item

        # resize items to fill page optimally.
        item_orientation_landscape = _image.width > _image.height

        if item_orientation_landscape != page_orientation_landscape:
            _image.rotate(90.0)

        # resize to whichever dimension fits best
        if page_width_px / _image.width > page_height_px / _image.height:
            # scale image to fill complete height, but possibly not complete width
            _image.resize(tuple(math.floor(_image.width * (page_height_px / _image.height)), page_height_px))
        else:
            # scale image to fill complete width, but possibly not complete height
            _image.resize(tuple(page_width_px, math.floor(_image.height * (page_width_px / _image.width))))

        packer.add_rect(_image.width, _image.height, index)
        scaled_items.push(_image)

    # process
    packer.pack()

    # must pack all rectangles or something went wrong
    assert len(packer.rect_list()) == len(print_items)

    pages: list[Image.Image] = []
    for page_num, page_items in enumerate(packer):
        print("Items on page ", page_num, ": ")  # Bin id if it has one

        pages.append(Image.new("RGB", tuple(page_width_px, page_height_px), "white"))  # empty page, white to not print anything on empty space

        for item in page_items:
            _image = scaled_items[item.rid]
            pages[page_num].paste(_image, tuple(item.x, item.y))

    return pages
