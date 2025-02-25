def calculate_rectangle_area(length: int, width: int):
    return length * width


dimensions = [100, 20]

# area = calculate_rectangle_area(dimensions[0], dimensions[1])
# print(area)

area = calculate_rectangle_area(*dimensions)
print(area)
