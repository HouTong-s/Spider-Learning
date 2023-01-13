import os
import shutil
dir1 = os.listdir('./摄图网图片')
#print(filenames)
for _dir1 in dir1:
    shutil.rmtree('./摄图网图片/'+_dir1+"/big")
    shutil.rmtree('./摄图网图片/'+_dir1+"/small")