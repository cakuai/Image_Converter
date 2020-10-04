from PIL import Image, ImageFilter

img = Image.open("./pokemon/皮卡丘.png")
filtered_img = img.convert("RGB").filter(ImageFilter.CONTOUR)
# 還有SMOOTH SHARPEN CONTOUR等功能可以選 但因原圖非滿版 係調色板圖 故要先convert 才能filter否則會跳error
converted_img = img.convert("L")  # L -> greyscale

filtered_img.save("pikachu_blur.png", "png")  # 存成新檔案
converted_img.save("pikachu_grey.png", "png")

crooked = filtered_img.rotate(90)  # 圖片逆時針翻轉
resize = filtered_img.resize((300, 300))  # 尺寸要用tuple 改變圖片大小

box = (100, 100, 400, 400)  # 左上為(0,0) 四個數字方別代表 (左, 上, 右, 下)
region = filtered_img.crop(box)
# filtered_img.show() #直接開啟檔案給你看

img.thumbnail((400, 400))
# 製作縮圖 為了不要讓圖片ratio跑掉 不用resize而改用這個 但thumbnail無回傳值 是「動作」 所以不能assign給變數
# tuple裡的是圖片max value
img.save("thumbnail.png")

