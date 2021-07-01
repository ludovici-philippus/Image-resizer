import PySimpleGUI as sg
from PIL import Image
from PySimpleGUI.PySimpleGUI import Button   

image = ""

sg.theme("DarkBlack")

layout = [[sg.Text("Let's resize some images", justification="center")], 
         [sg.Input("Enter the image's path", enable_events=True, visible=False,key="image"), sg.FileBrowse(target="image", size=(18, 2))], 
         [sg.InputText("Width", key="width", size=(9, 5)), sg.InputText("Height", key="height", size=(9, 5))], 
         [sg.Button("Save!", key="save", size=(18, 2))]]

window = sg.Window("Image Resizer", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "image":
        image_path = window["image"].get()
        image = Image.open(image_path)
        width, height = image.size
        window["width"].update(width)
        window["height"].update(height)
    
    if event == "save":
        width = int(eval(window["width"].get()))
        height = int(eval(window["height"].get()))
        image.resize((width, height)).save(f"{image.filename}-{width}x{height}.{image.format}")
window.close()