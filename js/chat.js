// AI Learning Assistant chat widget

const CHAT_LANG = window.MICOMP_LANG || 'en';
const CHAT_STRINGS = {
    en: { thinking: 'Thinking...', notConfigured: "The AI assistant isn't configured yet. Try exploring our courses instead!", unreachable: "Sorry, I couldn't reach the AI assistant right now. Please try again later." },
    fr: { thinking: 'Réflexion en cours...', notConfigured: "L'assistant IA n'est pas encore configuré. Essayez plutôt d'explorer nos cours !", unreachable: "Désolé, impossible de joindre l'assistant IA pour le moment. Veuillez réessayer plus tard." }
};
const CS = CHAT_STRINGS[CHAT_LANG] || CHAT_STRINGS.en;

function escapeHtml(text) {
    const map = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' };
    return text.replace(/[&<>"']/g, m => map[m]);
}

async function sendMessage() {
    const chatInput = document.getElementById('chatInput');
    const chatMessages = document.getElementById('chatMessages');
    const userMessage = chatInput.value.trim();

    if (userMessage === '') return;

    const userMsgDiv = document.createElement('div');
    userMsgDiv.className = 'message user-message';
    userMsgDiv.innerHTML = `<p>${escapeHtml(userMessage)}</p>`;
    chatMessages.appendChild(userMsgDiv);

    chatInput.value = '';
    chatMessages.scrollTop = chatMessages.scrollHeight;

    const aiMsgDiv = document.createElement('div');
    aiMsgDiv.className = 'message assistant-message';
    aiMsgDiv.innerHTML = `<p>${CS.thinking}</p>`;
    chatMessages.appendChild(aiMsgDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;

    try {
        const result = await apiClient.chat(userMessage, null, null, CHAT_LANG);

        if (result.status === 'success') {
            aiMsgDiv.innerHTML = `<p>${escapeHtml(result.answer)}</p>`;
        } else {
            aiMsgDiv.innerHTML = `<p>${CS.notConfigured}</p>`;
        }
    } catch (error) {
        aiMsgDiv.innerHTML = `<p>${CS.unreachable}</p>`;
    }

    chatMessages.scrollTop = chatMessages.scrollHeight;
}

document.getElementById('chatSendBtn')?.addEventListener('click', sendMessage);
document.getElementById('chatInput')?.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        sendMessage();
    }
});
