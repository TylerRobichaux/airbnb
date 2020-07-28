import pandas as pd
# import numpy as np
import category_encoders as ce
import joblib
# # !pip install pandas-profiling==2.8.0
# # !pip install category_encoders
# # !pip install eli5
#import *
from . import encoder1
from . import baseline1
from . import baseline2
encode = joblib.load("categorical_encoder.pkl")
nlp = joblib.load("baseline1.pkl")
rfr = joblib.load("baseline2.pkl")

# router = Flask(__name__)

@router.get('/propertyprediction')
async def add_property(description, neighborhood, property_type, room_type, zipcode, beds, number_of_reviews):
    """Returns a prediction of a given users property"""
    user_input = {
    "description": description,
    "neighborhood": neighborhood,
    "property_type": property_type,
    "room_type": room_type,
    "zipcode": zipcode,
    "beds": beds,
    "number_of_reviews": number_of_reviews
    }
    text = user_input["description"]
    prediction = nlp.predict([text])
    user_input.update(nlp_pred= prediction)
    del user_input['description']
    user_input = pd.DataFrame.from_dict(user_input, orient='index').T
    encoder = ce.OrdinalEncoder()
    user_input[['neighborhood', 'property_type', 'room_type']] = encoder.fit_transform(user_input[['neighborhood', 'property_type', 'room_type']])
    return  rfr.predict(user_input)  #.json()
