from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

class NmapReport:
    def __init__(self, filename):
        self.filename = filename
        self.report_data = {}
    
    def create_report(self):

        doc = SimpleDocTemplate("report.pdf")
        styles = getSampleStyleSheet()

                
        data = [
            ["Port", "Protocol", "State", "Service"],
            ["22", "tcp", "open", "ssh"],
            ["80", "tcp", "open", "http"],
        ]

        table = Table(data)
        table.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
            ("GRID", (0,0), (-1,-1), 0.5, colors.black),
            ("ALIGN", (0,0), (-1,-1), "CENTER"), ]))


        story = []
        story.append(Paragraph("Nmap Scan Report", styles["Title"]))
        story.append(Spacer(1, 12))
        story.append(Paragraph("This is a generated PDF report.", styles["BodyText"]))

        doc.build(story)

if __name__ == "__main__":
    report = NmapReport("report.pdf")
    report.create_report()