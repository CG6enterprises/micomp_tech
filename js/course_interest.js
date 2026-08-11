// Course detail page: "Notify Me" interest form

const INTEREST_LANG = window.MICOMP_LANG || 'en';
const INTEREST_FALLBACK_ERROR = INTEREST_LANG === 'fr'
    ? 'Un problème est survenu. Veuillez réessayer.'
    : 'Something went wrong. Please try again.';

document.getElementById('courseInterestForm')?.addEventListener('submit', async (event) => {
    event.preventDefault();
    const status = document.getElementById('interestStatus');
    const submitBtn = event.target.querySelector('button[type="submit"]');

    const courseTitle = document.getElementById('courseTitle').value;
    const name = document.getElementById('interestName').value.trim();
    const email = document.getElementById('interestEmail').value.trim();

    status.textContent = '';
    status.className = 'form-status';
    submitBtn.disabled = true;

    try {
        const result = await apiClient.submitContact({
            name,
            email,
            message: `Interested in enrolling in "${courseTitle}" once it opens.`,
            inquiry_type: 'course_interest',
            service_category: courseTitle,
            language: INTEREST_LANG
        });
        status.textContent = result.message || INTEREST_FALLBACK_ERROR;
        status.classList.add('form-status-success');
        event.target.reset();
    } catch (error) {
        status.textContent = error.message || INTEREST_FALLBACK_ERROR;
        status.classList.add('form-status-error');
    } finally {
        submitBtn.disabled = false;
    }
});
