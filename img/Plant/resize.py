import cv2
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
for i in ["./"]:
    image = os.path.dirname(os.path.abspath(__file__))
    for root, _, files in os.walk(image):
        for file in files:
            if file.endswith("bmp"):
                path = os.path.join(root, file)
                print(path)
                img = cv2.imread('{}'.format(path), cv2.IMREAD_UNCHANGED)

            
                dim = (192, 128)
                resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

                print('Resized Dimensions : ',resized.shape)
                cv2.imwrite(path,resized)
                cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows() 
