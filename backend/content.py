"""
Static content for the reference library: glossary terms, sample datasets,
and worked case studies. Kept as plain data (not DB models) since it's
authored content, not user-generated data.
"""

GLOSSARY = [
    {
        'term': 'Mean',
        'category': 'Descriptive Statistics',
        'definition': 'The arithmetic average of a set of values: add them all up, divide by how many there are. Sensitive to extreme values (outliers) pulling it away from the "typical" value.',
        'related_tool': 'descriptive',
    },
    {
        'term': 'Median',
        'category': 'Descriptive Statistics',
        'definition': 'The middle value when data is sorted from smallest to largest. Unlike the mean, it is not distorted by outliers, which makes it a better summary for skewed data like income or home prices.',
        'related_tool': 'descriptive',
    },
    {
        'term': 'Mode',
        'category': 'Descriptive Statistics',
        'definition': 'The most frequently occurring value in a dataset. A dataset can have no mode, one mode, or several (bimodal, multimodal).',
        'related_tool': 'descriptive',
    },
    {
        'term': 'Standard Deviation',
        'category': 'Descriptive Statistics',
        'definition': 'A measure of how spread out values are around the mean. A small standard deviation means values cluster tightly around the mean; a large one means they are spread widely.',
        'related_tool': 'descriptive',
    },
    {
        'term': 'Variance',
        'category': 'Descriptive Statistics',
        'definition': 'The standard deviation squared. Useful mathematically (it adds cleanly across independent variables) but harder to interpret directly since it is in squared units.',
        'related_tool': 'descriptive',
    },
    {
        'term': 'Quartile',
        'category': 'Descriptive Statistics',
        'definition': 'One of three values (Q1, Q2/median, Q3) that split sorted data into four equal groups. Q1 is the value below which 25% of the data falls; Q3 is the value below which 75% falls.',
        'related_tool': 'descriptive',
    },
    {
        'term': 'Outlier',
        'category': 'Descriptive Statistics',
        'definition': 'A data point that falls far outside the pattern of the rest of the dataset. Outliers can be genuine (a real extreme case) or errors (a typo in data entry) — the two require very different responses.',
        'related_tool': 'descriptive',
    },
    {
        'term': 'Population vs. Sample',
        'category': 'Study Design',
        'definition': 'A population is every member of the group you care about. A sample is the subset you actually collected data from. Statistics uses samples to make informed guesses about populations, because measuring an entire population is usually impossible.',
        'related_tool': None,
    },
    {
        'term': 'Sampling Bias',
        'category': 'Study Design',
        'definition': 'A systematic error introduced when your sample does not represent the population, because of how it was collected. A survey of only your existing customers cannot tell you why people who never bought from you stayed away.',
        'related_tool': None,
    },
    {
        'term': 'Probability Distribution',
        'category': 'Probability',
        'definition': 'A description of how likely each possible outcome of a random variable is. The normal (bell-curve) distribution is the most common one used in statistics.',
        'related_tool': None,
    },
    {
        'term': 'Normal Distribution',
        'category': 'Probability',
        'definition': 'A symmetric, bell-shaped distribution where most values cluster near the mean. Many statistical tests assume the data is roughly normally distributed.',
        'related_tool': None,
    },
    {
        'term': 'Correlation',
        'category': 'Relationships Between Variables',
        'definition': 'A measure, from -1 to 1, of how strongly two variables move together in a straight-line pattern. Positive means they rise together; negative means one rises as the other falls. A correlation near 0 means little to no linear relationship.',
        'related_tool': 'correlation',
    },
    {
        'term': 'Correlation vs. Causation',
        'category': 'Relationships Between Variables',
        'definition': 'Two variables being correlated does not mean one causes the other. Ice cream sales and drowning deaths both rise in summer — heat causes both, neither causes the other.',
        'related_tool': 'correlation',
    },
    {
        'term': 'P-value',
        'category': 'Hypothesis Testing',
        'definition': 'The probability of seeing a result at least as extreme as yours, if there were actually no real effect. A small p-value (conventionally under 0.05) suggests the result is unlikely to be due to chance alone.',
        'related_tool': 'ttest',
    },
    {
        'term': 'Statistical Significance',
        'category': 'Hypothesis Testing',
        'definition': 'A result is "statistically significant" when the p-value falls below a chosen threshold (usually 0.05). It means the result is unlikely to be random noise — it does not automatically mean the effect is large or important.',
        'related_tool': 'ttest',
    },
    {
        'term': 'Null Hypothesis',
        'category': 'Hypothesis Testing',
        'definition': 'The default assumption that there is no real effect or difference. A hypothesis test looks for enough evidence in the data to reject this assumption in favor of a real effect.',
        'related_tool': 'ttest',
    },
    {
        'term': 'T-test',
        'category': 'Hypothesis Testing',
        'definition': 'A statistical test that compares the means of two groups to see if the difference between them is likely to be real, or just due to random variation in the sample.',
        'related_tool': 'ttest',
    },
    {
        'term': 'Confidence Interval',
        'category': 'Hypothesis Testing',
        'definition': 'A range of values, calculated from your sample, that likely contains the true population value. A "95% confidence interval" means if you repeated the sampling many times, 95% of the intervals calculated would contain the true value.',
        'related_tool': None,
    },
    {
        'term': 'Sample Size',
        'category': 'Study Design',
        'definition': 'The number of observations in your data. Small samples produce noisy, unreliable estimates and can fail to detect a real effect (low statistical power) even when one exists.',
        'related_tool': None,
    },
    {
        'term': 'Linear Regression',
        'category': 'Relationships Between Variables',
        'definition': 'A technique that fits a straight line through your data to predict one variable from another. The slope tells you how much the outcome changes per unit of the predictor.',
        'related_tool': 'regression',
    },
    {
        'term': 'R-squared (R²)',
        'category': 'Relationships Between Variables',
        'definition': 'The proportion of variation in the outcome that is explained by the regression line, from 0 to 1. An R² of 0.80 means 80% of the variation in the outcome is explained by the predictor; the rest is other factors or noise.',
        'related_tool': 'regression',
    },
    {
        'term': 'ETL (Extract, Transform, Load)',
        'category': 'Data Processing',
        'definition': 'The standard workflow for preparing raw data for analysis: pull it from its source, clean and reshape it, then load it somewhere ready for analysis.',
        'related_tool': None,
    },
]

