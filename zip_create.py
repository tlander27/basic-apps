import FreeSimpleGUI as sg
from modules import zip_creator as zc

label1 = sg.Text("Select files:", background_color="black")
input1 = sg.Input()
source_button = sg.FilesBrowse("Source", key="files")

label2 = sg.Text("Select folder:", background_color="black")
input2 = sg.Input()
dest_button = sg.FolderBrowse("Destination", key="folder")

compress_button = sg.Button("Compress")
output_label = sg.Text("", key="output",
                       text_color="green",
                       background_color="black")

layout = [
    [label1, input1, source_button],
    [label2, input2, dest_button],
    [compress_button, output_label]
]

window = sg.Window("File Compressor", layout, background_color="black")

while True:
    event, values = window.read()
    print(event, values)

    try:
        filepaths = values["files"].split(";")
    except AttributeError:
        continue

    folder = values["folder"]
    zc.make_archive(filepaths, folder)
    window["output"].update(value="Compression complete.")

    match event:
        case sg.WIN_CLOSED:
            break

window.close()