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


mu_text = 20, 1522, 321, 1555
# print(calc_relative_position_2M(mu_text))

rupctools = 117, 489, 1085, 1114
# print(calc_relative_position_2M(rupctools))

mcu_mutl = 170, 168, 821, 658
print(calc_relative_position_2M(mcu_mutl))
mcu_mutl_with = mcu_mutl[2] - mcu_mutl[0]
mcu_mutl_height = mcu_mutl[3] - mcu_mutl[1]

new_2 = 282, 282
mcu_mutl_2 = new_2[0], new_2[1], new_2[0] + mcu_mutl_with, new_2[1] + mcu_mutl_height
print(calc_relative_position_2M(mcu_mutl_2))

new_3 = 63, 60
mcu_mutl_3 = new_3[0], new_3[1], new_3[0] + mcu_mutl_with, new_3[1] + mcu_mutl_height
print(calc_relative_position_2M(mcu_mutl_3))
