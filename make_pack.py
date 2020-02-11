import os
import plistlib
import shutil
import subprocess
from sys import argv
from tempfile import TemporaryDirectory
from uuid import uuid4
import zipfile


def make_pack_from(name, *filenames):
    with TemporaryDirectory() as tdn:
        images = []

        for filename in filenames:
            tfn = '{}.png'.format(str(uuid4()).upper())
            shutil.copyfile(filename, os.path.join(tdn, tfn))
            images.append(tfn)

        shutil.copyfile(
            os.path.join(tdn, images[0]),
            os.path.join(tdn, 'thumbnail.png'),
        )

        with open(os.path.join(tdn, 'Info.plist'), 'wb') as pf:
            plistlib.dump({
                'images': images,
                'size': 136,
                'title': name,
            }, pf)

        archive_name = shutil.make_archive('{}.adhesivepack'.format(name), 'zip', tdn)
        os.rename(archive_name, os.path.splitext(archive_name)[0])


if __name__ == '__main__':
    make_pack_from(argv[1], *argv[2:])
