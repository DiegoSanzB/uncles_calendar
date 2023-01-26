from PIL import Image, ImageDraw, ImageFont
import textwrap
import numpy as np

# CONSTANTS
NUMBER_TO_DAYS = np.array(['LUNES', 'MARTES', 'MIÉRCOLES', 'JUEVES',
                           'VIERNES', 'SÁBADO', 'DOMINGO'])
NUMBER_TO_MONTHS = np.array(['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 
                    'MAYO', 'JUNIO', 'JULIO', 'AGOSTO', 
                    'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE'])
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def generate_calendar(year):
    font = ImageFont.truetype("comic.ttf", 28)
    pass

def get_template(side, save = None):
    try:
        side_x, side_y = side
    except:
        side_x = side
        side_y = side

    width = side_x * 7 + 20
    height = side_y * 7 + 20

    template = Image.new('RGB', (width, height), WHITE)
    draw = ImageDraw.Draw(template)

    font_days = ImageFont.truetype("comic.ttf", side_x//7)

    for i in range(7):
        draw.rounded_rectangle([i*side_x + 10, (1*side_y)//2, (i+1)*side_x + 10, 1*side_y + 10], radius=side_x//4, outline=BLACK, fill=BLACK)
        draw.rectangle([i*side_x + 10, 3*side_y//4, (i+1)*side_x + 10, side_y + 10], outline=BLACK, fill=BLACK)
        draw.rectangle([i*side_x + 10, 0*side_y + 10, (i+1)*side_x + 10, 1*side_y + 10], outline=WHITE, fill=None, width=side_x//100)
        draw.text([i*side_x + 10 + side_x//2, 3*side_y/4 + 10/4], text=NUMBER_TO_DAYS[i], fill=WHITE, anchor='mm', font=font_days, spacing=0, align='center')

    for i in range(7):
        for j in range(1, 7):
            draw.rectangle([i*side_x + 10, j*side_y + 10, (i+1)*side_x + 10, (j + 1)*side_y + 10], outline=BLACK, fill=None, width=side_x//100)

    draw.rectangle([0*side_x + 10, 1*side_y + 10 - side_x//100, (6+1)*side_x + 10, (6 + 1)*side_y + 10], outline=BLACK, fill=None, width=side_x//100*2)

    if save is not None:
        try:
            template.save(save)
        except:
            print('save is not a valid path to save')

    return template

def enumerate_template(days, template, side, save):
    try:
        side_x, side_y = side
    except:
        side_x = side
        side_y = side

    try:
        first_day, past_day, total_days = days
    except:
        print('Wrong format for days')
        return -1

    draw = ImageDraw.Draw(template)
    font_number = ImageFont.truetype("comicbd.ttf", side_x//5)
    number = past_day - first_day
    
    j = 1
    for i in range(7):    
        number = number % past_day
        draw.text([i*side_x + 10 + side_x/2, j*side_y + 10 + side_y/2], text=str(number + 1), fill='red', anchor='mm', font=font_number, spacing=0, align='center')
        number += 1
    
    for j in range(2, 7):
        for i in range(7):    
            number = number % total_days
            draw.text([i*side_x + 10 + side_x/2, j*side_y + 10 + side_y/2], text=str(number + 1), fill='red', anchor='mm', font=font_number, spacing=0, align='center')
            number += 1

    if save is not None:
        try:
            template.save(save)
        except:
            print('save is not a valid path to save')

    return template

if __name__ == '__main__':
    side = (200, 120)
    template = get_template(side)
    enumerate_template((0, 31, 31), template, side, save='imgs/grid.png')