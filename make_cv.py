from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                HRFlowable, ListFlowable, ListItem)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT

ACCENT = colors.HexColor("#2563eb")   # royal blue
DARK   = colors.HexColor("#111827")
GRAY   = colors.HexColor("#4b5563")
LIGHT  = colors.HexColor("#9ca3af")

doc = SimpleDocTemplate(
    "Ishan_Rai_CV.pdf", pagesize=A4,
    leftMargin=16*mm, rightMargin=16*mm, topMargin=13*mm, bottomMargin=10*mm,
)

styles = getSampleStyleSheet()
name = ParagraphStyle('name', parent=styles['Title'], fontName='Helvetica-Bold',
                      fontSize=24, textColor=DARK, spaceAfter=2, leading=27)
role = ParagraphStyle('role', fontName='Helvetica', fontSize=12, textColor=ACCENT,
                      spaceAfter=6, leading=15)
contact = ParagraphStyle('contact', fontName='Helvetica', fontSize=9, textColor=GRAY, leading=13)
section = ParagraphStyle('section', fontName='Helvetica-Bold', fontSize=11, textColor=ACCENT,
                         spaceBefore=8, spaceAfter=3, leading=13)
body = ParagraphStyle('body', fontName='Helvetica', fontSize=9.3, textColor=GRAY, leading=13)
jobtitle = ParagraphStyle('jobtitle', fontName='Helvetica-Bold', fontSize=10.5, textColor=DARK, leading=13)
jobmeta = ParagraphStyle('jobmeta', fontName='Helvetica-Oblique', fontSize=9, textColor=LIGHT, leading=12, alignment=TA_RIGHT)
company = ParagraphStyle('company', fontName='Helvetica', fontSize=9.8, textColor=ACCENT, leading=12)
bullet = ParagraphStyle('bullet', fontName='Helvetica', fontSize=9.1, textColor=GRAY, leading=12.5)

story = []

def rule():
    story.append(Spacer(1, 2))
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#e5e7eb"),
                            spaceBefore=1, spaceAfter=4))

# ---- Header ----
story.append(Paragraph("Ishan Rai", name))
story.append(Paragraph("QA Engineer &nbsp;&middot;&nbsp; QA Analyst", role))
story.append(Paragraph(
    "Lalitpur, Nepal &nbsp;&bull;&nbsp; raiishan67@gmail.com &nbsp;&bull;&nbsp; +977 9865044105 "
    "&nbsp;&bull;&nbsp; github.com/77ishan", contact))
story.append(Spacer(1, 6))
story.append(HRFlowable(width="100%", thickness=1.4, color=ACCENT, spaceAfter=2))

# ---- Summary ----
story.append(Paragraph("PROFILE", section))
story.append(Paragraph(
    "QA Engineer with 3+ years of experience across product-based and service-based companies. "
    "I specialise in manual testing, test automation with Cypress, API testing with Postman, and "
    "performance testing with JMeter. I have built QA processes from the ground up, defined bug "
    "tracking workflows, and embedded quality early in agile development lifecycles, with a proven "
    "track record of reducing production defects and shipping high-quality software.", body))

# ---- Experience ----
story.append(Paragraph("EXPERIENCE", section))

def job(title, comp, dates, bullets, current=False):
    tag = ' &nbsp;<font color="#16a34a" size=8><b>CURRENT</b></font>' if current else ''
    head = Table(
        [[Paragraph(title + tag, jobtitle), Paragraph(dates, jobmeta)]],
        colWidths=[118*mm, 56*mm])
    head.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
                              ('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),
                              ('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0)]))
    story.append(head)
    story.append(Paragraph(comp, company))
    story.append(Spacer(1, 2))
    items = [ListItem(Paragraph(b, bullet), leftIndent=10, value='•') for b in bullets]
    story.append(ListFlowable(items, bulletType='bullet', start='•',
                              leftIndent=8, bulletColor=ACCENT, bulletFontSize=7))
    story.append(Spacer(1, 5))

job("QA Analyst", "Rara Labs", "Jun 2026 to Present", [
    "Driving end-to-end quality as QA Analyst on the core product team.",
    "Designing test strategy, test plans and detailed test cases.",
    "Running functional, regression and smoke testing cycles.",
    "Logging, tracking and verifying defects through to closure.",
    "Championing quality standards across the product team.",
], current=True)

job("QA Engineer", "Progressive Labs, Kalopul, Kathmandu", "Mar 2025 to Oct 2025", [
    "Pioneered and built the entire QA process from the ground up.",
    "Designed test suites covering functional, regression, smoke and UI testing.",
    "Defined and standardised bug-tracking workflows with severity and priority levels.",
    "Set up performance and load testing with JMeter.",
    "Established release-readiness checklists and sign-off procedures, reducing production defects.",
    "Integrated QA early into the agile development lifecycle.",
])

job("Associate QA Officer", "Khalti Digital Wallet, Lalitpur", "Mar 2024 to Mar 2025", [
    "Performed smoke testing on every mobile build of the Khalti App.",
    "Developed and executed automated test cases in Cypress for the Khalti web application.",
    "Conducted API testing across services using Postman.",
    "Ran performance testing on the Khalti mobile app with JMeter.",
    "Collaborated in a Scrum team, tracking tasks in Jira.",
])

job("QA Engineer", "Keela (Forty-two Tech), Lalitpur", "Apr 2023 to Feb 2024", [
    "Executed system, regression and smoke testing across modules.",
    "Wrote automated test cases with Cypress for multiple product areas.",
    "Performed end-to-end testing of the software.",
    "Authored detailed test cases for Keela's modules.",
    "Tracked and managed reported bugs in Linear.",
])

# ---- Skills ----
story.append(Paragraph("SKILLS", section))
skill_rows = [
    ("Testing", "Manual, Functional, Regression, Smoke, E2E, API, Performance"),
    ("Automation", "Cypress, Test Automation, End-to-End Testing"),
    ("Tools", "Postman, JMeter, Jira, Linear"),
    ("Technical", "HTML, CSS, JavaScript, SQL"),
    ("Methodologies", "Agile / Scrum, Test Case Design, Bug Tracking & Reporting"),
]
data = [[Paragraph("<b>%s</b>" % k, body), Paragraph(v, body)] for k, v in skill_rows]
t = Table(data, colWidths=[34*mm, 140*mm])
t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
                       ('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),
                       ('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2)]))
story.append(t)

# ---- Education ----
story.append(Paragraph("EDUCATION", section))
edu = [
    ("BSc CSIT", "Prime College", "2018 to 2023"),
    ("QA Training", "InfoDevelopers, Lalitpur", "2022 to 2023"),
]
for deg, inst, yr in edu:
    row = Table([[Paragraph("<b>%s</b> &nbsp; <font color='#4b5563'>%s</font>" % (deg, inst), body),
                  Paragraph(yr, jobmeta)]], colWidths=[130*mm, 44*mm])
    row.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
                            ('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),
                            ('TOPPADDING',(0,0),(-1,-1),1),('BOTTOMPADDING',(0,0),(-1,-1),1)]))
    story.append(row)

doc.build(story)
print("CV created: Ishan_Rai_CV.pdf")
