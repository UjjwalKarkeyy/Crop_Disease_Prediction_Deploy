import numpy as np
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import Pipeline
from pathlib import Path
import keras
from PIL import Image
from sklearn.base import BaseEstimator, TransformerMixin
from tensorflow.keras.applications.mobilenet import preprocess_input
import joblib

class KerasPreprocessorWrapper_MobileNet(BaseEstimator, TransformerMixin):
    def __init__(self, target_size=(224, 224)):
        self.target_size = target_size

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        processed_imgs = []
        for item in X:
            # Case 1: item is a string (file path)
            if isinstance(item, (str, Path)) and Path(item).suffix.lower() in ['.jpg', '.png']:
                img = Image.open(item).convert('RGB').resize(self.target_size)
    
            # Case 2: item is a PIL image (from FastAPI upload)
            elif isinstance(item, Image.Image):
                img = item.convert('RGB').resize(self.target_size)
    
            else:
                raise TypeError(f"Unsupported input type: {type(item)}")
    
            img_array = np.array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = preprocess_input(img_array)
            processed_imgs.append(img_array[0])
    
        return np.array(processed_imgs)

    
mobile_net = keras.saving.load_model(f'./mobileNet_model.keras')
pipeline_mobile_net = Pipeline(steps=[
    ('preprocess', KerasPreprocessorWrapper_MobileNet()),
    ('model', mobile_net),
])

joblib.dump(pipeline_mobile_net, "./crop_disease_pipeline.pkl")

