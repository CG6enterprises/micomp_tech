// Services page: Request a Quote form

const QUOTE_LANG = window.MICOMP_LANG || 'en';
const QUOTE_FALLBACK_ERROR = QUOTE_LANG === 'fr'
    ? 'Un problème est survenu. Veuillez réessayer.'
    : 'Something went wrong. Please try again.';

document.getElementById('quoteForm')?.addEventListener('submit', async (event) => {
    event.preventDefault();
    const status = document.getElementById('quoteStatus');
    const submitBtn = event.target.querySelector('button[type="submit"]');

    const name = document.getElementById('quoteName').value.trim();
    const email = document.getElementById('quoteEmail').value.trim();
    const category = document.getElementById('quoteCategory').value;
    const message = document.getElementById('quoteMessage').value.trim();

    status.textContent = '';
    status.className = 'form-status';
    submitBtn.disabled = true;

    try {
        const result = await apiClient.submitContact({
            name,
            email,
            message,
            inquiry_type: 'quote',
            service_category: category,
            language: QUOTE_LANG
        });
        status.textContent = result.message || QUOTE_FALLBACK_ERROR;
        status.classList.add('form-status-success');
        event.target.reset();
    } catch (error) {
        status.textContent = error.message || QUOTE_FALLBACK_ERROR;
        status.classList.add('form-status-error');
    } finally {
        submitBtn.disabled = false;
    }
});
