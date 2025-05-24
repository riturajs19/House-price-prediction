# House Price Prediction
This project focuses on building a machine learning model to predict house prices based on key features such as total square footage, number of bedrooms (BHK), and bathrooms. With real estate being a critical sector, accurate pricing models are useful for both buyers and sellers. The project involves data preprocessing, model training using Ridge Regression, and deployment through user-friendly web interfaces built with Flask and Streamlit.

## ⚙️ Methodology and Model
We experimented with multiple regression algorithms and selected Ridge Regression for its ability to handle multicollinearity and produce robust predictions. The data was transformed using one-hot encoding for categorical features like location. Once the model was finalized, it was serialized using pickle and saved as RidgeModel.pkl. The application takes four inputs from the user: location, number of bedrooms (BHK), number of bathrooms, and total square feet. These inputs are then passed to the trained model, which returns a price prediction.

Flask Version: The backend logic is handled by a Flask application (main.py), which connects an HTML frontend (in templates/) to the machine learning model.

Streamlit Version: Alternatively, the app is implemented as a single interactive Streamlit app (app.py), which combines frontend and backend logic in one place for easy deployment and interaction.

## 🚀 Deployment
Flask App:
The Flask app provides a simple web interface built with HTML forms.
To run locally:
-Install dependencies from requirements.txt
-Run python main.py
-Access the app at http://localhost:5000
For cloud deployment (e.g., Render, Heroku, Replit), you may need to add configuration files like Procfile, and set up environment variables.

Streamlit App:
The Streamlit app provides an interactive web interface accessible through the browser.
-To run locally:
-Install dependencies from requirements.txt
-Run streamlit run app.py
-Open the local URL shown in the terminal (http://localhost:8503/#house-price-prediction-app)
Deploy easily on Streamlit Community Cloud by connecting your GitHub repository.

## ✅ Conclusion
This project demonstrates a full machine learning pipeline—from data preprocessing and model training to deployment with two popular web frameworks: Flask and Streamlit. The Flask version offers more control over frontend design using HTML templates, while the Streamlit version allows rapid prototyping and deployment with minimal setup.

Both implementations make machine learning accessible to end users, enabling instant and accurate house price predictions through a clean and user-friendly web interface.
