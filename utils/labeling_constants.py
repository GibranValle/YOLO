LABELS = [
    "MU_OFFLINE",  # 0
    "MU_RESET",  # 1
    "MU_BLOCKED",  # 2
    "MU_STANDBY",  # 3
    "MU_EXPOSURE",  # 4
    "MCU_OFFLINE",  # 5
    "MCU_NO_MESSAGE",  # 6
    "MCU_CALIBRATING",  # 7
    "MCU_CALIB_OK",  # 8
    "EXPOSURE_REQUIRED",  # 9
    "ERROR_MESSAGE",  # 10
    "OK_BUTTON",  # 11
    "OK_GREEN",  # 12
    "RUPCTOOLS",  # 13
    "MCU_MUTL",  # 14
    "MU_MUTL",  # 15
    "GEN",  # 16
]

STATUS_MU_ICON_POSITION = "0.139330 0.985450 0.220459 0.023810"
STATUS_MU_TEXT_POSITION = "0.139991 0.984623 0.221561 0.023148"
STATUS_MCU_POSITION = "0.125461 0.960979 0.223986 0.027778"
EXPOSURE_REQ_POSITION = "0.497354 0.500000 0.347443 0.171958"
ERROR_MSG_POSITION = "0.283867 0.895692 0.425800 0.050391"
OK_BUTTON_POSITION = "0.451835 0.931910 0.088183 0.024565"
OK_GREEN_POSITION = "0.425926 0.598545 0.165785 0.085979"
RUPCTOOLS_POSITION = "0.5008333333333334 0.5009375 0.8066666666666666 0.390625"
MCU_MUTL_POSITION = "0.41291666666666665 0.258125 0.5425 0.30625"
MCU_MUTL_2_POSITION = "0.50625 0.329375 0.5425 0.30625"
MCU_MUTL_3_POSITION = "0.32375 0.190625 0.5425 0.30625"

POSITIONS = {
    "MU_OFFLINE": {
        "index": LABELS.index("MU_OFFLINE"),
        "position": STATUS_MU_ICON_POSITION,
    },
    "MU_OFFLINE_TEXT": {
        "index": LABELS.index("MU_OFFLINE"),
        "position": STATUS_MU_TEXT_POSITION,
    },
    "MU_RESET": {
        "index": LABELS.index("MU_RESET"),
        "position": STATUS_MU_TEXT_POSITION,
    },
    "MU_BLOCKED": {
        "index": LABELS.index("MU_BLOCKED"),
        "position": STATUS_MU_ICON_POSITION,
    },
    "MU_BLOCKED_TEXT": {
        "index": LABELS.index("MU_BLOCKED"),
        "position": STATUS_MU_TEXT_POSITION,
    },
    "MU_STANDBY": {
        "index": LABELS.index("MU_STANDBY"),
        "position": STATUS_MU_ICON_POSITION,
    },
    "MU_STANDBY_TEXT": {
        "index": LABELS.index("MU_STANDBY"),
        "position": STATUS_MU_TEXT_POSITION,
    },
    "MU_EXPOSURE": {
        "index": LABELS.index("MU_EXPOSURE"),
        "position": STATUS_MU_ICON_POSITION,
    },
    "MU_EXPOSURE_TEXT": {
        "index": LABELS.index("MU_EXPOSURE"),
        "position": STATUS_MU_TEXT_POSITION,
    },
    "MCU_OFFLINE": {
        "index": LABELS.index("MCU_OFFLINE"),
        "position": STATUS_MCU_POSITION,
    },
    "MCU_NO_MESSAGE": {
        "index": LABELS.index("MCU_NO_MESSAGE"),
        "position": STATUS_MCU_POSITION,
    },
    "MCU_CALIBRATING": {
        "index": LABELS.index("MCU_CALIBRATING"),
        "position": STATUS_MCU_POSITION,
    },
    "MCU_CALIB_OK": {
        "index": LABELS.index("MCU_CALIB_OK"),
        "position": STATUS_MCU_POSITION,
    },
    "ERROR_MESSAGE": {
        "index": LABELS.index("ERROR_MESSAGE"),
        "position": ERROR_MSG_POSITION,
    },
    "EXPOSURE_REQUIRED": {
        "index": LABELS.index("EXPOSURE_REQUIRED"),
        "position": EXPOSURE_REQ_POSITION,
    },
    "OK_BUTTON": {
        "index": LABELS.index("OK_BUTTON"),
        "position": OK_BUTTON_POSITION,
    },
    "OK_GREEN": {
        "index": LABELS.index("OK_GREEN"),
        "position": OK_GREEN_POSITION,
    },
    "MCU_MUTL": {
        "index": LABELS.index("MCU_MUTL"),
        "position": MCU_MUTL_POSITION,
    },
    "MCU_MUTL_2": {
        "index": LABELS.index("MCU_MUTL"),
        "position": MCU_MUTL_2_POSITION,
    },
    "MCU_MUTL_3": {
        "index": LABELS.index("MCU_MUTL"),
        "position": MCU_MUTL_3_POSITION,
    },
}
