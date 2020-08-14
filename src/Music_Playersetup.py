from cx_Freeze import *
includefiles = ["images.ico",'play-button.png','resume.png','unmute.png','mute.png','searching.png','volume-down.png','volume-up.png','stop.png','pause-button.png']
exclude = []
packages = []
base= None
if sys.platform == "win32":
    base = "win32GUI"

shortcut_table = [
    ("DesktopShortcut",  # Shortcut
     "DesktopFolder",  # Directory_
     "Music_Player",  # Name
     "TARGETDIR",  # Component_
     "[TARGETDIR]\Music_Player.exe", # Target
     None,  # Arguments
     None,  # Description
     None,  # Hotkey
     None,  # Icon
     None,  # IconIndex
     None,  # ShowCmd
     "TARGETDIR",  # WkDir
     )
]

msi_data = {"Shortcut":shortcut_table}
bdist_msi_options = {'data': msi_data}
setup(
    version="1.1",
    description="Music_Player Developed by Anant Prakash",
    author="Anant Prakash",
    name="Music_Player",
    options={'build_exe': {'include_files': includefiles}, "bdist_msi": bdist_msi_options,},
    executables=[
        Executable(
            script="Music_Player.py",
            base=base,
            icon='images.ico',
        )
    ]

)
