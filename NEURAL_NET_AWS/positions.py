from label_list import LABELS
from all_position_list import STATUS_MU_ICON_POSITION, STATUS_MU_TEXT_POSITION

POSITIONS = {
    "MU_OFFLINE": {
        "index": LABELS.index("MU_OFFLINE"),
        "position": STATUS_MU_TEXT_POSITION,
    },
    "MU_BLOCKED": {
        "index": LABELS.index("MU_BLOCKED"),
        "position": STATUS_MU_ICON_POSITION,
    },
    "MU_STANDBY": {
        "index": LABELS.index("MU_STANDBY"),
        "position": STATUS_MU_ICON_POSITION,
    },
    "MU_EXPOSURE": {
        "index": LABELS.index("MU_EXPOSURE"),
        "position": STATUS_MU_ICON_POSITION,
    },
}
