import FreeSimpleGUI as sg
from modules import zip_extractor as ze

sg.theme("Black")

label1 = sg.Text("Select archive:")
input1 = sg.Input()
select_button1 = sg.FileBrowse("Select", key="archive")

label2 = sg.Text("Select folder:")
input2 = sg.Input()
select_button2 = sg.FolderBrowse("Select", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")

layout = [
    [label1, input1, select_button1],
    [label2, input2, select_button2],
    [extract_button, output_label]
]

window = sg.Window("Archive Extractor", layout=layout)

while True:
    event, values = window.read()

    print(event, values)
    archivepath = values["archive"]
    dest_dir = values["folder"]
    ze.extract_archive(archivepath, dest_dir)
    window["output"].update(value="Extraction complete.")

    match event:
        case sg.WIN_CLOSED:
            break

window.close()
