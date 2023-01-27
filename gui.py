import PySimpleGUI as sg
from calendars import generate_calendar

sg.theme('DarkAmber')   # Add a touch of color

# Generamos un layout

# layout de inicio
layout_inicio = [[sg.T('Feliz cumpleaños tío, espero que le guste este regalito...')]]


# layout de dedcación
layout_msg = [[sg.T('¡Ha sido un gusto compartir contigo, eres una gran persona y te apreciamos mucho!')],
                 [sg.T('¡Esperamos que cumplas muchos más!') ]]



# layout de generación de calendario
layout_clndr = [[sg.Text('Generando calendario...')]]
 

 # layout final
layout = [[ sg.Column(layout_inicio, key = '0'),sg.Column(layout_msg, key = '1', visible = False), sg.Column(layout_clndr, key = '2', visible = False)], 
          [ sg.Button('Siguiente', key = 'next') ]]





window = sg.Window('Entrenamiento', layout)

count = 0
while True:
  event, values = window.read()

  if event == sg.WIN_CLOSED:
    break
  if event == 'next':
    window[str(count)].update(visible = False)
    count += 1
    
    if count == 3:
      break

    window[str(count)].update(visible = True)

    if count == 2:
      window['next'].update('Salir')
      generate_calendar(2023)
    


window.close()


