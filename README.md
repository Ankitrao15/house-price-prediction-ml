# House Price Prediction using Machine Learning

A GitHub-ready beginner ML project that predicts house values using Linear Regression.

## Tech Stack
Python, Pandas, NumPy, Scikit-learn, Joblib, Streamlit

## Project Structure
- `train.py` - trains and evaluates the model
- `predict.py` - makes a sample prediction
- `app.py` - Streamlit web application
- `data/california_housing.csv` - sample dataset
- `requirements.txt` - dependencies

## Run
```bash
pip install -r requirements.txt
python train.py
python predict.py
streamlit run app.py
```

## Model
Linear Regression with an 80/20 train-test split. Evaluation includes MAE, RMSE and R2.

## GitHub Repository Name
`house-price-prediction-ml`
