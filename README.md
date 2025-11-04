#  Trackr V2 — Desktop GUI for the Trackr CLI


<h1 align="center"> Trackr V2</h1>
<p align="center">
  A minimalist desktop GUI for your Go-based personal tracker.
  <br/>
  <a href="https://github.com/CBYeuler/trackr">V1</a> •
  <a href="https://github.com/CBYeuler/trackrV2">V2</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-2.0-blue.svg"/>
  <img src="https://img.shields.io/badge/python-3.12+-yellow.svg"/>
  <img src="https://img.shields.io/badge/go-1.23+-green.svg"/>
  <img src="https://img.shields.io/badge/license-MIT-lightgrey.svg"/>
</p>

---

###  About This Version

This repository serves as an **experimental prototype** to test how a GUI can integrate with the  
existing [Trackr CLI](https://github.com/CBYeuler/trackr) backend.  
The current version is functional but **not final** — it’s focused on validating the concept  
before moving to a professional UI stack in **Trackr V2.1**.

---

**TrackrV2** is a minimalist desktop interface built with **FreeSimpleGUI** (Python)  
that connects directly to the [Trackr CLI](https://github.com/CBYeuler/trackr).  
Together, they form a simple personal tracking system powered by Go + SQLite.

---

##  Overview

| Component | Language | Role |
|------------|-----------|------|
| [Trackr](https://github.com/CBYeuler/trackr) | Go | CLI backend that logs data to SQLite |
| TrackrV2 | Python | GUI frontend that wraps the CLI using FreeSimpleGUI |

The GUI executes the same commands you would type in the terminal, such as:

```bash
trackr add mood 7
trackr list
```

### Features:
- add Logs: Create Entries (category + value) instantly.
- Show Logs: List all your saved records
- Dual Mode:
        1- Go Run (Run directly from source)
        2- Executable (will add the exe soon!)
- Auto DB Migration: The Go backend automatically creates trackr.db
- Cross-Platform: Runs on Windows, macOS, and Linux (no CGO required)


### Installation:
```bash
# Core backend
git clone https://github.com/CBYeuler/trackr.git
cd trackr
go build -o trackr      # optional but recommended

# GUI frontend
git clone https://github.com/CBYeuler/trackrV2.git
cd trackrV2

```
##### Install Python dependencies:
```bash
pip install FreeSimpleGUI
```
##### Run the GUI:
```bash
python trackr_gui.py
```

##  Usage

1. **Open the GUI**
2. **Choose your Exec Mode:**
   -  **Executable:** Browse to the compiled `trackr` binary  
   -  **Go Run:** Point to your local Trackr source folder
3. **Enter a Category and Value**
4. **Click “Add Log”** to record it instantly
5. **Click “Show Logs”** to display your existing entries inside the GUI

All logs are stored locally in `tracker.db`, created automatically by the Go backend.

---

##  Tech Stack

###  Python 3.12+
- [**FreeSimpleGUI**](https://pypi.org/project/FreeSimpleGUI) — lightweight GUI framework  
- **subprocess** — used for executing Go backend commands

###  Go 1.23+
- [**modernc.org/sqlite**](https://pkg.go.dev/modernc.org/sqlite) — pure Go SQLite driver (no CGO required)  
- [**spf13/cobra**](https://github.com/spf13/cobra) — command-line structure and argument parsing



## File Struct:
```bash
trackrV2/
├── trackr_gui.py        # main GUI application
├── requirements.txt     # Python dependencies
└── README.md

trackr/ (backend)
├── cmd/
│   ├── add.go
│   ├── list.go
│   └── root.go
├── db/db.go
├── main.go
└── README.md

```

##  Future Plans

- [ ]  **Database Browser:** Add a scrollable table view for viewing and filtering logs  
- [ ]  **Export Tools:** Export logs to CSV and Markdown for easy sharing and backups  
- [ ]  **Summaries & Filtering:** Add daily summaries and category-based filters  
- [ ]  **TUI Version:** Create a terminal-based interface for power users  
- [ ]  **Automated Installer:** Provide a one-click download link that installs all required dependencies (Python, FreeSimpleGUI, etc.) automatically  
- [ ]  **Executable-Only Version:** Soon the GUI will run entirely as a standalone `.exe` — no manual setup or Python installation required  
- [ ]  **Trackr V2.1 Upgrade:** Migrate to a more professional frontend framework (such as **Qt**, **Electron**, or **Tauri**) with a modern design, native packaging, and smoother cross-platform support  
---

<p align="center">
  Built by <a href="https://github.com/CBYeuler">CBYeuler</a>  
  <br/>2025 • Open Source under the <a href="LICENSE">MIT License</a>
</p>
