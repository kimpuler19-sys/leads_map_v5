# 🚀 LightFantastic AI Lead Pro

**Enterprise Lead Generation & Outreach Platform**  
*v2.0 • Modular Architecture*

---

## Welcome

Welcome to **LightFantastic AI Lead Pro** — your all-in-one solution for scraping business leads, generating AI-powered outreach, and managing campaigns.

> ✅ **Quick Start Summary:**  
> **First time:** Run `installer.bat` → enter API keys in `config.py` → launch.  
> **Every day:** Double-click `launcher.bat` and start working.

---

## 🖥️ 1. First-Time Installation

The installer will automatically handle everything including Python installation. Just follow these simple steps:

### 1.1 Run the Installer (Everything Included)

1. **Extract the application package** to a folder on your computer (e.g. `C:\AI_Lead_Pro`).

2. **Double-click `installer.bat`**  
   The installer will automatically check if Python is installed.

3. **If Python is not found**, the installer will ask:  
   *“Download and install Python automatically? (Y/N)”*  
   Press `Y` to let the installer download and install Python 3.11.9 automatically.

4. **When prompted, choose “Y” for virtual environment** (recommended)  
   Wait for the installation to finish.

> ✅ **Python Auto-Installation:** The installer will download Python 3.11.9 from python.org, install it silently, and automatically add it to your system PATH. No manual steps required!

### 1.2 Launch for the First Time

5. **Double-click `launcher.bat`**  
   The application will start and open your browser automatically.

> ✅ **You're all set!** The application is now installed and ready for daily use.

---

## ⚡ 2. Daily Usage

Once the application is installed, using it every day is as simple as **one click**.

### 2.1 Quick Start

1. **Double-click `launcher.bat`**  
   That's it! The launcher will:
   - Check Python and installed packages
   - Start the Streamlit server
   - Open your browser to `http://localhost:8501`

> ⚠️ **Important:** Keep the command prompt window open while using the application. Closing it will stop the server.

### 2.2 What to Do in the Application

| Tab | What It Does | Action |
|-----|--------------|--------|
| **🏢 Profile** | Set your company details (name, product, offer, CTA) | Fill in once, save |
| **🔍 Scraper** | Search Google Maps for leads & generate AI emails | Enter keyword, location, click Start |
| **📊 Dashboard** | View campaign metrics & charts | Monitor performance |
| **✉️ Email** | Send bulk emails using your company profile | Configure SMTP, select leads, send |
| **💬 WhatsApp** | Generate & send WhatsApp messages | Select template, generate, send |
| **🌍 Multi Language** | Generate messages in 10+ Asian languages | Select language, generate |
| **📜 History** | View and download previous scraped data | Select file, download |

### 2.3 Stop the Application

2. **Go to the command prompt window** where the launcher is running.

3. **Press `Ctrl + C`**  
   Confirm with `Y` if prompted.

4. **Close the window** or press any key to exit.

---

## 📁 3. File Reference

Here is a quick overview of the files you will see in the application folder:

| File / Folder | Purpose |
|---------------|---------|
| `launcher.bat` | **Daily launch** — one click to start the app |
| `installer.bat` | **First-time setup** — installs Python + all packages |
| `config.py` | **API keys** — add your SerpApi and Groq keys here |
| `main_app.py` | Main application entry point |
| `core_*.py` (3 files) | Core business logic (auth, scraping, messaging) |
| `main_*.py` (3 files) | User interface components |
| `history/` | Folder where all scraped CSV files are saved |
| `*.json` files | Configuration & settings (company profile, email, etc.) |

---

## 🔧 4. Troubleshooting

> ❌ **“Python is not installed”**  
> Run `installer.bat` again and choose **Y** when asked to download Python automatically.

> ❌ **Application won't start**  
> Run `installer.bat` again to reinstall packages.

> ❌ **No results from scraping**  
> Check your SerpApi key in `config.py` and make sure you have credits.

> ❌ **Email sending fails**  
> For Gmail, use an **App Password** (not your regular password). Go to your Google Account → Security → App Passwords.

> ❌ **Port 8501 is already in use**  
> Change the port in `launcher.bat`:
> ```bash
> streamlit run main_app.py --server.port 8502
> ```

> ❌ **Python not found after auto-install**  
> Restart your computer or open a new Command Prompt window. The installer adds Python to PATH but it may need a restart.

> 💡 **Need more help?**  
> Contact support at [admin@kimpuler.com](mailto:admin@kimpuler.com)

---

## 📋 5. Quick Reference

| 🖥️ **First Install** | ⚡ **Daily Use** | 🔑 **API Keys** |
|----------------------|------------------|-----------------|
| 1. Run `installer.bat` | 1. Double-click `launcher.bat` | **SerpApi:** serpapi.com |
| 2. Press `Y` for Python auto-install | 2. Browser opens automatically | **Groq:** groq.com |
| 3. Add API keys to `config.py` | 3. Start scraping & sending | Edit in `config.py` |
| 4. Run `launcher.bat` | | |

---

## ✨ 6. What's New in v2.0

> 🚀 **Auto Python Installation**  
> The installer now automatically downloads and installs Python if it's not found on your system. No more manual Python setup required!

- **Modular Architecture:** 7 files (3 Core + 4 Main) for better maintainability
- **Auto Python Install:** Downloads and installs Python 3.11.9 automatically
- **API Keys in Config:** Keys stored in `config.py` (not in UI)
- **Multi Language Support:** 10+ Asian languages for outreach
- **Improved Email Extraction:** 80-90% success rate
- **Lead Scoring:** Automatic priority ranking based on multiple factors

---

## 📄 License

**LightFantastic AI Lead Pro v2.0** • Built with ❤️ by Kimpuler.com + PodiumVS

© 2026 All Rights Reserved • Support: [admin@kimpuler.com](mailto:admin@kimpuler.com)
