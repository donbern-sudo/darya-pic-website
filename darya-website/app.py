from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import json
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'darya_website_secret_key_2024'

# Data storage (in production, use a proper database)
DATA_FILE = 'website_data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {
        'about': {
            'name': 'Darya Bernard',
            'description': 'Darya Bernard is a videographer and photographer from Boston, MA',
            'phone': '704-789-3492',
            'email': 'darya.bernard603@gmail.com',
            'instagram': '@jpegdarya'
        },
        'videos': {
            'art': {
                'main_video': 'Art demo reel.mp4',
                'gallery': []
            },
            'corporate': {
                'main_video': 'Corporate demo reel.mp4',
                'gallery': []
            },
            'social': {
                'main_video': 'Social demo reel.mp4',
                'gallery': []
            }
        },
        'photos': {
            'people': [],
            'places': [],
            'sports': []
        }
    }

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/')
def home():
    data = load_data()
    return render_template('index.html', data=data)

@app.route('/art')
def art():
    data = load_data()
    return render_template('art.html', data=data)

@app.route('/corporate')
def corporate():
    data = load_data()
    return render_template('corporate.html', data=data)

@app.route('/social')
def social():
    data = load_data()
    return render_template('social.html', data=data)

@app.route('/people')
def people():
    data = load_data()
    return render_template('people.html', data=data)

@app.route('/places')
def places():
    data = load_data()
    return render_template('places.html', data=data)

@app.route('/sports')
def sports():
    data = load_data()
    return render_template('sports.html', data=data)

@app.route('/admin')
def admin():
    if not session.get('admin_logged_in'):
        return render_template('admin_login.html')
    data = load_data()
    return render_template('admin.html', data=data)

@app.route('/admin/login', methods=['POST'])
def admin_login():
    password = request.form.get('password')
    if password == 'darya_admin_2024':  # Simple password, change in production
        session['admin_logged_in'] = True
        return redirect(url_for('admin'))
    return redirect(url_for('admin'))

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('home'))

@app.route('/api/update_about', methods=['POST'])
def update_about():
    if not session.get('admin_logged_in'):
        return jsonify({'error': 'Unauthorized'}), 401
    
    data = load_data()
    data['about'] = request.json
    save_data(data)
    return jsonify({'success': True})

@app.route('/api/update_video', methods=['POST'])
def update_video():
    if not session.get('admin_logged_in'):
        return jsonify({'error': 'Unauthorized'}), 401
    
    data = load_data()
    category = request.json.get('category')
    video_data = request.json.get('video_data')
    
    if category in data['videos']:
        data['videos'][category] = video_data
        save_data(data)
        return jsonify({'success': True})
    
    return jsonify({'error': 'Invalid category'}), 400

@app.route('/api/update_photos', methods=['POST'])
def update_photos():
    if not session.get('admin_logged_in'):
        return jsonify({'error': 'Unauthorized'}), 401
    
    data = load_data()
    category = request.json.get('category')
    photos = request.json.get('photos')
    
    if category in data['photos']:
        data['photos'][category] = photos
        save_data(data)
        return jsonify({'success': True})
    
    return jsonify({'error': 'Invalid category'}), 400

if __name__ == '__main__':
    app.run(debug=True)
