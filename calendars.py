from PIL import Image, ImageDraw, ImageFont
from dates import first_day_year, get_deltas_of_months, weekday_delta
import textwrap
import numpy as np

# CONSTANTS
NUMBER_TO_DAYS = np.array(['LUNES', 'MARTES', 'MIERCOLES', 'JUEVES',
                           'VIERNES', 'SABADO', 'DOMINGO'])
NUMBER_TO_MONTHS = np.array(['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 
                    'MAYO', 'JUNIO', 'JULIO', 'AGOSTO', 
                    'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE'])
WHITE = 255, 255, 255
BLACK = 0, 0, 0
YELLOW = 230, 208, 44

def generate_calendar(year):
    month_deltas = get_deltas_of_months(year)
    first_day = first_day_year(year)
    past_day = 31
    
    side_x = 200
    side_y = 120
    side = side_x, side_y

    template = get_template(side)
    font_month = ImageFont.truetype("fonts/Circus.ttf", 128)

    img_array = []

    for i in range(12):
        total_days = 30 + month_deltas[i]
        days = (first_day, past_day, total_days)
        enumerate_i = enumerate_template(days, template.copy(), side)

        draw = ImageDraw.Draw(enumerate_i)

        first_day = weekday_delta(first_day, total_days)
        past_day = total_days

        draw.text([3*side_x + 10 + side_x/2, 10 + 3*side_y//4], text=NUMBER_TO_MONTHS[i], fill='purple', anchor='mm', font=font_month, spacing=0, align='center')

        width = side_x * 7 + 20
        height = side_y * 8 + 20
        img = Image.new('RGB', (width, height + 2*width//3 + 50), WHITE)
        photo = Image.open(f'imgs/{i}.png')
        
        photo = photo.resize((width-20, 2*(width-20)//3))
        
        draw_img = ImageDraw.Draw(img)
        

        Image.Image.paste(img, enumerate_i, (0, 2*(width-20)//3 + 25))
        
        Image.Image.paste(img, photo, (10, 25))

        draw_img.rectangle([10, 25, 10 + width-20, 25 + 2*(width-20)//3], outline=BLACK, fill=None, width=side_x//30)
        
        img.save(f'calendar_out/{i}.png')
        img_array.append(img)

    img_array[0].save('calendar_out/calendar.pdf', save_all=True, append_images=img_array[1:])

    return
    

def get_template(side, save = None):
    try:
        side_x, side_y = side
    except:
        side_x = side
        side_y = side

    width = side_x * 7 + 20
    height = side_y * 8 + 20

    template = Image.new('RGB', (width, height), WHITE)
    draw = ImageDraw.Draw(template)

    font_days = ImageFont.truetype("fonts/AURORA-PRO.otf", side_x//6)

    for i in range(7):
        draw.rounded_rectangle([i*side_x + 10, (1*side_y)//2 + side_y, (i+1)*side_x + 10, 2*side_y + 10], radius=side_x//4, outline=BLACK, fill=BLACK)
        draw.rectangle([i*side_x + 10, 3*side_y//4 + side_y, (i+1)*side_x + 10, 2*side_y + 10], outline=BLACK, fill=BLACK)
        draw.rectangle([i*side_x + 10, 0*side_y + 10 + side_y, (i+1)*side_x + 10, 2*side_y + 10], outline=WHITE, fill=None, width=side_x//100)
        draw.text([i*side_x + 10 + side_x//2, 3*side_y/4 + 10/4 + side_y], text=NUMBER_TO_DAYS[i], fill=YELLOW, anchor='mm', font=font_days, spacing=0, align='center')

    for i in range(7):
        for j in range(1, 7):
            draw.rectangle([i*side_x + 10, (j+1)*side_y + 10, (i+1)*side_x + 10, (j+2)*side_y + 10], outline=BLACK, fill=None, width=side_x//100)

    draw.rectangle([0*side_x + 10, 2*side_y + 10 - side_x//100, (6+1)*side_x + 10, (6+2)*side_y + 10], outline=BLACK, fill=None, width=side_x//100*2)

    if save is not None:
        try:
            template.save(save)
        except:
            print('save is not a valid path to save')

    return template

def enumerate_template(days, template, side, save=None):
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
    font_number = ImageFont.truetype("fonts/DalekPinpointBold.ttf", side_x//3)
    number = past_day - first_day
    
    color = 240, 132, 132
    j = 1
    for i in range(7):
        if number >= past_day:
            number = number % past_day
            color = 181, 38, 38
        draw.text([i*side_x + 10 + side_x/2, (j+1)*side_y + 10 + side_y/2], text=str(number + 1), fill=color, anchor='mm', font=font_number, spacing=0, align='center')
        number += 1
    
    for j in range(2, 7):
        for i in range(7):    
            if number >= total_days:
                number = number % total_days
                color = 240, 132, 132
            draw.text([i*side_x + 10 + side_x/2, (j+1)*side_y + 10 + side_y/2], text=str(number + 1), fill=color, anchor='mm', font=font_number, spacing=0, align='center')
            number += 1

    if save is not None:
        try:
            template.save(save)
        except:
            print('save is not a valid path to save')

    return template

if __name__ == '__main__':
    #side = (1000, 600)
    #template = get_template(side, save = 'imgs/template.png')
    #enumerate_template((5, 31, 28), template, side, save='imgs/grid.png')

    generate_calendar(2023)