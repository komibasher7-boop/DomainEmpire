import os

links = {
    "riwep": "https://www.afternic.com/domains/riwep.com/details",
    "lytren": "https://www.afternic.com/domains/lytren.com/details",
    "oryphonix": "https://www.afternic.com/domains/oryphonix.com/details"
}

for folder, link in links.items():
    file_path = f"{folder}/index.html"
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            content = f.read()
        
        # استبدال أي رابط قديم بالرابط الجديد الصحيح
        # سنبحث عن الرابط الافتراضي الذي وضعناه في القالب أو أي رابط Afternic سابق
        import re
        new_content = re.sub(r'https://www.afternic.com/domain/\{domain\}', link, content)
        new_content = re.sub(r'https://www.afternic.com/domains/riwep.com/details', link, new_content)
        
        with open(file_path, "w") as f:
            f.write(new_content)
        print(f"[+] Updated: {folder}/index.html -> {link}")

