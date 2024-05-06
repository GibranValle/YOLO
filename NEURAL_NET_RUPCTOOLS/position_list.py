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
_RUPCTOOLS_FRAME = 119, 488, 1080, 1109
_MUTL_FRAME = 172, 172, 820, 652
# YOLO POSITIONS
RUPCTOOLS_FRAME_POSITION = calc_relative_position_2M(_RUPCTOOLS_FRAME)


print(RUPCTOOLS_FRAME_POSITION)
