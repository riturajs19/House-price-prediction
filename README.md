# House-price-prediction
This project focuses on building a machine learning model to predict house prices based on key features such as total square footage, number of bedrooms (BHK), and bathrooms. With real estate being a critical sector, accurate pricing models are useful for both buyers and sellers. The project involves data preprocessing, model training using Ridge Regression, and finally, deployment through a user-friendly web interface built with Flask.
# 📌 Project Overview
The dataset used in this project (Cleaned_data.csv) contains cleaned and processed information about house listings, including location-based features, square footage, number of bathrooms, and BHK units. The initial analysis involved checking for outliers, data inconsistencies, and missing values. After thorough cleaning and feature selection, the dataset was prepared for modeling.

# ⚙️ Methodology and Model
We experimented with multiple regression algorithms and selected Ridge Regression for its ability to handle multicollinearity and produce robust predictions. The data was transformed using one-hot encoding for categorical features like location. The model was trained and evaluated using standard metrics such as R² score and Mean Squared Error. Once the model was finalized, it was serialized using pickle and saved as RidgeModel.pkl.

The application takes three inputs from the user: number of bedrooms (BHK), number of bathrooms, and total square footage. These are then passed to the trained model, which returns a price prediction. The entire backend logic is handled by a Flask application (main.py) that connects the HTML frontend with the machine learning model.

#🚀 Deployment
The project includes a simple web interface built using HTML (stored in the templates/ folder). Users can input property details directly into the form, and the Flask backend (main.py) processes the input and displays the predicted price. To run the project locally, install the required dependencies, launch the Flask app, and access it via http://localhost:5000 on your browser.

To deploy it on platforms like Render, Heroku, or Replit, additional setup such as requirements.txt, Procfile, and runtime configuration may be needed.

# ✅ Conclusion
This project demonstrates a complete pipeline of a machine learning application — from data preprocessing to model training, evaluation, and deployment. It provides a practical example of how data science can be applied in real-world domains like real estate. The web interface makes it easy for non-technical users to interact with the model and get instant price predictions.
