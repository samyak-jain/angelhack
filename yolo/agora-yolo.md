Python: module agora-yolo 

   
   
**agora-yolo**

[index](.)  
[/run/media/surya/F/codes/project_git/angelhack/yolo/agora-yolo.py](file:/run/media/surya/F/codes/project_git/angelhack/yolo/agora-yolo.py)

Module receives frames from the agora api and applies  
YOLO algorithm to every frame. Script emulates a browser  
in the python script on a server and parses frames off it

* * *

**requirements:** 

chrome/chromium, refer requirements.txt  
requires darkflow installed via python(refer docs)  
**usage:** 

`python [--execpath] agora-yolo.py`
CLI args: executable path of the chrome/chromium browser  
defaults to '/usr/bin/google-chrome-stable'  
Video will be displayed everytime a person is  
detected by the 'openlive' app available in the repo

   
**Modules**

 

[PIL.Image](PIL.Image.html)  
[argparse](argparse.html)  

[asyncio](asyncio.html)  
[Algorithms.conversion](Algorithms.conversion.html)  

[cv2](cv2.html)  
[io](io.html)  

[numpy](numpy.html)  
[time](time.html)  

   
**Functions**

 

**get_pred**(img)

**main**(execpath)

**update_locations**(annots)

**view**(img, annots)