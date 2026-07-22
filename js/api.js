// API Integration Module
// Handles communication with backend API

const API_BASE_URL = 'http://localhost:5000/api';

class APIClient {
    constructor(baseURL = API_BASE_URL) {
        this.baseURL = baseURL;
    }

    async request(endpoint, options = {}) {
        const url = `${this.baseURL}${endpoint}`;
        const config = {
            headers: {
                'Content-Type': 'application/json',
                ...options.headers
            },
            ...options
        };

        try {
            const response = await fetch(url, config);
            if (!response.ok) {
                throw new Error(`API Error: ${response.statusText}`);
            }
            return await response.json();
        } catch (error) {
            console.error('API Request Error:', error);
            throw error;
        }
    }

    // User endpoints
    async createUser(userData) {
        return this.request('/users', {
            method: 'POST',
            body: JSON.stringify(userData)
        });
    }

    async getUser(userId) {
        return this.request(`/users/${userId}`);
    }

    // Course endpoints
    async getCourses() {
        return this.request('/courses');
    }

    async getCourse(courseId) {
        return this.request(`/courses/${courseId}`);
    }

    async createCourse(courseData) {
        return this.request('/courses', {
            method: 'POST',
            body: JSON.stringify(courseData)
        });
    }

    // Enrollment endpoints
    async enrollCourse(enrollmentData) {
        return this.request('/enrollments', {
            method: 'POST',
            body: JSON.stringify(enrollmentData)
        });
    }

    async getUserEnrollments(userId) {
        return this.request(`/enrollments/${userId}`);
    }

    // Project endpoints
    async getProjects() {
        return this.request('/projects');
    }

    async createProject(projectData) {
        return this.request('/projects', {
            method: 'POST',
            body: JSON.stringify(projectData)
        });
    }

    // Invoice endpoints
    async createInvoice(invoiceData) {
        return this.request('/invoices', {
            method: 'POST',
            body: JSON.stringify(invoiceData)
        });
    }

    async getProjectInvoices(projectId) {
        return this.request(`/invoices/${projectId}`);
    }

    // Analysis endpoints
    async descriptiveStats(values) {
        return this.request('/analysis/descriptive', {
            method: 'POST',
            body: JSON.stringify({ values })
        });
    }

    async correlationAnalysis(x, y) {
        return this.request('/analysis/correlation', {
            method: 'POST',
            body: JSON.stringify({ x, y })
        });
    }

    async ttestAnalysis(group1, group2) {
        return this.request('/analysis/ttest', {
            method: 'POST',
            body: JSON.stringify({ group1, group2 })
        });
    }
}

// Initialize API client
const apiClient = new APIClient();

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = APIClient;
}