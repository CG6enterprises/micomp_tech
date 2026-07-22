"""
Micomp_Tech Backend Application
Statistical Sciences & Data Management Platform
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///micomp_tech.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# ==================== DATABASE MODELS ====================

class User(db.Model):
    """User model for students and professionals"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    user_type = db.Column(db.String(20), nullable=False)  # 'student' or 'professional'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<User {self.username}>'


class Course(db.Model):
    """Course model"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    level = db.Column(db.String(20), nullable=False)  # 'Beginner', 'Intermediate', 'Advanced'
    duration = db.Column(db.String(20), nullable=False)  # e.g., '4 weeks'
    content = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Course {self.title}>'


class Enrollment(db.Model):
    """Student enrollment in courses"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    progress = db.Column(db.Integer, default=0)  # 0-100%
    enrolled_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime, nullable=True)
    
    def __repr__(self):
        return f'<Enrollment {self.user_id} in {self.course_id}>'


class Project(db.Model):
    """Freelance project model"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)  # 'Business', 'Education', 'Taxes'
    client_name = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(20), default='completed')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Project {self.title}>'


class Invoice(db.Model):
    """Invoice/Billing model"""
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    billing_type = db.Column(db.String(20), nullable=False)  # 'hourly' or 'project'
    hours = db.Column(db.Float, nullable=True)
    hourly_rate = db.Column(db.Float, nullable=True)
    status = db.Column(db.String(20), default='pending')  # 'pending', 'paid'
    issued_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Invoice {self.id}>'


# ==================== API ROUTES ====================

@app.route('/', methods=['GET'])
def home():
    """Home endpoint"""
    return jsonify({
        'message': 'Welcome to Micomp_Tech API',
        'version': '1.0.0',
        'description': 'Statistical Sciences & Data Management Platform'
    })


@app.route('/api/health', methods=['GET'])
def health():
    """Health check"""
    return jsonify({'status': 'healthy'}), 200


# User Routes
@app.route('/api/users', methods=['POST'])
def create_user():
    """Create a new user"""
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('email'):
        return jsonify({'error': 'Missing required fields'}), 400
    
    try:
        user = User(
            username=data['username'],
            email=data['email'],
            password_hash=data.get('password', ''),
            user_type=data.get('user_type', 'student')
        )
        db.session.add(user)
        db.session.commit()
        
        return jsonify({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'user_type': user.user_type,
            'created_at': user.created_at.isoformat()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get user by ID"""
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'user_type': user.user_type,
        'created_at': user.created_at.isoformat()
    }), 200


# Course Routes
@app.route('/api/courses', methods=['GET'])
def get_courses():
    """Get all courses"""
    courses = Course.query.all()
    
    return jsonify([{
        'id': course.id,
        'title': course.title,
        'description': course.description,
        'level': course.level,
        'duration': course.duration,
        'created_at': course.created_at.isoformat()
    } for course in courses]), 200


