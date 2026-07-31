🚀 First-Time Installation
Step 1: Install Python
Download Python from: python.org/downloads

IMPORTANT: Check "Add Python to PATH" during installation

Verify installation:

Press Win + R, type cmd, press Enter

Type: python --version

You should see: Python 3.x.x

Step 2: Install the Application
Extract the application package to your computer

Double-click installer.bat

When prompted:

Choose "Y" for virtual environment (recommended)

Wait for installation to complete

When asked "Launch now?", select "Y"


API Service	Where to Get	What It Does
SerpApi	serpapi.com	Google Maps scraping
Groq	groq.com	AI content generation
🖥️ Daily Usage
Quick Start
Double-click launcher.bat

The application will automatically:

Check Python installation

Install missing packages (if any)

Start the server

Open your browser

Enter your API keys in the sidebar

Start generating leads!

Or Run Manually
Open Command Prompt in the application folder:

bash
streamlit run main_app.py
📁 Application Files
File	Purpose
launcher.bat	Quick start - use this daily
installer.bat	First-time setup only
main_app.py	Main application entry point
core_*.py	Core functions (3 files)
main_*.py	UI components (4 files)
history/	Saved lead data folder
*.json	Configuration files
🎯 Step-by-Step Usage Guide
1. Configure Your Company Profile
Go to the "🏢 Profile" tab

Fill in your company details:

Company name, phone, email

Product/service name

Special offer

Call to action

Click "Save Company Profile"

2. Scrape Leads
Go to the "🔍 Scraper" tab

Enter:

Keyword: e.g., "Restaurant", "Dentist", "Plumber"

Location: e.g., "Los Angeles", "London"

Max Leads: 5-50

Click "Start Scraping"

Wait for the AI to generate personalized emails

3. Export or Send
Download CSV: Use the download button

Send Emails: Go to "✉️ Email" tab

Send WhatsApp: Go to "💬 WhatsApp" tab

4. Track Performance
Go to the "📊 Dashboard" tab

View metrics and charts

🔧 Troubleshooting
Application Won't Start
Run installer again:

text
Double-click installer.bat
Check Python PATH:

Open Command Prompt

Type: python --version

If not found, reinstall Python with "Add to PATH"

Port 8501 in use:

Change port in launcher.bat:

Find --server.port 8501 and change to 8502

No Results from Scraping
Check SerpApi key is correct

Try different keywords/locations

Check SerpApi credits

Email Sending Fails
Use App Password for Gmail

Check SMTP settings:

Gmail: smtp.gmail.com:587 with TLS

Outlook: smtp.office365.com:587 with TLS

Need Support?
📧 Email: admin@kimpuler.com

📊 System Status
After installation, you should see:

text
✅ Python found: Version 3.x.x
✅ All packages installed
✅ Application files verified
✅ Environment prepared
🚀 Launching application...
🌐 URL: http://localhost:8501
⚠️ Important Notes
Do NOT close the launcher window while using the app

Press Ctrl+C in the window to stop the server

Save your data - CSV files are saved in history/ folder

API costs - SerpApi and Groq are paid services

Backup your *.json config files

📱 Support & Updates
📧 Support: admin@kimpuler.com

🔄 Updates: Download latest package from the provider

© 2026 Kimpuler Tech. All Rights Reserved.