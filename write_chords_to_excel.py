import openpyxl

#כותבת את האקורדים לקובץ אקסל
def write_chords_to_excel (chords_array, excel_file,num_chord_in_5) :
    wb = openpyxl.Workbook()
    sheet = wb.active

    row = 1
    col = 1
    mone = 0
    str_chord = ""
    for i in range(0, len(chords_array)):
        if(mone==num_chord_in_5):
            sheet.cell(row=row, column=col).value =str_chord
            str_chord = ""
            row += 4
            col = 1
            mone = 0
        str_chord += chords_array[i]
        str_chord += " "
        mone += 1
    wb.save(excel_file)