@app.route('/api/courses', methods=['POST'])
def create_course():
    """Create a new course"""
    data = request.get_json()
    
    if not data or not data.get('title'):
        return jsonify({'error': 'Missing required fields'}), 400
    
    try:
        course = Course(
            title=data['title'],
            description=data.get('description', ''),
            level=data.get('level', 'Beginner'),
            duration=data.get('duration', ''),
            content=data.get('content', '')
        )
        db.session.add(course)
        db.session.commit()
        
        return jsonify({
            'id': course.id,
            'title': course.title,
            'description': course.description,
            'level': course.level,
            'duration': course.duration,
            'created_at': course.created_at.isoformat()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """Get course by ID"""
    course = Course.query.get(course_id)
    
    if not course:
        return jsonify({'error': 'Course not found'}), 404
    
    return jsonify({
        'id': course.id,
        'title': course.title,
        'description': course.description,
        'level': course.level,
        'duration': course.duration,
        'content': course.content,
        'created_at': course.created_at.isoformat()
    }), 200


# Enrollment Routes
@app.route('/api/enrollments', methods=['POST'])
def create_enrollment():
    """Enroll a user in a course"""
    data = request.get_json()
    
    if not data or not data.get('user_id') or not data.get('course_id'):
        return jsonify({'error': 'Missing required fields'}), 400
    
    try:
        enrollment = Enrollment(
            user_id=data['user_id'],
            course_id=data['course_id']
        )
        db.session.add(enrollment)
        db.session.commit()
        
        return jsonify({
            'id': enrollment.id,
            'user_id': enrollment.user_id,
            'course_id': enrollment.course_id,
            'progress': enrollment.progress,
            'enrolled_at': enrollment.enrolled_at.isoformat()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@app.route('/api/enrollments/<int:user_id>', methods=['GET'])
def get_user_enrollments(user_id):
    """Get all courses enrolled by a user"""
    enrollments = Enrollment.query.filter_by(user_id=user_id).all()
    
    return jsonify([{
        'id': enrollment.id,
        'course_id': enrollment.course_id,
        'progress': enrollment.progress,
        'enrolled_at': enrollment.enrolled_at.isoformat(),
        'completed_at': enrollment.completed_at.isoformat() if enrollment.completed_at else None
    } for enrollment in enrollments]), 200


# Project Routes
@app.route('/api/projects', methods=['GET'])
def get_projects():
    """Get all projects"""
    projects = Project.query.all()
    
    return jsonify([{
        'id': project.id,
        'title': project.title,
        'description': project.description,
        'category': project.category,
        'client_name': project.client_name,
        'status': project.status,
        'created_at': project.created_at.isoformat()
    } for project in projects]), 200


@app.route('/api/projects', methods=['POST'])
def create_project():
    """Create a new project"""
    data = request.get_json()
    
    if not data or not data.get('title') or not data.get('category'):
        return jsonify({'error': 'Missing required fields'}), 400
    
    try:
        project = Project(
            title=data['title'],
            description=data.get('description', ''),
            category=data['category'],
            client_name=data.get('client_name', 'Anonymous'),
            status=data.get('status', 'completed')
        )
        db.session.add(project)
        db.session.commit()
        
        return jsonify({
            'id': project.id,
            'title': project.title,
            'description': project.description,
            'category': project.category,
            'client_name': project.client_name,
            'status': project.status,
            'created_at': project.created_at.isoformat()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


# Invoice Routes
@app.route('/api/invoices', methods=['POST'])
def create_invoice():
    """Create a new invoice"""
    data = request.get_json()
    
    if not data or not data.get('project_id') or not data.get('amount'):
        return jsonify({'error': 'Missing required fields'}), 400
    
    try:
        invoice = Invoice(
            project_id=data['project_id'],
            amount=data['amount'],
            billing_type=data.get('billing_type', 'project'),
            hours=data.get('hours'),
            hourly_rate=data.get('hourly_rate'),
            status=data.get('status', 'pending')
        )
        db.session.add(invoice)
        db.session.commit()
        
        return jsonify({
            'id': invoice.id,
            'project_id': invoice.project_id,
            'amount': invoice.amount,
            'billing_type': invoice.billing_type,
            'hours': invoice.hours,
            'hourly_rate': invoice.hourly_rate,
            'status': invoice.status,
            'issued_at': invoice.issued_at.isoformat()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@app.route('/api/invoices/<int:project_id>', methods=['GET'])
def get_project_invoices(project_id):
    """Get all invoices for a project"""
    invoices = Invoice.query.filter_by(project_id=project_id).all()
    
    return jsonify([{
        'id': invoice.id,
        'project_id': invoice.project_id,
        'amount': invoice.amount,
        'billing_type': invoice.billing_type,
        'hours': invoice.hours,
        'hourly_rate': invoice.hourly_rate,
        'status': invoice.status,
        'issued_at': invoice.issued_at.isoformat()
    } for invoice in invoices]), 200


# Statistical Analysis Routes
@app.route('/api/analysis/descriptive', methods=['POST'])
def descriptive_stats():
    """Calculate descriptive statistics"""
    import numpy as np
    
    data = request.get_json()
    
    if not data or not data.get('values'):
        return jsonify({'error': 'Missing data values'}), 400
    
    try:
        values = np.array(data['values'], dtype=float)
        
        stats = {
            'count': int(len(values)),
            'mean': float(np.mean(values)),
            'median': float(np.median(values)),
            'std_dev': float(np.std(values)),
            'variance': float(np.var(values)),
            'min': float(np.min(values)),
            'max': float(np.max(values)),
            'range': float(np.max(values) - np.min(values)),
            'q1': float(np.percentile(values, 25)),
            'q3': float(np.percentile(values, 75))
        }
        
        return jsonify(stats), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/analysis/correlation', methods=['POST'])
def correlation_analysis():
    """Calculate correlation between two variables"""
    from scipy.stats import pearsonr
    import numpy as np
    
    data = request.get_json()
    
    if not data or not data.get('x') or not data.get('y'):
        return jsonify({'error': 'Missing x and y values'}), 400
    
    try:
        x = np.array(data['x'], dtype=float)
        y = np.array(data['y'], dtype=float)
        
        if len(x) != len(y):
            return jsonify({'error': 'x and y must have the same length'}), 400
        
        correlation, p_value = pearsonr(x, y)
        
        return jsonify({
            'correlation': float(correlation),
            'p_value': float(p_value),
            'interpretation': 'Strong' if abs(correlation) > 0.7 else 'Moderate' if abs(correlation) > 0.5 else 'Weak'
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/analysis/ttest', methods=['POST'])
def ttest_analysis():
    """Perform t-test"""
    from scipy.stats import ttest_ind
    import numpy as np
    
    data = request.get_json()
    
    if not data or not data.get('group1') or not data.get('group2'):
        return jsonify({'error': 'Missing group1 and group2 values'}), 400
    
    try:
        group1 = np.array(data['group1'], dtype=float)
        group2 = np.array(data['group2'], dtype=float)
        
        t_stat, p_value = ttest_ind(group1, group2)
        
        return jsonify({
            't_statistic': float(t_stat),
            'p_value': float(p_value),
            'significant': p_value < 0.05,
            'interpretation': 'Significant difference' if p_value < 0.05 else 'No significant difference'
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500


# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == '__main__':
    # Create tables
    with app.app_context():
        db.create_all()
    
    # Run the app
    app.run(debug=True, host='0.0.0.0', port=5000)
