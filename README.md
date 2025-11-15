🫀 Heart Disease Prediction using Machine Learning

This project predicts the likelihood of heart disease using multiple machine learning models and a simple, interactive Streamlit web app.
The goal is to help users understand risk levels using medical parameters like age, cholesterol, resting BP, maximum heart rate, and more.

🚀 Project Highlights

Complete ML workflow in Jupyter Notebook

Tried 5 different algorithms and compared their performance

Selected the K-Nearest Neighbors (KNN) model

Live prediction UI built using Streamlit

Clean visualizations for understanding feature relationships

Easy-to-run app for demonstrating predictions in real-time

🧠 Machine Learning Models Tried

You trained and compared the following models:

K-Nearest Neighbors (KNN)

Logistic Regression

Naive Bayes

Support Vector Machine (SVM)

Decision Tree

After comparing accuracy, precision, recall, and F1 score:

✅ Final Selected Model: KNN

Accuracy: 88%

F1 Score: 89%

Performed the most stable on test data

Balanced precision–recall

Worked well with dataset distribution

Avoided overfitting compared to Decision Tree

Outperformed Logistic Regression on minority class detection

This makes KNN the best choice for reliable heart disease prediction in your project.

📊 Key Insights From Data Analysis (based on your screenshots)

You can adjust these slightly if needed:

Individuals with higher chest pain type (cp) often showed more risk.

Older age tended to have higher chances of heart disease.

High cholesterol and resting blood pressure were strongly associated with positive cases.

Maximum heart rate reached (thalach) was one of the strongest predictors — lower values increased risk.

The correlation heatmap showed that cp, thalach, oldpeak, and slope had strong influence on the target variable.

Your bar charts and countplots showed clear separation between healthy and diseased groups.

These analyses helped validate why simple distance-based methods like KNN performed so well.

📁 Project Structure
heart-disease-prediction/
│
├── notebooks/
│   └── heart_disease_prediction.ipynb     # Training & EDA
│
├── model/
│   └── knn_model.pkl                       # Final ML model
│
├── streamlit_app/
│   └── app.py                              # Frontend UI
│   └── components/                         # Input UI elements
│
├── screenshots/
│   ├── heatmap.png
│   ├── pairplot.png
│   ├── distribution.png
│   └── model_comparison.png
│
├── requirements.txt
└── README.md

🛠️ Tech Stack
Machine Learning

Python

NumPy

Pandas

Scikit-Learn

Matplotlib

Seaborn

Frontend

Streamlit

You didn’t use HTML/CSS/JS — your entire UI is Streamlit-based for simplicity and fast prototyping.

▶️ How to Run the Project
1️⃣ Clone the repo
git clone https://github.com/YOUR-USERNAME/heart-disease-prediction.git
cd heart-disease-prediction

2️⃣ Install requirements
pip install -r requirements.txt

3️⃣ Run Streamlit App
streamlit run streamlit_app/app.py

📸 Screenshots

Add these images in the screenshots/ folder and link like this:

🔹 Heatmap

🔹 Pairplot

🔹 Model Comparison

🔹 Streamlit UI

🙌 Author

Aman Goswami
Machine Learning & Data Analysis Enthusiast
