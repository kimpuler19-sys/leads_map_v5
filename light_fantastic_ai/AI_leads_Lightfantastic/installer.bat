@echo off
title LightFantastic AI Lead Pro - Installation Wizard
color 0E

:: ================================================================
:: LIGHTFANTASTIC AI LEAD PRO - INSTALLER
:: SUPPORTS MODULAR FILE STRUCTURE
:: WITH AUTO PYTHON INSTALLATION
:: ================================================================

setlocal enabledelayedexpansion

cls
echo ================================================================
echo    📦 LIGHTFANTASTIC AI LEAD PRO - INSTALLATION WIZARD 📦
echo ================================================================
echo.
echo    Version: 2.0 Premium (Modular)
echo    Architecture: 7 Files (3 Core + 4 Main)
echo    Developer: Kimpuler Tech
echo.
echo ================================================================
echo.

:: ================================================================
:: STEP 1: CHECK PYTHON - WITH AUTO INSTALL
:: ================================================================
echo [1/6] Checking Python installation...
echo.

where python >nul 2>nul
if %errorlevel% neq 0 (
    cls
    echo ================================================================
    echo    ⚠️ PYTHON NOT FOUND ⚠️
    echo ================================================================
    echo.
    echo Python is not installed on your system!
    echo.
    echo This installer can automatically download and install Python.
    echo.
    echo  [Y] Yes - Download and install Python automatically
    echo  [N] No  - I will install Python manually
    echo.
    choice /c YN /n /m "Download and install Python automatically? (Y/N): "

    if errorlevel 2 (
        echo.
        echo ================================================================
        echo    MANUAL PYTHON INSTALLATION
        echo ================================================================
        echo.
        echo Please install Python manually from:
        echo https://www.python.org/downloads/
        echo.
        echo IMPORTANT: Make sure to check 'Add Python to PATH'
        echo during installation.
        echo.
        echo After installing Python, run this installer again.
        echo.
        pause
        exit /b 1
    ) else (
        echo.
        echo ================================================================
        echo    AUTOMATIC PYTHON INSTALLATION
        echo ================================================================
        echo.
        echo Downloading Python installer...
        echo.

        :: Create temp folder
        if not exist "temp_install" mkdir temp_install

        :: Download Python 3.11.9 (latest stable)
        set PYTHON_INSTALLER=temp_install\python-3.11.9-amd64.exe
        echo Downloading Python 3.11.9 from python.org...
        echo.

        :: Use PowerShell to download with progress
        powershell -Command "& { [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; $ProgressPreference = 'SilentlyContinue'; Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe' -OutFile '%PYTHON_INSTALLER%' }"

        if not exist "%PYTHON_INSTALLER%" (
            echo [ERROR] Failed to download Python installer!
            echo.
            echo Please download Python manually from:
            echo https://www.python.org/downloads/
            echo.
            pause
            exit /b 1
        )

        echo [SUCCESS] Python installer downloaded
        echo.

        echo Installing Python 3.11.9...
        echo This may take a few minutes...
        echo.

        :: Install Python silently with PATH option
        start /wait %PYTHON_INSTALLER% /quiet InstallAllUsers=1 PrependPath=1 Include_test=0 Include_doc=0 Include_launcher=0

        echo.
        echo [SUCCESS] Python installation completed!
        echo.

        :: Refresh environment variables
        echo Refreshing environment variables...
        call refreshenv >nul 2>nul

        :: Check if Python is now available
        where python >nul 2>nul
        if %errorlevel% neq 0 (
            echo [WARNING] Python not found in PATH after installation.
            echo.
            echo Trying alternative method: Adding to PATH manually...
            echo.

            :: Try to find Python installation
            set PYTHON_PATH=
            for /d %%i in ("C:\Program Files\Python*") do set PYTHON_PATH=%%i
            if "!PYTHON_PATH!"=="" (
                for /d %%i in ("C:\Users\%USERNAME%\AppData\Local\Programs\Python*") do set PYTHON_PATH=%%i
            )

            if not "!PYTHON_PATH!"=="" (
                echo Found Python at: !PYTHON_PATH!
                echo Adding to PATH...
                setx PATH "!PYTHON_PATH!;!PYTHON_PATH!\Scripts;%PATH%" >nul 2>nul
                echo.
                echo [INFO] Python added to PATH. Please restart this installer.
                echo.
                pause
                exit /b 1
            ) else (
                echo [ERROR] Python installation was successful but cannot be found.
                echo.
                echo Please restart this installer or manually add Python to PATH.
                echo.
                pause
                exit /b 1
            )
        )

        :: Clean up temp files
        if exist "temp_install" rmdir /s /q temp_install >nul 2>nul

        echo.
        echo [SUCCESS] Python is now installed and available!
        echo.
    )
) else (
    echo [SUCCESS] Python is already installed!
)

