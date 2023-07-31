# Realtime Chat App

This is a realtime chat web application built with Django and Channels.

## Features

- User authentication system allowing users to sign up and login
- Realtime chat using WebSocket and ASGI for messaging
- One on one private messaging between users
- Chat rooms that users can join and chat **(Coming Soon)**
- Unread message counts and notifications **(Coming Soon)**

## Technologies Used 

- Django - Python web framework
- Channels - Provides ASGI and WebSocket support
- Redis - Message broker for Channels
- Django Templates - For rendering HTML
- Bootstrap - Front-end styling

## Usage

To run this app locally:

1. Clone this repository
2. Create and activate a virtual environment 
3. Install requirements - `pip install -r requirements.txt`
4. Run migrations - `python manage.py migrate`
5. Create superuser - `python manage.py createsuperuser` 
6. Run development server - `python manage.py runserver`

The app will be running at `http://127.0.0.1:8000`

## Customizing 

The main chat app logic is located in `chat/consumers.py` and `chat/views.py`. Templates are located in `templates/chat`.

Some things you may want to customize:

- Styling - templates inherit from `base.html` so you can easily update the styles
- Chat features - edit the consumers to update the chat logic  
- Data models - update `models.py` if you want to change the data structure

## License

This project is open source and available under the [MIT License](LICENSE).
