# Cookie Clicker Bot (Selenium Automation)

This project is a **browser automation bot** for the game [Cookie Clicker](http://orteil.dashnet.org/experiments/cookie/), built with **Selenium**.  
The bot automatically clicks on the main cookie and purchases upgrades to maximize cookie production.

## 📷 Demo
> When running the bot, it will automatically open your browser, click the cookie, and buy upgrades periodically.

## 🚀 Requirements
Make sure you have:
- Python 3.8+
- Google Chrome installed
- Python packages:

```
    bash
    pip install selenium webdriver-manager
```
  
## 📦 Installation & Usage
1. Clone this repository:
```
    bash
    git clone https://github.com/USERNAME/cookie-clicker-bot.git
    cd cookie-clicker-bot
```
2. Run the script:
```
    bash
    python main.py
```
## 🛠 Features
- Automatic clicking on the main cookie
- Checks current cookies count
- Purchases upgrades based on highest value
- Uses `Selenium` and `webdriver_manager` to manage ChromeDriver automatically

## ⚠ Notes
- Close any other open tabs of the game before running the bot.
- Running the bot for a long time can use high CPU.
- The game may change over time, requiring code updates.
