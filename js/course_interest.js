// Course detail page: "Notify Me" interest form

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
            service_category: courseTitle
        });
        status.textContent = result.message || "Thanks! We'll email you when this course opens.";
        status.classList.add('form-status-success');
        event.target.reset();
    } catch (error) {
        status.textContent = error.message || 'Something went wrong. Please try again.';
        status.classList.add('form-status-error');
    } finally {
        submitBtn.disabled = false;
    }
});
