# House-price-prediction
This project focuses on building a machine learning model to predict house prices based on key features such as total square footage, number of bedrooms (BHK), and bathrooms. With real estate being a critical sector, accurate pricing models are useful for both buyers and sellers. The project involves data preprocessing, model training using Ridge Regression, and finally, deployment through a user-friendly web interface built with Flask.

# ⚙️ Methodology and Model
We experimented with multiple regression algorithms and selected Ridge Regression for its ability to handle multicollinearity and produce robust predictions. The data was transformed using one-hot encoding for categorical features like location. Once the model was finalized, it was serialized using pickle and saved as RidgeModel.pkl.

The application takes four inputs from the user: location, number of bedrooms (BHK), number of bathrooms, and total square feet. These are then passed to the trained model, which returns a price prediction. The entire backend logic is handled by a Flask application (main.py) that connects the HTML frontend with the machine learning model.

# 🚀 Deployment
The project includes a simple web interface built using HTML (stored in the templates/ folder). Users can input property details directly into the form, and the Flask backend (main.py) processes the input and displays the predicted price. To run the project locally, install the required dependencies, launch the Flask app, and access it via http://localhost:5000 on your browser. To deploy it on platforms like Render, Heroku, or Replit, additional setup such as requirements.txt, Procfile, and runtime configuration may be needed.

# ✅ Conclusion
This project demonstrates a complete pipeline of a machine learning application — from data preprocessing to model training, evaluation, and deployment. It provides a practical example of how data science can be applied in real-world domains like real estate. The web interface makes it easy for non-technical users to interact with the model and get instant price predictions.
