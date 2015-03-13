# Running More Than 3 Applications #

The directory `/share/xip_style/` contains a file `current` which contains one line of text: the name of the current desktop template.

There will be a directory with that name, and in that directory will be (among other interesting things) a file called `style.data`.

Look down this file to the section beginning DESKTOP-CONF. There will be a line like:
```
MAX_AP_COUNT=3
```

You can change this setting (within reason).  It won't take effect until you reboot the laptop.  I have it set to 5 at the moment, and haven't needed to go beyond that.