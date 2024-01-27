import tkinter as tk
from tkinter import ttk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import csv  # Added import for the csv module

def classify_mail():
    input_mail = mail_entry.get()
    input_data_features = feature_extraction.transform([input_mail])
    prediction = model.predict(input_data_features)
    
    if prediction[0] == 1:
        result_label.config(text='Ham mail')
    else:
        result_label.config(text='Spam mail')

def add_example(label):
    example_mail = mail_entry.get()
    with open("D:\\SO LONG\\FOR GOOD\\College Files\\Mini Project\\NEW\\spam.csv", 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([label, example_mail])
    result_label.config(text=f'Example added as {label} mail')


# Load your data and preprocess as before
# loading the data from csv file to a pandas Dataframe
raw_mail_data = pd.read_csv("D:\\SO LONG\\FOR GOOD\\College Files\\Mini Project\\NEW\\spam.csv", encoding="ISO-8859-1")

# replace the null values with a null string
mail_data = raw_mail_data.where((pd.notnull(raw_mail_data)),'')

# label spam as 0 and ham as 1
mail_data['v1'] = mail_data['v1'].map({'spam': 0, 'ham': 1})


# Drop rows with missing values in 'v1' column
mail_data = mail_data.dropna(subset=['v1'])



# separating data as texts(x-axis) and labels(y-axis)
X = mail_data['v2']
Y = mail_data['v1']

# split train data(80% data) and test data(20% data)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)

# convert text into numerical for the input to the logistic regression
feature_extraction = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)

X_train_features = feature_extraction.fit_transform(X_train)
X_test_features = feature_extraction.transform(X_test)

# convert Y_test and Y_train values as integers
Y_train = Y_train.astype('int')
Y_test = Y_test.astype('int')

# training the logistic regression
model = LogisticRegression()

# training the logistic regression with training data
model.fit(X_train_features, Y_train)

# evaluating the trained model
# prediction on training data
prediction_on_training_data = model.predict(X_train_features)
accuracy_on_training_data = accuracy_score(Y_train, prediction_on_training_data)

# prediction on test data
prediction_on_test_data = model.predict(X_test_features)
accuracy_on_test_data = accuracy_score(Y_test, prediction_on_test_data)

# Create the main application window
root = tk.Tk()
root.title("Spam Classifier")

# Create and place widgets in the window
mail_label = ttk.Label(root, text="Enter an email:")
mail_label.grid(row=0, column=0, padx=10, pady=10)

mail_entry = ttk.Entry(root, width=40)
mail_entry.grid(row=0, column=1, padx=10, pady=10)

classify_button = ttk.Button(root, text="Classify", command=classify_mail)
classify_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = ttk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Buttons to add examples
spam_example_button = ttk.Button(root, text="Add Spam Example", command=lambda: add_example('spam'))
spam_example_button.grid(row=3, column=0, pady=10)

ham_example_button = ttk.Button(root, text="Add Ham Example", command=lambda: add_example('ham'))
ham_example_button.grid(row=3, column=1, pady=10)

# Run the Tkinter event loop
root.mainloop()
