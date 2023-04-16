import settings


# This function is used to set height percentage
def height_percentage(percentage):
    return (settings.HEIGHT / 100) * percentage


# This function is used to set width percentage
def width_percentage(percentage):
    return (settings.WIDTH / 100) * percentage


# To  calculates what percentage the second argument is of the first argument
def calculate_percentage(num1, num2):
    return (num2 / num1) * 100


