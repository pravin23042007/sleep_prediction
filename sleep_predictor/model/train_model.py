import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Loading the dataset
df = pd.read_csv('../data/sleep_data.csv')

# These are the input and output variables for the model
X = df[['screen_time', 'caffeine', 'stress', 'lighting']]
y = df['time_to_sleep']

# Splits the  data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Used to Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Used to save model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved successfully!")