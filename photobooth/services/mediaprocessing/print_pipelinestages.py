import logging

from PIL import Image

logger = logging.getLogger(__name__)


class ImageRect:
    """Image rectangle wrapper. Dimensions in pixels"""

    def __init__(self, width: int, height: int, id: int):
        self.width = width
        self.height = height
        self.left = 0
        self.top = 0
        self.id = id


class Page:
    """Page wrapper. Dimensions in pixels"""

    def __init__(self, width: int, height: int, spacing: int = 0):
        self.width = width
        self.height = height
        self.min_x = 0  # lowest empty x index
        self.min_y = 0  # lowest empty y index
        self.spacing = spacing
        self.image_list: list[ImageRect] = []

    def fit_image(self, image: ImageRect):
        space_x = self.width - self.min_x
        space_y = self.height - self.min_y
        fits_x = space_x >= image.width
        fits_y = space_y >= image.height
        if fits_x and fits_y:
            image.left = self.min_x
            image.top = self.min_y

            self.image_list.append(image)

            # update space left
            if image.width == self.width:
                self.min_y += image.height + self.spacing
            if image.height == self.height:
                self.min_x += image.width + self.spacing

            return True
        else:
            return False


class AutoLayoutCreator:
    """Auto-generate print layout for images.

    Note: Images are assumed to span the complete width or height of the page!
    """

    def __init__(self, page_width, page_height, spacing):
        self.page_width = page_width
        self.page_height = page_height
        self.spacing = spacing
        self.page_list: list[Page] = []
        self.image_list: list[ImageRect] = []

    def add_image(self, image_width, image_height, image_id):
        """Add image to the internal list to pack into a layout later."""
        assert (
            ((image_width == self.page_width) or (image_height == self.page_height))
            and (image_width <= self.page_width)
            and (image_height <= self.page_height)
        )

        self.image_list.append(ImageRect(image_width, image_height, image_id))

    def create_layout(self):
        """Try to find a page into which the image can be fit. If there is none, create a new page."""
        # iterate images
        for image in self.image_list:
            image_ok = False
            for page in self.page_list:
                if page.fit_image(image):
                    image_ok = True
                    break

            if not image_ok:
                self.page_list.append(Page(self.page_width, self.page_height, self.spacing))
                assert self.page_list[-1].fit_image(image)

        return self.page_list


def merge_print_items_stage(
    print_items: list[Image.Image], page_width_mm: float, page_height_mm: float, item_spacing_mm: float = 2, dpi: int = 300
) -> list[Image.Image]:
    """Merge list of images into a page layout

    Processes the list of images to print as follows:
        1. Rotate the image to fit the print mediums aspect ratio
        2. Resize the image to fill the print mediums complete height or width
        3. Automatically distribute these images amongst however many pages needed
        4. Returns a list of images (one per page) to print

    Arguments:
        print_items: list of the images to print
        page_width_mm: width of the print medium in millimeters
        page_height_mm: height of the print medium in millimeters
        item_spacing_mm: spacing between items in the automatically created layout
        dpi: dots per inch for printing

    Returns:
        list of images (one per page) to print
    """

    # fit images into a given page size
    # if necessary, return multiple pages to print

    # setup page canvas
    page_width_px = int((page_width_mm * dpi) / 25.4)
    page_height_px = int((page_height_mm * dpi) / 25.4)
    item_spacing_px = int((item_spacing_mm * dpi) / 25.4)
    page_orientation_landscape = page_width_mm > page_height_mm

    auto_layout = AutoLayoutCreator(page_width_px, page_height_px, item_spacing_px)

    scaled_items: list[Image.Image] = []
    for index, item in enumerate(print_items):
        _image = item

        # resize items to fill page optimally.
        item_orientation_landscape: bool = _image.width > _image.height

        if item_orientation_landscape != page_orientation_landscape:
            _image = _image.rotate(90.0, expand=True)

        if page_width_px / _image.width > page_height_px / _image.height:
            # scale image to fill complete height, but possibly not complete width
            newWidth = int(round(_image.width * (page_height_px / _image.height)))
            _image = _image.resize((newWidth, page_height_px))
        else:
            # scale image to fill complete width, but possibly not complete height
            newHeight = int(round(_image.height * (page_width_px / _image.width)))
            _image = _image.resize((page_width_px, newHeight))

        logger.debug(f"Adding pre-processed image with {_image.width}x{_image.height}")
        auto_layout.add_image(_image.width, _image.height, index)
        scaled_items.append(_image)

    # Get the layout per page
    page_layouts = auto_layout.create_layout()

    pages: list[Image.Image] = []
    for page_num, page_layout in enumerate(page_layouts):
        logger.info(f"Items on page {page_num} ({page_layout.width}x{page_layout.height}): ")  # Bin id if it has one

        pages.append(Image.new("RGB", (page_width_px, page_height_px), "white"))  # empty page, white to not print anything on empty space

        for page_image in page_layout.image_list:
            _image = scaled_items[page_image.id]
            pages[page_num].paste(_image, (page_image.left, page_image.top))
            logger.info(f"{page_image.id}: [{_image.width}x{_image.height}] at [{page_image.left},{page_image.top}]")

    return pages
