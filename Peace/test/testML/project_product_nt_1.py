import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

# 
output_file = r"D:\student\Peace\test\testML\output\ouput_predicted_product.xlsx"

# Load product name data
product_nt = pd.read_csv(r"D:\student\Peace\test\testML\MASTER_PRODUCT_PL_NT_202401.csv")

# Load train data
train_data = pd.read_csv(r"D:\student\Peace\test\testML\project_product_train_data.csv")

# Load test data
test_data = pd.read_csv(r"D:\student\Peace\test\testML\ข้อมูลจากระบบ SAP ECC6 04-67.csv")

test_data.columns = test_data.columns.str.strip()


# Prepare X and y for training
train_data["Text"] = train_data["Text"].str.strip()
X_train = train_data[["Account", "FA", "Text"]]
y_train = train_data["PRODUCT_KEY"]

# Prepare X for testing
test_data["Text"] = test_data["Text"].str.strip()
X_test = test_data[["Account", "FA", "Text"]]

# Preprocess text data using TfidfVectorizer
text_transformer = TfidfVectorizer()

# Preprocess categorical data using OneHotEncoder
categorical_transformer = OneHotEncoder(handle_unknown="ignore")

# Combine preprocessors
preprocessor = ColumnTransformer(
    transformers=[
        ('text', text_transformer, 'Text'),
        ('categorical', categorical_transformer, ['Account', 'FA'])
    ])

# Define the model pipeline
model = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', MultinomialNB())
])

# Train the model
model.fit(X_train, y_train)

# Make predictions on test data
predictions = model.predict(X_test)

# Add predictions to the test data
test_data['Predicted_PRODUCT_KEY'] = predictions

# Print the test data with predictions
print(test_data)

X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.25)

# Define the model pipeline
model_test = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', MultinomialNB())
])
model_test.fit(X_train, y_train)
# Model evaluation
y_pred = model_test.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# print(product_nt.dtypes)
# print(test_data.dtypes)
output = test_data[['Account', 'FA', 'Text', 'Predicted_PRODUCT_KEY', 'Amount in local cur.']]
output = pd.merge(output, product_nt, left_on="Predicted_PRODUCT_KEY", right_on="PRODUCT_KEY", how="left")
output = output[['Account', 'FA', 'Text', 'Predicted_PRODUCT_KEY', 'Amount in local cur.', 'PRODUCT_NAME', 'SERVICE', 'BUSINESS']]
output['Account'] = output['Account'].astype(str)
output['FA'] = output['FA'].astype(str)
output['Predicted_PRODUCT_KEY'] = output['Predicted_PRODUCT_KEY'].astype(str)
# clean amount value
# output.loc[:,"Amount in local cur."] = output["Amount in local cur."].str.strip()
# output.loc[:,"Amount in local cur."] = output["Amount in local cur."].mask(output["Amount in local cur."].str[-1].isin(['-','+']), output["Amount in local cur."].str[-1].str.cat(output["Amount in local cur."].str[:-1])).str.replace(',', '').astype(float)

# output = output.groupby(['Account', 'FA', 'Text', 'Predicted_PRODUCT_KEY', 'PRODUCT_NAME', 'SERVICE', 'BUSINESS'])['Amount in local cur.'].sum()
output.to_excel(output_file, index=False)
