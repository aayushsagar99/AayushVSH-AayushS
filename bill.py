from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# Define PDF filename
pdf_filename = "Bill_Form_Template.pdf"

# Setup document margins (0.5 inch margins for clean spacing)
doc = SimpleDocTemplate(
    pdf_filename,
    pagesize=letter,
    rightMargin=36,
    leftMargin=36,
    topMargin=36,
    bottomMargin=36
)

styles = getSampleStyleSheet()

# Custom styles matching a clean business receipt format
normal_style = ParagraphStyle(
    'FormNormal',
    parent=styles['Normal'],
    fontSize=10,
    leading=14
)

bold_style = ParagraphStyle(
    'FormBold',
    parent=styles['Normal'],
    fontSize=10,
    leading=14,
    fontName='Helvetica-Bold'
)

footer_style = ParagraphStyle(
    'FormFooter',
    parent=styles['Normal'],
    fontSize=8,
    leading=11
)

elements = []

# --- Header Section (Supplier Details & Bill Form Header) ---
header_data = [
    [
        Paragraph("<b>Details of Supplier:</b><br/><br/>State:<br/>State Code:", normal_style),
        Paragraph("<b>Bill Form</b><br/><br/>No. :<br/>Date :", normal_style)
    ]
]
header_table = Table(header_data, colWidths=[340, 200])
header_table.setStyle(TableStyle([
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#1A2B4C')),
    ('INNERGRID', (0,0), (-1,-1), 1, colors.HexColor('#1A2B4C')),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('PADDING', (0,0), (-1,-1), 8),
]))
elements.append(header_table)
elements.append(Spacer(1, 6))

# --- Receiver Details Section ---
receiver_data = [
    [Paragraph("<b>Details of Receiver:</b><br/><br/>State:<br/>State Code:", normal_style),
     Paragraph("<br/><br/>Receiver GSTIN:", normal_style)]
]
receiver_table = Table(receiver_data, colWidths=[340, 200])
receiver_table.setStyle(TableStyle([
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#1A2B4C')),
    ('INNERGRID', (0,0), (-1,-1), 1, colors.HexColor('#1A2B4C')),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('PADDING', (0,0), (-1,-1), 8),
]))
elements.append(receiver_table)
elements.append(Spacer(1, 10))

# --- Main Itemized Grid Table ---
# Width allocations: Description (240), HSN (60), Qty (50), Rate (70), Amount Rs (80), Amount P (40)
grid_data = [
    [
        Paragraph("<b>DESCRIPTION OF GOODS / SERVICES</b>", normal_style),
        Paragraph("<b>HSN<br/>Code</b>", normal_style),
        Paragraph("<b>Qnty.</b>", normal_style),
        Paragraph("<b>RATE</b>", normal_style),
        Paragraph("<b>AMOUNT</b>", normal_style),
        ""
    ],
    ["", "", "", "", "₹", "P."]
]

# Append 15 standard horizontal entry rows
for _ in range(15):
    grid_data.append(["", "", "", "", "", ""])

# Total and Thank You row
grid_data.append([Paragraph("Thank You !", normal_style), "", "", "", Paragraph("<b>Total</b>", bold_style), ""])

grid_table = Table(grid_data, colWidths=[240, 60, 50, 70, 80, 40], rowHeights=[24, 16] + [22]*15 + [24])
grid_table.setStyle(TableStyle([
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#1A2B4C')),
    ('INNERGRID', (0,0), (-1,-1), 1, colors.HexColor('#1A2B4C')),
    ('SPAN', (4,0), (5,0)), 
    ('SPAN', (0,-1), (3,-1)), 
    ('ALIGN', (0,0), (-1,1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('ALIGN', (4,1), (5,1), 'CENTER'), 
    ('ALIGN', (4,-1), (4,-1), 'RIGHT'), 
    ('PADDING', (0,0), (-1,-1), 4),
]))
elements.append(grid_table)
elements.append(Spacer(1, 6))

# --- Footer Section Terms & Signatory Area ---
footer_text = """<b>E. & O.E.</b><br/>
1. Goods once sold will not be taken back.<br/>
2. Interest @ 18% p.a. will be charged if the bill is not paid within due date."""

footer_data = [
    [Paragraph(footer_text, footer_style), Paragraph("<br/><br/>Authorised Signatory", normal_style)]
]
footer_table = Table(footer_data, colWidths=[360, 180])
footer_table.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'BOTTOM'),
    ('ALIGN', (1,0), (1,0), 'RIGHT'),
    ('PADDING', (0,0), (-1,-1), 4),
]))
elements.append(footer_table)

# Render and write file
doc.build(elements)
