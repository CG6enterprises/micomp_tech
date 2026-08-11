// Contact page form

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
            inquiry_type: 'general'
        });
        status.textContent = result.message || 'Thanks! We received your message.';
        status.classList.add('form-status-success');
        event.target.reset();
    } catch (error) {
        status.textContent = error.message || 'Something went wrong. Please try again.';
        status.classList.add('form-status-error');
    } finally {
        submitBtn.disabled = false;
    }
});
