"""
Static content for the reference library: glossary terms, sample datasets,
and worked case studies. Kept as plain data (not DB models) since it's
authored content, not user-generated data.

Every entry carries both English and a '_fr' French counterpart. Use
localize_glossary()/localize_datasets()/localize_case_studies() to get a
flat, language-selected list that templates can render exactly as before.
"""

GLOSSARY = [
    {
        'term': 'Mean', 'term_fr': 'Moyenne',
        'category': 'Descriptive Statistics', 'category_fr': 'Statistiques descriptives',
        'definition': 'The arithmetic average of a set of values: add them all up, divide by how many there are. Sensitive to extreme values (outliers) pulling it away from the "typical" value.',
        'definition_fr': 'La moyenne arithmétique d\'un ensemble de valeurs : on les additionne toutes, puis on divise par leur nombre. Sensible aux valeurs extrêmes (aberrantes) qui l\'éloignent de la valeur « typique ».',
        'related_tool': 'descriptive',
    },
    {
        'term': 'Median', 'term_fr': 'Médiane',
        'category': 'Descriptive Statistics', 'category_fr': 'Statistiques descriptives',
        'definition': 'The middle value when data is sorted from smallest to largest. Unlike the mean, it is not distorted by outliers, which makes it a better summary for skewed data like income or home prices.',
        'definition_fr': 'La valeur du milieu lorsque les données sont triées du plus petit au plus grand. Contrairement à la moyenne, elle n\'est pas faussée par les valeurs aberrantes, ce qui en fait un meilleur résumé pour des données asymétriques comme le revenu ou le prix des maisons.',
        'related_tool': 'descriptive',
    },
    {
        'term': 'Mode', 'term_fr': 'Mode',
        'category': 'Descriptive Statistics', 'category_fr': 'Statistiques descriptives',
        'definition': 'The most frequently occurring value in a dataset. A dataset can have no mode, one mode, or several (bimodal, multimodal).',
        'definition_fr': 'La valeur qui revient le plus souvent dans un jeu de données. Un jeu de données peut n\'avoir aucun mode, un seul, ou plusieurs (bimodal, multimodal).',
        'related_tool': 'descriptive',
    },
    {
        'term': 'Standard Deviation', 'term_fr': 'Écart type',
        'category': 'Descriptive Statistics', 'category_fr': 'Statistiques descriptives',
        'definition': 'A measure of how spread out values are around the mean. A small standard deviation means values cluster tightly around the mean; a large one means they are spread widely.',
        'definition_fr': 'Une mesure de la dispersion des valeurs autour de la moyenne. Un écart type faible signifie que les valeurs sont regroupées près de la moyenne ; un écart type élevé signifie qu\'elles sont très dispersées.',
        'related_tool': 'descriptive',
    },
    {
        'term': 'Variance', 'term_fr': 'Variance',
        'category': 'Descriptive Statistics', 'category_fr': 'Statistiques descriptives',
        'definition': 'The standard deviation squared. Useful mathematically (it adds cleanly across independent variables) but harder to interpret directly since it is in squared units.',
        'definition_fr': 'L\'écart type au carré. Utile mathématiquement (elle s\'additionne proprement entre variables indépendantes) mais plus difficile à interpréter directement puisqu\'elle est exprimée en unités au carré.',
        'related_tool': 'descriptive',
    },
    {
        'term': 'Quartile', 'term_fr': 'Quartile',
        'category': 'Descriptive Statistics', 'category_fr': 'Statistiques descriptives',
        'definition': 'One of three values (Q1, Q2/median, Q3) that split sorted data into four equal groups. Q1 is the value below which 25% of the data falls; Q3 is the value below which 75% falls.',
        'definition_fr': 'L\'une des trois valeurs (Q1, Q2/médiane, Q3) qui divisent des données triées en quatre groupes égaux. Q1 est la valeur en dessous de laquelle se trouvent 25 % des données ; Q3, celle en dessous de laquelle se trouvent 75 % des données.',
        'related_tool': 'descriptive',
    },
    {
        'term': 'Outlier', 'term_fr': 'Valeur aberrante',
        'category': 'Descriptive Statistics', 'category_fr': 'Statistiques descriptives',
        'definition': 'A data point that falls far outside the pattern of the rest of the dataset. Outliers can be genuine (a real extreme case) or errors (a typo in data entry) — the two require very different responses.',
        'definition_fr': 'Une donnée qui s\'écarte fortement du reste du jeu de données. Une valeur aberrante peut être authentique (un cas extrême réel) ou une erreur (une faute de saisie) — les deux appellent des réponses très différentes.',
        'related_tool': 'descriptive',
    },
    {
        'term': 'Population vs. Sample', 'term_fr': 'Population et échantillon',
        'category': 'Study Design', 'category_fr': 'Conception d\'étude',
        'definition': 'A population is every member of the group you care about. A sample is the subset you actually collected data from. Statistics uses samples to make informed guesses about populations, because measuring an entire population is usually impossible.',
        'definition_fr': 'Une population regroupe tous les membres du groupe qui vous intéresse. Un échantillon est le sous-ensemble sur lequel vous avez réellement recueilli des données. La statistique utilise des échantillons pour formuler des estimations éclairées sur les populations, car mesurer une population entière est généralement impossible.',
        'related_tool': None,
    },
    {
        'term': 'Sampling Bias', 'term_fr': 'Biais d\'échantillonnage',
        'category': 'Study Design', 'category_fr': 'Conception d\'étude',
        'definition': 'A systematic error introduced when your sample does not represent the population, because of how it was collected. A survey of only your existing customers cannot tell you why people who never bought from you stayed away.',
        'definition_fr': 'Une erreur systématique introduite lorsque votre échantillon ne représente pas la population, à cause de la façon dont il a été constitué. Un sondage mené uniquement auprès de vos clients existants ne peut pas vous dire pourquoi les gens qui n\'ont jamais acheté chez vous s\'en sont tenus à l\'écart.',
        'related_tool': None,
    },
    {
        'term': 'Probability Distribution', 'term_fr': 'Distribution de probabilité',
        'category': 'Probability', 'category_fr': 'Probabilité',
        'definition': 'A description of how likely each possible outcome of a random variable is. The normal (bell-curve) distribution is the most common one used in statistics.',
        'definition_fr': 'Une description de la probabilité de chaque résultat possible d\'une variable aléatoire. La distribution normale (en forme de cloche) est la plus utilisée en statistique.',
        'related_tool': None,
    },
    {
        'term': 'Normal Distribution', 'term_fr': 'Distribution normale',
        'category': 'Probability', 'category_fr': 'Probabilité',
        'definition': 'A symmetric, bell-shaped distribution where most values cluster near the mean. Many statistical tests assume the data is roughly normally distributed.',
        'definition_fr': 'Une distribution symétrique en forme de cloche où la plupart des valeurs se regroupent près de la moyenne. De nombreux tests statistiques supposent que les données suivent approximativement une distribution normale.',
        'related_tool': None,
    },
    {
        'term': 'Correlation', 'term_fr': 'Corrélation',
        'category': 'Relationships Between Variables', 'category_fr': 'Relations entre variables',
        'definition': 'A measure, from -1 to 1, of how strongly two variables move together in a straight-line pattern. Positive means they rise together; negative means one rises as the other falls. A correlation near 0 means little to no linear relationship.',
        'definition_fr': 'Une mesure, de -1 à 1, de la force avec laquelle deux variables évoluent ensemble selon une tendance linéaire. Positive signifie qu\'elles augmentent ensemble ; négative signifie que l\'une augmente quand l\'autre diminue. Une corrélation proche de 0 indique peu ou pas de relation linéaire.',
        'related_tool': 'correlation',
    },
    {
        'term': 'Correlation vs. Causation', 'term_fr': 'Corrélation et causalité',
        'category': 'Relationships Between Variables', 'category_fr': 'Relations entre variables',
        'definition': 'Two variables being correlated does not mean one causes the other. Ice cream sales and drowning deaths both rise in summer — heat causes both, neither causes the other.',
        'definition_fr': 'Deux variables corrélées ne signifient pas que l\'une cause l\'autre. Les ventes de crème glacée et les noyades augmentent toutes deux l\'été — la chaleur cause les deux, ni l\'une ni l\'autre ne se causent mutuellement.',
        'related_tool': 'correlation',
    },
    {
        'term': 'P-value', 'term_fr': 'Valeur p',
        'category': 'Hypothesis Testing', 'category_fr': 'Tests d\'hypothèses',
        'definition': 'The probability of seeing a result at least as extreme as yours, if there were actually no real effect. A small p-value (conventionally under 0.05) suggests the result is unlikely to be due to chance alone.',
        'definition_fr': 'La probabilité d\'observer un résultat au moins aussi extrême que le vôtre, s\'il n\'y avait en réalité aucun effet réel. Une petite valeur p (généralement inférieure à 0,05) suggère que le résultat est peu susceptible d\'être dû au seul hasard.',
        'related_tool': 'ttest',
    },
    {
        'term': 'Statistical Significance', 'term_fr': 'Signification statistique',
        'category': 'Hypothesis Testing', 'category_fr': 'Tests d\'hypothèses',
        'definition': 'A result is "statistically significant" when the p-value falls below a chosen threshold (usually 0.05). It means the result is unlikely to be random noise — it does not automatically mean the effect is large or important.',
        'definition_fr': 'Un résultat est « statistiquement significatif » lorsque la valeur p tombe sous un seuil choisi (généralement 0,05). Cela signifie que le résultat est peu susceptible d\'être du bruit aléatoire — cela ne signifie pas automatiquement que l\'effet est important ou considérable.',
        'related_tool': 'ttest',
    },
    {
        'term': 'Null Hypothesis', 'term_fr': 'Hypothèse nulle',
        'category': 'Hypothesis Testing', 'category_fr': 'Tests d\'hypothèses',
        'definition': 'The default assumption that there is no real effect or difference. A hypothesis test looks for enough evidence in the data to reject this assumption in favor of a real effect.',
        'definition_fr': 'L\'hypothèse par défaut selon laquelle il n\'existe aucun effet ou différence réel. Un test d\'hypothèse cherche suffisamment de preuves dans les données pour rejeter cette hypothèse en faveur d\'un effet réel.',
        'related_tool': 'ttest',
    },
    {
        'term': 'T-test', 'term_fr': 'Test t',
        'category': 'Hypothesis Testing', 'category_fr': 'Tests d\'hypothèses',
        'definition': 'A statistical test that compares the means of two groups to see if the difference between them is likely to be real, or just due to random variation in the sample.',
        'definition_fr': 'Un test statistique qui compare les moyennes de deux groupes pour voir si leur différence est probablement réelle, ou simplement due à une variation aléatoire dans l\'échantillon.',
        'related_tool': 'ttest',
    },
    {
        'term': 'Confidence Interval', 'term_fr': 'Intervalle de confiance',
        'category': 'Hypothesis Testing', 'category_fr': 'Tests d\'hypothèses',
        'definition': 'A range of values, calculated from your sample, that likely contains the true population value. A "95% confidence interval" means if you repeated the sampling many times, 95% of the intervals calculated would contain the true value.',
        'definition_fr': 'Une plage de valeurs, calculée à partir de votre échantillon, qui contient probablement la vraie valeur de la population. Un « intervalle de confiance à 95 % » signifie que si vous répétiez l\'échantillonnage de nombreuses fois, 95 % des intervalles calculés contiendraient la vraie valeur.',
        'related_tool': None,
    },
    {
        'term': 'Sample Size', 'term_fr': 'Taille de l\'échantillon',
        'category': 'Study Design', 'category_fr': 'Conception d\'étude',
        'definition': 'The number of observations in your data. Small samples produce noisy, unreliable estimates and can fail to detect a real effect (low statistical power) even when one exists.',
        'definition_fr': 'Le nombre d\'observations dans vos données. Les petits échantillons produisent des estimations bruitées et peu fiables, et peuvent échouer à détecter un effet réel (faible puissance statistique) même lorsqu\'il en existe un.',
        'related_tool': None,
    },
    {
        'term': 'Linear Regression', 'term_fr': 'Régression linéaire',
        'category': 'Relationships Between Variables', 'category_fr': 'Relations entre variables',
        'definition': 'A technique that fits a straight line through your data to predict one variable from another. The slope tells you how much the outcome changes per unit of the predictor.',
        'definition_fr': 'Une technique qui ajuste une droite à travers vos données pour prédire une variable à partir d\'une autre. La pente indique de combien le résultat change par unité du prédicteur.',
        'related_tool': 'regression',
    },
    {
        'term': 'R-squared (R²)', 'term_fr': 'Coefficient de détermination (R²)',
        'category': 'Relationships Between Variables', 'category_fr': 'Relations entre variables',
        'definition': 'The proportion of variation in the outcome that is explained by the regression line, from 0 to 1. An R² of 0.80 means 80% of the variation in the outcome is explained by the predictor; the rest is other factors or noise.',
        'definition_fr': 'La proportion de la variation du résultat expliquée par la droite de régression, de 0 à 1. Un R² de 0,80 signifie que 80 % de la variation du résultat est expliquée par le prédicteur ; le reste provient d\'autres facteurs ou du bruit.',
        'related_tool': 'regression',
    },
    {
        'term': 'ETL (Extract, Transform, Load)', 'term_fr': 'ETL (extraction, transformation, chargement)',
        'category': 'Data Processing', 'category_fr': 'Traitement des données',
        'definition': 'The standard workflow for preparing raw data for analysis: pull it from its source, clean and reshape it, then load it somewhere ready for analysis.',
        'definition_fr': 'Le flux de travail standard pour préparer des données brutes en vue d\'une analyse : les extraire de leur source, les nettoyer et les remodeler, puis les charger quelque part, prêtes pour l\'analyse.',
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
TOOL_LABELS_FR = {
    'descriptive': 'Statistiques descriptives',
    'correlation': 'Analyse de corrélation',
    'ttest': 'Test d\'hypothèse',
    'regression': 'Analyse de régression',
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
RESULT_LABELS_FR = {
    'equation': 'Équation',
    'r_squared': 'R²',
    'p_value': 'Valeur p',
    'slope': 'Pente',
    'correlation': 'Corrélation (r)',
    't_statistic': 'Statistique t',
    'tutor_mean': 'Moyenne (avec tuteur)',
    'no_tutor_mean': 'Moyenne (sans tuteur)',
}

DATASETS = [
    {
        'slug': 'business',
        'name': 'Business: Daily Sales & Marketing Spend',
        'name_fr': 'Commerce : ventes quotidiennes et dépenses marketing',
        'category': 'Business', 'category_fr': 'Commerce',
        'filename': 'business_sample_data.csv',
        'rows': 30,
        'description': 'Thirty days of synthetic sales data: marketing spend, units sold, revenue, and whether the day was a weekday or weekend. Built to practice correlation and regression.',
        'description_fr': 'Trente jours de données de ventes synthétiques : dépenses marketing, unités vendues, revenus, et si le jour était un jour de semaine ou de fin de semaine. Conçu pour pratiquer la corrélation et la régression.',
        'columns': ['day', 'day_type', 'marketing_spend', 'units_sold', 'revenue'],
    },
    {
        'slug': 'education',
        'name': 'Education: Study Habits & Exam Scores',
        'name_fr': 'Éducation : habitudes d\'étude et résultats d\'examen',
        'category': 'Education', 'category_fr': 'Éducation',
        'filename': 'education_sample_data.csv',
        'rows': 30,
        'description': 'Thirty synthetic students with prep hours, practice tests taken, tutor usage, and final exam score. Built to practice correlation, regression, and two-group comparisons.',
        'description_fr': 'Trente élèves synthétiques avec heures de préparation, tests pratiques effectués, recours à un tuteur, et résultat final à l\'examen. Conçu pour pratiquer la corrélation, la régression et les comparaisons entre deux groupes.',
        'columns': ['student_id', 'prep_hours', 'practice_tests_taken', 'used_tutor', 'exam_score'],
    },
    {
        'slug': 'tax',
        'name': 'Tax: Income & Itemized Deductions (Synthetic)',
        'name_fr': 'Fiscalité : revenu et déductions détaillées (synthétique)',
        'category': 'Tax', 'category_fr': 'Fiscalité',
        'filename': 'tax_sample_data.csv',
        'rows': 30,
        'description': 'Thirty fully synthetic filer records relating income bracket to itemized deductions and charitable contributions. Generated for statistics practice only — not real client data, and not tax advice.',
        'description_fr': 'Trente dossiers de déclarants entièrement synthétiques reliant la tranche de revenu aux déductions détaillées et aux dons de bienfaisance. Générés uniquement pour la pratique statistique — ce ne sont pas de vraies données clients, et ceci ne constitue pas un conseil fiscal.',
        'columns': ['filer_id', 'filing_year', 'income_bracket_midpoint', 'itemized_deductions', 'charitable_contributions'],
    },
]

CASE_STUDIES = [
    {
        'slug': 'marketing-spend-vs-revenue',
        'title': 'Does Marketing Spend Predict Revenue?',
        'title_fr': 'Les dépenses marketing prédisent-elles les revenus ?',
        'category': 'Business', 'category_fr': 'Commerce',
        'dataset_slug': 'business',
        'technique': 'Linear Regression', 'technique_fr': 'Régression linéaire',
        'summary': 'A regression walkthrough on 30 days of sales data, showing how to go from raw numbers to a defensible answer.',
        'summary_fr': 'Une démonstration de régression sur 30 jours de données de vente, montrant comment passer de chiffres bruts à une réponse défendable.',
        'question': 'A retail client wants to know: if they increase daily marketing spend, can they predict how much extra revenue to expect?',
        'question_fr': 'Un client du commerce de détail veut savoir : s\'il augmente ses dépenses marketing quotidiennes, peut-il prédire le revenu supplémentaire à attendre ?',
        'why_this_technique': 'We have one numeric predictor (marketing spend) and one numeric outcome (revenue), and we want to both measure the strength of the relationship and predict future values. That is exactly what linear regression is for — correlation alone would tell us the relationship is strong, but regression gives us an actual equation to plan around.',
        'why_this_technique_fr': 'Nous avons un prédicteur numérique (les dépenses marketing) et un résultat numérique (le revenu), et nous voulons à la fois mesurer la force de la relation et prédire des valeurs futures. C\'est exactement à cela que sert la régression linéaire — la corrélation seule nous dirait que la relation est forte, mais la régression nous donne une véritable équation pour planifier.',
        'steps': [
            'Loaded 30 days of marketing_spend and revenue values from the Business dataset.',
            'Ran the Regression Analysis tool with marketing_spend as X and revenue as Y.',
            'Read the resulting equation, R², and p-value to judge both the strength and reliability of the relationship.',
        ],
        'steps_fr': [
            'Chargement de 30 jours de valeurs marketing_spend et revenue depuis le jeu de données Commerce.',
            'Exécution de l\'outil d\'analyse de régression avec marketing_spend comme X et revenue comme Y.',
            'Lecture de l\'équation résultante, du R² et de la valeur p pour juger à la fois la force et la fiabilité de la relation.',
        ],
        'results': {
            'equation': 'y = 4.0509x + 3127.51',
            'r_squared': 0.9524,
            'p_value': 0.00000,
            'slope': 4.0509,
        },
        'interpretation': 'The R² of 0.95 means marketing spend explains about 95% of the variation in daily revenue in this dataset — an unusually strong relationship. The slope says every additional $1 in marketing spend is associated with about $4.05 more in revenue. The p-value is essentially zero, meaning this relationship is extremely unlikely to be due to chance.',
        'interpretation_fr': 'Le R² de 0,95 signifie que les dépenses marketing expliquent environ 95 % de la variation du revenu quotidien dans ce jeu de données — une relation inhabituellement forte. La pente indique que chaque dollar supplémentaire de dépenses marketing est associé à environ 4,05 $ de revenu en plus. La valeur p est essentiellement nulle, ce qui signifie que cette relation est extrêmement peu susceptible d\'être due au hasard.',
        'caveat': 'This is 30 days of synthetic practice data with no other variables competing for influence, which is why the relationship looks this clean. Real sales data is almost always noisier, with seasonality, competitor activity, and inventory constraints all pulling in different directions. Treat this as a demonstration of the method, not a promise about real-world marketing returns.',
        'caveat_fr': 'Il s\'agit de 30 jours de données synthétiques de pratique, sans autre variable venant concurrencer l\'influence, ce qui explique pourquoi la relation paraît aussi nette. Les vraies données de vente sont presque toujours plus bruitées, avec la saisonnalité, l\'activité des concurrents et les contraintes d\'inventaire qui tirent chacune dans des directions différentes. Considérez ceci comme une démonstration de la méthode, non comme une promesse de rendement marketing réel.',
    },
    {
        'slug': 'study-hours-vs-exam-scores',
        'title': 'Do Study Hours Improve Exam Scores — and Does a Tutor Help?',
        'title_fr': 'Les heures d\'étude améliorent-elles les résultats d\'examen — et un tuteur aide-t-il ?',
        'category': 'Education', 'category_fr': 'Éducation',
        'dataset_slug': 'education',
        'technique': 'Correlation, Regression & Hypothesis Testing', 'technique_fr': 'Corrélation, régression et test d\'hypothèse',
        'summary': 'Two questions, two different tools: one clear yes, and one honestly inconclusive result — which is itself the lesson.',
        'summary_fr': 'Deux questions, deux outils différents : une réponse claire, et un résultat honnêtement non concluant — ce qui constitue la leçon en soi.',
        'question': 'A school wants to know two things: does study time before an exam actually help, and does hiring a tutor make a measurable difference?',
        'question_fr': 'Une école veut savoir deux choses : le temps d\'étude avant un examen aide-t-il réellement, et engager un tuteur fait-il une différence mesurable ?',
        'why_this_technique': 'The first question — does more prep time relate to a higher score — is a numeric-to-numeric relationship, so correlation and regression fit. The second question — tutor vs. no tutor — compares two groups on one outcome, which is exactly what a hypothesis test (t-test) is built for.',
        'why_this_technique_fr': 'La première question — plus de temps de préparation est-il lié à un meilleur résultat — est une relation numérique-numérique, la corrélation et la régression conviennent donc. La seconde question — avec ou sans tuteur — compare deux groupes sur un seul résultat, exactement ce pour quoi un test d\'hypothèse (test t) est conçu.',
        'steps': [
            'Ran Correlation Analysis on prep_hours vs. exam_score across all 30 students.',
            'Ran Regression Analysis on the same two variables to get a predictive equation.',
            'Split students into "used a tutor" (12 students) and "no tutor" (18 students) groups and ran a two-group Hypothesis Test on their exam scores.',
        ],
        'steps_fr': [
            'Exécution de l\'analyse de corrélation sur prep_hours et exam_score pour les 30 élèves.',
            'Exécution de l\'analyse de régression sur les deux mêmes variables pour obtenir une équation prédictive.',
            'Répartition des élèves en groupes « avec tuteur » (12 élèves) et « sans tuteur » (18 élèves), puis test d\'hypothèse à deux groupes sur leurs résultats d\'examen.',
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
        'interpretation_fr': 'Les heures d\'étude montrent une relation forte et statistiquement significative avec les résultats d\'examen (corrélation de 0,79, R² de 0,63) — chaque heure de préparation supplémentaire est associée à environ 1,55 point de plus. La question du tuteur raconte une autre histoire : les élèves avec tuteur ont obtenu en moyenne 80,0 contre 76,0 pour ceux sans tuteur, mais le test d\'hypothèse a donné p = 0,35, bien au-dessus du seuil habituel de 0,05. Cette différence n\'est pas statistiquement distinguable d\'une variation aléatoire dans cet échantillon.',
        'caveat': 'This is the most important lesson in the whole case study: "no significant difference" does not mean tutoring definitely does not help. With only 12 tutored students, the test has low statistical power — a real, moderate effect could easily hide inside a sample this small. The honest conclusion is "we cannot confirm an effect with this much data," not "tutoring does not work." A larger sample would be needed to say more.',
        'caveat_fr': 'C\'est la leçon la plus importante de toute cette étude de cas : « aucune différence significative » ne signifie pas que le tutorat n\'aide certainement pas. Avec seulement 12 élèves tutorés, le test a une faible puissance statistique — un effet réel et modéré pourrait facilement se cacher dans un échantillon aussi petit. La conclusion honnête est « nous ne pouvons pas confirmer d\'effet avec cette quantité de données », et non « le tutorat ne fonctionne pas ». Un échantillon plus large serait nécessaire pour en dire plus.',
    },
    {
        'slug': 'income-vs-deductions',
        'title': 'Does Income Predict Itemized Deductions?',
        'title_fr': 'Le revenu prédit-il les déductions détaillées ?',
        'category': 'Tax', 'category_fr': 'Fiscalité',
        'dataset_slug': 'tax',
        'technique': 'Correlation & Regression', 'technique_fr': 'Corrélation et régression',
        'summary': 'A correlation and regression walkthrough on fully synthetic filer data, built for practicing the method — not for drawing real tax conclusions.',
        'summary_fr': 'Une démonstration de corrélation et de régression sur des données de déclarants entièrement synthétiques, conçue pour pratiquer la méthode — non pour tirer de vraies conclusions fiscales.',
        'question': 'Using a synthetic set of filer records, is there a measurable relationship between income level and the size of itemized deductions claimed?',
        'question_fr': 'À partir d\'un ensemble synthétique de dossiers de déclarants, existe-t-il une relation mesurable entre le niveau de revenu et le montant des déductions détaillées réclamées ?',
        'why_this_technique': 'Both income and deduction amount are numeric, and we want to know both how strongly they move together and what the relationship looks like as a line, so correlation plus regression is the right pairing.',
        'why_this_technique_fr': 'Le revenu et le montant des déductions sont tous deux numériques, et nous voulons savoir à la fois à quel point ils évoluent ensemble et à quoi ressemble la relation sous forme de droite ; la corrélation combinée à la régression est donc le bon choix.',
        'steps': [
            'Ran Correlation Analysis on income_bracket_midpoint vs. itemized_deductions across 30 synthetic filer records.',
            'Ran Regression Analysis on the same two variables to get a predictive equation.',
        ],
        'steps_fr': [
            'Exécution de l\'analyse de corrélation sur income_bracket_midpoint et itemized_deductions pour 30 dossiers de déclarants synthétiques.',
            'Exécution de l\'analyse de régression sur les deux mêmes variables pour obtenir une équation prédictive.',
        ],
        'results': {
            'correlation': 0.8923,
            'equation': 'y = 0.0921x + -325.91',
            'r_squared': 0.7962,
            'p_value': 0.00000,
        },
        'interpretation': 'The correlation of 0.89 and R² of 0.80 show a strong relationship in this synthetic dataset: higher income brackets are associated with larger itemized deductions, with each additional dollar of income associated with roughly 9.2 cents more in itemized deductions.',
        'interpretation_fr': 'La corrélation de 0,89 et le R² de 0,80 montrent une relation forte dans ce jeu de données synthétique : les tranches de revenu plus élevées sont associées à des déductions détaillées plus importantes, chaque dollar de revenu supplémentaire étant associé à environ 9,2 cents de déductions détaillées en plus.',
        'caveat': 'This dataset was generated specifically to demonstrate the technique and is not derived from real filer data. It should not be used to draw conclusions about actual tax filing patterns, and nothing here constitutes tax advice. Real filing data involves far more variables — filing status, state, deduction type mix — than this simplified two-variable example.',
        'caveat_fr': 'Ce jeu de données a été généré spécifiquement pour démontrer la technique et n\'est pas issu de données réelles de déclarants. Il ne doit pas être utilisé pour tirer des conclusions sur de véritables tendances de déclaration fiscale, et rien ici ne constitue un conseil fiscal. Les données de déclaration réelles impliquent bien plus de variables — statut de déclaration, état, répartition des types de déductions — que cet exemple simplifié à deux variables.',
    },
]


def localize_glossary(lang='en'):
    """Return the glossary with term/category/definition selected for the given language."""
    if lang == 'fr':
        return [
            {**t, 'term': t['term_fr'], 'category': t['category_fr'], 'definition': t['definition_fr']}
            for t in GLOSSARY
        ]
    return GLOSSARY


def localize_datasets(lang='en'):
    if lang == 'fr':
        return [
            {**d, 'name': d['name_fr'], 'category': d['category_fr'], 'description': d['description_fr']}
            for d in DATASETS
        ]
    return DATASETS


def localize_case_studies(lang='en'):
    if lang == 'fr':
        return [
            {
                **c,
                'title': c['title_fr'], 'category': c['category_fr'], 'technique': c['technique_fr'],
                'summary': c['summary_fr'], 'question': c['question_fr'],
                'why_this_technique': c['why_this_technique_fr'], 'steps': c['steps_fr'],
                'interpretation': c['interpretation_fr'], 'caveat': c['caveat_fr'],
            }
            for c in CASE_STUDIES
        ]
    return CASE_STUDIES
