# Professional Profile Generator
# Displays formatted professional information with salary calculations

# Display constants
bold_line = "=================================="
semi_bold_line = "----------------------------------"

# Profile information
full_name = "Jane Smith"
email = "jane.smith@mail.com"
job_title = "Senior Developer"
experience = 5  # years
hourly_rate = 80.00  # dollars per hour

# Calculate earnings (assuming 40-hour work week, 52 weeks/year)
annual_salary = hourly_rate * 40 * 52
lifetime_earnings = experience * annual_salary

# Display profile
print(bold_line)
print(f"\tPROFESSIONAL PROFILE\n")
print(bold_line)
print(f"Name:             {full_name.title()}")
print(f"Email:            {email.lower()}")
print(f"Title:            {job_title.title()}")
print(f"Experience:       {experience} years")
print(f"Hourly Rate:      ${hourly_rate:.2f}")
print(semi_bold_line)
print(f"Annual Salary:    ${annual_salary:,.2f}")
print(f"Lifetime Earnings: ${lifetime_earnings:,.2f}")
print(bold_line)