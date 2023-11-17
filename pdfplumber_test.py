import pandas as pd
import pdfplumber

with pdfplumber.open('docs/YearlyReport_Debajyoti-Bera_Jun2020.pdf') as pdf:
    final_output = ''
    for i in range(len(pdf.pages)):
        page = pdf.pages[i]
        text = page.extract_text()
        final_output += text
        # table = page.extract_table()
        # df = pd.DataFrame(table)

print(final_output)
# print(df.values)
