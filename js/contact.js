// Contact page form

const CONTACT_LANG = window.MICOMP_LANG || 'en';
const CONTACT_FALLBACK_ERROR = CONTACT_LANG === 'fr'
    ? 'Un problème est survenu. Veuillez réessayer.'
    : 'Something went wrong. Please try again.';

document.getElementById('contactForm')?.addEventListener('submit', async (event) => {
    event.preventDefault();
    const status = document.getElementById('contactStatus');
    const submitBtn = event.target.querySelector('button[type="submit"]');

    const name = document.getElementById('contactName').value.trim();
    const email = document.getElementById('contactEmail').value.trim();
    const message = document.getElementById('contactMessage').value.trim();

    status.textContent = '';
    status.className = 'form-status';
    submitBtn.disabled = true;

    try {
        const result = await apiClient.submitContact({
            name,
            email,
            message,
            inquiry_type: 'general',
            language: CONTACT_LANG
        });
        status.textContent = result.message || CONTACT_FALLBACK_ERROR;
        status.classList.add('form-status-success');
        event.target.reset();
    } catch (error) {
        status.textContent = error.message || CONTACT_FALLBACK_ERROR;
        status.classList.add('form-status-error');
    } finally {
        submitBtn.disabled = false;
    }
});
