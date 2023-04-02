# Import the necessary libraries
import pandas as pd

# Take user inputs for monthly investment, time period, and interest rate
monthly_investment = int(input("Enter monthly investment amount: "))
time_period = int(input("Enter time period in years: "))
interest_rate = float(input("Enter interest rate in percentage: ")) / 100

# Calculate the total investment amount
total_investment = monthly_investment * 12 * time_period

# Create a list to store the investment and interest earned for each year
investment_list = []
interest_list = []
remaining_years_list = []
total_deposited_list = []
maturity_amount_list = []

# Calculate the investment, interest earned, maturity amount till date, and total amount deposited for each year
for year in range(1, time_period+1):
    investment = monthly_investment * 12
    interest_earned = round(total_investment * interest_rate - sum(interest_list), 2)
    maturity_amount = round(total_investment, 2)
    total_investment += investment + interest_earned
    remaining_years = time_period - year
    total_deposited = monthly_investment * 12 * year
    investment_list.append(investment)
    interest_list.append(interest_earned)
    remaining_years_list.append(remaining_years)
    total_deposited_list.append(total_deposited)
    maturity_amount_list.append(maturity_amount)

# Create a DataFrame to store the investment and interest details for each year
df = pd.DataFrame({'Year': range(1, time_period+1), 
                   'Investment Amount (Year)': investment_list,
                   'Total Amount Deposited': total_deposited_list,
                   'Interest Earned (Till Date)': interest_list, 
                   'Maturity Amount (Till Date)': maturity_amount_list,
                   'Remaining Years for Maturity Date': remaining_years_list})

# Display the DataFrame in table format
print(df.to_string(index=False))

# Calculate and display the total maturity amount
total_maturity_amount = round(sum(maturity_amount_list), 2)
print(f"\nTotal Maturity Amount: {total_maturity_amount}")
