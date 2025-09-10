# Darya Bernard - Portfolio Website

A professional portfolio website for videographer and photographer Darya Bernard, featuring an admin panel for easy content management.

## Features

### Public Website
- **Home Page**: Auto-playing demo reel with about section and contact information
- **Video Galleries**: Art, Corporate, and Social video showcases with fullscreen viewing
- **Photo Galleries**: People, Places, and Sports photography with scroll-triggered animations
- **Responsive Design**: Mobile-friendly layout with custom styling
- **Modern UI**: Clean design with specified color scheme (#FAF0DC background, #A67A5B text)

### Admin Panel
- **Content Management**: Edit about information, contact details
- **Video Management**: Upload and manage videos for each category
- **Photo Management**: Upload and organize photos for each gallery
- **Real-time Updates**: Changes reflect immediately on the website

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Navigate to the project directory:**
   ```bash
   cd "h:\Coding Projects\Python\darya-website"
   ```

2. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Access the website:**
   - Public website: http://localhost:5000
   - Admin panel: http://localhost:5000/admin
   - Admin password: `darya_admin_2024` (change this in production!)

## File Structure

```
darya-website/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── website_data.json     # Data storage (auto-created)
├── templates/            # HTML templates
│   ├── base.html         # Base template with styling
│   ├── index.html        # Home page
│   ├── art.html          # Art video gallery
│   ├── corporate.html    # Corporate video gallery
│   ├── social.html       # Social video gallery
│   ├── people.html       # People photo gallery
│   ├── places.html       # Places photo gallery
│   ├── sports.html       # Sports photo gallery
│   ├── admin.html        # Admin panel
│   └── admin_login.html  # Admin login page
└── static/               # Static files
    ├── videos/           # Video files
    └── photos/           # Photo files
        ├── people/       # People photography
        ├── places/       # Places photography
        └── sports/       # Sports photography
```

## Adding Content

### Videos
1. Place video files in the `static/videos/` directory
2. Use the admin panel to set main videos and manage galleries
3. Supported formats: MP4, WebM, OGG

### Photos
1. Place photo files in the appropriate `static/photos/[category]/` directory
2. Use the admin panel to manage photo galleries
3. Supported formats: JPG, JPEG, PNG, WebP

### Admin Panel Usage
1. Go to http://localhost:5000/admin
2. Login with password: `darya_admin_2024`
3. Edit about information, upload videos/photos, manage content
4. Changes are saved automatically

## Customization

### Colors
- Background: #FAF0DC
- Text: #A67A5B
- Hover: #bec991

### Font
- Primary: Inter (Google Fonts)
- Fallback: Sans-serif

### Styling
All custom CSS is in the `base.html` template for easy modification.

## Production Deployment

For production deployment:

1. **Change the admin password** in `app.py`:
   ```python
   if password == 'your_secure_password_here':
   ```

2. **Set a secure secret key** in `app.py`:
   ```python
   app.secret_key = 'your_very_secure_secret_key_here'
   ```

3. **Use a production WSGI server** like Gunicorn:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:8000 app:app
   ```

4. **Set up a reverse proxy** with Nginx or Apache

5. **Use a proper database** instead of JSON file storage

## Browser Support

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## Features Implemented

✅ Home page with auto-playing demo reel  
✅ Horizontal menu with dropdown submenus  
✅ Video galleries (Art, Corporate, Social)  
✅ Photo galleries (People, Places, Sports)  
✅ Fullscreen viewing for videos and photos  
✅ Scroll-triggered photo animations  
✅ Admin panel for content management  
✅ Responsive design  
✅ Custom color scheme and typography  
✅ Video and photo upload functionality  

## Support

For technical support or questions about the website, contact the developer or refer to the Flask documentation for advanced customization.

---

**Note**: This website is designed specifically for Darya Bernard's portfolio. All styling and functionality are tailored to her requirements as specified in the project brief.

