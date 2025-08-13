# 🛰 ISS Overhead Notifier (Python)

A small script that checks the real-time location of the International Space Station (ISS) and sends you an alert when it’s near your location at night.

## 📂 Project Structure
iss_notifier/
│
├── main.py        # The script (requests + sunrise/sunset + SMTP)
├── .env           # Environment variables (email, app password, coords) — not committed
└── README.md      # This file

## 🚀 Features
- Pulls ISS position from Open Notify API.
- Checks night-time using Sunrise–Sunset API (UTC).
- Sends an email notification when ISS is close and it’s dark.
- Polls roughly once per minute.

## ⚙️ How It Works (Logic)
1) Get current ISS latitude/longitude.  
2) Get today’s sunrise/sunset for your coordinates (UTC).  
3) If ISS is within your proximity window AND now is after sunset or before sunrise → send alert email.  
4) Repeat every minute.

## 🛠 Setup
Requirements:
- Python 3
- requests (pip install requests)

Files:
- main.py (your code)
- tomato.png (not needed here)
- .env (create it yourself; see below)

## 🔐 Security (DO THIS!)
Never hardcode secrets (email, app password, exact home coordinates) in code or commits.

1) Put secrets in a .env file:
   - MY_EMAIL=your_email@example.com
   - MY_PASSWORD=your_app_password
   - MY_LAT= your_latitude
   - MY_LONG= your_longitude

2) Load them in code with python-dotenv (optional but recommended), or read from os.environ.

3) Add .env to .gitignore so it won’t be pushed:
   - .env

4) If you already committed secrets, rotate them immediately:
   - Revoke/replace your Gmail App Password.
   - Force-push removal doesn’t guarantee secrecy; assume it’s leaked.

Tips:
- Use Gmail “App Passwords” (2FA required) rather than your real password.
- For public demos, obfuscate location (round coordinates or use a nearby city).

## ▶️ Run
From the project directory:
- pip install requests
- python main.py

## 🧭 Configuration Notes
- Sunrise/Sunset API returns times in UTC. Ensure your comparison uses UTC consistently.
- The “nearby” check in the sample (lat 30–40, lon 46–56) is a crude window; replace with a ±delta around your own coords for better accuracy.
- Network hiccups are handled with a simple try/except; you can add retries/backoff.

## 🧪 Example Alert
Subject: LOOK UP!

## 📚 Learning Goals
- Working with REST APIs in Python
- Scheduling periodic checks
- Timezones and UTC handling
- Sending secure email alerts with SMTP

---  
Made with ❤️ in Python
