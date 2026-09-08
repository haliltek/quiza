import subprocess

cmd = ['ssh', 'root@142.93.104.78', 'pdftotext -v']
res = subprocess.run(cmd, capture_output=True, text=True)
print(res.stderr or res.stdout)
