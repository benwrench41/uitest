import sys
import os
from cx_Freeze import setup, Executable

files = ["programlogo.ico","activities_info.db","Bannerblue roundedlogo.png", "customer_info.db", "dives_record.db", "payment.db", "staff_info.db",  "tabs_info.db", "main.py", "ui_main.py","cil-arrow-bottom.png","cil-check-alt.png","cil-magnifying-glass.png","cil-menu.png","cil-size-grip.png","cil-user-follow.png","facebook logo.png", "facebook logo16.png","facebook logo32.png","facebook logo64.png","files.qrc","files_rc.py","icons8-euro-16.png","icons8-scuba-diving-16.png","icons8-to-do-16.png","ui_functions.py","ui_stlyes.py"]

target = Executable(
            script="main.py",
            base= win32GUI,
            icon="programlogo.ico",

)

setup(
    name = "Get Wet Divers",
    version =  " 1.0",
    decription = "Get Wet Divers booking system",
    author = "Ben",
    options = {"build_exe" : {"include_files" : files}},
    executables = [target]
)