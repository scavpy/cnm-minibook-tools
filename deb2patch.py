#! /usr/bin/env python3
"""
Unpack a .deb (from Debian mipsel port) and re-pack as
.info and .patch files for CnM Minibook

deb2patch PACKAGE_ver_mipsel.deb

Files are created in a directory named after the PACKAGE

GNU GPLv3
(C) Peter Harris 2009

"""


import sys
import os
import tarfile
import time

def deb2patch(fname):
    package, version, arch = os.path.basename(fname).split("_")
    if (arch != "mipsel.deb"):
        raise ValueError("deb2patch only works for mipsel .deb files")
    os.mkdir(package)
    pname = "%s_%s" % (package,version)
    os.system("cp -a %s %s/%s.ar" % (fname,package,pname))
    os.chdir(package)
    os.system("ar x %s.ar control.tar.gz data.tar.gz" % pname)
    control_tar = tarfile.open("control.tar.gz","r")
    control_tar.extract("./control") # mostly so you can check Depends: line
    control_tar.close()
    data_tar = tarfile.open("data.tar.gz","r")
    file_list = []
    info_file = open("%s.info" % pname, "w")
    patch_file = tarfile.open("%s.patch" % pname, "w:bz2")
    print("%s.patch" % pname,package,version,sep="\n",file=info_file)
    for data_info in data_tar.getmembers():
        if data_info.name == ".": continue
        if data_info.name.startswith("./"):
            data_info.name = data_info.name[2:]
        if data_info.isfile():
            data_file = data_tar.extractfile(data_info.name)
            print(data_info.name)
            patch_file.addfile(data_info, data_file)
            data_file.close()
        else:
            patch_file.addfile(data_info) # directory or symlink
        file_list.append((data_info.name, "%dk" % (data_info.size // 1024)))
    data_tar.close()
    # info file also goes into the patch
    file_list.append(("share/info/%s.info" % pname, "4k"))
    print(len(file_list), time.strftime("%F",time.gmtime()), sep=":", file=info_file)
    for name,size in file_list:
        print("%-6s" % size, name, file=info_file)
    info_file.close()
    os.makedirs("share/info")
    os.system("cp -a %s.info share/info" % pname)
    patch_file.add("share/info/%s.info" % pname)
    patch_file.close()
    # tidy up
    os.remove("control.tar.gz")
    os.remove("data.tar.gz")
    os.remove("%s.ar" % pname)
    
if __name__ == '__main__':
    try:
        fname = sys.argv[1]
        deb2patch(fname)
    except (IndexError, ValueError):
        print(__doc__)
        raise
