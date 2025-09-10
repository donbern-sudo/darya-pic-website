# Darya Bernard Website - Deployment Guide

## 🚀 Quick Deployment Options

### Option 1: Railway (Recommended - Easiest)

**Why Railway?**
- ✅ Free tier available
- ✅ Automatic deployments from Git
- ✅ Built-in SSL certificates
- ✅ Easy environment variable management
- ✅ 99.9% uptime guarantee

**Steps:**
1. Go to [railway.app](https://railway.app) and sign up
2. Connect your GitHub account
3. Create a new project from GitHub
4. Select your `darya-website` repository
5. Railway will automatically detect it's a Python app
6. Add environment variables:
   - `SECRET_KEY`: Generate a random string (32+ characters)
   - `ADMIN_PASSWORD`: Set a secure password for admin access
7. Deploy! Your site will be live at `https://your-app-name.railway.app`

**Cost:** Free for 500 hours/month, then $5/month

---

### Option 2: Render (Great for Portfolios)

**Why Render?**
- ✅ Free tier with custom domain support
- ✅ Automatic SSL
- ✅ Easy Git integration
- ✅ Great for static sites and web apps

**Steps:**
1. Go to [render.com](https://render.com) and sign up
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Environment:** Python 3
5. Add environment variables:
   - `SECRET_KEY`: Your secret key
   - `ADMIN_PASSWORD`: Admin password
6. Deploy!

**Cost:** Free tier available, $7/month for production

---

### Option 3: DigitalOcean App Platform

**Why DigitalOcean?**
- ✅ Very reliable (99.99% uptime)
- ✅ Great performance
- ✅ Easy scaling
- ✅ Professional features

**Steps:**
1. Go to [DigitalOcean App Platform](https://cloud.digitalocean.com/apps)
2. Create new app from GitHub
3. Select your repository
4. Configure:
   - **Type:** Web Service
   - **Build Command:** `pip install -r requirements.txt`
   - **Run Command:** `gunicorn app:app`
5. Add environment variables
6. Deploy!

**Cost:** $5/month

---

## 🔧 Pre-Deployment Setup

### 1. Update Admin Password
Before deploying, change the admin password in `app.py`:

```python
# Change this line:
if password == 'darya_admin_2025':  # Simple password, change in production

# To something secure like:
if password == 'YourSecurePassword123!':
```

### 2. Set Up Git Repository
If you haven't already:

```bash
cd "h:\Coding Projects\Python\darya-website"
git init
git add .
git commit -m "Initial commit - Darya's portfolio website"
git branch -M main
git remote add origin https://github.com/yourusername/darya-website.git
git push -u origin main
```

### 3. Environment Variables
Set these in your deployment platform:

- `SECRET_KEY`: Random string (32+ characters)
- `ADMIN_PASSWORD`: Secure password for admin access
- `PORT`: Usually set automatically by the platform

---

## 📝 How to Edit the Website After Deployment

### Method 1: Through Admin Panel (Easiest)
1. Go to `https://your-website.com/admin`
2. Login with your admin password
3. Edit content directly through the web interface
4. Changes save automatically

### Method 2: Through Git (For Code Changes)
1. Make changes to your local files
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Updated website content"
   git push
   ```
3. Your deployment platform will automatically redeploy

### Method 3: Direct File Upload
- Most platforms allow you to upload files directly
- Upload new photos/videos to the appropriate folders
- Use the admin panel to manage them

---

## 🎯 Recommended Workflow

### For Content Updates (Photos, Videos, Text):
1. Use the admin panel at `/admin`
2. Upload new content through the web interface
3. No technical knowledge required

### For Code Changes (New features, styling):
1. Edit files locally
2. Test with `python app.py`
3. Commit and push to GitHub
4. Platform automatically redeploys

---

## 🔒 Security Checklist

- [ ] Changed admin password from default
- [ ] Set a secure SECRET_KEY
- [ ] Enable HTTPS (automatic on most platforms)
- [ ] Regular backups of website_data.json
- [ ] Monitor admin access logs

---

## 📊 Monitoring & Maintenance

### Check Website Status
- Most platforms provide dashboards
- Set up uptime monitoring (UptimeRobot, Pingdom)
- Monitor error logs

### Regular Tasks
- Update content through admin panel
- Backup website data monthly
- Check for platform updates
- Monitor storage usage

---

## 🆘 Troubleshooting

### Website Not Loading
1. Check platform status page
2. Verify environment variables
3. Check build logs
4. Ensure all files are committed to Git

### Admin Panel Not Working
1. Verify admin password is correct
2. Check if SECRET_KEY is set
3. Clear browser cache
4. Try incognito mode

### Content Not Updating
1. Check if changes were saved
2. Clear browser cache
3. Verify file permissions
4. Check platform logs

---

## 💡 Pro Tips

1. **Custom Domain**: Most platforms allow custom domains (e.g., `daryabernard.com`)
2. **CDN**: Use Cloudflare for faster loading worldwide
3. **Backups**: Export website_data.json regularly
4. **Analytics**: Add Google Analytics for visitor tracking
5. **SEO**: Add meta tags for better search engine visibility

---

## 📞 Support

If you need help with deployment:
1. Check the platform's documentation
2. Look at the build/deployment logs
3. Contact the platform's support
4. Refer to Flask deployment guides

---

**Your sister's website will be live 24/7 and easily editable! 🎉**
