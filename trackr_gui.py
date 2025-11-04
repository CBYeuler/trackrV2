import os, subprocess
from pathlib import Path

try:
    import FreeSimpleGUI as sg
except ImportError:
    import PySimpleGUI as sg

sg.theme("SystemDefault")

layout = [
    [sg.Text("trackr GUI", font=("Segoe UI", 16, "bold"))],
    [sg.Text("Exec Mode"), sg.Combo(["Go Run", "Executable"], default_value="Go Run", key="mode", readonly=True)],
    [sg.Text("Repo Folder"), sg.Input(str(Path.cwd()), key="repo", expand_x=True), sg.FolderBrowse()],
    [sg.Text("Trackr Exec"), sg.Input("trackr", key="exec", expand_x=True), sg.FileBrowse()],
    [sg.HSep()],
    [sg.Text("Category"), sg.Input("mood", key="cat", expand_x=True)],
    [sg.Text("Value"), sg.Input("", key="val", expand_x=True)],
    [sg.Button("Add Log"), sg.Button("Show Logs"), sg.Button("Exit")],
    [sg.Text("Output:")],
    [sg.Multiline(size=(80, 10), key="out", autoscroll=True, expand_x=True, expand_y=True)]
]

window = sg.Window("Trackr", layout, resizable = True, finalize = True)

def run_command(cmd, cwd=None):
    result = subprocess.run(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout, result.stderr, result.returncode
while True:
    event, values = window.read()

    if event in (sg.WINDOW_CLOSED, "Exit"):
        break

    if event == "Add Log":
        cat = (values.get("cat") or "").strip()
        val = (values.get("val") or "").strip()

        if not cat or not val:
            window["out"].print("Please fill in both Category and Value.\n")
            continue

        # Choose between 'go run' or compiled executable
        if values.get("mode") == "Go Run":
            cmd = ["go", "run", "main.go", "add", cat, val]
            cwd = values.get("repo") or None
        else:
            cmd = [values.get("exec") or "trackr", "add", cat, val]
            cwd = None

        # Print the command to output area
        window["out"].print("> " + " ".join(cmd))
        out, err, code = run_command(cmd, cwd)

        # Display stdout and stderr
        if out.strip():
            window["out"].print(out.strip())
        if err.strip():
            window["out"].print(err.strip())

        window["out"].print(f"Exit code: {code}\n")
        if event == "Show Logs":
            if values.get("mode") == "Go Run":
                cmd = ["go", "run", "main.go", "list"]
                cwd = values.get("repo") or None
            else:
                cmd = [values.get("exec") or "trackr", "list"]
                cwd = None

            window["out"].print("> " + " ".join(cmd))
            out, err, code = run_command(cmd, cwd)
            if out.strip():
                window["out"].print(out.strip())
            if err.strip():
                window["out"].print(err.strip())
            window["out"].print(f"Exit code: {code}\n")



window.close()