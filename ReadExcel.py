import string
import openpyxl

path = 'files/'



ABCD = list(string.ascii_uppercase)  # matriz con todas las letras del abcedario
wb = openpyxl.load_workbook(path+"Validations.xlsx")

sheet = wb.active
max_col = sheet.max_column


#wb[a]

print(wb["A"])

excel_data = []

for letter in ABCD:
    print(letter)
    data_letter = []
    sheet = wb[letter]
    max_col = sheet.max_column
    for i in range(25) :
        row = []
        for i in range(1, max_col + 1):
            cell_obj = sheet.cell(row=1, column=i)
            row.append(cell_obj.value)
        data_letter.append(row)
    excel_data.append(data_letter)
print(excel_data)

            # Escojo la primera por su nombre
# La variable es un objeto <sheet>
