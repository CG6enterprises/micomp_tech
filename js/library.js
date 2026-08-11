// Library page: glossary search/filter + AI "explain this simply" buttons

const LIB_LANG = window.MICOMP_LANG || 'en';
const LIB_STRINGS = {
    en: { thinking: 'Thinking...', notConfigured: "The AI assistant isn't configured yet.", unreachable: "Couldn't reach the AI assistant right now." },
    fr: { thinking: 'Réflexion en cours...', notConfigured: "L'assistant IA n'est pas encore configuré.", unreachable: "Impossible de joindre l'assistant IA pour le moment." }
};
const LS = LIB_STRINGS[LIB_LANG] || LIB_STRINGS.en;

const searchInput = document.getElementById('glossarySearch');
const filterChips = document.querySelectorAll('.filter-chip');
const terms = document.querySelectorAll('.glossary-term');
const noResults = document.getElementById('noResults');

let activeCategory = 'all';

function applyFilters() {
    const query = (searchInput?.value || '').trim().toLowerCase();
    let visibleCount = 0;

    terms.forEach(termEl => {
        const matchesCategory = activeCategory === 'all' || termEl.dataset.category === activeCategory;
        const matchesQuery = query === '' || termEl.dataset.term.includes(query) || termEl.textContent.toLowerCase().includes(query);
        const visible = matchesCategory && matchesQuery;
        termEl.style.display = visible ? '' : 'none';
        if (visible) visibleCount++;
    });

    if (noResults) noResults.style.display = visibleCount === 0 ? 'block' : 'none';
}

searchInput?.addEventListener('input', applyFilters);

filterChips.forEach(chip => {
    chip.addEventListener('click', () => {
        filterChips.forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        activeCategory = chip.dataset.category;
        applyFilters();
    });
});

// AI "explain this simply" buttons
document.querySelectorAll('.explain-btn').forEach((btn, index) => {
    btn.addEventListener('click', async () => {
        const concept = btn.dataset.concept;
        const targetId = btn.closest('.glossary-term').querySelector('.ai-explanation').id;
        const target = document.getElementById(targetId);

        target.style.display = 'block';
        target.textContent = LS.thinking;
        btn.disabled = true;

        try {
            const result = await apiClient.request('/explain', {
                method: 'POST',
                body: JSON.stringify({ concept, level: 'beginner', language: LIB_LANG })
            });
            if (result.status === 'success') {
                target.textContent = result.answer;
            } else {
                target.textContent = LS.notConfigured;
            }
        } catch (error) {
            target.textContent = LS.unreachable;
        } finally {
            btn.disabled = false;
        }
    });
});