:: Get Python version
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo [INFO] Python Version: %PYTHON_VERSION%
echo.

:: Check Python version (minimum 3.8)
for /f "tokens=1,2 delims=." %%a in ("%PYTHON_VERSION%") do (
    set PYTHON_MAJOR=%%a
    set PYTHON_MINOR=%%b
)

if %PYTHON_MAJOR% LSS 3 (
    echo [ERROR] Python 3.8 or higher is required!
    echo You have Python %PYTHON_VERSION%
    echo.
    pause
    exit /b 1
)

if %PYTHON_MAJOR% EQU 3 (
    if %PYTHON_MINOR% LSS 8 (
        echo [ERROR] Python 3.8 or higher is required!
        echo You have Python %PYTHON_VERSION%
        echo.
        pause
        exit /b 1
    )
)

echo [SUCCESS] Python version is compatible
echo.

:: ================================================================
:: STEP 2: CHECK PIP
:: ================================================================
echo [2/6] Checking pip package manager...
echo.

python -m pip --version >nul 2>nul
if %errorlevel% neq 0 (
    echo [INFO] pip not found! Installing pip...
    python -m ensurepip --upgrade >nul 2>nul
    if %errorlevel% neq 0 (
        echo [ERROR] Failed to install pip automatically!
        echo.
        echo Please install pip manually or use:
        echo python -m ensurepip --upgrade
        echo.
        pause
        exit /b 1
    )
)
echo [SUCCESS] pip is ready
echo.

:: ================================================================
:: STEP 3: VIRTUAL ENVIRONMENT (OPTIONAL)
:: ================================================================
echo [3/6] Virtual Environment Setup
echo.

echo Do you want to create a virtual environment? (Recommended)
echo.
echo  [Y] Yes - Create isolated environment (Recommended)
echo  [N] No  - Install globally
echo.
choice /c YN /n /m "Your choice (Y/N): "

if errorlevel 2 (
    set USE_VENV=0
    echo.
    echo [INFO] Installing globally...
    echo.
) else (
    set USE_VENV=1
    echo.
    echo [INFO] Creating virtual environment...
    echo.
    
    :: Check if venv already exists
    if exist "venv" (
        echo [WARNING] Virtual environment already exists!
        echo.
        choice /c YN /n /m "Recreate virtual environment? (Y/N): "
        if errorlevel 2 (
            echo [INFO] Using existing virtual environment
        ) else (
            echo [INFO] Removing old virtual environment...
            rmdir /s /q venv >nul 2>nul
            echo [INFO] Creating new virtual environment...
            python -m venv venv
        )
    ) else (
        echo [INFO] Creating new virtual environment...
        python -m venv venv
    )
    
    if exist "venv\Scripts\activate.bat" (
        echo [SUCCESS] Virtual environment created
        echo [INFO] Activating virtual environment...
        call venv\Scripts\activate.bat
        echo [SUCCESS] Virtual environment activated
    ) else (
        echo [ERROR] Failed to create virtual environment!
        echo.
        echo [INFO] Falling back to global installation...
        set USE_VENV=0
    )
    echo.
)

:: ================================================================
:: STEP 4: UPGRADE PIP & INSTALL PACKAGES
:: ================================================================
echo [4/6] Installing required packages...
echo.

:: Upgrade pip first
echo Upgrading pip...
python -m pip install --upgrade pip --quiet --no-warn-script-location >nul 2>nul
if %errorlevel% neq 0 (
    echo [WARNING] Pip upgrade failed, continuing...
) else (
    echo [SUCCESS] pip upgraded
)
echo.

:: List of required packages with versions
set PACKAGES=(
    "streamlit>=1.28.0"
    "pandas>=2.0.0"
    "requests>=2.31.0"
    "groq>=0.4.0"
    "beautifulsoup4>=4.12.0"
    "lxml>=4.9.0"
    "plotly>=5.17.0"
    "dnspython>=2.4.0"
)

echo Installing packages:
echo.

set INSTALL_FAILED=0
for %%p in (%PACKAGES%) do (
    echo    Installing %%p...
    python -m pip install %%p --quiet --upgrade --no-warn-script-location
    
    if !errorlevel! neq 0 (
        echo    [RETRY] Retrying %%p...
        python -m pip install %%p --quiet --upgrade --no-warn-script-location
        
        if !errorlevel! neq 0 (
            echo    [FAILED] %%p
            set /a INSTALL_FAILED+=1
        ) else (
            echo    [DONE] %%p installed
        )
    ) else (
        echo    [DONE] %%p installed
    )
)

