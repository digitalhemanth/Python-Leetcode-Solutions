import pandas as pd

# Get the input values from the user
monthly_investment = float(input("Enter the monthly investment amount: "))
time_period = int(input("Enter the time period (in years): "))
interest_rate = float(input("Enter the interest rate (in percentage): ")) / 100

# Calculate the total investment amount
total_investment = 0
investment_list = []
interest_list = []
maturity_amount_list = []
remaining_years_list = []

for year in range(1, time_period+1):
    investment = monthly_investment * 12
    total_investment += investment
    interest_earned = round(total_investment * interest_rate, 2)
    maturity_amount = round(total_investment + interest_earned, 2)
    remaining_years = time_period - year
    investment_list.append(investment)
    interest_list.append(interest_earned)
    maturity_amount_list.append(maturity_amount)
    remaining_years_list.append(remaining_years)

# Calculate the total maturity amount
total_maturity_amount = round(total_investment * ((1 + interest_rate)**time_period), 2)

# Create a DataFrame to store the investment and interest details for each year
df = pd.DataFrame({'Year': range(1, time_period+1), 
                   'Investment Amount (Year)': investment_list, 
                   'Total Investment Amount': [sum(investment_list[:i+1]) for i in range(len(investment_list))],
                   'Interest Earned (Till Date)': interest_list, 
                   'Maturity Amount (Till Date)': maturity_amount_list,
                   'Remaining Years for Maturity Date': remaining_years_list})

# Display the DataFrame in table format
print(df.to_string(index=False))

# Display the total maturity amount
print(f"\nTotal Maturity Amount: {total_maturity_amount}")
