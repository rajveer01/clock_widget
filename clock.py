import PySimpleGUI as Sg
from datetime import datetime as dt

Sg.theme('Dark Blue 3')

layout = [
    [Sg.Text(dt.now().strftime('%I:%M %p'), background_color='#000001',
             text_color='#000000', font='Calibri 30 bold', key='_TIME_')]
]

window = Sg.Window('', layout, no_titlebar=True, grab_anywhere=True,
                   background_color='#000001', keep_on_top=True, transparent_color='#000001',
                   alpha_channel=0.9, location=(0, 000), finalize=True)

window.bind('<Enter>', '+MOUSE OVER+')

pos = True
loc = [(1100, 0), (0, 000)]


def new_position():
    global pos
    pos = not pos
    return loc[int(pos)]


while True:
    event, values = window.read(timeout=100,)
    print(event)
    window.Element('_TIME_').Update(value=dt.now().strftime('%I:%M %p'))
    if event == '+MOUSE OVER+':
        window.move(*new_position())