# related_tool values map to the tool panel IDs used on /tools (see tools.html + tools.js)
TOOL_LABELS = {
    'descriptive': 'Descriptive Statistics',
    'correlation': 'Correlation Analysis',
    'ttest': 'Hypothesis Testing',
    'regression': 'Regression Analysis',
}

# Human-readable labels for keys that appear in CASE_STUDIES[i]['results']
RESULT_LABELS = {
    'equation': 'Equation',
    'r_squared': 'R²',
    'p_value': 'P-value',
    'slope': 'Slope',
    'correlation': 'Correlation (r)',
    't_statistic': 'T-statistic',
    'tutor_mean': 'Tutor Group Mean',
    'no_tutor_mean': 'No-Tutor Group Mean',
}

DATASETS = [
    {
        'slug': 'business',
        'name': 'Business: Daily Sales & Marketing Spend',
        'category': 'Business',
        'filename': 'business_sample_data.csv',
        'rows': 30,
        'description': 'Thirty days of synthetic sales data: marketing spend, units sold, revenue, and whether the day was a weekday or weekend. Built to practice correlation and regression.',
        'columns': ['day', 'day_type', 'marketing_spend', 'units_sold', 'revenue'],
    },
    {
        'slug': 'education',
        'name': 'Education: Study Habits & Exam Scores',
        'category': 'Education',
        'filename': 'education_sample_data.csv',
        'rows': 30,
        'description': 'Thirty synthetic students with prep hours, practice tests taken, tutor usage, and final exam score. Built to practice correlation, regression, and two-group comparisons.',
        'columns': ['student_id', 'prep_hours', 'practice_tests_taken', 'used_tutor', 'exam_score'],
    },
    {
        'slug': 'tax',
        'name': 'Tax: Income & Itemized Deductions (Synthetic)',
        'category': 'Tax',
        'filename': 'tax_sample_data.csv',
        'rows': 30,
        'description': 'Thirty fully synthetic filer records relating income bracket to itemized deductions and charitable contributions. Generated for statistics practice only — not real client data, and not tax advice.',
        'columns': ['filer_id', 'filing_year', 'income_bracket_midpoint', 'itemized_deductions', 'charitable_contributions'],
    },
]

