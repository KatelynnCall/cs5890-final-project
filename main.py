import io
import os
import PySimpleGUI as sg
from PIL import Image
import xarray as xr
import matplotlib
import matplotlib.pyplot as plt
import scipy
import cartopy.crs as ccrs
import cartopy
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

matplotlib.use("TkAgg")

LOGAN_UTAH_LAT = 41
LOGAN_UTAH_LONG = -111


def plotMap(data, title):
    fig = plt.figure(figsize=(10, 10))
    ax = plt.axes(projection=ccrs.Robinson())
    ax.coastlines(resolution='10m')
    ax.gridlines()
    plt.title(title)
    plot = data.plot(cmap=plt.cm.coolwarm, transform=ccrs.PlateCarree(), cbar_kwargs={'shrink': 0.6})
    return plot


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(expand=False, fill='none')
    return figure_canvas_agg


def visGui(name):
    sg.theme('GreenMono')  # Add a touch of color
    data = xr.open_dataset('data/download.grib', engine='cfgrib')

    dataSets = {
        'Soil Temperature': data.stl1,
        'Soil Water Level': data.swvl1,
        'Vegetation': data.lai_lv
    }

    dates = {
        '1990': 0,
        '1995': 1,
        '2000': 2,
        '2005': 3,
        '2010': 4,
        '2015': 5,
        '2020': 6,
    }

    layout = [[sg.Text('Choose your datasets to compare')],
              [sg.Combo(['Soil Temperature', 'Soil Water Level', 'Vegetation'], default_value='Soil Temperature', key='-COMP1-'),
              sg.Combo(['1990', '1995', '2000', '2005', '2010', '2015', '2020'], default_value='1990', key='-DATE1-'),
               sg.Combo(['Soil Temperature', 'Soil Water Level', 'Vegetation'], default_value='Soil Temperature', key='-COMP2-'),
               sg.Combo(['1990', '1995', '2000', '2005', '2010', '2015', '2020'], default_value='1990', key='-DATE2-'),
                sg.Button('Compare')],
              [sg.Image(key="-IMAGE-")],
              [sg.Text('Select pre-rendered picture to view:'),
               sg.Combo(['Soil Temp And Vegetation', 'Soil Temp vs Vegetation'],
                        default_value='Soil Temp And Vegetation', key="-FILE-"), sg.Button('Load Image')],

              ]
    compare1Layout = [[sg.Canvas(key='-CANVAS1-', size=(300, 300), background_color='red')]]
    compare2Layout = [[sg.Canvas(key='-CANVAS2-', size=(300, 300), background_color='blue')]]

    # sg.Window(title="Visualization", layout=[[sg.Combo(['Dataset 1','Soil Temp'],default_value='Dataset 1'), sg.Combo(['High Vegitation', 'Dataset 4', 'Dataset 5']),sg.Button('ok')]], margins=(300, 150)).read()
    window = sg.Window('Visualization Comparer', layout, size=(1000, 1000))

    files = {
        'Soil Temp And Vegetation': 'images/SoilTempAndVegCombined.jpg',
        'Soil Temp vs Vegetation': 'images/soilTempAndVegitation.jpg'
    }

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        if event == "Load Image":
            filename = files[values["-FILE-"]]
            if os.path.exists(filename):
                image = Image.open(files[values["-FILE-"]])
                image.thumbnail((600, 600))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["-IMAGE-"].update(data=bio.getvalue())
        if event == "Compare":
            compare1 = sg.Window(values['-COMP1-'] + ' - ' + values['-DATE1-'], compare1Layout, size=(750, 750), finalize=True)
            compare2 = sg.Window(values['-COMP2-'] + ' - ' + values['-DATE2-'], compare2Layout, size=(750, 750), finalize=True)
            plot = plotMap(dataSets[values['-COMP1-']][dates[values['-DATE1-']]], values['-COMP1-'] + ' - ' + values['-DATE1-'])
            draw_figure(compare1['-CANVAS1-'].TKCanvas, plot.figure)
            plot2 = plotMap(dataSets[values['-COMP2-']][dates[values['-DATE1-']]], values['-COMP2-'] + ' - ' + values['-DATE2-'])
            draw_figure(compare2['-CANVAS2-'].TKCanvas, plot2.figure)

    window.close()
    compare1.close()
    compare2.close()


if __name__ == '__main__':
    visGui('PyCharm')
