import os
# Built-in Python module to interact with personal computer's file system
from docxtpl import DocxTemplate
# Import added and installed to use Python-Docx-Template
# Refer to documentation here: https://docxtpl.readthedocs.io/en/latest/
from datetime import datetime as dt
# Imports needed to set up the date

t = dt.now()
# Variable to set up the date

todays_date = (t.strftime("%B" " " "%d" ", " "%Y"))
company_name = input("Enter the name of the company: ")
position_name = input("Enter the name of the position: ")
company_address = input("Enter the address: ")
company_city = input("Enter the company's city: ")
company_province = input("Enter the province: ")
company_postal = input("Enter the postal code: ")
company_country = input("Enter the country: ")
letter_addressee = input("Enter the hiring managers' name, or NA if not applicable: ")

if (letter_addressee == "NA"):
    letter_addressee = "Hiring Manager"
# Inputs for the addressee's name, which will either default to filling in the name or use "Hiring Manager" if there's no person

mission_statement = input("What is their mission statement?")
# Inputs for all the address-related information for the company

job_type = input("Enter the job type (SWE, Data Analyst, Data Science, Bioinformatics, QA): ")
# Inputs for job type to determine what cover letter format to use


context = {
    'todays_date': todays_date,
    'company_name': company_name,
    'position_name': position_name,
    'company_address': company_address,
    'company_city': company_city,
    'company_province': company_province,
    'company_country': company_country,
    'company_postal': company_postal,
    'letter_addressee': letter_addressee,
    'mission_statement': mission_statement
}

output_folder = r"C:\Users\Sam's PC\Downloads\Cover Letters To Convert"

if (job_type == "SWE"):
    doc = DocxTemplate("SWE_CoverLetterTemplate.docx")
    doc.render(context)
    letter_name = input("What would you like to name this letter?")
    output_path = os.path.join(output_folder, f"SL_{letter_name}_CoverLetter.docx")
    doc.save(output_path)

elif (job_type == "Data Analyst"):
    doc = DocxTemplate("DataAnalyst_CoverLetterTemplate.docx")
    doc.render(context)
    letter_name = input("What would you like to name this letter?")
    output_path = os.path.join(output_folder, f"SL_{letter_name}_CoverLetter.docx")
    doc.save(output_path)
elif (job_type == "QA"):
    doc = DocxTemplate("QA_Testing_CoverLetterTemplate.docx")
    doc.render(context)
    letter_name = input("What would you like to name this letter?")
    output_path = os.path.join(output_folder, f"SL_{letter_name}_CoverLetter.docx")
    doc.save(output_path)
elif (job_type == "Data Science"):
    doc = DocxTemplate("DataScience_CoverLetterTemplate.docx")
    doc.render(context)
    letter_name = input("What would you like to name this letter?")
    output_path = os.path.join(output_folder, f"SL_{letter_name}_CoverLetter.docx")
    doc.save(output_path)
elif (job_type == "IT Analyst"):
    doc = DocxTemplate("IT_CoverLetterTemplate.docx")
    doc.render(context)
    letter_name = input("What would you like to name this letter?")
    output_path = os.path.join(output_folder, f"SL_{letter_name}_CoverLetter.docx")
    doc.save(output_path)
elif (job_type == "Bioinformatics"):
    doc = DocxTemplate("Bioinformatics_CoverLetterTemplate.docx")
    doc.render(context)
    letter_name = input("What would you like to name this letter?")
    output_path = os.path.join(output_folder, f"SL_{letter_name}_CoverLetter.docx")
    doc.save(output_path)

# Set up the conditional statements needed to ensure that the correct template is being used

# https://medium.com/@alice.yang_10652/convert-word-doc-or-docx-to-pdf-with-python-a-comprehensive-guide-6c8e8b5a079a
# ^Alice Yang's reference on how to set up PDF converter