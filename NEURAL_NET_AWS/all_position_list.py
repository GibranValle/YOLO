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


# POSITION IN PIXELS....
# X0, Y0, X1, Y1
MU_ICON = 1095, 1521, 1157, 1575  # BOTTOM RIGHT CORNER
MU_TEXT = 26, 1560, 260, 1594  # BOTTOM LEFT CORNER

# YOLO POSITIONS
STATUS_MU_ICON_POSITION = calc_relative_position_2M(MU_ICON)
STATUS_MU_TEXT_POSITION = calc_relative_position_2M(MU_TEXT)

print(STATUS_MU_ICON_POSITION)
print(STATUS_MU_TEXT_POSITION)
