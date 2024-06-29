![Image to Bin Convertor - Master System BANNER](https://github.com/zigaudrey/paint-to-hex-convertor-SMS/assets/129554573/1d856ba1-4b54-4b9e-a5a6-209c6f6f5861)

# Paint to Hex Convertor Scripts (Sega Master System)
A Python script that convert a picture to bin file for Sega Master System plus a script that convert palette data into a picture

## Setups
1. If you don't have PIL, **open the command prompt and install it with PIP**
2. Open the Rom file with **YY-CHR, choose the pattern FC/SNES x16 and locate the sprites to have a look on how the sprites are placed**. The sprite sheet should have **a width of 32 and the height a divisible of 24.**
3. To be color accurate, **use Master_Sytem_File.png as palette.**
4. I don't know how to find the color in the rom but if you manage to do it, **use the hex-to-palette-SMS script to generate the palette picture. Its bin lenght has to be 16**

## Steps
5. **Choose the palette picture and the sprite sheet**
6. **Two bin files will be created**, ready to be used in Rom Hacking

## Author's Note
I was excited to work with binaries on Python until I end up creating a script for the GameBoy sprite format. Days later, I realize that the MasterSystem sprite format is 4BPP, I just need to add 2 binary rows and it worked! Thus this become my first Python script goes on binary instead on Hexadecimal.

For now, this repertory is an one-way convertor and it is published as a 3-quarter to fill the gap.

YY-CHR says that Master System and Game Gear share the same sprite format (except the tiles placement) but the different palette format drive me to make it Master System only.

## Similar Tools
+ [Paint - Hex Convertor (Sega Megadrive)](https://github.com/zigaudrey/paint-hex-convertor-MSX)
+ [Paint - Hex Convertor (Gameboy Advance / DS 16-Colors)](https://github.com/zigaudrey/paint-hex-convertor-GBA-DS)
+ [Paint - Hex Convertor DS-256 colors](https://github.com/zigaudrey/paint-hex-convertor-DS-256/tree/main)