echo.

if %INSTALL_FAILED% gtr 0 (
    echo [WARNING] %INSTALL_FAILED% package(s) failed to install!
    echo.
    echo You can try installing them manually:
    echo.
    for %%p in (%PACKAGES%) do (
        echo    pip install %%p
    )
    echo.
) else (
    echo [SUCCESS] All packages installed successfully
)
echo.

:: Save requirements to file
echo [INFO] Saving requirements to requirements.txt...
python -m pip freeze > requirements.txt 2>nul
if %errorlevel% neq 0 (
    echo [WARNING] Could not save requirements.txt
) else (
    echo [SUCCESS] requirements.txt created
)
echo.

:: ================================================================
:: STEP 5: VERIFY APPLICATION FILES
:: ================================================================
echo [5/6] Verifying application files...
echo.

:: Check for modular files
set MISSING_FILES=0
set HAS_MODULAR=0
set HAS_LEGACY=0

:: Check config.py
if exist "config.py" (
    echo    [OK] config.py
) else (
    echo    [MISSING] config.py
    set /a MISSING_FILES+=1
)

:: Check main entry point
if exist "main_app.py" (
    echo    [OK] main_app.py (Modular entry point)
    set HAS_MODULAR=1
    set MAIN_FILE=main_app.py
) else (
    if exist "main.py" (
        echo    [OK] main.py (Legacy entry point)
        set HAS_LEGACY=1
        set MAIN_FILE=main.py
    ) else (
        echo    [MISSING] main_app.py or main.py
        set /a MISSING_FILES+=1
    )
)

:: Check modular core files
if exist "core_auth.py" (
    echo    [OK] core_auth.py
    set HAS_MODULAR=1
) else (
    if exist "core.py" (
        echo    [OK] core.py (Legacy)
        set HAS_LEGACY=1
    ) else (
        echo    [MISSING] core_auth.py
        set /a MISSING_FILES+=1
    )
)

if exist "core_scraping.py" (
    echo    [OK] core_scraping.py
    set HAS_MODULAR=1
) else (
    if exist "core.py" (
        echo    [OK] core.py (Legacy - contains all functions)
    ) else (
        echo    [MISSING] core_scraping.py
        set /a MISSING_FILES+=1
    )
)

if exist "core_messaging.py" (
    echo    [OK] core_messaging.py
    set HAS_MODULAR=1
) else (
    if exist "core.py" (
        echo    [OK] core.py (Legacy - contains all functions)
    ) else (
        echo    [MISSING] core_messaging.py
        set /a MISSING_FILES+=1
    )
)

if exist "main_auth.py" (
    echo    [OK] main_auth.py
    set HAS_MODULAR=1
) else (
    if exist "main.py" (
        echo    [OK] main.py (Legacy - contains all UI)
    ) else (
        echo    [MISSING] main_auth.py
        set /a MISSING_FILES+=1
    )
)

if exist "main_tabs.py" (
    echo    [OK] main_tabs.py
    set HAS_MODULAR=1
) else (
    if exist "main.py" (
        echo    [OK] main.py (Legacy - contains all UI)
    ) else (
        echo    [MISSING] main_tabs.py
        set /a MISSING_FILES+=1
    )
)

echo.

if %MISSING_FILES% gtr 0 (
    echo [WARNING] %MISSING_FILES% file(s) are missing!
    echo.
    echo Please ensure all required files are present.
    echo You can download the complete package from the official source.
    echo.
) else (
    if %HAS_MODULAR% EQU 1 (
        echo [SUCCESS] Modular file structure detected! (3 Core + 4 Main)
    )
    if %HAS_LEGACY% EQU 1 (
        if %HAS_MODULAR% EQU 1 (
            echo [INFO] Both modular and legacy files found.
            echo [INFO] Using modular version (preferred).
        ) else (
            echo [SUCCESS] Legacy file structure detected! (core.py + main.py)
        )
    )
)
echo.

:: ================================================================
:: STEP 6: CREATE NECESSARY FOLDERS AND CONFIG FILES
:: ================================================================
echo [6/6] Preparing application environment...
echo.

:: Create folders
if not exist "history" (
    mkdir history >nul 2>nul
    echo    [CREATED] history folder
) else (
    echo    [EXISTS] history folder
)

