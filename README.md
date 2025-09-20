# Personal Expense Tracker

A Django-based web application for tracking personal expenses with user authentication and advanced filtering capabilities. This application helps users manage their daily expenses by providing an intuitive interface to log, track, and analyze their spending habits with secure user accounts.

## Features

- **User Authentication & Security**
  - User registration and login system
  - Secure session management
  - User-specific expense tracking
  - Protected routes with login requirements

- **Expense Management**
  - Add new expenses with details (amount, category, date, description)
  - View all expenses in an organized list
  - Edit existing expense entries
  - Delete unwanted expense records
  - User-specific expense isolation
  
- **Advanced Filtering & Analytics**
  - Session-based month filtering that persists across navigation
  - Filter expenses by specific months or view all-time data
  - Real-time expense summaries and totals
  - Weekly, monthly, and all-time spending analysis

- **Category Organization**
  - Categorize expenses (Food, Transport, Bills, Entertainment, Other)
  - Visual category tags with color coding
  - Track spending patterns by category

- **Professional User Interface**
  - Modern, responsive design for all devices
  - Clean and intuitive navigation
  - Professional sticky header with user controls
  - Enhanced form inputs with smooth animations
  - Visual feedback with success/error messages

## Tech Stack

- **Backend Framework:** Django 5.2.6
- **Database:** SQLite3 (with user relationships)
- **Frontend:** HTML5, CSS3, Django Templates
- **Authentication:** Django's built-in authentication system
- **Session Management:** Django sessions for filter persistence
- **Python Version:** 3.11+

## Installation

1. **Clone the Repository**
   ```bash
   git clone [your-repository-url]
   cd expense_tracker
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
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create Superuser (Optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

8. **Access the Application**
   - Open your web browser and navigate to: http://127.0.0.1:8000/
   - You'll be redirected to the login page
   - Register a new account or login with existing credentials

## Project Structure

```
expense_tracker/
├── expenses/                    # Main application directory
│   ├── templates/              # HTML templates
│   │   ├── expenses/           # Expense-related templates
│   │   └── registration/       # Authentication templates
│   ├── static/                 # Static files (CSS, JS, images)
│   ├── migrations/             # Database migrations
│   ├── models.py               # Database models (User-linked expenses)
│   ├── views.py                # View logic with authentication
│   ├── urls.py                 # URL configurations
│   ├── forms.py                # Form definitions
│   └── admin.py                # Admin interface configuration
├── expensetracker/             # Project settings directory
├── manage.py                   # Django management script
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

## Usage

### Getting Started
1. **Register/Login**: Create an account or login to access the expense tracker
2. **Dashboard**: View your expense overview with summary cards
3. **Add Expenses**: Click "Add New Expense" to log new expenses
4. **Filter by Month**: Use the month filter to view expenses for specific periods
5. **Manage Expenses**: Edit or delete existing expense entries

### Key Features
- **Session Persistence**: Your selected month filter stays active across page navigations
- **User Isolation**: You can only view and manage your own expenses
- **Real-time Analytics**: See spending totals for different time periods
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices

### Filter Functionality
- Select any month from the dropdown to filter expenses
- Choose "All Time" to view all your expenses
- Your filter selection is saved in your session
- Filter persists until you change it or logout

## Security Features

- **Authentication Required**: All expense operations require user login
- **User Data Isolation**: Users can only access their own expense data
- **CSRF Protection**: Forms are protected against cross-site request forgery
- **Session Security**: Secure session management for user state
- **Input Validation**: Server-side validation for all user inputs

## Development

### Adding New Features
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Make your changes following Django best practices
4. Test thoroughly with user authentication
5. Submit a pull request

### Database Schema
- **User Model**: Django's built-in User model
- **Expense Model**: Custom model with user foreign key
  - Fields: user, title, amount, category, date, created_at
  - Relationships: Many expenses to one user

### Customization
- Modify categories in `models.py`
- Update styling in `static/css/style.css`
- Add new views in `views.py` with `@login_required` decorator
- Extend templates in `templates/expenses/`

## Contributing

We welcome contributions! Please:
1. Follow Django coding standards
2. Ensure all new features require authentication
3. Add appropriate tests for new functionality
4. Update documentation for any changes
5. Maintain the existing UI/UX design patterns

## License

This project is open source and available under the [MIT License](LICENSE)

## Support

For issues or questions:
1. Check the existing issues on GitHub
2. Create a new issue with detailed description
3. Include steps to reproduce any bugs
4. Mention your environment details (Python version, OS, etc.)
