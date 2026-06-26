# Heart Disease Prediction (KNN) — Live Streamlit App
A machine learning app that predicts heart disease risk from medical
parameters (age, cholesterol, resting BP, max heart rate, and more),
deployed as an interactive Streamlit web app.
Live app: https://heart-disease-prediction-quupfp7kxdeptvcckpse8j.streamlit.app/
## What I did
- Trained and compared 5 models: KNN, Logistic Regression, Naive Bayes,
 SVM, and Decision Tree
- Evaluated each on accuracy, precision, recall, and F1 score
- - Selected K-Nearest Neighbors as the final model: 88% accuracy,
 89% F1 score, most stable performance on the test set with no
 overfitting
- Built a Streamlit front end so anyone can enter their own values
 and get a real-time prediction
## Tech stack
Python · Pandas · NumPy · Scikit-Learn · Matplotlib · Seaborn · Streamlit
## Run it locally
git clone https://github.com/amang2844/Heart-Disease-Prediction.git
cd Heart-Disease-Prediction
pip install -r requirements.txt
streamlit run app.py
## Author
Aman Goswami · [LinkedIn](https://linkedin.com/in/aman-goswami-09622924b)
