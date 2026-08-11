"""
Micomp_Tech Backend Application
Statistical Sciences & Data Management Platform
"""

import json
import os
from datetime import datetime

from dotenv import load_dotenv
from flask import Flask, abort, g, jsonify, render_template, request, send_from_directory
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

from translations import translate

# Load environment variables
load_dotenv()

# Frontend static assets (css/js) live one level up from backend/ (repo root)
FRONTEND_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Initialize Flask app (Jinja templates live in backend/templates/)
app = Flask(__name__)
CORS(app)

# ---- Public contact info (shown in footer + Contact page) ----
# CONTACT_EMAIL is a PLACEHOLDER domain that has not been purchased yet.
# Swap it here once the real domain is registered - it propagates everywhere via the context processor below.
CONTACT_EMAIL = 'info@micomptech.com'
CONTACT_PHONE_DISPLAY = '(586) 221-3679'
CONTACT_PHONE_TEL = '+15862213679'


@app.context_processor
def inject_contact_info():
    return dict(
        contact_email=CONTACT_EMAIL,
        contact_phone=CONTACT_PHONE_DISPLAY,
        contact_phone_tel=CONTACT_PHONE_TEL
    )


# ---- Language (English default at /, French under /fr/) ----

@app.before_request
def set_language():
    g.lang = 'fr' if request.path == '/fr' or request.path.startswith('/fr/') else 'en'


def lang_switch_path():
    """The equivalent URL for the current page in the other language."""
    path = request.path
    if g.lang == 'fr':
        remainder = path[3:]  # strip leading '/fr'
        return remainder if remainder.startswith('/') else '/'
    return '/fr' + path


@app.context_processor
def inject_language():
    return dict(lang=g.lang, t=lambda key: translate(g.lang, key), lang_switch_path=lang_switch_path())

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


LEVEL_LABELS = {
    'en': {'Beginner': 'Beginner', 'Intermediate': 'Intermediate', 'Advanced': 'Advanced'},
    'fr': {'Beginner': 'Débutant', 'Intermediate': 'Intermédiaire', 'Advanced': 'Avancé'},
}


