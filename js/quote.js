// Services page: Request a Quote form

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
            service_category: category
        });
        status.textContent = result.message || 'Thanks! We received your request.';
        status.classList.add('form-status-success');
        event.target.reset();
    } catch (error) {
        status.textContent = error.message || 'Something went wrong. Please try again.';
        status.classList.add('form-status-error');
    } finally {
        submitBtn.disabled = false;
    }
});
