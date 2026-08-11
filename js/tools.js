// Statistical Analysis Tools page logic

const CHART_BLUE = '#0055B8';
const CHART_NAVY = '#003366';
const CHART_GOLD = '#D4AF37';

function parseNumberList(text) {
    const parts = text.split(',').map(s => s.trim()).filter(s => s.length > 0);
    if (parts.length === 0) {
        throw new Error('Enter at least one number');
    }
    const values = parts.map(Number);
    if (values.some(v => Number.isNaN(v))) {
        throw new Error('All values must be numbers, separated by commas');
    }
    return values;
}

function setError(elId, message) {
    const el = document.getElementById(elId);
    if (el) el.textContent = message || '';
}

function renderResultCards(containerId, entries) {
    const container = document.getElementById(containerId);
    if (!container) return;
    container.innerHTML = entries.map(([label, value]) => `
        <div class="result-card">
            <span class="result-label">${label}</span>
            <span class="result-value">${value}</span>
        </div>
    `).join('');
}

function fmt(n, digits = 3) {
    return typeof n === 'number' ? n.toFixed(digits) : n;
}

// ---- Canvas charts ----

function clearCanvas(canvas) {
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

function drawBarChart(canvas, values) {
    canvas.style.display = 'block';
    const ctx = canvas.getContext('2d');
    clearCanvas(canvas);
    const padding = 30;
    const w = canvas.width - padding * 2;
    const h = canvas.height - padding * 2;
    const maxV = Math.max(...values, 0);
    const minV = Math.min(...values, 0);
    const range = (maxV - minV) || 1;
    const barWidth = w / values.length;

    ctx.strokeStyle = '#ccc';
    ctx.beginPath();
    ctx.moveTo(padding, canvas.height - padding);
    ctx.lineTo(canvas.width - padding, canvas.height - padding);
    ctx.stroke();

    values.forEach((v, i) => {
        const barHeight = ((v - minV) / range) * h;
        const x = padding + i * barWidth + barWidth * 0.15;
        const y = canvas.height - padding - barHeight;
        ctx.fillStyle = CHART_BLUE;
        ctx.fillRect(x, y, barWidth * 0.7, barHeight);
    });
}

function drawScatter(canvas, xs, ys, fitLine = null) {
    canvas.style.display = 'block';
    const ctx = canvas.getContext('2d');
    clearCanvas(canvas);
    const padding = 35;
    const w = canvas.width - padding * 2;
    const h = canvas.height - padding * 2;

    const minX = Math.min(...xs), maxX = Math.max(...xs);
    const minY = Math.min(...ys), maxY = Math.max(...ys);
    const rangeX = (maxX - minX) || 1;
    const rangeY = (maxY - minY) || 1;

    const toPx = (x, y) => [
        padding + ((x - minX) / rangeX) * w,
        canvas.height - padding - ((y - minY) / rangeY) * h
    ];

    ctx.strokeStyle = '#ccc';
    ctx.beginPath();
    ctx.moveTo(padding, padding);
    ctx.lineTo(padding, canvas.height - padding);
    ctx.lineTo(canvas.width - padding, canvas.height - padding);
    ctx.stroke();

    if (fitLine) {
        const [x1, y1] = toPx(minX, fitLine.slope * minX + fitLine.intercept);
        const [x2, y2] = toPx(maxX, fitLine.slope * maxX + fitLine.intercept);
        ctx.strokeStyle = CHART_GOLD;
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(x1, y1);
        ctx.lineTo(x2, y2);
        ctx.stroke();
        ctx.lineWidth = 1;
    }

    ctx.fillStyle = CHART_NAVY;
    xs.forEach((x, i) => {
        const [px, py] = toPx(x, ys[i]);
        ctx.beginPath();
        ctx.arc(px, py, 4, 0, Math.PI * 2);
        ctx.fill();
    });
}

// ---- Descriptive Statistics ----

document.getElementById('descBtn')?.addEventListener('click', async () => {
    setError('descError', '');
    try {
        const values = parseNumberList(document.getElementById('descValues').value);
        const result = await apiClient.descriptiveStats(values);
        renderResultCards('descResults', [
            ['Count', result.count],
            ['Mean', fmt(result.mean)],
            ['Median', fmt(result.median)],
            ['Std Dev', fmt(result.std_dev)],
            ['Variance', fmt(result.variance)],
            ['Min', fmt(result.min)],
            ['Max', fmt(result.max)],
            ['Range', fmt(result.range)],
            ['Q1', fmt(result.q1)],
            ['Q3', fmt(result.q3)]
        ]);
        drawBarChart(document.getElementById('descChart'), values);
    } catch (error) {
        setError('descError', error.message);
        document.getElementById('descResults').innerHTML = '';
    }
});

// ---- Correlation ----

document.getElementById('corrBtn')?.addEventListener('click', async () => {
    setError('corrError', '');
    try {
        const x = parseNumberList(document.getElementById('corrX').value);
        const y = parseNumberList(document.getElementById('corrY').value);
        if (x.length !== y.length) {
            throw new Error('X and Y must have the same number of values');
        }
        const result = await apiClient.correlationAnalysis(x, y);
        renderResultCards('corrResults', [
            ['Correlation (r)', fmt(result.correlation)],
            ['P-value', fmt(result.p_value, 4)],
            ['Strength', result.interpretation]
        ]);
        drawScatter(document.getElementById('corrChart'), x, y);
    } catch (error) {
        setError('corrError', error.message);
        document.getElementById('corrResults').innerHTML = '';
    }
});

// ---- Hypothesis Testing ----

document.getElementById('ttestBtn')?.addEventListener('click', async () => {
    setError('ttestError', '');
    try {
        const group1 = parseNumberList(document.getElementById('ttestG1').value);
        const group2 = parseNumberList(document.getElementById('ttestG2').value);
        const result = await apiClient.ttestAnalysis(group1, group2);
        renderResultCards('ttestResults', [
            ['T-statistic', fmt(result.t_statistic)],
            ['P-value', fmt(result.p_value, 4)],
            ['Significant (p < 0.05)', result.significant ? 'Yes' : 'No'],
            ['Interpretation', result.interpretation]
        ]);
    } catch (error) {
        setError('ttestError', error.message);
        document.getElementById('ttestResults').innerHTML = '';
    }
});

// ---- Regression ----

// ---- Deep-link support: /tools?open=descriptive|correlation|ttest|regression ----

(function scrollToRequestedPanel() {
    const params = new URLSearchParams(window.location.search);
    const target = params.get('open');
    const panelMap = {
        descriptive: 0,
        correlation: 1,
        ttest: 2,
        regression: 3
    };
    if (target && target in panelMap) {
        const panels = document.querySelectorAll('.tool-panel');
        const panel = panels[panelMap[target]];
        if (panel) {
            panel.classList.add('tool-panel-highlight');
            setTimeout(() => panel.scrollIntoView({ behavior: 'smooth', block: 'center' }), 100);
        }
    }
})();

document.getElementById('regBtn')?.addEventListener('click', async () => {
    setError('regError', '');
    try {
        const x = parseNumberList(document.getElementById('regX').value);
        const y = parseNumberList(document.getElementById('regY').value);
        if (x.length !== y.length) {
            throw new Error('X and Y must have the same number of values');
        }
        const result = await apiClient.regressionAnalysis(x, y);
        renderResultCards('regResults', [
            ['Equation', result.equation],
            ['Slope', fmt(result.slope)],
            ['Intercept', fmt(result.intercept)],
            ['R²', fmt(result.r_squared)],
            ['P-value', fmt(result.p_value, 4)],
            ['Std Error', fmt(result.std_err)]
        ]);
        drawScatter(document.getElementById('regChart'), x, y, { slope: result.slope, intercept: result.intercept });
    } catch (error) {
        setError('regError', error.message);
        document.getElementById('regResults').innerHTML = '';
    }
});
