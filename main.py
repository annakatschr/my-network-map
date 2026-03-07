from NmapScanner import NmapScanner
from NmapReport import NmapReport

# Create NmapScanner instance and call a method
scanner = NmapScanner()
result = scanner.do_open_port_analysis()
print("Scan result:", result)

# Create NmapReport instance and call a method
#report = NmapReport("report.pdf")
#report.create_report()