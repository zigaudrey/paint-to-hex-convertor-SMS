import os
import struct

from PIL import Image
from tkinter import filedialog

PAL_path = ""
PAL_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Pal File", filetype=(('BIN file', '*.bin'),("ALL file",'*.*')))

if len(PAL_path) != 0:
    PAL_open = open(PAL_path, 'rb')
    PAL_data = PAL_open.read()
    PAL_open.close()

    if len(PAL_data) == 16:

        over_3F = False
        for i in range(0,len(PAL_data)):
            if PAL_data[i] > 63:
                over_3F = True

        if over_3F == False:

            PAL_List = []

            R, G, B = 0, 0, 0
            
            for i in range(0,len(PAL_data)):
                Dec_Color = PAL_data[i]
                B = (Dec_Color // 16 % 4) * 85
                G = (Dec_Color // 4 % 4) * 85
                R = (Dec_Color % 4) * 85
                PAL_List.append((R, G, B))

            if PAL_List.count(PAL_List[0]) != 16:

                n=len(PAL_path) - 1
                SHORT_name = ""
                        
                while n!= 0 and PAL_path[n] != '.':
                    n -= 1
                n -= 1
                while n!= 0 and PAL_path[n] != '/':
                    SHORT_name = PAL_path[n] + SHORT_name
                    n -= 1

                PAL_OUTCOME= Image.new('RGB', (8 , 2))

                np = 0
                for y in range(2):
                    for x in range(8):
                        PAL_OUTCOME.putpixel((x,y), PAL_List[np])
                        np += 1

                PAL_OUTCOME.save(SHORT_name + " SMS Pal Image.png")
                
                print("Pal Image Done!")

            else:
                print("Palette File Empty")

        else:
            print("One byte is over 3F (63)")

    else:

        print("The Palette Bin file has to be 32 long")

else:
    print("No Palette File Selected")

