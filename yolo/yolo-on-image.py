import matplotlib.pyplot as plt
from darkflow.net.build import TFNet
import cv2
from glob import glob
from scipy.misc import imread
from PIL import Image

options = {
    "model": "config/tiny-yolo-voc.cfg",
    "load": "config/tiny-yolo-voc.weights",
    "labels": "config/labels.txt"
}

tfnet = TFNet(options)


def get_pred(img):
    preds = tfnet.return_predict(img)
    results = []

    for pred in preds:
        if pred['label'] != 'person':
            continue

        result = {}
        result['tl'] = [pred['topleft']['x'], pred['topleft']['y']]
        result['br'] = [pred['bottomright']['x'], pred['bottomright']['y']]
        results.append(result)

    return results


def view(img, annots, outfile=None):
    images = []

    for annot in annots:
        x, y, x2, y2 = annot['tl'] + annot['br']
        im = img[x:x2, y:y2]
        images.append(im)
        # cv2.rectangle(img, (x, y), (x2, y2), (0, 255, 0), 2)

    if not outfile:
        plt.imshow(images[0])
        plt.show()
    else:
        print(outfile)
        for img in images:
            img = Image.fromarray(img)
            img.save(outfile)

def main():
    frames_cnt = 0
    datadir = '/run/media/surya/F/codes/project_git/skcript/imageclassifier/data/downloads/'
    imgfolder = 'indian traiditonal dress'
    output = datadir + imgfolder + '/new/'

    names = glob(datadir+imgfolder+'/*.*')

    for name in names:
        img = imread(name)

        # img = np.array(image)
        # img = np.roll(img, 1, axis=-1)

        pred = get_pred(img)
        print(pred)

        imgtitle = name.split('/')[-1]

        if pred != []:
            print('saving ' + imgtitle)
            view(img, pred)
            # break
        else:
            print('no anots for ' + imgtitle)


if __name__ == '__main__':
    main()
