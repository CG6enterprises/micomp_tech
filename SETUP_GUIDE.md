# Micomp_Tech Setup Guide

Complete step-by-step guide to set up and run the Micomp_Tech platform.

## Table of Contents
1. [System Requirements](#system-requirements)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Running the Application](#running-the-application)
5. [API Documentation](#api-documentation)
6. [Troubleshooting](#troubleshooting)

## System Requirements

- **Python:** 3.8 or higher
- **Node.js:** 14.0 or higher (optional, for frontend enhancements)
- **Database:** SQLite (built-in) or PostgreSQL (for production)
- **OS:** Windows, macOS, or Linux
- **RAM:** Minimum 2GB (4GB recommended)
- **Storage:** 500MB for application and dependencies

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/CG6enterprises/micomp-tech.git
cd micomp-tech
```

### 2. Create Virtual Environment (Recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r backend/requirements.txt
```

### 4. Set Up Environment Variables
```bash
# Copy example environment file
cp .env.example .env

# Edit .env with your configuration
# Add your AI API keys (Claude, Gemini, ChatGPT)
```

### 5. Initialize Database
```bash
python backend/app.py
# The database will be created automatically on first run
```

## Configuration

### Environment Variables (.env)

```env
# Database
DATABASE_URL=sqlite:///micomp_tech.db

# AI Keys (Get from respective platforms)
CLAUDE_API_KEY=your_key_here
GEMINI_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here

# Flask
FLASK_ENV=development
SECRET_KEY=your_secret_key_here
```

### Getting AI API Keys

#### Claude (Anthropic)
1. Visit https://console.anthropic.com
2. Sign up for a free account
3. Create an API key
4. Add to .env as CLAUDE_API_KEY

#### Gemini (Google)
1. Visit https://makersuite.google.com/app/apikey
2. Create an API key
3. Add to .env as GEMINI_API_KEY

#### ChatGPT (OpenAI)
1. Visit https://platform.openai.com/account/api-keys
2. Create an API key
3. Add to .env as OPENAI_API_KEY

## Running the Application

### Start the Backend Server
```bash
python backend/app.py
```

The server will start at `http://localhost:5000`

### Open in Browser
```bash
# Navigate to the frontend
Open http://localhost:5000 in your browser
```

### Verify Installation
- You should see the Micomp_Tech landing page
- Blue and gold professional theme
- All navigation links functional

## API Documentation

### Base URL
```
http://localhost:5000/api
```

### Authentication Endpoints

#### Create User
```
POST /api/users
Content-Type: application/json

{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "password123",
  "user_type": "student"
}
```

#### Get User
```
GET /api/users/{user_id}
```

### Course Endpoints

#### Get All Courses
```
GET /api/courses
```

#### Create Course
```
POST /api/courses
Content-Type: application/json

{
  "title": "Data Collection 101",
  "description": "Learn data collection methods",
  "level": "Beginner",
  "duration": "4 weeks"
}
```

#### Get Course Details
```
GET /api/courses/{course_id}
```

### Enrollment Endpoints

#### Enroll in Course
```
POST /api/enrollments
Content-Type: application/json

{
  "user_id": 1,
  "course_id": 1
}
```

#### Get User Enrollments
```
GET /api/enrollments/{user_id}
```

### Analysis Endpoints

#### Descriptive Statistics
```
POST /api/analysis/descriptive
Content-Type: application/json

{
  "values": [10, 20, 30, 40, 50]
}
```

#### Correlation Analysis
```
POST /api/analysis/correlation
Content-Type: application/json

{
  "x": [1, 2, 3, 4, 5],
  "y": [2, 4, 5, 4, 6]
}
```

#### T-Test Analysis
```
POST /api/analysis/ttest
Content-Type: application/json

{
  "group1": [10, 12, 14, 15, 16],
  "group2": [18, 20, 19, 22, 21]
}
```

### Project Endpoints

#### Create Project
```
POST /api/projects
Content-Type: application/json

{
  "title": "Sales Analysis",
  "description": "Quarterly sales analysis",
  "category": "Business",
  "client_name": "ABC Corp"
}
```

#### Get All Projects
```
GET /api/projects
```

### Invoice Endpoints

#### Create Invoice
```
POST /api/invoices
Content-Type: application/json

{
  "project_id": 1,
  "amount": 5000,
  "billing_type": "project",
  "status": "pending"
}
```

## Troubleshooting

### Port Already in Use
```bash
# On Windows
netstat -ano | findstr :5000

# On macOS/Linux
lsof -i :5000

# Kill the process (replace PID with actual process id)
# Windows: taskkill /PID <PID> /F
# macOS/Linux: kill -9 <PID>
```

### Database Errors
```bash
# Delete old database and recreate
rm micomp_tech.db
python backend/app.py
```

### API Key Errors
- Verify your .env file is in the project root
- Check that API keys are valid and not expired
- Ensure keys have proper permissions

### Dependency Issues
```bash
# Reinstall dependencies
pip install --upgrade pip
pip install -r backend/requirements.txt --force-reinstall
```

### Frontend Not Loading
- Clear browser cache (Ctrl+Shift+Delete)
- Check browser console for errors (F12)
- Verify all CSS and JS files are loading

## Next Steps

1. **Add Sample Data**
   - Load sample datasets into the platform
   - Create test courses and enrollments

2. **Configure AI Features**
   - Set up AI chatbot with your API keys
   - Test concept explanations

3. **Deploy**
   - Use Gunicorn for production
   - Set up PostgreSQL for scalability
   - Configure domain and SSL certificate

4. **Customize**
   - Update branding and colors
   - Add your logo
   - Customize course content

## Support

For issues or questions:
1. Check this guide's troubleshooting section
2. Review API documentation
3. Check GitHub issues
4. Contact support@micomp-tech.com

## Security Considerations

### Production Checklist
- [ ] Change SECRET_KEY in .env
- [ ] Set DEBUG=False
- [ ] Use HTTPS/SSL
- [ ] Hash passwords properly
- [ ] Enable CORS restrictions
- [ ] Set up proper authentication
- [ ] Regular security updates
- [ ] Database backups

---

**Last Updated:** 2024
**Version:** 1.0