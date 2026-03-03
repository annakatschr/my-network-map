from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

class NmapReport:
    def __init__(self, filename):
        self.filename = filename
        self.report_data = {}
    
    def create_report(self):

        doc = SimpleDocTemplate("report.pdf")
        styles = getSampleStyleSheet()

        story = []
        story.append(Paragraph("Nmap Scan Report", styles["Title"]))
        story.append(Spacer(1, 12))
        story.append(Paragraph("This is a generated PDF report.", styles["BodyText"]))

        doc.build(story)

if __name__ == "__main__":
    report = NmapReport("report.pdf")
    report.create_report()