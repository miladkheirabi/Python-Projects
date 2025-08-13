# ⏳ Pomodoro Timer (Python, Tkinter)

A simple GUI-based Pomodoro timer that helps boost productivity by alternating between work sessions and breaks.

## 📂 Project Structure
pomodoro_timer/  
│  
├── main.py       # Main application code  
├── tomato.png    # Tomato image for the UI  
└── README.md     # Project documentation  

## 🚀 Features
- **Work & Break Sessions**: Follows the Pomodoro technique (25 min work, 5 min short break, 20 min long break).  
- **Progress Tracking**: Shows checkmarks for completed work sessions.  
- **Reset Function**: Allows resetting the timer at any point.  
- **GUI with Tkinter**: Simple and clean interface using a tomato image as the centerpiece.  

## 🛠 How to Run
Make sure you have Python 3 installed.  
Clone the repository and run:  

python main.py  

## 📸 Example
![image info](./capture.png)

1. Click **Start** to begin a work session.  
2. Timer counts down from 25 minutes.  
3. After work session → short break (5 min) or long break (20 min after 4 work sessions).  
4. Click **Reset** anytime to stop and clear progress.  

## 📚 Learning Goals
This project is great for:  
- Learning **Tkinter** for Python GUI development  
- Working with **timers** and the `after()` method  
- Managing application **state** with global variables  
- Practicing modular function design  

---  
Made with ❤️ in Python