class Course(db.Model):
    """Course model"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    level = db.Column(db.String(20), nullable=False)  # 'Beginner', 'Intermediate', 'Advanced'
    duration = db.Column(db.String(20), nullable=False)  # e.g., '4 weeks'
    icon = db.Column(db.String(10), nullable=True)
    content = db.Column(db.Text, nullable=True)
    outcomes = db.Column(db.Text, nullable=True)  # JSON list of strings
    prerequisites = db.Column(db.Text, nullable=True)
    syllabus = db.Column(db.Text, nullable=True)  # JSON list of {title, lessons, hours}
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # French counterparts (nullable - falls back to English if not set)
    title_fr = db.Column(db.String(120), nullable=True)
    description_fr = db.Column(db.Text, nullable=True)
    duration_fr = db.Column(db.String(20), nullable=True)
    outcomes_fr = db.Column(db.Text, nullable=True)
    prerequisites_fr = db.Column(db.Text, nullable=True)
    syllabus_fr = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Course {self.title}>'

    def localized(self, lang='en'):
        """Return a plain dict of this course's fields in the requested language.
        Falls back to English for any field without a French translation set."""
        if lang == 'fr':
            return {
                'id': self.id,
                'title': self.title_fr or self.title,
                'description': self.description_fr or self.description,
                'level': LEVEL_LABELS['fr'].get(self.level, self.level),
                'duration': self.duration_fr or self.duration,
                'icon': self.icon,
                'content': self.content,
                'outcomes': json.loads(self.outcomes_fr) if self.outcomes_fr else (json.loads(self.outcomes) if self.outcomes else []),
                'prerequisites': self.prerequisites_fr or self.prerequisites,
                'syllabus': json.loads(self.syllabus_fr) if self.syllabus_fr else (json.loads(self.syllabus) if self.syllabus else []),
                'created_at': self.created_at.isoformat()
            }
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'level': self.level,
            'duration': self.duration,
            'icon': self.icon,
            'content': self.content,
            'outcomes': json.loads(self.outcomes) if self.outcomes else [],
            'prerequisites': self.prerequisites,
            'syllabus': json.loads(self.syllabus) if self.syllabus else [],
            'created_at': self.created_at.isoformat()
        }

    def to_dict(self, detailed=False):
        data = {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'level': self.level,
            'duration': self.duration,
            'icon': self.icon,
            'created_at': self.created_at.isoformat()
        }
        if detailed:
            data['content'] = self.content
            data['outcomes'] = json.loads(self.outcomes) if self.outcomes else []
            data['prerequisites'] = self.prerequisites
            data['syllabus'] = json.loads(self.syllabus) if self.syllabus else []
        return data


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


class ContactMessage(db.Model):
    """Inbound contact form / quote request / course-interest messages"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    inquiry_type = db.Column(db.String(20), default='general')  # 'general', 'quote', 'course_interest'
    service_category = db.Column(db.String(120), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<ContactMessage {self.id} from {self.email}>'


# ==================== PAGE ROUTES (server-rendered) ====================
# Each page is registered twice: once at its English path, once under /fr/.
# set_language() (above) reads request.path to decide g.lang before the view runs.

@app.route('/', methods=['GET'])
@app.route('/fr/', methods=['GET'])
def home():
    courses = Course.query.order_by(Course.id).limit(4).all()
    localized_courses = [c.localized(g.lang) for c in courses]
    return render_template('home.html', active_page='home', courses=localized_courses)


@app.route('/courses', methods=['GET'])
@app.route('/fr/courses', methods=['GET'])
def courses_page():
    courses = Course.query.order_by(Course.id).all()
    localized_courses = [c.localized(g.lang) for c in courses]
    return render_template('courses.html', active_page='courses', courses=localized_courses)


@app.route('/courses/<int:course_id>', methods=['GET'])
@app.route('/fr/courses/<int:course_id>', methods=['GET'])
def course_detail_page(course_id):
    course = Course.query.get(course_id)
    if not course:
        abort(404)
    localized = course.localized(g.lang)
    return render_template(
        'course_detail.html',
        active_page='courses',
        course=localized,
        outcomes=localized['outcomes'],
        syllabus=localized['syllabus']
    )


@app.route('/tools', methods=['GET'])
@app.route('/fr/tools', methods=['GET'])
def tools_page():
    return render_template('tools.html', active_page='tools')


@app.route('/services', methods=['GET'])
@app.route('/fr/services', methods=['GET'])
def services_page():
    return render_template('services.html', active_page='services')


@app.route('/contact', methods=['GET'])
@app.route('/fr/contact', methods=['GET'])
def contact_page():
    return render_template('contact.html', active_page='contact')


@app.route('/library', methods=['GET'])
@app.route('/fr/library', methods=['GET'])
def library_page():
    from content import localize_glossary, TOOL_LABELS, TOOL_LABELS_FR
    glossary = localize_glossary(g.lang)
    categories = sorted(set(term['category'] for term in glossary))
    tool_labels = TOOL_LABELS_FR if g.lang == 'fr' else TOOL_LABELS
    return render_template(
        'library.html',
        active_page='library',
        glossary=glossary,
        categories=categories,
        tool_labels=tool_labels
    )


@app.route('/which-test-should-i-use', methods=['GET'])
@app.route('/fr/which-test-should-i-use', methods=['GET'])
def which_test_page():
    return render_template('which_test.html', active_page='library')


@app.route('/datasets', methods=['GET'])
@app.route('/fr/datasets', methods=['GET'])
def datasets_page():
    from content import localize_datasets
    return render_template('datasets.html', active_page='datasets', datasets=localize_datasets(g.lang))


@app.route('/datasets/download/<path:filename>', methods=['GET'])
def download_dataset(filename):
    from content import DATASETS
    valid_names = {d['filename'] for d in DATASETS}
    if filename not in valid_names:
        abort(404)
    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
    return send_from_directory(data_dir, filename, as_attachment=True)


@app.route('/case-studies', methods=['GET'])
@app.route('/fr/case-studies', methods=['GET'])
def case_studies_page():
    from content import localize_case_studies
    return render_template('case_studies.html', active_page='case-studies', case_studies=localize_case_studies(g.lang))


@app.route('/case-studies/<slug>', methods=['GET'])
@app.route('/fr/case-studies/<slug>', methods=['GET'])
def case_study_detail_page(slug):
    from content import localize_case_studies, localize_datasets, RESULT_LABELS, RESULT_LABELS_FR
    case_study = next((c for c in localize_case_studies(g.lang) if c['slug'] == slug), None)
    if not case_study:
        abort(404)
    dataset = next((d for d in localize_datasets(g.lang) if d['slug'] == case_study['dataset_slug']), None)

    labels = RESULT_LABELS_FR if g.lang == 'fr' else RESULT_LABELS
    results_display = []
    for key, value in case_study['results'].items():
        label = labels.get(key, key.replace('_', ' ').title())
        if isinstance(value, float):
            formatted = f'{value:.4f}'
        else:
            formatted = value
        results_display.append((label, formatted))

    return render_template(
        'case_study_detail.html',
        active_page='case-studies',
        case_study=case_study,
        dataset=dataset,
        results_display=results_display
    )


# ==================== STATIC ASSETS ====================

@app.route('/css/<path:filename>', methods=['GET'])
def css_files(filename):
    return send_from_directory(os.path.join(FRONTEND_DIR, 'css'), filename)


@app.route('/js/<path:filename>', methods=['GET'])
def js_files(filename):
    return send_from_directory(os.path.join(FRONTEND_DIR, 'js'), filename)


# ==================== JSON API ====================

@app.route('/api', methods=['GET'])
def api_root():
    """API welcome/info endpoint"""
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

    if not data or not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        user = User(
            username=data['username'],
            email=data['email'],
            password_hash=generate_password_hash(data['password']),
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
    return jsonify([course.to_dict() for course in courses]), 200


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
            icon=data.get('icon', '📊'),
            content=data.get('content', ''),
            outcomes=json.dumps(data.get('outcomes', [])),
            prerequisites=data.get('prerequisites', ''),
            syllabus=json.dumps(data.get('syllabus', []))
        )
        db.session.add(course)
        db.session.commit()

        return jsonify(course.to_dict(detailed=True)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """Get course by ID"""
    course = Course.query.get(course_id)

    if not course:
        return jsonify({'error': 'Course not found'}), 404

    return jsonify(course.to_dict(detailed=True)), 200


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


# Contact / Lead Routes
@app.route('/api/contact', methods=['POST'])
def submit_contact():
    """Handle contact form, quote requests, and course-interest submissions"""
    data = request.get_json()

    if not data or not data.get('name') or not data.get('email') or not data.get('message'):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        msg = ContactMessage(
            name=data['name'],
            email=data['email'],
            message=data['message'],
            inquiry_type=data.get('inquiry_type', 'general'),
            service_category=data.get('service_category')
        )
        db.session.add(msg)
        db.session.commit()

        success_message = (
            "Merci ! Nous avons bien reçu votre message et vous répondrons bientôt."
            if data.get('language') == 'fr'
            else "Thanks! We've received your message and will get back to you soon."
        )

        return jsonify({
            'status': 'success',
            'message': success_message
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@app.route('/api/contact-messages', methods=['GET'])
def list_contact_messages():
    """List inbound messages. NOTE: unauthenticated - restrict this once accounts/auth exist."""
    messages = ContactMessage.query.order_by(ContactMessage.created_at.desc()).all()

    return jsonify([{
        'id': m.id,
        'name': m.name,
        'email': m.email,
        'message': m.message,
        'inquiry_type': m.inquiry_type,
        'service_category': m.service_category,
        'created_at': m.created_at.isoformat()
    } for m in messages]), 200


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
            'significant': bool(p_value < 0.05),
            'interpretation': 'Significant difference' if p_value < 0.05 else 'No significant difference'
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/analysis/regression', methods=['POST'])
def regression_analysis():
    """Simple linear regression"""
    from scipy.stats import linregress
    import numpy as np

    data = request.get_json()

    if not data or not data.get('x') or not data.get('y'):
        return jsonify({'error': 'Missing x and y values'}), 400

    try:
        x = np.array(data['x'], dtype=float)
        y = np.array(data['y'], dtype=float)

        if len(x) != len(y):
            return jsonify({'error': 'x and y must have the same length'}), 400
        if len(x) < 2:
            return jsonify({'error': 'Need at least 2 data points'}), 400

        result = linregress(x, y)

        return jsonify({
            'slope': float(result.slope),
            'intercept': float(result.intercept),
            'r_value': float(result.rvalue),
            'r_squared': float(result.rvalue ** 2),
            'p_value': float(result.pvalue),
            'std_err': float(result.stderr),
            'equation': f'y = {result.slope:.4f}x + {result.intercept:.4f}'
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# AI Assistant Route
@app.route('/api/chat', methods=['POST'])
def chat():
    """Ask the AI learning assistant a question"""
    from ai_integration import get_ai_response

    data = request.get_json()

    if not data or not data.get('message'):
        return jsonify({'error': 'Missing message'}), 400

    result = get_ai_response(
        data['message'],
        provider=data.get('provider') or 'gemini',
        context=data.get('context'),
        language=data.get('language', 'en')
    )

    return jsonify(result), 200


@app.route('/api/explain', methods=['POST'])
def explain():
    """Ask the AI to explain a statistical concept in plain language"""
    from ai_integration import explain_statistical_concept

    data = request.get_json()

    if not data or not data.get('concept'):
        return jsonify({'error': 'Missing concept'}), 400

    result = explain_statistical_concept(
        data['concept'],
        level=data.get('level', 'beginner'),
        provider=data.get('provider') or 'gemini',
        language=data.get('language', 'en')
    )

    return jsonify(result), 200


@app.route('/api/exercise', methods=['POST'])
def exercise():
    """Ask the AI to generate a practice exercise on a topic"""
    from ai_integration import generate_practice_exercise

    data = request.get_json()

    if not data or not data.get('topic'):
        return jsonify({'error': 'Missing topic'}), 400

    result = generate_practice_exercise(
        data['topic'],
        difficulty=data.get('difficulty', 'medium'),
        provider=data.get('provider') or 'gemini',
        language=data.get('language', 'en')
    )

    return jsonify(result), 200


# Error handlers
@app.errorhandler(404)
def not_found(error):
    if request.path.startswith('/api'):
        return jsonify({'error': 'Resource not found'}), 404
    return render_template('404.html', active_page=None), 404


@app.errorhandler(500)
def internal_error(error):
    if request.path.startswith('/api'):
        return jsonify({'error': 'Internal server error'}), 500
    return render_template('500.html', active_page=None), 500


# ==================== SEED DATA ====================

def seed_courses():
    """Populate the four core courses with real syllabus content on first run."""
    if Course.query.count() > 0:
        return

    courses = [
        {
            'title': 'Data Collection 101',
            'title_fr': 'Collecte de données 101',
            'icon': '📊',
            'description': 'Learn systematic methods for collecting quality data. Covers sampling techniques, survey design, and data quality assurance.',
            'description_fr': 'Apprenez des méthodes systématiques pour collecter des données de qualité. Couvre les techniques d\'échantillonnage, la conception d\'enquêtes et l\'assurance qualité des données.',
            'level': 'Beginner',
            'duration': '4 weeks',
            'duration_fr': '4 semaines',
            'prerequisites': 'None. This is a great starting point if you are new to data work.',
            'prerequisites_fr': 'Aucun. C\'est un excellent point de départ si vous débutez dans le travail avec les données.',
            'outcomes': [
                'Design a sampling plan appropriate to your research question',
                'Build survey instruments that minimize bias',
                'Evaluate data quality using completeness, accuracy, and consistency checks',
                'Apply ethical standards for data collection and privacy'
            ],
            'outcomes_fr': [
                'Concevoir un plan d\'échantillonnage adapté à votre question de recherche',
                'Construire des instruments d\'enquête qui minimisent les biais',
                'Évaluer la qualité des données à l\'aide de contrôles de complétude, d\'exactitude et de cohérence',
                'Appliquer des normes éthiques pour la collecte de données et la confidentialité'
            ],
            'syllabus': [
                {'title': 'Foundations of Data Collection', 'lessons': 4, 'hours': 1.5},
                {'title': 'Sampling Methods & Study Design', 'lessons': 5, 'hours': 2},
                {'title': 'Building Effective Surveys', 'lessons': 4, 'hours': 1.5},
                {'title': 'Data Quality & Validation', 'lessons': 4, 'hours': 1.5}
            ],
            'syllabus_fr': [
                {'title': 'Fondements de la collecte de données', 'lessons': 4, 'hours': 1.5},
                {'title': 'Méthodes d\'échantillonnage et conception d\'étude', 'lessons': 5, 'hours': 2},
                {'title': 'Construire des enquêtes efficaces', 'lessons': 4, 'hours': 1.5},
                {'title': 'Qualité et validation des données', 'lessons': 4, 'hours': 1.5}
            ]
        },
        {
            'title': 'Statistical Basics',
            'title_fr': 'Bases de la statistique',
            'icon': '📈',
            'description': 'Master fundamental statistical concepts. Probability, distributions, hypothesis testing, and confidence intervals.',
            'description_fr': 'Maîtrisez les concepts statistiques fondamentaux. Probabilité, distributions, tests d\'hypothèses et intervalles de confiance.',
            'level': 'Beginner',
            'duration': '5 weeks',
            'duration_fr': '5 semaines',
            'prerequisites': 'Basic algebra. No prior statistics experience required.',
            'prerequisites_fr': 'Algèbre de base. Aucune expérience préalable en statistique n\'est requise.',
            'outcomes': [
                'Explain core probability concepts and common distributions',
                'Calculate and interpret descriptive statistics',
                'Construct and interpret confidence intervals',
                'Run and interpret a basic hypothesis test'
            ],
            'outcomes_fr': [
                'Expliquer les concepts de probabilité de base et les distributions courantes',
                'Calculer et interpréter des statistiques descriptives',
                'Construire et interpréter des intervalles de confiance',
                'Réaliser et interpréter un test d\'hypothèse de base'
            ],
            'syllabus': [
                {'title': 'Descriptive Statistics & Summarizing Data', 'lessons': 5, 'hours': 2},
                {'title': 'Probability Fundamentals', 'lessons': 5, 'hours': 2},
                {'title': 'Common Distributions', 'lessons': 5, 'hours': 2},
                {'title': 'Confidence Intervals', 'lessons': 4, 'hours': 1.5},
                {'title': 'Introduction to Hypothesis Testing', 'lessons': 5, 'hours': 2}
            ],
            'syllabus_fr': [
                {'title': 'Statistiques descriptives et synthèse des données', 'lessons': 5, 'hours': 2},
                {'title': 'Fondamentaux des probabilités', 'lessons': 5, 'hours': 2},
                {'title': 'Distributions courantes', 'lessons': 5, 'hours': 2},
                {'title': 'Intervalles de confiance', 'lessons': 4, 'hours': 1.5},
                {'title': 'Introduction aux tests d\'hypothèses', 'lessons': 5, 'hours': 2}
            ]
        },
        {
            'title': 'Data Processing',
            'title_fr': 'Traitement des données',
            'icon': '🔧',
            'description': 'Learn ETL processes, data cleaning, transformation, and preparation for analysis. Hands-on with real datasets.',
            'description_fr': 'Apprenez les processus ETL, le nettoyage des données, la transformation et la préparation pour l\'analyse. Travaux pratiques avec de vrais jeux de données.',
            'level': 'Intermediate',
            'duration': '6 weeks',
            'duration_fr': '6 semaines',
            'prerequisites': 'Statistical Basics, or equivalent familiarity with core statistics concepts.',
            'prerequisites_fr': 'Bases de la statistique, ou une familiarité équivalente avec les concepts statistiques fondamentaux.',
            'outcomes': [
                'Clean messy, real-world datasets: missing values, duplicates, and outliers',
                'Build repeatable ETL (extract, transform, load) workflows',
                'Reshape and merge datasets for analysis',
                'Prepare a dataset end to end for a statistical analysis'
            ],
            'outcomes_fr': [
                'Nettoyer des jeux de données réels et désordonnés : valeurs manquantes, doublons et valeurs aberrantes',
                'Construire des flux ETL (extraction, transformation, chargement) reproductibles',
                'Remodeler et fusionner des jeux de données pour l\'analyse',
                'Préparer un jeu de données de bout en bout pour une analyse statistique'
            ],
            'syllabus': [
                {'title': 'Understanding ETL Pipelines', 'lessons': 4, 'hours': 1.5},
                {'title': 'Cleaning Real-World Data', 'lessons': 5, 'hours': 2},
                {'title': 'Transforming & Reshaping Data', 'lessons': 5, 'hours': 2},
                {'title': 'Merging & Joining Datasets', 'lessons': 4, 'hours': 1.5},
                {'title': 'Case Study: Business Dataset', 'lessons': 4, 'hours': 1.5},
                {'title': 'Case Study: Survey Dataset', 'lessons': 4, 'hours': 1.5}
            ],
            'syllabus_fr': [
                {'title': 'Comprendre les pipelines ETL', 'lessons': 4, 'hours': 1.5},
                {'title': 'Nettoyer des données réelles', 'lessons': 5, 'hours': 2},
                {'title': 'Transformer et remodeler les données', 'lessons': 5, 'hours': 2},
                {'title': 'Fusionner et joindre des jeux de données', 'lessons': 4, 'hours': 1.5},
                {'title': 'Étude de cas : jeu de données commercial', 'lessons': 4, 'hours': 1.5},
                {'title': 'Étude de cas : jeu de données d\'enquête', 'lessons': 4, 'hours': 1.5}
            ]
        },
        {
            'title': 'Advanced Analysis',
            'title_fr': 'Analyse avancée',
            'icon': '🎓',
            'description': 'Dive into regression, ANOVA, multivariate analysis, and predictive modeling. Advanced statistical techniques.',
            'description_fr': 'Plongez dans la régression, l\'ANOVA, l\'analyse multivariée et la modélisation prédictive. Techniques statistiques avancées.',
            'level': 'Advanced',
            'duration': '8 weeks',
            'duration_fr': '8 semaines',
            'prerequisites': 'Statistical Basics and Data Processing, or equivalent experience.',
            'prerequisites_fr': 'Bases de la statistique et Traitement des données, ou une expérience équivalente.',
            'outcomes': [
                'Build and interpret linear and multiple regression models',
                'Run and interpret ANOVA for comparing multiple groups',
                'Apply multivariate analysis techniques',
                'Build a basic predictive model and evaluate its performance'
            ],
            'outcomes_fr': [
                'Construire et interpréter des modèles de régression linéaire simple et multiple',
                'Réaliser et interpréter une ANOVA pour comparer plusieurs groupes',
                'Appliquer des techniques d\'analyse multivariée',
                'Construire un modèle prédictif de base et évaluer sa performance'
            ],
            'syllabus': [
                {'title': 'Simple & Multiple Linear Regression', 'lessons': 6, 'hours': 2.5},
                {'title': 'Analysis of Variance (ANOVA)', 'lessons': 5, 'hours': 2},
                {'title': 'Multivariate Analysis Techniques', 'lessons': 5, 'hours': 2},
                {'title': 'Introduction to Predictive Modeling', 'lessons': 6, 'hours': 2.5},
                {'title': 'Model Evaluation & Validation', 'lessons': 5, 'hours': 2},
                {'title': 'Capstone Project', 'lessons': 3, 'hours': 3}
            ],
            'syllabus_fr': [
                {'title': 'Régression linéaire simple et multiple', 'lessons': 6, 'hours': 2.5},
                {'title': 'Analyse de la variance (ANOVA)', 'lessons': 5, 'hours': 2},
                {'title': 'Techniques d\'analyse multivariée', 'lessons': 5, 'hours': 2},
                {'title': 'Introduction à la modélisation prédictive', 'lessons': 6, 'hours': 2.5},
                {'title': 'Évaluation et validation du modèle', 'lessons': 5, 'hours': 2},
                {'title': 'Projet de synthèse', 'lessons': 3, 'hours': 3}
            ]
        }
    ]

    for c in courses:
        db.session.add(Course(
            title=c['title'],
            title_fr=c['title_fr'],
            icon=c['icon'],
            description=c['description'],
            description_fr=c['description_fr'],
            level=c['level'],
            duration=c['duration'],
            duration_fr=c['duration_fr'],
            prerequisites=c['prerequisites'],
            prerequisites_fr=c['prerequisites_fr'],
            outcomes=json.dumps(c['outcomes']),
            outcomes_fr=json.dumps(c['outcomes_fr']),
            syllabus=json.dumps(c['syllabus']),
            syllabus_fr=json.dumps(c['syllabus_fr'])
        ))
    db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        seed_courses()

    app.run(debug=True, host='0.0.0.0', port=5000)
