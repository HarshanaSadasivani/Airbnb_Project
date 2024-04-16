from flask import Flask, render_template, jsonify, request, redirect, url_for
import pandas as pd

app = Flask(__name__, template_folder='templates', static_folder='static')


df = pd.read_csv('listings.csv')


users = {
    "user1": "password1",
    "user2": "password2",
}


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']
    
    if username in users and users[username] == password:
        
        return redirect(url_for('main_page'))
    else:
        
        return redirect(url_for('login'))


@app.route('/main_page')
def main_page():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        
        
        return redirect(url_for('main_page'))
    else:
        return render_template('signup.html')



@app.route('/get_unique_property_types')
def get_unique_property_types():
    unique_property_types = df['property_type'].unique().tolist()
    return jsonify(unique_property_types=unique_property_types)


@app.route('/get_listing_details', methods=['POST'])
def get_listing_details():
    selected_property_type = request.form.get('selected_property_type')
    
    
    selected_listing = df[df['property_type'] == selected_property_type].iloc[0]
    
    
    listing_url = selected_listing['listing_url']
    description = selected_listing['description']
    picture_url = selected_listing['picture_url']
    host_name = selected_listing['host_name']
    
    
    amenities = selected_listing['amenities'].replace('[', '').replace(']', '').replace('"', '').split(', ')
    
    
    return jsonify(listing_url=listing_url,
                   description=description,
                   picture_url=picture_url,
                   host_name=host_name,
                   amenities=amenities)

if __name__ == '__main__':
    app.run(debug=True)
