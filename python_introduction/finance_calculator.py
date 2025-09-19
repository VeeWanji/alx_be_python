income = input1 ("Enter your monthly income:")
expenses = input2 ("Enter your monthly expenses:")
savings = income - expenses
projected_savings = savings * 12 + (savings * 12 * 0.05)
print(f"Projected savings after one year, with interest, is: {projected_savings}")
