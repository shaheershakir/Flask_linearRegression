import pickle

def prediction(height):
    pickled_model = pickle.load(open("model.pkl", "rb"))
    weight = pickled_model.predict(height)
    print(weight)
    print(height)
    return weight