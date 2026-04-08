import os

base = "/Users/satoseiya/Desktop/AG/タイ植毛/"
files = ["index.html", "clinics.html", "cases.html", "price-flow.html", "contact.html"]

for f in files:
    path = os.path.join(base, f)
    if not os.path.exists(path):
        continue
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
    
    # 1. Replace logo div with a tag
    content = content.replace('<div class="logo-placeholder">サイトロゴ</div>', '<a href="index.html" class="logo-placeholder" style="text-decoration: none;">サイトロゴ</a>')
    
    # 2. If contact.html, replace the select with radio buttons
    if f == "contact.html":
        select_block = """<select class="input-select">
                            <option value="">▼選択</option>
                            <option value="なるべく早く">なるべく早く</option>
                            <option value="半年以内">半年以内</option>
                            <option value="1年以内">1年以内</option>
                            <option value="未定">未定（まずは話を聞きたい）</option>
                        </select>"""
        radio_block = """<div class="checkbox-group" style="display: flex; gap: 24px; flex-wrap: wrap;">
                            <label><input type="radio" name="timing" value="なるべく早く"> なるべく早く</label>
                            <label><input type="radio" name="timing" value="半年以内"> 半年以内</label>
                            <label><input type="radio" name="timing" value="1年以内"> 1年以内</label>
                            <label><input type="radio" name="timing" value="未定" checked> 未定（まずは話を聞きたい）</label>
                        </div>"""
        content = content.replace(select_block, radio_block)
        
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)
print("Updated logo in all pages and created radio buttons for contact form.")
