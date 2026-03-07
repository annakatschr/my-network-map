import subprocess
import json

class NmapScanner:
    def __init__(self, target="scanme.nmap.org"):
        self.FULL_PATH = "C:\\Program Files (x86)\\Nmap\\nmap.exe"
        self.target = target


    def run_command(self, cmd):
        result = subprocess.run(cmd, capture_output=True, text=True)
       # data = json.loads(result.stdout)
        print("Command output:", result.stdout)
        return result.stdout


    def do_open_port_analysis(self):
        cmd = [self.FULL_PATH, "-oJ", "-", "-sV", self.target]
        return self.run_command(cmd)
      #  print("Parsed JSON keys:", list(data.keys()))
      

    def do_stealthy_scan(self):
        cmd = [self.FULL_PATH, "-sS", self.target]
        return self.run_command(cmd)
    

    def find_udp_ports(self):
        cmd = [self.FULL_PATH, "-sU", self.target]
        return self.run_command(cmd)


    def guess_os(self):
        cmd = [self.FULL_PATH, "-O", self.target]
        return self.run_command(cmd)
    
    def do_aggressive_scan(self):
        cmd = [self.FULL_PATH, "-A", self.target]
        return self.run_command(cmd)
    
    # A banner is simply the initial text a service sends back when you connect to it, often before you even authenticate.
    # 1. Identify services quickl
    # 2. Check for outdated or vulnerable version
    # If banner contains “Apache”, run web-specific scripts
    # If banner contains “OpenSSH”, check auth methods
    # If banner contains “ProFTPD”, check for anonymous login
    def run_nse_banner_script(self):
        cmd = [self.FULL_PATH, "--script=banner", self.target]
        return self.run_command(cmd)
    
    def run_nse_ftp_anonymous_script(self):
        cmd = [self.FULL_PATH, "--script=ftp-anon", self.target]
        return self.run_command(cmd)
    
    def run_nse_ftp_system_script(self):
        cmd = [self.FULL_PATH, "--script=ftp-syst", self.target]
        return self.run_command(cmd)
    
    def run_nse_tftp_enum_script(self):
        cmd = [self.FULL_PATH, "--script=tftp-enum", self.target]
        return self.run_command(cmd)

if __name__ == "__main__":
    scanner = NmapScanner()
    scanner.guess_os()