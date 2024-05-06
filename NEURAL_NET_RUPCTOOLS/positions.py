from label_list import LABELS
from position_list import *

POSITIONS = {
    "OK_GREY": {
        "index": LABELS.index("OK_GREY"),
        "position": OK_GREY_ICON_POSITION,
    },
    "MU_STANDBY": {
        "index": LABELS.index("MU_STANDBY"),
        "position": STATUS_MU_ICON_POSITION,
    },
    "MU_OFFLINE": {
        "index": LABELS.index("MU_OFFLINE"),
        "position": STATUS_MU_TEXT_POSITION,
    },
    "MU_EXPOSURE": {
        "index": LABELS.index("MU_EXPOSURE"),
        "position": STATUS_MU_ICON_POSITION,
    },
    "MU_BLOCKED": {
        "index": LABELS.index("MU_BLOCKED"),
        "position": STATUS_MU_ICON_POSITION,
    },
    "EXPOSURE_REQUIRED": {
        "index": LABELS.index("EXPOSURE_REQUIRED"),
        "position": EXPOSURE_REQUIRED_POSITION,
    },
    "MCU_CALIB_PASS": {
        "index": LABELS.index("MCU_CALIB_PASS"),
        "position": MCU_TEXT_PASS_POSITION,
    },
    "MCU_CALIBRATION": {
        "index": LABELS.index("MCU_CALIBRATION"),
        "position": MCU_TEXT_LONG_POSITION,
    },
    "MCU_NO_MESSAGE": {
        "index": LABELS.index("MCU_NO_MESSAGE"),
        "position": MCU_TEXT_LONG_POSITION,
    },
    "AWS_CALIB": {
        "index": LABELS.index("AWS_CALIB"),
        "position": AWS_CALIB_ICON_POSITION,
    },
    "AWS_FIELD": {
        "index": LABELS.index("AWS_FIELD"),
        "position": AWS_FIELD_ICON_POSITION,
    },
}
