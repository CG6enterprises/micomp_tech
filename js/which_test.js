// "Which Test Should I Use?" decision guide

const steps = document.querySelectorAll('[data-step]');

function showStep(stepKey) {
    steps.forEach(el => el.classList.remove('active'));
    const target = document.querySelector(`[data-step="${stepKey}"]`);
    if (target) target.classList.add('active');
}

document.querySelectorAll('.decision-option').forEach(btn => {
    btn.addEventListener('click', () => showStep(btn.dataset.next));
});

document.querySelectorAll('.decision-back').forEach(btn => {
    btn.addEventListener('click', () => showStep(btn.dataset.back));
});