CASE_STUDIES = [
    {
        'slug': 'marketing-spend-vs-revenue',
        'title': 'Does Marketing Spend Predict Revenue?',
        'category': 'Business',
        'dataset_slug': 'business',
        'technique': 'Linear Regression',
        'summary': 'A regression walkthrough on 30 days of sales data, showing how to go from raw numbers to a defensible answer.',
        'question': 'A retail client wants to know: if they increase daily marketing spend, can they predict how much extra revenue to expect?',
        'why_this_technique': 'We have one numeric predictor (marketing spend) and one numeric outcome (revenue), and we want to both measure the strength of the relationship and predict future values. That is exactly what linear regression is for — correlation alone would tell us the relationship is strong, but regression gives us an actual equation to plan around.',
        'steps': [
            'Loaded 30 days of marketing_spend and revenue values from the Business dataset.',
            'Ran the Regression Analysis tool with marketing_spend as X and revenue as Y.',
            'Read the resulting equation, R², and p-value to judge both the strength and reliability of the relationship.',
        ],
        'results': {
            'equation': 'y = 4.0509x + 3127.51',
            'r_squared': 0.9524,
            'p_value': 0.00000,
            'slope': 4.0509,
        },
        'interpretation': 'The R² of 0.95 means marketing spend explains about 95% of the variation in daily revenue in this dataset — an unusually strong relationship. The slope says every additional $1 in marketing spend is associated with about $4.05 more in revenue. The p-value is essentially zero, meaning this relationship is extremely unlikely to be due to chance.',
        'caveat': 'This is 30 days of synthetic practice data with no other variables competing for influence, which is why the relationship looks this clean. Real sales data is almost always noisier, with seasonality, competitor activity, and inventory constraints all pulling in different directions. Treat this as a demonstration of the method, not a promise about real-world marketing returns.',
    },
    {
        'slug': 'study-hours-vs-exam-scores',
        'title': 'Do Study Hours Improve Exam Scores — and Does a Tutor Help?',
        'category': 'Education',
        'dataset_slug': 'education',
        'technique': 'Correlation, Regression & Hypothesis Testing',
        'summary': 'Two questions, two different tools: one clear yes, and one honestly inconclusive result — which is itself the lesson.',
        'question': 'A school wants to know two things: does study time before an exam actually help, and does hiring a tutor make a measurable difference?',
        'why_this_technique': 'The first question — does more prep time relate to a higher score — is a numeric-to-numeric relationship, so correlation and regression fit. The second question — tutor vs. no tutor — compares two groups on one outcome, which is exactly what a hypothesis test (t-test) is built for.',
        'steps': [
            'Ran Correlation Analysis on prep_hours vs. exam_score across all 30 students.',
            'Ran Regression Analysis on the same two variables to get a predictive equation.',
            'Split students into "used a tutor" (12 students) and "no tutor" (18 students) groups and ran a two-group Hypothesis Test on their exam scores.',
        ],
        'results': {
            'correlation': 0.7939,
            'equation': 'y = 1.5479x + 63.80',
            'r_squared': 0.6303,
            'tutor_mean': 80.04,
            'no_tutor_mean': 76.03,
            't_statistic': 0.9525,
            'p_value': 0.34901,
        },
        'interpretation': 'Study hours show a strong, statistically meaningful relationship with exam scores (correlation 0.79, R² of 0.63) — each additional hour of prep is associated with roughly 1.55 more points. The tutor question tells a different story: tutored students averaged 80.0 versus 76.0 for non-tutored students, but the hypothesis test came back with p = 0.35, well above the usual 0.05 cutoff. That difference is not statistically distinguishable from random variation in this sample.',
        'caveat': 'This is the most important lesson in the whole case study: "no significant difference" does not mean tutoring definitely does not help. With only 12 tutored students, the test has low statistical power — a real, moderate effect could easily hide inside a sample this small. The honest conclusion is "we cannot confirm an effect with this much data," not "tutoring does not work." A larger sample would be needed to say more.',
    },
    {
        'slug': 'income-vs-deductions',
        'title': 'Does Income Predict Itemized Deductions?',
        'category': 'Tax',
        'dataset_slug': 'tax',
        'technique': 'Correlation & Regression',
        'summary': 'A correlation and regression walkthrough on fully synthetic filer data, built for practicing the method — not for drawing real tax conclusions.',
        'question': 'Using a synthetic set of filer records, is there a measurable relationship between income level and the size of itemized deductions claimed?',
        'why_this_technique': 'Both income and deduction amount are numeric, and we want to know both how strongly they move together and what the relationship looks like as a line, so correlation plus regression is the right pairing.',
        'steps': [
            'Ran Correlation Analysis on income_bracket_midpoint vs. itemized_deductions across 30 synthetic filer records.',
            'Ran Regression Analysis on the same two variables to get a predictive equation.',
        ],
        'results': {
            'correlation': 0.8923,
            'equation': 'y = 0.0921x + -325.91',
            'r_squared': 0.7962,
            'p_value': 0.00000,
        },
        'interpretation': 'The correlation of 0.89 and R² of 0.80 show a strong relationship in this synthetic dataset: higher income brackets are associated with larger itemized deductions, with each additional dollar of income associated with roughly 9.2 cents more in itemized deductions.',
        'caveat': 'This dataset was generated specifically to demonstrate the technique and is not derived from real filer data. It should not be used to draw conclusions about actual tax filing patterns, and nothing here constitutes tax advice. Real filing data involves far more variables — filing status, state, deduction type mix — than this simplified two-variable example.',
    },
]
