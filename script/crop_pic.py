#! usr/bin/env Python
# coding=utf-8


from PIL import Image
import time
start_time = time.time()
for n in range(119, 175):
    img = Image.open("/Users/Arthur/Downloads/HSK_v3/"+str(n)+".png")
    print(n, img.size)
    if (n % 2) != 0:
        cropped_left = img.crop((400, 450, 800, 3850))
        cropped_left.save('/Users/Arthur/Downloads/HSK_v3/crops/'+str(n)+'_left.png')
        cropped_right = img.crop((1600, 450, 2000, 3850))
        cropped_right.save('/Users/Arthur/Downloads/HSK_v3/crops/'+str(n)+'_right.png')
    else:
        cropped_left = img.crop((500, 450, 900, 3850))
        cropped_left.save('/Users/Arthur/Downloads/HSK_v3/crops/'+str(n)+'_left.png')
        cropped_right = img.crop((1700, 450, 2100, 3850))
        cropped_right.save('/Users/Arthur/Downloads/HSK_v3/crops/'+str(n)+'_right.png')
end_time = time.time()
print("耗时:", int(end_time-start_time), "秒")

