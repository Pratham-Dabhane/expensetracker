# Personal Expense Tracker

A Django-based web application for tracking personal expenses. This application helps users manage their daily expenses by providing an intuitive interface to log, track, and analyze their spending habits.

## Features

- **Expense Management**
  - Add new expenses with details (amount, category, date, description)
  - View all expenses in a organized list
  - Edit existing expense entries
  - Delete unwanted expense records
  
- **Category Organization**
  - Categorize expenses for better organization
  - Track spending patterns by category

- **User Interface**
  - Clean and intuitive web interface
  - Responsive design for all devices
  - Easy navigation between features

## Tech Stack

- **Backend Framework:** Django 5.2.6
- **Database:** SQLite3
- **Frontend:** HTML, Django Templates
- **Python Version:** 3.11+

## Installation

1. **Clone the Repository**
   ```bash
   git clone [your-repository-url]
   cd expensetracker
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv myenv
   ```

3. **Activate Virtual Environment**
   - Windows:
     ```bash
     myenv\Scripts\activate
     ```
   - Unix or MacOS:
     ```bash
     source myenv/bin/activate
     ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply Database Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**
   - Open your web browser and navigate to: http://127.0.0.1:8000/

## Project Structure

```
expensetracker/
├── expenses/                 # Main application directory
│   ├── templates/           # HTML templates
│   ├── models.py            # Database models
│   ├── views.py            # View logic
│   ├── urls.py             # URL configurations
│   └── forms.py            # Form definitions
├── expensetracker/         # Project settings directory
├── manage.py               # Django management script
└── requirements.txt        # Project dependencies
```

## Usage

1. Start the development server
2. Navigate to http://127.0.0.1:8000/ in your web browser
3. Use the interface to add, view, edit, or delete expenses
4. View your expense summaries and categorized spending

## Development

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE)
