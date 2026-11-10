import re

with open('/tmp/Antigravity_Export_Package/Mechanics_of_Materials_Final_Exam_Techniques_Guide.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Check style
style_match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
print("Style length:", len(style_match.group(1)) if style_match else 0)

# Check main sections
sections = re.findall(r'<section\s+id="([^"]+)"[^>]*>(.*?)</section>', html, re.DOTALL)
for s_id, body in sections:
    print(f"Section {s_id}: length {len(body)}")
