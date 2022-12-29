from typing import Final

from ..schema.nexusphp import AttendanceHR
from ..utils.value_handler import size


class MainClass(AttendanceHR):
    URL: Final = 'https://gamegamept.cn/'
    USER_CLASSES: Final = {
        'downloaded': [size(750, 'GiB'), size(3, 'TiB')],
        'share_ratio': [3.05, 4.55],
        'days': [280, 700]
    }
