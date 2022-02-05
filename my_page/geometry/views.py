from django.http import HttpResponse, HttpResponseNotFound


def get_rectangle_area(request, width: int, height: int):
    area = width * height
    return HttpResponse(f'The area of the {width}x{height} rectangle is {area}!')


def get_rectangle_area_error(request, width, height):
    return HttpResponseNotFound('Please, enter valid values!')


def get_square_area(request, width: int):
    area = width ** 2
    return HttpResponse(f'The area of the {width}x{width} square is {area}!')


def get_square_area_error(request, width):
    return HttpResponseNotFound('Please, enter valid value!')


def get_circle_area(request, radius: int):
    PI = 3.14
    area = 2 * PI * radius
    return HttpResponse(f'The area of the circle with {radius} radius is ~ {area}!')


def get_circle_area_error(request, radius):
    return HttpResponseNotFound('Please, enter valid value!')
