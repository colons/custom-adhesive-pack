# custom adhesive pack

A little utility to quickly create big sticker packs for [Adhesive][adhesive] so that you can use them in iMessage.

## Requirements

- Python 3.x
- an iOS device running [Adhesive][adhesive]
- Some png files you want to use as iMessage stickers

## Usage

- clone and `cd` to this repo
- run `python3 make_pack.py '[name of sticker pack]' [image_1.png image_2.png image_3.png ...]`
    - using your shell's wildcard expansion, you can do something like `python3 make_pack.py 'Don-chan' ~/Desktop/don-chan/*.png`
- open the `[name of sticker pack].adhesivepack` file that's been created in the current directory on your target iOS device
    - I do this by sending it with AirDrop from the Finder

## Notes

- Rather than the composited thumbnails Adhesive makes for itself, the thumbnail for your pack will just be the first image you provide.

[adhesive]: https://apps.apple.com/us/app/adhesive/id1153165424
