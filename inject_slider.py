import os

base = "/Users/satoseiya/Desktop/AG/タイ植毛/"
files = ["index.html", "clinics.html", "cases.html", "price-flow.html"]

slider_html = """
    <!-- 無限スライダー -->
    <div class="marquee-wrapper">
        <div class="marquee-content">
            <div class="marquee-item">症例写真</div>
            <div class="marquee-item">クリニック内観</div>
            <div class="marquee-item">手術室</div>
            <div class="marquee-item">症例写真</div>
            <div class="marquee-item">クリニック内観</div>
            <div class="marquee-item">手術室</div>
            <div class="marquee-item">症例写真</div>
            <div class="marquee-item">クリニック内観</div>
            <!-- Duplicate for seamless loop -->
            <div class="marquee-item">症例写真</div>
            <div class="marquee-item">クリニック内観</div>
            <div class="marquee-item">手術室</div>
            <div class="marquee-item">症例写真</div>
            <div class="marquee-item">クリニック内観</div>
            <div class="marquee-item">手術室</div>
            <div class="marquee-item">症例写真</div>
            <div class="marquee-item">クリニック内観</div>
        </div>
    </div>

    <!-- CTA: まずは匿名相談、無料カウンセリングへ -->
    <section class="section section-bg">
"""

for f in files:
    path = os.path.join(base, f)
    if not os.path.exists(path):
        continue
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Avoid duplicate injection
    if '<div class="marquee-wrapper">' not in content:
        # replace CTA section opening
        target = '    <!-- CTA: まずは匿名相談、無料カウンセリングへ -->\n    <section class="section section-bg">'
        content = content.replace(target, slider_html.lstrip('\n'))
        
        with open(path, "w", encoding="utf-8") as file:
            file.write(content)

print("Injected slider successfully.")
