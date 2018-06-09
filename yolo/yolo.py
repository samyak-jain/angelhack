from darkflow.net.build import TFNet
import cv2

options = {
    "model": "config/tiny-yolo-voc.cfg",
    "load": "config/tiny-yolo-voc.weights",
    "labels" : "config/labels.txt"
}

tfnet = TFNet(options)

def get_pred(img):
    preds = tfnet.return_predict(img)
    print(preds)
    results = []

    for pred in preds:
        result = {}
        result['tl'] = [pred['topleft']['x'], pred['topleft']['y']]
        result['br'] = [pred['bottomright']['x'], pred['bottomright']['y']]
        results.append(result)

    return results
