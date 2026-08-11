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
async function sendMessage() {
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
    chatMessages.scrollTop = chatMessages.scrollHeight;

    // Show a placeholder while the AI answers
    const aiMsgDiv = document.createElement('div');
    aiMsgDiv.className = 'message assistant-message';
    aiMsgDiv.innerHTML = '<p>Thinking...</p>';
    chatMessages.appendChild(aiMsgDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;

    try {
        const result = await apiClient.chat(userMessage);

        if (result.status === 'success') {
            aiMsgDiv.innerHTML = `<p>${escapeHtml(result.answer)}</p>`;
        } else {
            aiMsgDiv.innerHTML = '<p>The AI assistant isn\'t configured yet. Try exploring our courses instead!</p>';
        }
    } catch (error) {
        aiMsgDiv.innerHTML = '<p>Sorry, I couldn\'t reach the AI assistant right now. Please try again later.</p>';
    }

    chatMessages.scrollTop = chatMessages.scrollHeight;
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