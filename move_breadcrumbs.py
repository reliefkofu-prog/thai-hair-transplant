import re
import os

base_path = "/Users/satoseiya/Desktop/AG/タイ植毛"
files = ["index.html", "clinics.html", "price-flow.html", "cases.html", "contact.html"]

for f in files:
    path = os.path.join(base_path, f)
    if not os.path.exists(path):
        continue
    
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
    
    # 1. Menu Links Correction
    header_nav = """<ul class="nav-links">
                    <li><a href="index.html">ホーム</a></li>
                    <li><a href="clinics.html">提携クリニック</a></li>
                    <li><a href="cases.html">症例（ブログ）</a></li>
                    <li><a href="price-flow.html">費用や手術の流れ</a></li>
                </ul>"""
    # Replace the existing nav-links with correct global links but keeping active state if possible.
    # It's easier to just use standard links. We'll leave the active states alone or remove them since standard SWELL highlights based on URL. 
    # Actually wait! The user said "全体的にメニューのリンクがされてないところがあったりするので、全部リンクが推せるか確認して"
    
    # 2. Moving breadcrumbs
    # Extract breadcrumbs block
    breadcrumb_pattern = re.compile(r'(\s*<!-- パンくずリスト -->\s*<div[^>]*>.*?</div>\s*</div>)', re.DOTALL)
    match = breadcrumb_pattern.search(content)
    if match:
        bc_block = match.group(1)
        # Remove it from current position
        content = content.replace(bc_block, '')
        
        # Insert before <!-- Footer -->
        footer_pos = content.find('<!-- Footer -->')
        if footer_pos != -1:
            content = content[:footer_pos] + bc_block + '\n    ' + content[footer_pos:]
            
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)
print("Breadcrumbs moved.")
