from datetime import datetime as dt
# Imports needed to set up the date
# Library added for 

t = dt.now()
# Variable to set up the date

print(t.strftime("%B" " " "%d" ", " "%Y"))
# Test print of the date in format that I would like

company_name = input("Enter the name of the company: ")
position_name = input("Enter the name of the position: ")
company_address = input("Enter the address: ")
# Inputs for company, position name and company address

job_type = input("Input the job type (SWE, Data Analyst, Data Science, Bioinformatics, QA: ")
# Inputs for job type to determine what cover letter format to use
