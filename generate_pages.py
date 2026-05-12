import os

domains = [
    {"name": "riwep.com", "price": "1,950", "desc": "Premium Web & Tech Solutions Brand"},
    {"name": "lytren.com", "price": "2,400", "desc": "Next-Gen Logistics & Trend Platform"},
    {"name": "oryphonix.com", "price": "3,200", "desc": "High-End Communications & Security Identity"}
]

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{domain} is for sale!</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {{ background: radial-gradient(circle at center, #1a1a1a 0%, #000 100%); }}
        .glass {{ background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.1); }}
    </style>
</head>
<body class="text-white flex items-center justify-center min-h-screen">
    <div class="glass p-12 rounded-3xl shadow-2xl text-center max-w-2xl mx-4">
        <h1 class="text-5xl font-extrabold mb-4 bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-purple-600 uppercase tracking-tighter">
            {domain}
        </h1>
        <p class="text-xl text-gray-400 mb-8 tracking-wide">{desc}</p>
        <div class="text-3xl font-mono mb-10 text-green-400">Est. Value: ${price}</div>
        <div class="space-y-4">
            <a href="https://www.afternic.com/domain/{domain}" class="block w-full py-4 bg-blue-600 hover:bg-blue-700 rounded-xl font-bold transition-all transform hover:scale-105 shadow-lg shadow-blue-500/20">
                BUY IT NOW
            </a>
            <p class="text-sm text-gray-500 mt-6">Secure Transfer via Afternic/GoDaddy Escrow</p>
        </div>
    </div>
</body>
</html>
"""

for d in domains:
    folder = d['name'].split('.')[0]
    os.makedirs(folder, exist_ok=True)
    with open(f"{folder}/index.html", "w") as f:
        f.write(html_template.format(domain=d['name'], price=d['price'], desc=d['desc']))
    print(f"[+] Generated Landing Page for: {d['name']}")

