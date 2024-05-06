def calc_relative_position_2M(pixel_position: tuple[int, int, int, int]):
    # x0, y0, x1, y1
    img_resolution = 1200, 1600
    width = pixel_position[2] - pixel_position[0]
    height = pixel_position[3] - pixel_position[1]
    x_center = pixel_position[0] + width / 2
    y_center = pixel_position[1] + height / 2
    # x_center, y_center, w, h
    pixel_format = (x_center, y_center, width, height)
    relative_position = [
        f"{pixel_format[0] / img_resolution[0]}",
        f"{pixel_format[1] / img_resolution[1]}",
        f"{pixel_format[2] / img_resolution[0]}",
        f"{pixel_format[3] / img_resolution[1]}",
    ]
    return (" ").join(relative_position)


# x0, y0, x1, y1
# POSITION IN PIXELS....
_MU_ICON = 1095, 1521, 1157, 1575  # BOTTOM RIGHT CORNER
_MU_TEXT = 26, 1560, 260, 1594  # BOTTOM LEFT CORNER
_EXPOSURE_REQUIRED_FRAME = 398, 668, 802, 931
_ERROR_MESSAGE_FRAME = 13, 1398, 598, 1513
_OK_GREY_ICON = 490, 1467, 598, 1513
# _OK_GREEN_ICON = 538, 929, 661, 1003
# _ERROR_CONSOLE_FRAME = 87, 551, 1108, 1048
_MCU_TEXT_PASS = 26, 1516, 283, 1559
_MCU_TEXT_LONG = 26, 1516, 411, 1559
_AWS_CALIB_ICON = 1134, 1388, 1184, 1434
_AWS_FIELD_ICON = 975, 1285, 1185, 1340

# YOLO POSITIONS
STATUS_MU_ICON_POSITION = calc_relative_position_2M(_MU_ICON)
STATUS_MU_TEXT_POSITION = calc_relative_position_2M(_MU_TEXT)
EXPOSURE_REQUIRED_POSITION = calc_relative_position_2M(_EXPOSURE_REQUIRED_FRAME)
ERROR_MESSAGE_POSITION = calc_relative_position_2M(_ERROR_MESSAGE_FRAME)
OK_GREY_ICON_POSITION = calc_relative_position_2M(_OK_GREY_ICON)
MCU_TEXT_PASS_POSITION = calc_relative_position_2M(_MCU_TEXT_PASS)
MCU_TEXT_LONG_POSITION = calc_relative_position_2M(_MCU_TEXT_LONG)
AWS_CALIB_ICON_POSITION = calc_relative_position_2M(_AWS_CALIB_ICON)
AWS_FIELD_ICON_POSITION = calc_relative_position_2M(_AWS_FIELD_ICON)


print(STATUS_MU_ICON_POSITION)
print(STATUS_MU_TEXT_POSITION)
print(EXPOSURE_REQUIRED_POSITION)
print(ERROR_MESSAGE_POSITION)
print(OK_GREY_ICON_POSITION)
