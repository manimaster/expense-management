import json
import datetime
from fpdf import FPDF

class PDF(FPDF):
    pass  # for now, can customize later

def generate_report(report_type, start_date, end_date):
    transactions = []
    with open('transactions.json', 'r') as f:
        for line in f:
            transactions.append(json.loads(line))

    filtered_transactions = [t for t in transactions if start_date <= datetime.datetime.strptime(t["date"], '%Y-%m-%d').date() <= end_date and t["type"] == report_type]

    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for transaction in filtered_transactions:
        pdf.cell(200, 10, txt=f"{transaction['date']} - {transaction['time']} - {transaction['place']} - {transaction['amount']} - {transaction['category']}", ln=True)

    pdf_file_name = f"{report_type}_{start_date}_{end_date}.pdf"
    pdf.output(f"reports/{pdf_file_name}")

    return pdf_file_name
