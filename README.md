# CoLearner

CoLearner is a web-based platform designed for collaborative learning and discussion. It allows users to create and join "Rooms" focused on specific topics, enabling real-time discussions and knowledge sharing.

## Features

*   **User Authentication**: Secure registration, login, and logout functionality.
*   **Room Management**:
    *   **Create Rooms**: Users can host their own rooms centered around a specific topic.
    *   **Update/Delete Rooms**: Hosts have full control to update details or delete their rooms.
    *   **Browse & Search**: Users can search for rooms by name, topic, or description.
*   **Real-time Discussion**:
    *   **Messaging**: Participants can send messages within rooms to discuss the topic.
    *   **History**: View past messages and conversation history.
*   **Topics**: Rooms are categorized by topics, making it easy to find relevant discussions.
*   **User Profiles**: View user profiles, including the rooms they host and their recent activity.
*   **Responsive Design**: Built with a focus on usability across devices.

## Tech Stack

*   **Backend**: Python, Django
*   **Database**: SQLite (default configuration)
*   **Frontend**: HTML, CSS, Django Templates

## Installation & Setup

Follow these steps to get the project running on your local machine.

### Prerequisites

*   Python 3.x installed
*   pip (Python package manager)

### Steps

1.  **Clone the repository:**
    ```bash
    git clone <https://github.com/parthu05/CoLearner.git>
    cd coLearner
    ```

2.  **Create a virtual environment (Optional but recommended):**
    ```bash
    # Windows
    python -m venv env
    .\env\Scripts\activate

    # macOS/Linux
    python3 -m venv env
    source env/bin/activate
    ```

3.  **Install dependencies:**
    Since this is a Django project, you need to install Django.
    ```bash
    pip install django
    ```
    Install all other dependencies using:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    Initialize the database with the defined models.
    ```bash
    python manage.py migrate
    ```

5.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

6.  **Access the application:**
    Open your web browser and go to:
    `http://127.0.0.1:8000/`

## Usage

1.  **Register/Login**: Create an account or log in to access full features.
2.  **Create a Room**: Click on "Create Room", enter a topic, room name, and description.
3.  **Join a Room**: Browse the home page for interesting topics and click to join the discussion.
4.  **Post Messages**: Type your message in the room to interact with other participants.

## Project Structure

*   `base/`: Contains the main application logic (models, views, urls).
*   `coLearner/`: Project configuration settings.
*   `templates/`: HTML templates for the application.
*   `static/`: Static files (CSS, Images, JS).
*   `db.sqlite3`: SQLite database file.
*   `manage.py`: Django's command-line utility for administrative tasks.
