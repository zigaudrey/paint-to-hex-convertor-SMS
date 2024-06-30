![Image to Bin Convertor - Master System BANNER](https://github.com/zigaudrey/paint-to-hex-convertor-SMS/assets/129554573/1d856ba1-4b54-4b9e-a5a6-209c6f6f5861)

# Paint to Hex Convertor Script (Sega Master System)
A Python script that convert a picture to bin file for Sega Master System plus a script that convert palette data into a picture

## Setups
1. If you don't have PIL, **open the command prompt and install it with PIP**
2. Open the Rom file with **[YY-CHR](https://www.romhacking.net/utilities/119/), choose the pattern FC/SNES x16 and locate the sprites to have a look on how they are placed**. The sprite sheet should have **the width a divisible of 24 and the height of 32 (divisible of 16)**
3. To be color accurate, **use Master_Sytem_Palette.png as palette.**
4. Use [MEKA](https://www.smspower.org/meka/) to get the color palette, **use the hex-to-palette-SMS script to generate the palette picture. Its bin lenght has to be 16**

## Steps
5. **Choose the palette picture and the sprite sheet**
6. **Two bin files will be created**, ready to be used in Rom Hacking

## Result

![Meta-Knight-in-Taz-Mania-SMS-Gif-WIP](https://github.com/zigaudrey/paint-to-hex-convertor-SMS/assets/129554573/b21eb301-a058-4686-869c-1c5f9fe98c02)
Meta Knight in Taz-Mania SMS (Work in Progress)

## Author's Note
I was excited to work with binaries on Python until I end up creating a script for the GameBoy sprite format. Days later, I realize that the MasterSystem sprite format is 4BPP, I just need to add 2 binary rows and it worked! Thus this become my first Python script goes on binary instead on Hexadecimal.

For now, this repertory is an one-way convertor and it is published as a 3-quarter to fill the gap.

YY-CHR says that Master System and Game Gear share the same sprite format (except the tiles placement) but the different palette format drive me to make it Master System only.

The palette picture come from this [SegaRetro Wiki Page](https://segaretro.org/Palette)

## Similar Tools
+ [Paint - Hex Convertor (Sega Megadrive)](https://github.com/zigaudrey/paint-hex-convertor-MSX)
+ [Paint - Hex Convertor (Gameboy Advance / DS 16-Colors)](https://github.com/zigaudrey/paint-hex-convertor-GBA-DS)
+ [Paint - Hex Convertor DS-256 colors](https://github.com/zigaudrey/paint-hex-convertor-DS-256/tree/main)
