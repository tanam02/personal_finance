import pandas as pd

# Constants
base_score = 80  # Base score to start with
necessary_weight = 0.15
good_to_have_weight = 0.35
unnecessary_weight = 0.5

# Monthly budget constants (for the 10th day)
monthly_income = 210000
rent = 95000
allocated_for_expenses = 0.80  # 80% of income allocated for expenses

# Calculate the remaining budget after rent
# monthly_expense_budget = (monthly_income * allocated_for_expenses) - rent
monthly_expense_budget = 73000

# Calculate daily budgets for each category
necessary_daily_budget = (monthly_expense_budget * 0.85) / 30
good_to_have_daily_budget = (monthly_expense_budget * 0.10) / 30
unnecessary_daily_budget = (monthly_expense_budget * 0.05) / 30

# Read CSV with multiple scenarios
df = pd.read_csv('scenarios.csv')

# Add daily budget columns to the DataFrame for comparison
df['Necessary Daily Budget'] = necessary_daily_budget * 10  # 10 days budget for Necessary
df['Good to Have Daily Budget'] = good_to_have_daily_budget * 10  # 10 days budget for Good to Have
df['Unnecessary Daily Budget'] = unnecessary_daily_budget * 10  # 10 days budget for Unnecessary

# Calculate the overspending or underspending for each category (difference for the 10th day)
df['Necessary Difference'] = df['Necessary Spending'] - df['Necessary Daily Budget']
df['Good to Have Difference'] = df['Good to Have Spending'] - df['Good to Have Daily Budget']
df['Unnecessary Difference'] = df['Unnecessary Spending'] - df['Unnecessary Daily Budget']

# Apply weight to the difference (penalties or rewards)
df['Necessary Adjustment'] = df['Necessary Difference'] * necessary_weight
df['Good to Have Adjustment'] = df['Good to Have Difference'] * good_to_have_weight
df['Unnecessary Adjustment'] = df['Unnecessary Difference'] * unnecessary_weight

# Calculate the total adjustment for each scenario by summing the adjustments
df['Total Adjustment'] = df['Necessary Adjustment'] + df['Good to Have Adjustment'] + df['Unnecessary Adjustment']

# Calculate the final score for each scenario
df['Final Score'] = base_score - df['Total Adjustment']/50  # The /50 helps to scale the adjustment to a reasonable range

# Output the full DataFrame with adjustments and final scores
print("Expense Summary for Each Scenario:")
print(df[['Scenario', 'Necessary Spending', 'Good to Have Spending', 'Unnecessary Spending', 'Necessary Daily Budget', 
          'Good to Have Daily Budget', 'Unnecessary Daily Budget', 'Necessary Difference', 'Good to Have Difference',
          'Unnecessary Difference', 'Necessary Adjustment', 'Good to Have Adjustment', 'Unnecessary Adjustment', 
          'Total Adjustment', 'Final Score']])

# Output the final scores per scenario
print("\nFinal Scores for Each Scenario:")
final_scores = df[['Scenario', 'Final Score']]
print(final_scores)
