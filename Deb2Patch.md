# Deb2Patch #

This utility is a Python program (for Python 3), which re-packages a Debian package into
.info and .patch files.

Note that it doesn't run on the laptop itself, unless you have Python 3 already working on it. This is unlikely to be the case, so you want to do this on a 'normal' PC.

There is no conflict or dependency resolution, nor any guarantee that installing the files won't hose your laptop if they overwrite something that has been carefully customised to work with the hardware.  **Use with care.**

However, I have had some success with it.

## Step 1 ##

Find your Debian packages.  Make sure you get all the required dependencies.  A good place to find them is http://www.debian.org/distrib/packages.  Follow the download link for the **mipsel** architecture to get a `.deb`.

## Step 2 ##

In the same directory as your `.deb` file, run `deb2patch.py`. For example, to get the excellent `joe` editor:
```
$ deb2patch.py joe_3.7-1_mipsel.deb
... prints a big list of files ...
```

A subdirectory is created, named after the package (in this case `joe`), containing
a .info file, a .patch file and the Debian `control` file, which you can examine later
to double-check the dependencies and conflicts to your own satisfaction.
```
$ ls joe
control  joe_3.7-1.info  joe_3.7-1.patch
```

## Step 3 ##

Copy the created files onto a USB stick or otherwise transfer them to your little laptop.
Put them in `/My\ Documents/Download` and run the software installer to install them.

You now either have new software or have badly broken something! Yay!