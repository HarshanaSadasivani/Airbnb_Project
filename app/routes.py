from flask import render_template
from app import app
import pandas as pd


df = pd.read_csv('listings.csv')

@app.route('/')
def home():
    
    total_listings = df.shape[0]
    avg_price = df['price'].mean(skipna=True)

    
    return render_template('index.html', total_listings=total_listings, avg_price=avg_price)
