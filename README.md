# Django Blog Application

A full-featured, production-ready blog application built with Django featuring user authentication, CRUD operations, and a modern responsive design.

![Django](https://img.shields.io/badge/Django-5.2.7-green)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.1-purple)

## 🚀 Features

### Core Functionality
- **User Authentication**: Registration, login, logout, and user sessions
- **Blog Post Management**: Create, read, update, and delete blog posts
- **Rich Text Content**: Support for lengthy blog posts with proper formatting
- **Categories & Tags**: Organize posts with multiple categories
- **Comment System**: Users can comment on posts (with admin approval)
- **Image Uploads**: Featured images for blog posts

### User Experience
- **Responsive Design**: Mobile-friendly Bootstrap 5 interface
- **Search Functionality**: Search posts by title, content, or excerpt
- **Pagination**: Efficiently browse through post lists
- **Category Filtering**: Filter posts by categories
- **Breadcrumb Navigation**: Easy navigation through the site

### Admin Features
- **Django Admin**: Full administrative interface
- **Post Management**: Draft/published status control
- **Comment Moderation**: Approve or reject user comments
- **User Management**: Comprehensive user administration

## 📸 Screenshots

*(You can add screenshots later)*
- Homepage with post listings
- Individual post detail page
- Admin dashboard
- Mobile responsive views

## 🛠️ Technology Stack

- **Backend**: Django 5.2.7
- **Frontend**: Bootstrap 5.1, HTML5, CSS3
- **Database**: SQLite (Development), PostgreSQL ready
- **Authentication**: Django built-in auth system
- **File Storage**: Local file system (configurable for AWS S3)

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/brianmahove/django-blog.git
   cd django-blog
Set up virtual environment

bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
Install dependencies

bash
pip install -r requirements.txt
Configure environment (optional)

bash
cp .env.example .env
# Edit .env with your settings
Run migrations

bash
python manage.py migrate
Create superuser

bash
python manage.py createsuperuser
Collect static files

bash
python manage.py collectstatic
Run development server

bash
python manage.py runserver
Access the application

Website: http://127.0.0.1:8000

Admin: http://127.0.0.1:8000/admin

🗄️ Database Models
Post
Title, slug, content, excerpt

Author (ForeignKey to User)

Featured image, categories (ManyToMany)

Created/updated/publish dates

Status (draft/published)

Category
Name

Comment
Post (ForeignKey), author (ForeignKey)

Content, created date, approved status

🎯 API Endpoints
(If you add Django REST Framework later)

GET /api/posts/ - List all published posts

GET /api/posts/<slug>/ - Retrieve specific post

POST /api/comments/ - Create new comment

🚀 Deployment
For Production
Set DEBUG = False

Configure ALLOWED_HOSTS

Set up proper database (PostgreSQL recommended)

Configure static files with Whitenoise or CDN

Set up production web server (Gunicorn + Nginx)

Environment Variables
python
DEBUG=False
SECRET_KEY=your-production-secret-key
ALLOWED_HOSTS=.yourdomain.com
DATABASE_URL=postgres://...
🤝 Contributing
We welcome contributions! Please follow these steps:

Fork the repository

Create a feature branch: git checkout -b feature/amazing-feature

Commit your changes: git commit -m 'Add amazing feature'

Push to the branch: git push origin feature/amazing-feature

Open a Pull Request

Development Setup
bash
# Run tests
python manage.py test

# Check code style
flake8 .

# Run security check
python manage.py check --deploy
🐛 Bug Reports & Feature Requests
Found a bug or have a feature request? Please open an issue with:

Detailed description

Steps to reproduce (for bugs)

Expected vs actual behavior

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
Django framework and community

Bootstrap for the frontend design

Contributors and testers

📞 Support
If you need help with:

Setup and installation

Bug fixes

Feature explanations

Please open an issue or contact [Your Email].

⭐ Star this repository if you find it helpful!

text

## 2. Add supporting files

### LICENSE file
**LICENSE** (MIT License)
```text
MIT License

Copyright (c) 2025 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
CONTRIBUTING.md
CONTRIBUTING.md

markdown
# Contributing to Django Blog

Thank you for considering contributing to our Django Blog project!

## Code Style
- Follow PEP 8 guidelines
- Use meaningful variable names
- Add comments for complex logic
- Write docstrings for functions and classes

## Pull Request Process
1. Ensure your code passes all tests
2. Update documentation if needed
3. Add your name to CONTRIBUTORS.md
4. Request review from maintainers

## Development Workflow
1. Create an issue describing the change
2. Fork the repository
3. Create a feature branch
4. Make your changes
5. Add tests if applicable
6. Submit pull request
3. Repository description and topics
Repository Description:
"🚀 A full-featured blog application built with Django featuring user authentication, CRUD operations, categories, comments, and responsive Bootstrap design."

Topics (keywords):
text
django, blog, python, web-application, bootstrap, crud, authentication, 
blog-platform, django-project, web-development, python-django
4. Badges (add to README)
You can add these badges later when you set up CI/CD:

markdown
![Build Status](https://github.com/YOUR_USERNAME/django-blog/actions/workflows/django.yml/badge.svg)
![Code Coverage](https://coveralls.io/repos/github/YOUR_USERNAME/django-blog/badge.svg)
![License](https://img.shields.io/github/license/YOUR_USERNAME/django-blog)
5. Project structure overview
Add this to your README:

markdown
## Project Structure
django-blog/
├── blog/ # Main application
│ ├── models.py # Database models
│ ├── views.py # View logic
│ ├── urls.py # URL routing
│ ├── admin.py # Admin configuration
│ └── templates/ # App-specific templates
├── blog_project/ # Project configuration
│ ├── settings.py # Django settings
│ ├── urls.py # Root URL config
│ └── wsgi.py # WSGI configuration
├── templates/ # Global templates
│ ├── base.html # Base template
│ └── blog/ # Blog templates
├── static/ # Static files (CSS, JS, images)
├── media/ # User-uploaded files
├── requirements.txt # Dependencies
├── manage.py # Django management script
└── README.md # Project documentation

text

## 6. Commit and push these enhancements

```bash
# Add all new files
git add README.md LICENSE CONTRIBUTING.md

# Commit
git commit -m "Add comprehensive documentation: README, LICENSE, contributing guidelines"

# Push to GitHub
git push origin main
