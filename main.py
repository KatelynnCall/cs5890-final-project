import io
import os
import PySimpleGUI as sg
from PIL import Image


def visGui(name):
    sg.theme('DarkAmber')  # Add a touch of color
    layout = [[sg.Text('Choose your datasets to compare')],
              [sg.Combo(['Dataset 1','Soil Temp'], default_value='Dataset 1')], [sg.Combo(['High Vegitation', 'Dataset 4', 'Dataset 5'], default_value='Dataset 4')],
              [sg.Button('Compare')],
              [sg.Image(key="-IMAGE-")],
              [sg.Combo(['Soil Temp And Vegetation', 'Soil Temp vs Vegetation'], default_value='Soil Temp And Vegetation', key="-FILE-"), sg.Button('Load Image')],
              ]

    # sg.Window(title="Visualization", layout=[[sg.Combo(['Dataset 1','Soil Temp'],default_value='Dataset 1'), sg.Combo(['High Vegitation', 'Dataset 4', 'Dataset 5']),sg.Button('ok')]], margins=(300, 150)).read()
    window = sg.Window('Visualization Comparer', layout, size=(500,500))

    while True:
        files = {
            'Soil Temp And Vegetation': 'images/SoilTempAndVegCombined.jpg',
            'Soil Temp vs Vegetation': 'images/soilTempAndVegitation.jpg'
        }

        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        if event == "Load Image":
            filename = files[values["-FILE-"]]
            if os.path.exists(filename):
                image = Image.open(files[values["-FILE-"]])
                image.thumbnail((400, 400))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["-IMAGE-"].update(data=bio.getvalue())
        print('You entered', values[0], 'and', values[1])

    window.close()

if __name__ == '__main__':
    visGui('PyCharm')


