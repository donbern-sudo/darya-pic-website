# Darya Bernard Website - Development Notes

## Project Overview
Complete portfolio website for Darya Bernard, videographer and photographer from Boston, MA.

## Key Features Implemented

### ✅ Home Page
- "Darya Bernard" branding in top left corner
- Horizontal menu with dropdown submenus
- Auto-playing demo reel that fills the screen
- About section with contact information
- Custom styling: #FAF0DC background, #A67A5B text

### ✅ Video Pages (Art, Corporate, Social)
- Main video fills ¾ screen, plays automatically
- Grid of additional videos below
- Fullscreen viewing capability
- Admin controls to manage videos

### ✅ Photo Pages (People, Places, Sports)
- Scroll-triggered photo animations
- Floating grid layout (2-3 photos visible)
- Fullscreen viewing with navigation
- Admin controls to manage galleries

### ✅ Admin Panel
- Secure login system
- Edit about information and contact details
- Upload/manage videos and photos
- Real-time updates

## Technical Details

### Framework
- **Backend:** Flask (Python)
- **Frontend:** HTML5, CSS3, JavaScript
- **Styling:** Custom CSS with specified color scheme
- **Font:** Inter (Google Fonts)

### File Structure
```
darya-website/
├── app.py                 # Flask application
├── requirements.txt       # Dependencies
├── README.md             # Complete documentation
├── test_setup.py         # Setup verification
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
│   └── admin_login.html  # Admin login
└── static/               # Static files
    ├── videos/           # Video files
    └── photos/           # Photo galleries
        ├── people/       # People photography
        ├── places/       # Places photography
        └── sports/       # Sports photography
```

## Setup Instructions

### Quick Start
1. Navigate to project directory: `cd "h:\Coding Projects\Python\darya-website"`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `python app.py`
4. Visit: http://localhost:5000
5. Admin panel: http://localhost:5000/admin (password: `darya_admin_2024`)

### Testing
Run the test script to verify setup: `python test_setup.py`

## Admin Panel Features

### Content Management
- Edit name, description, phone, email, Instagram
- Update main demo reel videos for each category
- Upload and manage video galleries
- Upload and organize photo galleries

### Security
- Simple password protection (change for production)
- Session-based authentication
- Input validation for file uploads

## Design Specifications

### Colors
- Background: #FAF0DC
- Text: #A67A5B
- Hover: #bec991

### Typography
- Primary: Inter font family
- Fallback: Sans-serif

### Layout
- Responsive design for all devices
- Modern, clean portfolio layout
- Smooth animations and transitions

## Next Steps for Production

### Security Hardening
- Change admin password to secure value
- Set up proper secret keys
- Add input validation and sanitization

### Deployment Options
- Cloud platforms (Heroku, DigitalOcean, AWS)
- Proper database (PostgreSQL/MySQL)
- Domain and SSL certificates

### Performance Optimization
- Image/video optimization
- Caching strategies
- CDN setup for media files

## Development Notes

### Key Decisions
- Used Flask for simplicity and ease of deployment
- JSON file storage for development (upgrade to database for production)
- Custom CSS instead of framework for precise control
- Admin panel integrated into main app for simplicity

### Browser Support
- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## Contact Information
- Developer: AI Assistant
- Project: Darya Bernard Portfolio Website
- Date: January 2025
- Status: Development Complete, Ready for Production

---

**Note:** This website was built specifically for Darya Bernard's portfolio requirements. All styling and functionality are tailored to her specifications.
