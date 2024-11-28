def rectangle(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Длины сторон должны быть положительными!")
    perimeter = 2 * (length + width)
    area = length * width
    return perimeter, area 