// Micomp_Tech - Main Application Logic

// Modal Functions
function openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.add('active');
    }
}

function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.remove('active');
    }
}

// Login Button
document.getElementById('loginBtn')?.addEventListener('click', () => {
    openModal('loginModal');
});

// Signup Button
document.getElementById('signupBtn')?.addEventListener('click', () => {
    openModal('signupModal');
});

// Close modal when clicking outside of it
window.addEventListener('click', (event) => {
    if (event.target.classList.contains('modal')) {
        event.target.classList.remove('active');
    }
});

// Tool Functions
function openTool(toolName) {
    alert(`Opening ${toolName} tool. Feature coming soon!`);
}

// Client Form Function
function openForm(formType) {
    alert(`Opening ${formType} form. Feature coming soon!`);
}

// Chat Functions
function sendMessage() {
    const chatInput = document.getElementById('chatInput');
    const chatMessages = document.getElementById('chatMessages');
    const userMessage = chatInput.value.trim();

    if (userMessage === '') return;

    // Add user message to chat
    const userMsgDiv = document.createElement('div');
    userMsgDiv.className = 'message user-message';
    userMsgDiv.innerHTML = `<p>${escapeHtml(userMessage)}</p>`;
    chatMessages.appendChild(userMsgDiv);

    // Clear input
    chatInput.value = '';

    // Simulate AI response (replace with actual API call later)
    setTimeout(() => {
        const aiResponse = getAIResponse(userMessage);
        const aiMsgDiv = document.createElement('div');
        aiMsgDiv.className = 'message assistant-message';
        aiMsgDiv.innerHTML = `<p>${aiResponse}</p>`;
        chatMessages.appendChild(aiMsgDiv);
        
        // Scroll to bottom
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }, 500);

    // Scroll to bottom
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function getAIResponse(userMessage) {
    const responses = {
        'statistics': 'Statistics is the science of collecting, analyzing, and interpreting data. It helps us make informed decisions based on evidence.',
        'data collection': 'Data collection is the first step in any analysis. Good data collection ensures accuracy and reliability of results.',
        'sample': 'A sample is a subset of a population selected for analysis. Good sampling methods include random sampling, stratified sampling, and cluster sampling.',
        'mean': 'The mean is the average of all values in a dataset. It\'s calculated by summing all values and dividing by the number of values.',
        'hypothesis': 'Hypothesis testing is a statistical method used to determine if there is enough evidence to reject a null hypothesis.',
        'regression': 'Regression analysis is used to model the relationship between a dependent variable and one or more independent variables.',
        'default': 'That\'s a great question! I\'m learning about this topic. For now, I recommend exploring our courses to dive deeper into statistical concepts.'
    };

    const lowerMessage = userMessage.toLowerCase();
    for (const [key, response] of Object.entries(responses)) {
        if (lowerMessage.includes(key)) {
            return response;
        }
    }

    return responses.default;
}

function escapeHtml(text) {
    const map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
    };
    return text.replace(/[&<>"']/g, m => map[m]);
}

// Allow Enter key to send message
document.getElementById('chatInput')?.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        sendMessage();
    }
});

// Smooth Scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// Form Submission
document.getElementById('contactForm')?.addEventListener('submit', (e) => {
    e.preventDefault();
    alert('Thank you for your message! We will get back to you soon.');
    e.target.reset();
});

// Initialize
console.log('Micomp_Tech Application Loaded');