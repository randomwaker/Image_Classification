from PIL import Image
import os , glob
import numpy as np
try:
    from sklearn import cross_validation
except ImportError:
    from sklearn.model_selection import cross_validate

classes = ["monkey", "boar", "crow", "deer"]

num_classes = len(classes)
image_size = 50

#画像の読み込み

X = []
Y = []

for index, classlabel in enumerate(classes):
    print("index" + str(index))
    photo_dir = "./" + classlabel
    files = glob.glob(photo_dir + "/*.jpg")
    print(photo_dir + "/*.jpg")

    for i, file in enumerate(files):
        if i >= 200: break
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((image_size, image_size))
        data = np.asarray(image)
        X.append(data)
        Y.append(index)

X = np.array(X)
Y = np.array(Y)


