# Copyright (c) victor su. All rights reserved.
import time, os

class DummyPredict(object):
    """
    The Dummy Prediction Wrapper
    """
    def __init__(self, model_path):
        """
        Init
        """
        self._model_path = model_path
        # self._version = version
        self._flag = 1

    def model_path(self):
        """
        Return the cached model path
        """
        return self._model_path

    def run(self, image):
        """
        Run the prediction
        """
        # mock the prediction
        time.sleep(1)
        if self._flag % 3 == 1:
            res = "NG"
        else:
            res = "OK"
        self._flag = self._flag + 1
        return res

if __name__ == "__main__":
    work_dir = os.path.dirname(os.path.abspath(__file__)) + '/../'
    model_path = work_dir + 'models/trained_0.model'
    image =work_dir + 'dataset/OK/00.jpg'
    predict = DummyPredict(model_path)
    res = predict.run(image)
    print('predict result:', res)