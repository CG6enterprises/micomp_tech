"""
One-time generator for synthetic sample datasets used by the Datasets page
and the Case Studies. Deterministic (fixed seed) so results are reproducible.

Run with: venv/Scripts/python.exe backend/generate_datasets.py
"""
import csv
import os

import numpy as np
from scipy.stats import linregress, pearsonr, ttest_ind

rng = np.random.default_rng(42)

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
os.makedirs(DATA_DIR, exist_ok=True)


# ---- Business: marketing spend vs revenue, weekday vs weekend ----
n = 30
marketing_spend = rng.uniform(200, 2000, n).round(2)
revenue = (marketing_spend * 4.1 + rng.normal(0, 600, n) + 3000).round(2)
day_type = rng.choice(['Weekday', 'Weekend'], n, p=[5 / 7, 2 / 7])
units_sold = (revenue / rng.uniform(18, 24, n)).round().astype(int)

with open(os.path.join(DATA_DIR, 'business_sample_data.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['day', 'day_type', 'marketing_spend', 'units_sold', 'revenue'])
    for i in range(n):
        w.writerow([i + 1, day_type[i], marketing_spend[i], units_sold[i], revenue[i]])

corr, p = pearsonr(marketing_spend, revenue)
reg = linregress(marketing_spend, revenue)
weekday_rev = revenue[day_type == 'Weekday']
weekend_rev = revenue[day_type == 'Weekend']
t_stat, t_p = ttest_ind(weekend_rev, weekday_rev)

print("=== BUSINESS ===")
print(f"correlation(marketing_spend, revenue) = {corr:.4f}, p = {p:.5f}")
print(f"regression: slope={reg.slope:.4f} intercept={reg.intercept:.2f} r2={reg.rvalue**2:.4f} p={reg.pvalue:.5f}")
print(f"weekday n={len(weekday_rev)} mean={weekday_rev.mean():.2f} | weekend n={len(weekend_rev)} mean={weekend_rev.mean():.2f}")
print(f"ttest weekend vs weekday: t={t_stat:.4f} p={t_p:.5f}")


# ---- Education: prep hours vs exam score, tutor vs no tutor ----
n = 30
prep_hours = rng.uniform(0, 20, n).round(1)
used_tutor = rng.choice(['Yes', 'No'], n, p=[0.4, 0.6])
tutor_bonus = np.where(used_tutor == 'Yes', 6, 0)
exam_score = np.clip(58 + prep_hours * 1.9 + tutor_bonus + rng.normal(0, 6, n), 0, 100).round(1)
practice_tests = rng.integers(0, 6, n)

with open(os.path.join(DATA_DIR, 'education_sample_data.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['student_id', 'prep_hours', 'practice_tests_taken', 'used_tutor', 'exam_score'])
    for i in range(n):
        w.writerow([i + 1, prep_hours[i], practice_tests[i], used_tutor[i], exam_score[i]])

corr2, p2 = pearsonr(prep_hours, exam_score)
reg2 = linregress(prep_hours, exam_score)
tutor_scores = exam_score[used_tutor == 'Yes']
no_tutor_scores = exam_score[used_tutor == 'No']
t_stat2, t_p2 = ttest_ind(tutor_scores, no_tutor_scores)

print("\n=== EDUCATION ===")
print(f"correlation(prep_hours, exam_score) = {corr2:.4f}, p = {p2:.5f}")
print(f"regression: slope={reg2.slope:.4f} intercept={reg2.intercept:.2f} r2={reg2.rvalue**2:.4f} p={reg2.pvalue:.5f}")
print(f"tutor n={len(tutor_scores)} mean={tutor_scores.mean():.2f} | no-tutor n={len(no_tutor_scores)} mean={no_tutor_scores.mean():.2f}")
print(f"ttest tutor vs no-tutor: t={t_stat2:.4f} p={t_p2:.5f}")


# ---- Tax (synthetic, generic - NOT real client data): income bracket vs itemized deductions ----
n = 30
income_bracket_midpoint = rng.choice([35000, 55000, 75000, 95000, 125000, 165000, 220000], n)
itemized_deductions = np.clip(income_bracket_midpoint * 0.09 + rng.normal(0, 2500, n), 500, None).round(2)
charitable_contributions = np.clip(income_bracket_midpoint * 0.015 + rng.normal(0, 400, n), 0, None).round(2)
filing_year = rng.choice([2024, 2025], n)

with open(os.path.join(DATA_DIR, 'tax_sample_data.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['filer_id', 'filing_year', 'income_bracket_midpoint', 'itemized_deductions', 'charitable_contributions'])
    for i in range(n):
        w.writerow([i + 1, filing_year[i], income_bracket_midpoint[i], itemized_deductions[i], charitable_contributions[i]])

corr3, p3 = pearsonr(income_bracket_midpoint, itemized_deductions)
reg3 = linregress(income_bracket_midpoint, itemized_deductions)

print("\n=== TAX (synthetic) ===")
print(f"correlation(income_bracket_midpoint, itemized_deductions) = {corr3:.4f}, p = {p3:.5f}")
print(f"regression: slope={reg3.slope:.6f} intercept={reg3.intercept:.2f} r2={reg3.rvalue**2:.4f} p={reg3.pvalue:.5f}")

print("\nDatasets written to:", DATA_DIR)
