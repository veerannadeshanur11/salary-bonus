# Salary Bonus Calculator Program

salary = float(input("Enter the employee's salary: "))

print("\nOriginal Salary:", int(salary))

# Salary Bonus Calculator Program (with 10% bonus)

salary = float(input("Enter the employee's salary: "))

bonus_salary = salary + (salary * 0.10)

print("\nOriginal Salary:", int(salary))
print("Bonus Added:", int(bonus_salary))

# Salary Bonus Calculator Program (Bonus + Tax Deduction)

salary = float(input("Enter the employee's salary: "))

# 10% bonus
bonus_salary = salary + (salary * 0.10)

# 5% tax on the total after bonus
tax = bonus_salary * 0.05
final_salary = bonus_salary - tax

print("\nOriginal Salary:", int(salary))
print("Bonus Added:", int(bonus_salary))
print("After Tax Deduction:", int(final_salary))