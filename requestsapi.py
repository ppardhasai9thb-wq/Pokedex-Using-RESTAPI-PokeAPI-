import requests
import numpy as np
import cv2
print("enter pokemon name:- ",end="")
pokemon_name=input().lower()
baseurl="https://pokeapi.co/api/v2"
url=f"{baseurl}/pokemon/{pokemon_name}"
r=requests.get(url)
request_code=r.status_code

if request_code==200:
    pokemon_info = r.json()
    print(f"NAME:- {(pokemon_info["name"]).capitalize()}")
    print(f"HEIGHT:- {pokemon_info["height"]}m")
    print(f"WEIGHT:- {pokemon_info["weight"]}kg")
    print(f"ID:- {pokemon_info["id"]}")
    print(f"TYPE:- {(pokemon_info["types"][0]["type"]["name"]).capitalize()}")
else:
    print(f"{pokemon_name} not found")
    print(f"error:- {request_code}")
if request_code!=200:
    pass
else:
    print("want an img?(Y/n)")
    n=input()
    imgvariable=pokemon_info["sprites"]["front_shiny"]
    imgsource=requests.get(imgvariable)
    if(n=="Y" or n=="y"):
        if(imgsource.status_code==200):
            imgarr=np.asarray(bytearray(imgsource.content),dtype=np.uint8)
            dispimg=cv2.imdecode(imgarr,cv2.IMREAD_COLOR)
            scale_factor = 4

            # 2. Calculate new dimensions based on the original size
            new_width = int(dispimg.shape[1] * scale_factor)
            new_height = int(dispimg.shape[0] * scale_factor)
            new_dimensions = (new_width, new_height)

            # 3. Resize using INTER_NEAREST to keep pixel art sharp and crisp
            large_dispimg = cv2.resize(dispimg, new_dimensions, interpolation=cv2.INTER_NEAREST)
            # 4. Initialize a named window frame with normal property flags
            cv2.namedWindow(pokemon_name, cv2.WINDOW_NORMAL)

            # 5. FORCE the OS window manager to bring this specific window to the foreground
            cv2.setWindowProperty(pokemon_name, cv2.WND_PROP_TOPMOST, 1)
            cv2.imshow(pokemon_name,large_dispimg)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("Error")
    else:
        print("Image fetching was unsuccessful")
# r=requests.get(url)
# # print(requests.get(url))
# # print(r.text)
# print(r.json())
