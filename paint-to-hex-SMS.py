import os
from PIL import Image
from tkinter import filedialog
import struct
from math import floor

pal_file = ""
pal_file = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Palette Image", filetype=(('PNG file', '*.png'),('BMP file', '*.bmp'),("ALL file",'*.*')))

if len(pal_file)!=0:
    list_colors = []
    openpal = Image.open(pal_file).convert("RGB")
    wp,hp = openpal.size

    BGR_pal = bytearray()
    
    if wp * hp == 16:
        R, G, B = 0, 0, 0
        for y in range(0,hp):
            for x in range (0,wp):
                R, G, B = openpal.getpixel((x,y))
                list_colors.append((R, G, B))
                R = floor(R // 85)
                G = floor(G // 85)
                B = floor(B // 85)
                BGR_pal += struct.pack("B", (B * 16) + (G * 4) + R)

        if list_colors.count(list_colors[0]) != 16:

            bit_paint = bytearray()
            targ_file = ""
            targ_file = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Picture", filetype=(('PNG file', '*.png'),('BMP file', '*.bmp'),("ALL file",'*.*')))
            new_bin_file = ""

            if len(targ_file) != 0 :

                openpic = Image.open(targ_file).convert("RGB")
                w,h = openpic.size

                if w % 24 == 0 and h % 32 == 0:

                    n=len(targ_file)-1
                    while n!= 0 and targ_file[n] != '.':
                        n -= 1
                    n -= 1
                    while n!= 0 and targ_file[n] != '/':
                        new_bin_file = targ_file[n] + new_bin_file
                        n -= 1

                    for xw in range (0, w, 24):
                        for yh in range(0, h, 16):
                            for x in range (0, 24, 8):
                                for y in range(0, 16, 8):
                                    for iz in range(0, 8):
                                        br1, br2, br3, br4 = "", "", "", ""
                                        data_row_1, data_row_2, data_row_3, data_row_4 = bytearray(), bytearray(), bytearray(), bytearray()
                                        for ix in range(0, 8):
                                            RGB_P = openpic.getpixel((xw+x+ix,yh+y+iz))
                                            RGB_data = "0"*(4-len(format(list_colors.index(RGB_P), 'b'))) + format(list_colors.index(RGB_P), 'b')
                                            br1 += RGB_data[-1]
                                            br2 += RGB_data[-2]
                                            br3 += RGB_data[-3]
                                            br4 += RGB_data[-4]
                                        br1 = struct.pack("B",int(br1 , 2))
                                        br2 = struct.pack("B",int(br2 , 2))
                                        br3 = struct.pack("B",int(br3 , 2))
                                        br4 = struct.pack("B",int(br4 , 2))
                                        bit_paint += br1 + br2 + br3 + br4

                    out_file = open(new_bin_file + " SMS Pal.bin", "wb+")
                    out_file.write(BGR_pal)
                    out_file.close()
                                    
                    out_file = open(new_bin_file + " SMS Image.bin", "wb+")
                    out_file.write(bit_paint)
                    out_file.close()

                    print("Pic and Pal Bin file done!")

                else:

                    if w % 24 == 0:
                        print("Image Width isn't a divisible of 24")
                    else:
                        print("Image Height isn't a divisible of 32")
        else:
             print("Palette File Empty")   

    else:
        if wp * hp > 16:
            print("The palette Picture exceed 16 colors")
        else:
            print("The palette Picture is too small")

else:
    print("No Palette Picture Selected")
