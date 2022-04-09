import pickle

# Writing aa pickle file
ordering = {"First": 1, "Second": 2, "Third": 3}
pickle.dump(ordering, open("new.pkl", "wb"))

# Read from the pickel file
reading_pickle = pickle.load(open("new.pkl", "rb"))
print(reading_pickle)