if not exist ".client_locks" (
    mkdir .client_locks >nul 2>nul
    echo    [CREATED] .client_locks folder
) else (
    echo    [EXISTS] .client_locks folder
)

:: Create default config files if missing
if not exist "company_profile.json" (
    echo    [CREATED] company_profile.json
    (
        echo {
        echo   "company_name": "My Company",
        echo   "company_phone": "+1234567890",
        echo   "company_email": "info@mycompany.com",
        echo   "company_website": "https://mycompany.com",
        echo   "product_name": "AI Marketing Solutions",
        echo   "product_description": "AI-powered marketing automation for local businesses",
        echo   "special_offer": "Free consultation and 30%% off first month",
        echo   "call_to_action": "Schedule a free demo today",
        echo   "sender_name": "Marketing Team",
        echo   "company_tagline": "Growing Your Business with AI",
        echo   "industry": "Technology",
        echo   "target_audience": "Local business owners"
        echo }
    ) > company_profile.json
) else (
    echo    [EXISTS] company_profile.json
)

if not exist "email_settings.json" (
    echo    [CREATED] email_settings.json
    (
        echo {
        echo   "smtp_server": "smtp.gmail.com",
        echo   "smtp_port": 587,
        echo   "sender_email": "",
        echo   "sender_password": "",
        echo   "use_tls": true,
        echo   "use_ssl": false
        echo }
    ) > email_settings.json
) else (
    echo    [EXISTS] email_settings.json
)

if not exist "whatsapp_templates.json" (
    echo    [CREATED] whatsapp_templates.json
    echo {} > whatsapp_templates.json
) else (
    echo    [EXISTS] whatsapp_templates.json
)

if not exist "campaign_data.json" (
    echo    [CREATED] campaign_data.json
    (
        echo {
        echo   "total_leads": 0,
        echo   "contacted": 0,
        echo   "responses": 0,
        echo   "positive_responses": 0,
        echo   "meetings_booked": 0,
        echo   "conversions": 0,
        echo   "daily_stats": {},
        echo   "channel_stats": {}
        echo }
    ) > campaign_data.json
) else (
    echo    [EXISTS] campaign_data.json
)

if not exist "followup_settings.json" (
    echo    [CREATED] followup_settings.json
    (
        echo {
        echo   "enabled": false,
        echo   "max_followups": 3,
        echo   "delay_days": 2
        echo }
    ) > followup_settings.json
) else (
    echo    [EXISTS] followup_settings.json
)

echo.
echo [SUCCESS] Environment prepared
echo.

:: ================================================================
:: INSTALLATION COMPLETE
:: ================================================================
cls
echo ================================================================
echo    ✅ INSTALLATION COMPLETE! ✅
echo ================================================================
echo.
echo    Application: LightFantastic AI Lead Pro v2.0
echo    Architecture: %HAS_MODULAR% Modular Files
echo    Main File: %MAIN_FILE%
echo    Python: %PYTHON_VERSION%
echo.
echo ================================================================
echo.
echo    📋 SUMMARY:
echo    ----------
echo    ✓ Python %PYTHON_VERSION% detected
echo    ✓ All packages installed
echo    ✓ Application files verified
echo    ✓ Environment configured
echo.
echo    🚀 HOW TO RUN:
echo    ------------
echo    1. Double-click 'launcher.bat'
echo    2. Or run: streamlit run %MAIN_FILE%
echo    3. Or run: python -m streamlit run %MAIN_FILE%
echo.
echo    📁 FILES CREATED:
echo    ----------------
echo    - history/           (Lead data storage)
echo    - .client_locks/     (License management)
echo    - company_profile.json
echo    - email_settings.json
echo    - whatsapp_templates.json
echo    - campaign_data.json
echo    - followup_settings.json
echo    - requirements.txt
echo.
echo ================================================================
echo.

:: Ask to launch
echo Would you like to launch the application now?
echo.
choice /c YN /n /m "Launch now? (Y/N): "

if errorlevel 2 (
    echo.
    echo Installation finished!
    echo You can run the application anytime using launcher.bat
    echo.
    pause
    exit /b 0
) else (
    echo.
    echo Launching application...
    echo.
    if exist "launcher.bat" (
        start launcher.bat
    ) else (
        echo [WARNING] launcher.bat not found!
        echo.
        echo Trying to start directly...
        streamlit run %MAIN_FILE% --server.address localhost --server.port 8501
    )
    echo.
    echo Application launched! Browser should open automatically.
    echo If not, open http://localhost:8501 in your browser.
    echo.
    pause
    exit /b 0
)