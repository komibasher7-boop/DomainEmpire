import os

domains = [
    {
        "name": "riwep.com",
        "price": "$2,900",
        "desc": "Advanced Intelligence & Cloud Infrastructure Solutions.",
        "color": "from-cyan-500 to-blue-600",
        "wa_msg": "Hello, I am interested in acquiring the premium domain RIWEP.com. Please provide more details.",
        "logo_text": "RIWEP"
    },
    {
        "name": "lytren.com",
        "price": "$3,500",
        "desc": "Modern Logistics, Trend Analysis & Strategic Mobility.",
        "color": "from-emerald-400 to-teal-600",
        "wa_msg": "Hello, I want to discuss the purchase of LYTREN.com for my logistics platform.",
        "logo_text": "LYTREN"
    },
    {
        "name": "oryphonix.com",
        "price": "$4,800",
        "desc": "Cyber Security, Elite Hardware & Communication Identity.",
        "color": "from-orange-500 to-red-600",
        "wa_msg": "Greetings, I am looking to purchase ORYPHONIX.com. What is your final offer?",
        "logo_text": "ORYPHONIX"
    }
]

email = "bashradam97@gmail.com"
phone = "33767747072"

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Acquire {name} | Premium Digital Identity</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@200;400;800&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Plus Jakarta Sans', sans-serif; background: #050505; color: white; }}
        .glass {{ background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.08); }}
        .premium-shadow {{ shadow-lg shadow-{color}/20 }}
        .logo-font {{ font-weight: 800; letter-spacing: -2px; }}
    </style>
</head>
<body class="flex flex-col items-center justify-center min-h-screen overflow-hidden p-6">
    <div class="absolute inset-0 bg-gradient-to-tr {color} opacity-10"></div>
    
    <div class="glass w-full max-w-4xl p-16 rounded-[40px] text-center relative z-10">
        <!-- Logo Section -->
        <div class="mb-12">
            <h1 class="text-7xl logo-font bg-clip-text text-transparent bg-gradient-to-b from-white to-gray-500 italic">
                {logo_text}
            </h1>
            <div class="h-1 w-24 bg-gradient-to-r {color} mx-auto mt-2 rounded-full"></div>
        </div>

        <p class="text-2xl text-gray-400 mb-4 max-w-2xl mx-auto font-light leading-relaxed">
            This premium digital asset is available for strategic acquisition.
        </p>
        <p class="text-gray-500 mb-12 italic">{desc}</p>

        <div class="text-5xl font-bold mb-12 text-white">
            <span class="text-sm uppercase tracking-widest text-gray-500 block mb-2">Est. Market Value</span>
            {price}
        </div>

        <!-- Action Buttons -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-xl mx-auto">
            <a href="https://www.afternic.com/domains/{name}/details" class="group relative flex items-center justify-center p-5 bg-white text-black font-bold rounded-2xl transition-all hover:scale-105 active:scale-95">
                SECURE PURCHASE (AFTERNIC)
            </a>
            <a href="https://wa.me/{phone}?text={wa_msg}" class="flex items-center justify-center p-5 bg-green-600/20 border border-green-500/50 text-green-400 font-bold rounded-2xl hover:bg-green-600 hover:text-white transition-all hover:scale-105">
                NEGOTIATE VIA WHATSAPP
            </a>
        </div>

        <div class="mt-12 pt-12 border-t border-white/5">
            <p class="text-sm text-gray-500">Contact the Domain Strategist Directly</p>
            <a href="mailto:{email}?subject=Inquiry for {name}" class="text-lg text-blue-400 hover:underline">{email}</a>
        </div>
    </div>

    <!-- Security Footer -->
    <div class="mt-8 text-gray-600 text-xs tracking-widest uppercase">
        Safe Transfer Guarantee • Escrow Secured • 2026 Sovereign Assets
    </div>
</body>
</html>
"""

for d in domains:
    folder = d['name'].split('.')[0]
    os.makedirs(folder, exist_ok=True)
    with open(f"{folder}/index.html", "w") as f:
        # Fill colors and data
        page = html_template.format(
            name=d['name'], 
            price=d['price'], 
            desc=d['desc'], 
            color=d['color'], 
            logo_text=d['logo_text'],
            wa_msg=d['wa_msg'].replace(" ", "%20"),
            phone=phone,
            email=email
        )
        f.write(page)
    print(f"[+] V2.0 PREMIUM DEPLOYED: {d['name']}")
