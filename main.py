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
    fig = plt.figure(figsize=(10,10))
    ax = plt.axes(projection=ccrs.Robinson())
    ax.coastlines(resolution='10m')
    ax.gridlines()
    plt.title(title)
    plot = data.plot(cmap=plt.cm.coolwarm, transform=ccrs.PlateCarree(), cbar_kwargs={'shrink':0.6})
    return plot

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def visGui(name):
    sg.theme('DarkAmber')  # Add a touch of color
    layout = [[sg.Text('Choose your datasets to compare')],
              [sg.Combo(['Dataset 1','Soil Temp'], default_value='Dataset 1'), sg.Combo(['High Vegitation', 'Dataset 4', 'Dataset 5'], default_value='Dataset 4'),
              sg.Button('Compare')],
              [sg.Image(key="-IMAGE-")],
              [sg.Text('Select pre-rendered picture to view:'), sg.Combo(['Soil Temp And Vegetation', 'Soil Temp vs Vegetation'], default_value='Soil Temp And Vegetation', key="-FILE-"), sg.Button('Load Image')],
              [sg.Canvas(key='-CANVAS-')]
              ]

    # sg.Window(title="Visualization", layout=[[sg.Combo(['Dataset 1','Soil Temp'],default_value='Dataset 1'), sg.Combo(['High Vegitation', 'Dataset 4', 'Dataset 5']),sg.Button('ok')]], margins=(300, 150)).read()
    window = sg.Window('Visualization Comparer', layout, size=(600,500))

    data = xr.open_dataset('data/download.grib', engine='cfgrib')
    stl1 = data.stl1

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
                image.thumbnail((600, 600))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["-IMAGE-"].update(data=bio.getvalue())
        if event == "Compare":
            plot = plotMap(stl1[0], 'test')
            draw_figure(window['-CANVAS-'].TKCanvas, plot.figure)
        print('You entered', values[0], 'and', values[1])

    window.close()

if __name__ == '__main__':
    visGui('PyCharm')


