import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    x = np.zeros(len(__data_columns))
    try:

        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >=0:

        x[loc_index] = 1
    else:
        x[loc_index] = 1


    return round(__model.predict([x])[0],2)

def get_locations_names():

    return __locations

def load_artifacts():
    print('loading artifacts Start...')

    global __locations
    global __data_columns
    global __model

    with open('artifacts/columns.json','r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    with open('artifacts/model.pickle','rb') as f:
        __model = pickle.load(f)

    print('loading artifacts Done...')



if __name__ == '__main__':
    load_artifacts()

