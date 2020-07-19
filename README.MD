
[![](https://img.shields.io/badge/Twitter--blue.svg?maxAge=2592000)](https://twitter.com/zadow28) ![Python version](https://img.shields.io/badge/python-2.7-brightgreen.svg?maxAge=2592000) ![PyQ5t](https://img.shields.io/badge/PyQt5-5.6-orange.svg) [![](https://img.shields.io/badge/Donate-Paypal-blue.svg?maxAge=2592000)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=8KXM6W2JVRUWL) [![](https://img.shields.io/badge/Latest-Release-red.svg?maxAge=2592000)](https://github.com/techbliss/Windows_Screenrecorder/releases/tag/releases)

# **Windows screen recorder**

Windows screen recorder is a simple systray and GUI screen recorder for windows. It is coded with Python 2.7 and PyQt5.

Installer does not depend on either python or Qt installations.


![1475268530_device-camera-recorder-video-outline-stroke](https://cloud.githubusercontent.com/assets/3592375/18997872/96fd543a-8736-11e6-8487-0bdc51673f49.png)


# **Screens**

**Countdown**

![countdown](https://cloud.githubusercontent.com/assets/3592375/18998349/a529e210-8738-11e6-9fd0-a9c6264fc3d7.png)

**System tray**

![systray](https://cloud.githubusercontent.com/assets/3592375/18998381/cbffc7ba-8738-11e6-973f-51f3f6dd6b2d.png)

**Minimalistic Gui**

![gui](https://cloud.githubusercontent.com/assets/3592375/19000314/3bd09b42-8742-11e6-9bb3-01759b567c42.png)

# **Usage**

Installer will show in windows start menu, but you can run directly with the python code also.
It will show a Record icon in system tray.

There a different features in the icon menu, simply left click and right click to see the different options.
As now there a two ways of recordings
Record wia left click menu or using gui in the menu.
If you use the left click menu i added a splashscreen countdown, counting down from 5 sconds.

# **Installer**

Simply install the installer, and find it under start menu.
Note: Installer will add ffmpeg binaries to your system path.
It will also register the capture filter's automatic. 
Remember to restart PC.

# **Run with Python code without installer**

First time you have to register the capture filters in registry.
Run register_run_as_admin.bat to register the Qt-screen-capture-recorder.dll and Qt-screen-capture-recorder-x64.dll
Note remember to unregister if you move the filters to a different folder, and then you have to reregister them in the new folder.
Then you would need to add ffmpeg.exe to system path. 

in windows CMD type

`ffmpeg -list_devices true -f dshow -i dummy`

output will display if there are capture filters present.

```
C:\Users\Storm Shadow>ffmpeg -list_devices true -f dshow -i dummy
ffmpeg version N-81784-g92de2c2 Copyright (c) 2000-2016 the FFmpeg developers
  built with gcc 5.4.0 (GCC)

[dshow @ 0000000000eb24e0] DirectShow video devices (some may be both video and audio devices)
[dshow @ 0000000000eb24e0]  "Qt-screen-capture"
[dshow @ 0000000000eb24e0] DirectShow audio devices
[dshow @ 0000000000eb24e0] Could not enumerate audio only devices (or none found).
dummy: Immediate exit requested
```

# **Build installer yourself**
*Tools needed*

[Inno Install](http://www.jrsoftware.org/isinfo.php)

[PyInstaller](https://github.com/pyinstaller/pyinstaller)

from repo folder type

`pyinstaller --window --icon=app.ico rec_main.py icons.py`


**Find build under dist.**

from **PyQt5** folder copy platforms from **PyQt5\plugins\**


to **dist\rec_main**

also copy the **ffmpeg** folder with **subfolders** build folder 

to **dist\rec_main**

Use supplied innosetup script to build. and install

**Sound record you say**

ffmpeg is a lttile wierd about that.
you have to know what sound filter you have and put that into the ffmpeg.exe line in rec_main.py 
to see what filter you have when microphone is plugged in type once agin in windows CMD

`ffmpeg -list_devices true -f dshow -i dummy`

i will see how to add this in future version automatic.

# **Codecs**
In order to play the movies you might need codecs.

I used the awsome [Combined codec community pack ](http://www.cccp-project.net/) for years.


# **Todo**
Add Streaming.

Add updater for new version.

Add automatic sound.

# **Side note on filters**

im using the filter by Roger slidly modded.
If you want to skip those filters and use win 8 /10 internal one.
replace filters in rec_main.py with

`-f gdigrab`

However it produce bad framerate and video do not look good.

# **Side note on 4k recording**

if you have 4k screen, then right click ffmpeg.exe and under settings 

tick "deactivate display scaling on high DPI devices" 

# **Credits**
[![](https://img.shields.io/badge/ffmpeg--green.svg?maxAge=2592000)](httphttps://ffmpeg.org/)
[![](https://img.shields.io/badge/Pyinstaller--blue.svg?maxAge=2592000)](https://github.com/pyinstaller/pyinstaller)
[![](https://img.shields.io/badge/Iconfinder free icons--red.svg?maxAge=2592000)](https://www.iconfinder.com)

**Special thx to Roger for original filters that i have modded**

[![](https://img.shields.io/badge/Original Capture filters--yellow.svg?maxAge=2592000)](https://github.com/rdp/screen-capture-recorder-to-video-windows-free)


