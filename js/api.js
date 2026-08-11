// API Integration Module
// Handles communication with backend API

// Relative path: works regardless of host/port since pages are served by the same Flask app.
const API_BASE_URL = '/api';

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

        let response;
        try {
            response = await fetch(url, config);
        } catch (error) {
            throw new Error('Network error: could not reach the server');
        }

        let data = null;
        try {
            data = await response.json();
        } catch (error) {
            // Response had no JSON body
        }

        if (!response.ok) {
            const message = (data && data.error) ? data.error : `Request failed (${response.status})`;
            throw new Error(message);
        }

        return data;
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

    // Contact / lead endpoints
    async submitContact(payload) {
        return this.request('/contact', {
            method: 'POST',
            body: JSON.stringify(payload)
        });
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

    async regressionAnalysis(x, y) {
        return this.request('/analysis/regression', {
            method: 'POST',
            body: JSON.stringify({ x, y })
        });
    }

    // AI Assistant endpoint
    async chat(message, context = null, provider = null) {
        return this.request('/chat', {
            method: 'POST',
            body: JSON.stringify({ message, context, provider })
        });
    }
}

// Initialize API client
const apiClient = new APIClient();

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = APIClient;
}
