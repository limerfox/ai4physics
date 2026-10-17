import urllib.request
import urllib.parse
import ssl

# Read the tex file
with open(r'C:\Users\ForcePC\source\ai\ai4physics\cnt\physics_prob\paper\paper.tex', 'r') as f:
    tex = f.read()

# Read the bib file
with open(r'C:\Users\ForcePC\source\ai\ai4physics\cnt\physics_prob\paper\paper.bib', 'r') as f:
    bib = f.read()

# Try latexonline.cc API
data = urllib.parse.urlencode({
    'tex': tex,
    'bib': bib,
    'action': 'compile'
}).encode()

# Create SSL context that doesn't verify (for testing)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request(
    'https://latexonline.cc/compile',
    data=data,
    headers={'Content-Type': 'application/x-www-form-urlencoded'},
    method='POST'
)

try:
    with urllib.request.urlopen(req, timeout=120, context=ctx) as resp:
        content = resp.read()
        print(f'Status: {resp.status}')
        print(f'Size: {len(content)} bytes')
        # Check if it's a PDF
        if content[:5] == b'%PDF-':
            with open(r'C:\Users\ForcePC\source\ai\ai4physics\cnt\physics_prob\paper\paper.pdf', 'wb') as out:
                out.write(content)
            print('PDF saved successfully.')
        else:
            print('Not a PDF. First 200 bytes:')
            print(content[:200])
except urllib.error.HTTPError as e:
    print(f'HTTP Error: {e.code} {e.reason}')
    with e as resp:
        content = resp.read()
        print(content[:500])
except Exception as e:
    print(f'Error: {e}')