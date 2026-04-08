import re

path = "/Users/satoseiya/Desktop/AG/タイ植毛/cases.html"

with open(path, "r", encoding="utf-8") as file:
    content = file.read()

# Replace <div class="card-meta">DATE <span style="...">|</span> CATEGORY</div>
# with <div class="card-meta">DATE</div>
content = re.sub(r'(<div class="card-meta">[^<]+)<span[^>]*>[^<]*</span>[^<]*</div>', r'\1</div>', content)

with open(path, "w", encoding="utf-8") as file:
    file.write(content)

print("Categories removed from cases.html successfully.")
