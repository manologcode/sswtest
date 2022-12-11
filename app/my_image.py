import os
from PIL import Image

class MyImage():

    @staticmethod
    def compare_img(first_path,second_path):
        i1 = Image.open(first_path)
        i2 = Image.open(second_path)
        assert i1.mode == i2.mode, "Different kinds of images."
        assert i1.size == i2.size, "Different sizes."

        pairs = zip(i1.getdata(), i2.getdata())
        if len(i1.getbands()) == 1:
            dif = sum(abs(p1-p2) for p1,p2 in pairs)
        else:
            dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))

        ncomponents = i1.size[0] * i1.size[1] * 3
        return (dif / 255.0 * 100) / ncomponents
    
    @staticmethod
    def compare_two_folders(path1, path2):
        response=[]
        for file in os.listdir(path1):
            img1 = os.path.join(path1, file)
            img2 = os.path.join(path2, file)
            data ={'file': file}
            if os.path.isfile(img2):
                diff = MyImage.compare_img(img1, img2)
            else:
                diff = "No existe"
            data['diff'] = diff
            response.append(data)
        return response