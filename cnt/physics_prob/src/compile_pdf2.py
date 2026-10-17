import urllib.request
import urllib.parse
import ssl
import json

# Read the tex file
with open(r'C:\Users\ForcePC\source\ai\ai4physics\cnt\physics_prob\paper\paper.tex', 'r') as f:
    tex = f.read()

# Read the bib file
with open(r'C:\Users\ForcePC\source\ai\ai4physics\cnt\physics_prob\paper\paper.bib', 'r') as f:
    bib = f.read()

# Try collab.latex API
payload = json.dumps({
    'file': tex,
    'bib': bib,
    'engine': 'pdflatex'
}).encode()

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request(
    'https://collab.latex/api/compile',
    data=payload,
    headers={
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    },
    method='POST'
)

try:
    with urllib.request.urlopen(req, timeout=120, context=ctx) as resp:
        content = resp.read()
        print(f'Status: {resp.status}')
        print(f'Size: {len(content)} bytes')
        print(content[:500])
except urllib.error.HTTPError as e:
    print(f'HTTP Error: {e.code} {e.reason}')
    print(e.read()[:500])
except Exception as e:
    print(f'Error: {e}')