from fpdf import FPDF

import CLI


class PDFReport:
    """
    Creates a PDF report of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        pdf.set_font('Arial', 'B', size=36)
        pdf.cell(w=0, h = 80, txt= "Flatmates Bill", border=1, align='C', ln=1)

        pdf.set_font('Arial', 'B', size=24)
        pdf.cell(w=200, h = 40, txt = "Period", border=1)
        pdf.cell(w=200, h = 40, txt =CLI.period, border=1, ln=1)

        pdf.set_font('Arial', 'B', size=12)
        pdf.cell(w=200, h = 40, txt = flatmate1.name, border=1)
        pdf.cell(w=200, h = 40, txt = '$'+str(flatmate1.pays(bill, flatmate2)), border=1, ln=1)

        pdf.set_font('Arial', 'B', size=12)
        pdf.cell(w=200, h = 40, txt = flatmate2.name, border=1)
        pdf.cell(w=200, h = 40, txt = '$'+str(flatmate2.pays(bill, flatmate1)), border=1, ln=1)

        pdf.output(self.filename)
