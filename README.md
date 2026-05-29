# StudySync - Collaborative Study Room Platform

StudySync is a distraction-free virtual study room platform designed for students to collaborate, track study sessions, and communicate in real time.

## Features

- **Authentication**: Secure sign-up and sign-in system.
- **Study Rooms**: Create public or private rooms with unique invite codes.
- **Real-time Chat**: Instant communication within study rooms using WebSockets.
- **Study Timer**: Track session duration and store study history.
- **Activity Dashboard**: Overview of joined rooms, total study time, and recent activities.
- **Responsive Design**: Clean, modern UI that works on desktop and mobile.

## Tech Stack

- **Backend**: Python (Flask)
- **Database**: SQLite (SQLAlchemy)
- **Real-time**: Flask-SocketIO
- **Frontend**: HTML5, CSS3 (Flexbox/Grid), Vanilla JavaScript
- **Templating**: Jinja2

## Setup Instructions

### Prerequisites

- Python 3.8 or higher

### Installation

1. **Clone the repository** (or extract the files):
   ```bash
   cd study_platform
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python run.py
   ```

5. **Access the app**:
   Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
study_platform/
├── app/
│   ├── routes/          # Flask Blueprints
│   ├── static/          # CSS and JS files
│   ├── templates/       # Jinja2 HTML templates
│   ├── __init__.py      # App initialization
│   ├── models.py        # Database models
│   └── events.py        # Socket.IO event handlers
├── instance/            # SQLite database (auto-generated)
├── requirements.txt     # Python dependencies
├── run.py               # Entry point
└── README.md            # Project documentation
```

## License

MIT
