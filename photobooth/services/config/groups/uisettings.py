"""
AppConfig class providing central config

"""


from pydantic import BaseModel, ConfigDict, Field

from .mediaprocessing import EnumPilgramFilter


class GroupUiSettings(BaseModel):
    """Personalize the booth's UI."""

    model_config = ConfigDict(title="Personalize the User Interface")

    show_takepic_on_frontpage: bool = Field(
        default=True,
        description="Show link to capture single picture on frontpage.",
    )
    show_takecollage_on_frontpage: bool = Field(
        default=True,
        description="Show link to capture collage on frontpage.",
    )
    show_takeanimation_on_frontpage: bool = Field(
        default=True,
        description="Show link to capture animated GIF on frontpage.",
    )
    show_gallery_on_frontpage: bool = Field(
        default=True,
        description="Show link to gallery on frontpage.",
    )
    show_admin_on_frontpage: bool = Field(
        default=True,
        description="Show link to admin center, usually only during setup.",
    )

    livestream_mirror_effect: bool = Field(
        default=True,
        description="Flip livestream horizontally to create a mirror effect feeling more natural to users.",
    )
    FRONTPAGE_TEXT: str = Field(
        default='<div class="fixed-center text-h2 text-weight-bold text-center text-white" style="text-shadow: 4px 4px 4px #666;">Hey!<br>Let\'s take some pictures! <br>📷💕</div>',
        description="Text/HTML displayed on frontpage.",
    )

    TAKEPIC_MSG_TIME: float = Field(
        default=0.5,
        description="Offset in seconds, the smile-icon shall be shown.",
    )
    AUTOCLOSE_NEW_ITEM_ARRIVED: int = Field(
        default=30,
        description="Timeout in seconds a new item popup closes automatically.",
    )

    GALLERY_EMPTY_MSG: str = Field(
        default='<div class="fixed-center text-h2 text-weight-bold text-center text-white" style="text-shadow: 4px 4px 4px #666;">Empty, Zero, Nada! 🤷‍♂️<br>Let\'s take some pictures! <br>📷💕</div>',
        description="Message displayed if gallery is empty.",
    )
    gallery_show_qrcode: bool = Field(
        default=True,
        description="Show QR code in gallery. If shareservice is enabled the URL is automatically generated, if not go to share config and provide URL.",
    )
    gallery_show_filter: bool = Field(
        default=True,
        description="Show instagramlike filter (pilgram2).",
    )
    gallery_filter_userselectable: list[EnumPilgramFilter] = Field(
        title="Pic1 Filter Userselectable",
        default=[e.value for e in EnumPilgramFilter],
        description="Filter the user may choose from in the gallery. 'original' applies no filter.",
    )
    gallery_show_download: bool = Field(
        default=True,
        description="Show download button in gallery.",
    )
    gallery_show_delete: bool = Field(
        default=True,
        description="Show delete button for items in gallery.",
    )
    gallery_show_print: bool = Field(
        default=True,
        description="Show print button for items in gallery.",
    )

    TAKEPIC_MSG_TEXT: str = Field(default="😃", description="Message to display at the end of the capture countdown.")

    TAKEPIC_BUTTON_TEXT: str = Field(
        default="Take a photo",
        description="Text on the 'take a photo' button.",
    )

    TAKECOLLAGE_BUTTON_TEXT: str = Field(
        default="Create a collage",
        description="Text on the 'create a collage' button.",
    )

    TAKEANIMATION_BUTTON_TEXT: str = Field(
        default="Create an animation",
        description="Text on the 'create an animation' button.",
    )

    TAKEVIDEO_BUTTON_TEXT: str = Field(
        default="Create a video",
        description="Text on the 'create a video' button.",
    )

    GALLERY_BUTTON_TEXT: str = Field(
        default="Gallery",
        description="Text on the 'gallery' button.",
    )

    PRINT_BUTTON_TEXT: str = Field(
        default="Print",
        description="Text on the 'print' button.",
    )

    DELETE_BUTTON_TEXT: str = Field(
        default="Delete",
        description="Text on the 'delete' button.",
    )

    FILTER_BUTTON_TEXT: str = Field(
        default="Filter",
        description="Text on the 'filter' button.",
    )

    DOWNLOAD_BUTTON_TEXT: str = Field(
        default="Download",
        description="Text on the 'download' button in the gallery.",
    )

    BACK_BUTTON_TEXT: str = Field(
        default="Start",
        description="Text on the button to get back the the main page.",
    )

    PRIMARY_COLOR: str = Field(
        default="#123456",
        description="Primary color (e.g. buttons, title bar). Use hex encoding as in CSS.",
    )

    SECONDARY_COLOR: str = Field(
        default="#123456",
        description="Secondary color (admin interface, accents). Use hex encoding as in CSS.",
    )
