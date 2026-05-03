import json
from datetime import datetime

class ReportGen:
    def generate(self, data, filename):
        # JSON report
        report = {
            'timestamp': datetime.now().isoformat(),
            'tool': 'Network Intelligence Suite (NIS)',
            'author': 'Abhishek',
            'results': data
        }
        
        with open(f"{filename}.json", 'w') as f:
            json.dump(report, f, indent=2)
        
        # HTML report
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>NIS Scan Report</title>
    <style>
        body {{ font-family: monospace; background: #0a0a0a; color: #00ff00; padding: 20px; }}
        h1 {{ color: #ff4444; }}
        pre {{ background: #1a1a1a; padding: 15px; border-left: 3px solid #00ff00; }}
    </style>
</head>
<body>
    <h1>Network Intelligence Suite - Scan Report</h1>
    <p>Generated: {datetime.now().isoformat()}</p>
    <pre>{json.dumps(data, indent=2)}</pre>
</body>
</html>
        """
        
        with open(f"{filename}.html", 'w') as f:
            f.write(html)
