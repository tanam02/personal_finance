# Personal Finance Health Metric

## Idea:
- **Goal**: Create a personal finance health metric to quickly assess one's financial situation and evaluate the impact of a purchase or expense on overall financial health. This would allow users to make data-driven decisions.
- **Key Focus**: The metric is the most important feature. While other elements like asset trends and category analysis can be done using tools like Daak, the core feature is the financial score.
- **Data Requirements**: Metrics from tools like Daak are necessary for calculating the score. Consider omitting category and sub-category details in favor of focusing only on daily expense types (e.g., Necessary, Good to Have, Unnecessary).

## Planning:
### Budget and Expense Ratios:
- The financial score will reflect how well the user is managing their budget by tracking the ratio of expenses to budget.
- **Budget Types**: Define three types of expenses:
  - Necessary (85% of monthly income)
  - Good to Have (10% of monthly income)
  - Unnecessary (5% of monthly income)
- Budgets will be divided into daily amounts for tracking.

### Grading System:
- The grading system evaluates how well the user is spending compared to the budget.
- **Budget Calculation**:
  - 80% of income is allocated for expenses (the remaining 20% goes to savings).
  - **Note**: It may be necessary to reconsider the budget calculation methodology by using the minimum monthly expenditure instead of total income, as this approach would help mitigate lifestyle inflation and promote more consistent spending habits.
  - **Penalties for Overspending**: There will be penalties for overspending, particularly on Unnecessary expenses.
  - **Rewards for Savings**: Incentives will be provided for good saving habits.

### Weight Distribution:
- **Penalty/Reward Weights**:
  - Unnecessary expenses: Weight = 0.5 (Higher penalty)
  - Good to Have expenses: Weight = 0.35
  - Necessary expenses: Weight = 0.15
- The financial score will consider spending and budget performance starting from the first day of the month to the current day.

### Score Range:
- You want the score to fall between 0 to 100, but you're unsure how to normalize the range for the score calculation yet.

## Example:
Let's assume your monthly income is ¥210,000, and your monthly rent is ¥95,000. We’ll calculate the monthly and daily budgets for the three expense types based on the 80% of income allocated for expenses.
1. **Total Monthly Budget for Expenses**:
   - Monthly income: ¥210,000
   - 80% allocated for expenses: ¥210,000 × 80% = ¥168,000
   - After deducting the rent (¥95,000), the remaining budget is:  
     ¥168,000 - ¥95,000 = ¥73,000
2. **Monthly Budget Breakdown**: Based on the 3 types of expenses:
   - Necessary: 85% of the budget  
     85% × ¥73,000 = ¥62,050
   - Good to Have: 10% of the budget  
     10% × ¥73,000 = ¥7,300
   - Unnecessary: 5% of the budget  
     5% × ¥73,000 = ¥3,650
3. **Daily Budget Breakdown**: Since there are 30 days in the month, we’ll divide each category by 30 to get the daily budget for each type.
   - Necessary:  
     ¥62,050 ÷ 30 = ¥2,068.33 per day
   - Good to Have:  
     ¥7,300 ÷ 30 = ¥243.33 per day
   - Unnecessary:  
     ¥3,650 ÷ 30 = ¥121.67 per day
```
