import subprocess
import json

class NmapScanner:
    def __init__(self):
        self.FULL_PATH = "C:\\Program Files (x86)\\Nmap\\nmap.exe"
        self.target = "scanme.nmap.org"
    
    def do_open_port_analysis(self):

        """
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        """
        cmd = [self.FULL_PATH, "-oJ", "-", "-sV", self.target]
        result = subprocess.run(cmd, capture_output=True, text=True)
        print("Nmap output:", result.stdout)
        """
        json_buffer = ""

        for line in process.stdout:
            if line.strip().startswith("{") or json_buffer:
                json_buffer += line
            else:
                print("[progress]", line.strip())

        process.wait()

        data = json.loads(json_buffer)
        print("Parsed JSON keys:", data.keys()
        """

    def do_stealthy_scan(self):
        cmd = [self.FULL_PATH, "-sS", self.target]
        result = subprocess.run(cmd, capture_output=True, text=True)
        print("Stealthy scan output:", result.stdout)

    def finf_udp_ports(self):
        cmd = [self.FULL_PATH, "-sU", self.target]
        result = subprocess.run(cmd, capture_output=True, text=True)
        print("UDP scan output:", result.stdout)

    def guess_os(self):
        cmd = [self.FULL_PATH, "-O", self.target]
        result = subprocess.run(cmd, capture_output=True, text=True)
        print("OS detection output:", result.stdout)

if __name__ == "__main__":
    scanner = NmapScanner()
    scanner.guess_os()