import pandas as pd
from fpdf import FPDF


def excel_to_pdf(excel_file_path, pdf_file_path):
    # קריאת קובץ ה-Excel באמצעות pandas
    df = pd.read_excel(excel_file_path)

    # יצירת מסמך PDF חדש
    pdf = FPDF()
    pdf.add_page()
    print("pdf")
    # הוספת גופן תומך Unicode
    font_path = "DejaVuSans.ttf"  # ודא שקובץ הגופן נמצא באותו מיקום של הסקריפט או ציין את הנתיב המלא
    print("pdf2")
    pdf.add_font("DejaVu", "", font_path, uni=True)
    pdf.set_font("DejaVu", size=12)

    # הגדרת רוחב העמוד ושולי התא
    page_width = pdf.w - 2 * pdf.l_margin
    col_width = page_width / len(df.columns)
    cell_height = 10

    # כתיבת הכותרות
    for column in df.columns:
        pdf.cell(col_width, cell_height, column, border=1, align='C')
    pdf.ln(cell_height)

    # כתיבת הנתונים
    for row in df.itertuples(index=False):
        for cell in row:
            pdf.cell(col_width, cell_height, str(cell), border=1)
        pdf.ln(cell_height)

    # שמירת קובץ ה-PDF
    pdf.output(pdf_file_path)
    print(f"Data has been written to {pdf_file_path}")


# דוגמה לשימוש בפונקציה
excel_to_pdf("chords.xlsx", "output.pdf")
