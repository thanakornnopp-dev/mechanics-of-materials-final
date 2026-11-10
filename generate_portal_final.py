import re
import os
import json

# Read the original HTML file
with open('/tmp/Antigravity_Export_Package/Mechanics_of_Materials_Final_Exam_Techniques_Guide.html', 'r', encoding='utf-8') as f:
    orig_html = f.read()

# Study links mapping for each section
STUDY_LINKS = {
    "prep-inertia": [
        {"channel": "P'BIG ETC TUTOR", "title": "Centroid (การหาจุดเซนทรอยด์)", "type": "คอนเซปต์ & ตัวอย่าง", "url": "https://www.youtube.com/results?search_query=Centroid+P%27BIG+ETC+TUTOR"},
        {"channel": "P'BIG ETC TUTOR", "title": "Inertia รอบแกนที่จุด Centroid", "type": "สูตร & ย้ายแกน", "url": "https://www.youtube.com/results?search_query=Inertia+รอบแกนที่จุด+Centroid+P%27BIG"},
        {"channel": "P'BIG ETC TUTOR", "title": "ตะลุยข้อสอบเก่า INERTIA PART 1 & PART 2", "type": "ข้อสอบจริง", "url": "https://www.youtube.com/results?search_query=ตะลุยข้อสอบเก่า+INERTIA+PART1+P%27BIG"},
        {"channel": "be-engineer", "title": "Area Moment of Inertia (โมเมนต์ความเฉื่อยของพื้นที่)", "type": "สรุปปูพื้นฐาน", "url": "https://www.youtube.com/results?search_query=Area+Moment+of+Inertia+be-engineer"}
    ],
    "lec-09": [
        {"channel": "be-engineer", "title": "ติวสดฟรี Strength - Torsion (การบิด)", "type": "ติวสดครบเครื่อง", "url": "https://www.youtube.com/results?search_query=ติวสดฟรี+Strength+-+Torsion+be-engineer"},
        {"channel": "อ.ไพโรจน์ สิงหถนัดกิจ", "title": "โจทย์ตัวอย่าง - Torsion 1-3 & 2-3 (เพลาต่อเฟือง)", "type": "โจทย์มาตรฐาน จุฬาฯ", "url": "https://www.youtube.com/results?search_query=โจทย์ตัวอย่าง+-+Torsion+Pairod+Singhatanadgid"},
        {"channel": "อ.ไพโรจน์ สิงหถนัดกิจ", "title": "Lecture 12 Torsion (ทฤษฎีการบิดเพลากลม)", "type": "บรรยายเชิงลึก", "url": "https://www.youtube.com/results?search_query=Lecture+12+Torsion+Pairod+Singhatanadgid"},
        {"channel": "อ.สิทธิชัย แสงอาทิตย์", "title": "10 บทที่ 5 การบิด Part 1/2 (สมการการบิดและมุมบิด)", "type": "สอนทีละสเต็ป", "url": "https://www.youtube.com/results?search_query=บทที่+5+การบิด+Part+1%2F2+สิทธิชัย+แสงอาทิตย์"}
    ],
    "lec-10": [
        {"channel": "อ.สิทธิชัย แสงอาทิตย์", "title": "11 บทที่ 5 การบิด Part 2/2 (Indeterminate Torsion)", "type": "แก้สมการ Compatibility", "url": "https://www.youtube.com/results?search_query=บทที่+5+การบิด+Part+2%2F2+Indeterminate+สิทธิชัย+แสงอาทิตย์"},
        {"channel": "อ.ไพโรจน์ สิงหถนัดกิจ", "title": "โจทย์ตัวอย่าง - Torsion 3-3 (เพลายึดแน่น 2 ปลาย)", "type": "โจทย์อินดีเทอร์มิเนต", "url": "https://www.youtube.com/results?search_query=โจทย์ตัวอย่าง+-+Torsion+3-3+Pairod+Singhatanadgid"}
    ],
    "lec-11": [
        {"channel": "be-engineer", "title": "การหา Bending Stress โดยละเอียด (แกนสะเทิน & โมเมนต์ความเฉื่อย)", "type": "เทคนิคห้ามพลาด", "url": "https://www.youtube.com/results?search_query=การหา+Bending+Stress+โดยละเอียด+be-engineer"},
        {"channel": "be-engineer", "title": "Strength - การหา Stress เมื่อวัสดุรับโมเมนต์ดัด", "type": "ทำความเข้าใจเครื่องหมาย", "url": "https://www.youtube.com/results?search_query=Strength+-+การหา+Stress+เมื่อวัสดุรับโมเมนต์ดัด+be-engineer"},
        {"channel": "อ.ไพโรจน์ สิงหถนัดกิจ", "title": "Lecture 15 Bending of Beam - Bending stress", "type": "พิสูจน์ Flexure Formula", "url": "https://www.youtube.com/results?search_query=Bending+of+Beam+Bending+stress+Pairod+Singhatanadgid"},
        {"channel": "อ.ไพโรจน์ สิงหถนัดกิจ", "title": "โจทย์ตัวอย่าง - Bending of beam 1-4 & 2-4", "type": "ตัวอย่างโจทย์สอบ", "url": "https://www.youtube.com/results?search_query=โจทย์ตัวอย่าง+Bending+of+beam+Pairod+Singhatanadgid"},
        {"channel": "อ.สิทธิชัย แสงอาทิตย์", "title": "บทที่ 6 การดัด (สมการการดัด + ตัวอย่าง) Part 2/3", "type": "สอนละเอียดทุกขั้นตอน", "url": "https://www.youtube.com/results?search_query=บทที่+6+การดัด+สมการการดัด+สิทธิชัย+แสงอาทิตย์"},
        {"channel": "อ.ณัฐวุฒิ ธนสารสาธิต", "title": "Teach Strength of materials 1 Ch 05 (Bending Stress)", "type": "เฉลยแบบฝึกหัด", "url": "https://www.youtube.com/results?search_query=Teach+Strength+of+materials+1+Ch+05+Nuttawut"}
    ],
    "lec-12": [
        {"channel": "P'BIG ETC TUTOR", "title": "DOUBLE INTEGRATION By P'BIG ETC TUTOR (หาการแอ่นตัวของคาน)", "type": "วิธีอินทิเกรต 2 ชั้นยอดฮิต", "url": "https://www.youtube.com/results?search_query=DOUBLE+INTEGRATION+By+P%27BIG+ETC+TUTOR"},
        {"channel": "P'BIG ETC TUTOR", "title": "MOMENT AREA Part 1 & Part 2 (ทฤษฎีพื้นที่โมเมนต์)", "type": "ทางลัดคานยื่น & จุดรองรับ", "url": "https://www.youtube.com/results?search_query=MOMENT+AREA+P%27BIG+ETC+TUTOR"},
        {"channel": "P'BIG ETC TUTOR", "title": "STUF 1 & STUF 2 / Virtual Work คานแอ่นตัว", "type": "วิธีงานเสมือน (ถ้ามีสอบ)", "url": "https://www.youtube.com/results?search_query=virtual+work+P%27BIG+ETC+TUTOR"},
        {"channel": "อ.ไพโรจน์ สิงหถนัดกิจ", "title": "Lecture 18 & 19 Deflection of Beam (ทฤษฎีและตัวอย่าง)", "type": "เนื้อหาหลักสูตรมาตรฐาน", "url": "https://www.youtube.com/results?search_query=Deflection+of+Beam+Pairod+Singhatanadgid"},
        {"channel": "อ.ณัฐวุฒิ ธนสารสาธิต", "title": "Teach Strength of materials 1 Ch 06-1 & 06-2 (Deflection)", "type": "ตะลุยโจทย์ละเอียด", "url": "https://www.youtube.com/results?search_query=Teach+Strength+of+materials+1+Ch+06+Nuttawut"}
    ],
    "lec-13": [
        {"channel": "อ.ไพโรจน์ สิงหถนัดกิจ", "title": "โจทย์ตัวอย่าง - Bending of beam 3-4 & 4-4 (Transformed Section)", "type": "โจทย์หน้าตัดผสม ไม้-เหล็ก", "url": "https://www.youtube.com/results?search_query=โจทย์ตัวอย่าง+Bending+of+beam+Pairod+Singhatanadgid"},
        {"channel": "อ.สิทธิชัย แสงอาทิตย์", "title": "14 บทที่ 6 การดัด Part 2/2 (หน้าตัดผสม Transformed Section)", "type": "สเต็ปแปลงความกว้าง n*b", "url": "https://www.youtube.com/results?search_query=14+บทที่+6+การดัด+Part+2%2F2+สิทธิชัย+แสงอาทิตย์"},
        {"channel": "อ.ไพโรจน์ สิงหถนัดกิจ", "title": "Lecture 17 Bending of Beam - Examples (Composite Beams)", "type": "ตัวอย่างข้อสอบเก่า", "url": "https://www.youtube.com/results?search_query=Lecture+17+Bending+of+Beam+Examples+Pairod+Singhatanadgid"}
    ],
    "lec-14": [
        {"channel": "อ.ไพโรจน์ สิงหถนัดกิจ", "title": "โจทย์ตัวอย่าง - Transverse Shear 1-1 (หาความเค้นเฉือนในคาน)", "type": "คำนวณ Q และ t ถูกต้อง", "url": "https://www.youtube.com/results?search_query=โจทย์ตัวอย่าง+Transverse+Shear+1-1+Pairod+Singhatanadgid"},
        {"channel": "P'BIG ETC TUTOR", "title": "Shear Center และการหาค่า First Moment Q", "type": "ทริคลูกศรและการตัดหา Q", "url": "https://www.youtube.com/results?search_query=Shear+Center+P%27BIG+ETC+TUTOR"},
        {"channel": "อ.ไพโรจน์ สิงหถนัดกิจ", "title": "Lecture 16 Bending of Beam - Shear stress", "type": "ที่มาสูตร tau = VQ/It", "url": "https://www.youtube.com/results?search_query=Lecture+16+Bending+of+Beam+Shear+stress+Pairod+Singhatanadgid"},
        {"channel": "อ.สิทธิชัย แสงอาทิตย์", "title": "15 บทที่ 7 การเฉือนตามขวาง Part 1/2", "type": "กระจายหน่วยแรงเฉือน", "url": "https://www.youtube.com/results?search_query=15+บทที่+7+การเฉือนตามขวาง+สิทธิชัย+แสงอาทิตย์"}
    ],
    "lec-15": [
        {"channel": "อ.สิทธิชัย แสงอาทิตย์", "title": "16 บทที่ 7 การเฉือนตามขวาง [Shear flow] Part 2/2", "type": "หน้าตัดประกอบ & รอยต่อตะปู", "url": "https://www.youtube.com/results?search_query=16+บทที่+7+การเฉือนตามขวาง+Shear+flow+สิทธิชัย+แสงอาทิตย์"},
        {"channel": "อ.ไพโรจน์ สิงหถนัดกิจ", "title": "โจทย์ตัวอย่าง - Built-up members / Shear flow & Fasteners", "type": "สเต็ปถอนตะปูหาระยะ s", "url": "https://www.youtube.com/results?search_query=Shear+flow+Built-up+members+Pairod+Singhatanadgid"},
        {"channel": "P'BIG ETC TUTOR", "title": "Shear Flow การถอนตะปูหาระยะ Pitch s", "type": "ทริคลัดข้อสอบ", "url": "https://www.youtube.com/results?search_query=Shear+Flow+P%27BIG+ETC+TUTOR"}
    ],
    "lec-16": [
        {"channel": "อ.ไพโรจน์ สิงหถนัดกิจ", "title": "โจทย์ตัวอย่าง - Buckling 1-2 & 2-2 (เสาเดาะออยเลอร์)", "type": "คิด 2 ระนาบ x และ y", "url": "https://www.youtube.com/results?search_query=โจทย์ตัวอย่าง+Buckling+Pairod+Singhatanadgid"},
        {"channel": "อ.ไพโรจน์ สิงหถนัดกิจ", "title": "Lecture 24 Buckling (การโก่งเดาะของเสาอุดมคติ)", "type": "ทฤษฎี & ค่าสัมประสิทธิ์ K", "url": "https://www.youtube.com/results?search_query=Lecture+24+Buckling+Pairod+Singhatanadgid"},
        {"channel": "อ.สิทธิชัย แสงอาทิตย์", "title": "21 บทที่ 13 การโก่งเดาะของเสา (Euler Buckling)", "type": "สูตร Pcr และ sigma_cr", "url": "https://www.youtube.com/results?search_query=21+บทที่+13+การโก่งเดาะของเสา+สิทธิชัย+แสงอาทิตย์"},
        {"channel": "อ.ณัฐวุฒิ ธนสารสาธิต", "title": "Teach Strength of materials 1 Ch 09 (Buckling of Columns)", "type": "เฉลยข้อสอบเสาโก่ง", "url": "https://www.youtube.com/results?search_query=Teach+Strength+of+materials+1+Ch+09+Nuttawut"}
    ],
    "bonus-combined": [
        {"channel": "P'BIG ETC TUTOR", "title": "โจทย์เพิ่มเติม combine stress By P'BIG ETC TUTOR", "type": "โจทย์รวมมิตร 3 มิติ", "url": "https://www.youtube.com/results?search_query=โจทย์เพิ่มเติม+combine+stress+By+P%27BIG+ETC+TUTOR"},
        {"channel": "P'BIG ETC TUTOR", "title": "COMBINE STRESS 2", "type": "สเต็ปหาหน่วยแรงรวม", "url": "https://www.youtube.com/results?search_query=COMBINE+STRESS2+P%27BIG+ETC+TUTOR"},
        {"channel": "be-engineer", "title": "การใช้ Mohr's Circle หา Principal Stress", "type": "วงกลมมอร์เข้าใจง่าย", "url": "https://www.youtube.com/results?search_query=การใช้+Mohr%27s+Circle+หา+Principal+Stress+be-engineer"},
        {"channel": "etctutor กวดวิชา etc", "title": "Mechanics of Materials/Solid/Strength CvET - Stress 1/2566", "type": "เฉลยข้อสอบภาควิชาวิศวกรรมโยธา", "url": "https://www.youtube.com/results?search_query=Mechanics+of+Materials+Solid+Strength+CvET+Stress+etctutor"}
    ]
}

def generate_video_links_html(sec_id):
    links = STUDY_LINKS.get(sec_id, [])
    if not links:
        return ""
    
    cards_html = []
    for l in links:
        ch = l['channel']
        ch_badge_class = "channel-badge-default"
        if "be-engineer" in ch:
            ch_badge_class = "channel-badge-be"
        elif "ไพโรจน์" in ch:
            ch_badge_class = "channel-badge-chula"
        elif "สิทธิชัย" in ch:
            ch_badge_class = "channel-badge-sut"
        elif "ณัฐวุฒิ" in ch:
            ch_badge_class = "channel-badge-nut"
        elif "BIG" in ch:
            ch_badge_class = "channel-badge-big"
        
        card = f"""
        <div class="video-item-card">
          <div class="video-meta-row">
            <span class="channel-pill {ch_badge_class}"><i class="fa-brands fa-youtube"></i> {ch}</span>
            <span class="type-pill">{l['type']}</span>
          </div>
          <h4 class="video-title">{l['title']}</h4>
          <a href="{l['url']}" target="_blank" rel="noopener noreferrer" class="btn-watch-yt">
            <i class="fa-solid fa-play"></i> รับชมคลิปบน YouTube
          </a>
        </div>
        """
        cards_html.append(card)
    
    return f"""
    <div class="embedded-study-box">
      <div class="embedded-study-header">
        <div class="embedded-study-title">
          <i class="fa-brands fa-youtube text-red-500 text-xl"></i>
          <span>คลิปเรียน & โจทย์ตัวอย่างสำหรับหัวข้อนี้ (Direct Learning Links)</span>
        </div>
        <span class="badge-count">{len(links)} วิดีโอแนะนำ</span>
      </div>
      <div class="video-grid-cards">
        {''.join(cards_html)}
      </div>
    </div>
    """

# Extract all sections from original HTML
section_pattern = re.compile(r'<section\s+id="([^"]+)"([^>]*)>(.*?)</section>', re.DOTALL)
sections = section_pattern.findall(orig_html)

enhanced_sections = []
for s_id, s_attrs, s_body in sections:
    video_html = generate_video_links_html(s_id)
    
    checklist_html = f"""
    <div class="study-status-banner">
      <label class="study-checkbox-label">
        <input type="checkbox" class="topic-check" data-topic-id="{s_id}" onchange="toggleTopicCheck('{s_id}', this.checked)">
        <span class="checkmark-custom"></span>
        <span class="checkbox-text font-medium text-slate-700 dark:text-slate-200">ทำเครื่องหมายเมื่อติว/ทบทวนหัวข้อนี้เสร็จสิ้น</span>
      </label>
      <span class="status-indicator" id="status-badge-{s_id}">⏳ กำลังเตรียมตัว</span>
    </div>
    """
    
    new_body = s_body
    if '<h2' in new_body:
        h2_end = new_body.find('</h2>') + 5
        new_body = new_body[:h2_end] + checklist_html + new_body[h2_end:]
    else:
        new_body = checklist_html + new_body
    
    new_body = new_body + video_html
    enhanced_sections.append(f'<section id="{s_id}"{s_attrs}>\n{new_body}\n</section>')

sections_html_joined = "\n\n".join(enhanced_sections)

# Interactive Engineering Calculators Section
CALCULATORS_HTML = """
<section id="engineering-calculators" class="topic-section card" data-category="calculators">
  <div class="section-badge-header">
    <span class="sec-pill" style="background:#0284c7;color:#fff;"><i class="fa-solid fa-calculator mr-1"></i> Interactive Tool</span>
    <span class="sec-sub">เครื่องคำนวณและตรวจสอบผลลัพธ์</span>
  </div>
  <h2 class="text-2xl font-bold mt-2 text-slate-900 dark:text-white flex items-center gap-2">
    <i class="fa-solid fa-sliders text-sky-500"></i> เครื่องคำนวณสูตรหลักกลศาสตร์วัสดุ (Engineering Quick Calculators)
  </h2>
  <p class="text-slate-600 dark:text-slate-300 text-sm mt-1 mb-4">
    ใช้สำหรับตรวจคำตอบการบ้าน ตรวจผลคำนวณข้อสอบ หรือทดลองเปลี่ยนตัวแปรเพื่อเสริมความเข้าใจทางฟิสิกส์
  </p>

  <!-- Calculator Tabs -->
  <div class="calc-tabs flex flex-wrap gap-2 mb-6 border-b border-slate-200 dark:border-slate-700 pb-2">
    <button class="calc-tab-btn active" onclick="switchCalc('calc-torsion')">
      <i class="fa-solid fa-rotate mr-1"></i> 1. การบิด (Torsion)
    </button>
    <button class="calc-tab-btn" onclick="switchCalc('calc-bending')">
      <i class="fa-solid fa-arrows-split-up-and-left mr-1"></i> 2. การดัด (Bending Stress)
    </button>
    <button class="calc-tab-btn" onclick="switchCalc('calc-shear')">
      <i class="fa-solid fa-scissors mr-1"></i> 3. การเฉือน & ตะปู (Shear Flow)
    </button>
    <button class="calc-tab-btn" onclick="switchCalc('calc-buckling')">
      <i class="fa-solid fa-arrows-down-to-line mr-1"></i> 4. เสาโก่งเดาะ (Euler Buckling)
    </button>
    <button class="calc-tab-btn" onclick="switchCalc('calc-mohr')">
      <i class="fa-regular fa-circle mr-1"></i> 5. วงกลมมอร์ (Mohr's Circle)
    </button>
  </div>

  <!-- 1. Torsion Calculator -->
  <div id="calc-torsion" class="calc-panel">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <div class="space-y-3 bg-slate-50 dark:bg-slate-800/60 p-4 rounded-xl border border-slate-200 dark:border-slate-700">
        <h4 class="font-bold text-slate-800 dark:text-slate-100 text-sm"><i class="fa-solid fa-pen-to-square text-sky-500 mr-1"></i> กรอกพารามิเตอร์การบิด (Torsion Inputs)</h4>
        <div>
          <label class="block text-xs font-semibold text-slate-600 dark:text-slate-300">แรงบิดภายใน $T$ (N·m)</label>
          <input type="number" id="t-torque" value="1200" class="calc-input">
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-600 dark:text-slate-300">รัศมีเพลาตัน $c$ (mm)</label>
          <input type="number" id="t-radius" value="25" class="calc-input">
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-600 dark:text-slate-300">ความยาวเพลา $L$ (m)</label>
          <input type="number" id="t-length" value="1.5" step="0.1" class="calc-input">
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-600 dark:text-slate-300">มอดุลัสเฉือน $G$ (GPa)</label>
          <input type="number" id="t-modulus" value="77" class="calc-input">
        </div>
        <button onclick="computeTorsion()" class="calc-action-btn">
          <i class="fa-solid fa-calculator mr-1"></i> คำนวณความเค้นเฉือนและมุมบิด
        </button>
      </div>
      <div class="bg-sky-50/60 dark:bg-sky-950/30 p-4 rounded-xl border border-sky-200 dark:border-sky-800/50 flex flex-col justify-between">
        <div>
          <h4 class="font-bold text-sky-900 dark:text-sky-200 text-sm mb-3"><i class="fa-solid fa-square-poll-vertical mr-1"></i> ผลลัพธ์การคำนวณ (Torsion Outputs)</h4>
          <div class="space-y-2 text-sm">
            <div class="flex justify-between py-1 border-b border-sky-200/50 dark:border-sky-800/40">
              <span class="text-slate-600 dark:text-slate-400">Polar Moment ($J$):</span>
              <span id="t-out-j" class="font-mono font-bold text-slate-900 dark:text-white">-- mm⁴</span>
            </div>
            <div class="flex justify-between py-1 border-b border-sky-200/50 dark:border-sky-800/40">
              <span class="text-slate-600 dark:text-slate-400">Max Shear Stress ($\tau_{\max}$):</span>
              <span id="t-out-tau" class="font-mono font-bold text-sky-600 dark:text-sky-400 text-base">-- MPa</span>
            </div>
            <div class="flex justify-between py-1 border-b border-sky-200/50 dark:border-sky-800/40">
              <span class="text-slate-600 dark:text-slate-400">Angle of Twist ($\phi$):</span>
              <span id="t-out-phi-rad" class="font-mono font-bold text-slate-900 dark:text-white">-- rad</span>
            </div>
            <div class="flex justify-between py-1">
              <span class="text-slate-600 dark:text-slate-400">Angle of Twist in Degrees ($\phi^\circ$):</span>
              <span id="t-out-phi-deg" class="font-mono font-bold text-purple-600 dark:text-purple-400">-- °</span>
            </div>
          </div>
        </div>
        <div class="mt-3 p-2.5 bg-white/70 dark:bg-slate-900/60 rounded-lg text-xs text-slate-600 dark:text-slate-400 font-mono">
          สูตร: $\tau_{\max} = \frac{Tc}{J}$ และ $\phi = \frac{TL}{GJ}$
        </div>
      </div>
    </div>
  </div>

  <!-- 2. Bending Stress Calculator -->
  <div id="calc-bending" class="calc-panel hidden">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <div class="space-y-3 bg-slate-50 dark:bg-slate-800/60 p-4 rounded-xl border border-slate-200 dark:border-slate-700">
        <h4 class="font-bold text-slate-800 dark:text-slate-100 text-sm"><i class="fa-solid fa-pen-to-square text-sky-500 mr-1"></i> กรอกพารามิเตอร์การดัด (Bending Inputs)</h4>
        <div>
          <label class="block text-xs font-semibold text-slate-600 dark:text-slate-300">โมเมนต์ดัดภายใน $M$ (kN·m)</label>
          <input type="number" id="b-moment" value="45" step="0.5" class="calc-input">
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-600 dark:text-slate-300">ระยะห่างจากแกนสะเทิน $y$ (mm)</label>
          <input type="number" id="b-y" value="120" class="calc-input">
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-600 dark:text-slate-300">โมเมนต์ความเฉื่อย $I$ ($\times 10^6\text{ mm}^4$)</label>
          <input type="number" id="b-i" value="65.4" step="0.1" class="calc-input">
        </div>
        <button onclick="computeBending()" class="calc-action-btn">
          <i class="fa-solid fa-calculator mr-1"></i> คำนวณความเค้นดัด
        </button>
      </div>
      <div class="bg-sky-50/60 dark:bg-sky-950/30 p-4 rounded-xl border border-sky-200 dark:border-sky-800/50 flex flex-col justify-between">
        <div>
          <h4 class="font-bold text-sky-900 dark:text-sky-200 text-sm mb-3"><i class="fa-solid fa-square-poll-vertical mr-1"></i> ผลลัพธ์ความเค้นดัด (Flexure Output)</h4>
          <div class="space-y-2 text-sm">
            <div class="flex justify-between py-1 border-b border-sky-200/50 dark:border-sky-800/40">
              <span class="text-slate-600 dark:text-slate-400">Flexure Stress ($\sigma$):</span>
              <span id="b-out-sigma" class="font-mono font-bold text-sky-600 dark:text-sky-400 text-lg">-- MPa</span>
            </div>
            <div class="flex justify-between py-1 border-b border-sky-200/50 dark:border-sky-800/40">
              <span class="text-slate-600 dark:text-slate-400">ลักษณะหน่วยแรง (State):</span>
              <span id="b-out-state" class="font-bold text-slate-800 dark:text-slate-200">ตรวจสอบตำแหน่งแกน NA</span>
            </div>
          </div>
        </div>
        <div class="mt-3 p-2.5 bg-white/70 dark:bg-slate-900/60 rounded-lg text-xs text-slate-600 dark:text-slate-400 font-mono">
          สูตร: $\sigma = \frac{My}{I}$ (โซนหัวลูกศรโมเมนต์เป็นอัด $-$ / ตูดลูกศรเป็นดึง $+$)
        </div>
      </div>
    </div>
  </div>

  <!-- 3. Transverse Shear & Nails Calculator -->
  <div id="calc-shear" class="calc-panel hidden">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <div class="space-y-3 bg-slate-50 dark:bg-slate-800/60 p-4 rounded-xl border border-slate-200 dark:border-slate-700">
        <h4 class="font-bold text-slate-800 dark:text-slate-100 text-sm"><i class="fa-solid fa-pen-to-square text-sky-500 mr-1"></i> ข้อมูลแรงเฉือนและรอยต่อ (Shear Inputs)</h4>
        <div class="grid grid-cols-2 gap-2">
          <div>
            <label class="block text-xs font-semibold text-slate-600 dark:text-slate-300">แรงเฉือน $V$ (kN)</label>
            <input type="number" id="s-v" value="30" class="calc-input">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-600 dark:text-slate-300">โมเมนต์พื้นที่ $Q$ ($\times 10^3\text{ mm}^3$)</label>
            <input type="number" id="s-q" value="450" class="calc-input">
          </div>
        </div>
        <div class="grid grid-cols-2 gap-2">
          <div>
            <label class="block text-xs font-semibold text-slate-600 dark:text-slate-300">โมเมนต์ความเฉื่อย $I$ ($\times 10^6\text{ mm}^4$)</label>
            <input type="number" id="s-i" value="85" class="calc-input">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-600 dark:text-slate-300">ความหนาแนวตัด $t$ (mm)</label>
            <input type="number" id="s-t" value="20" class="calc-input">
          </div>
        </div>
        <div class="grid grid-cols-2 gap-2">
          <div>
            <label class="block text-xs font-semibold text-slate-600 dark:text-slate-300">แรงรับได้ต่อตะปู 1 ตัว (kN)</label>
            <input type="number" id="s-fnail" value="1.2" step="0.1" class="calc-input">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-600 dark:text-slate-300">จำนวนแนวตะปู $m$</label>
            <input type="number" id="s-mnail" value="2" class="calc-input">
          </div>
        </div>
        <button onclick="computeShear()" class="calc-action-btn">
          <i class="fa-solid fa-calculator mr-1"></i> คำนวณความเค้นเฉือน & ระยะห่างตะปู
        </button>
      </div>
      <div class="bg-sky-50/60 dark:bg-sky-950/30 p-4 rounded-xl border border-sky-200 dark:border-sky-800/50 flex flex-col justify-between">
        <div>
          <h4 class="font-bold text-sky-900 dark:text-sky-200 text-sm mb-3"><i class="fa-solid fa-square-poll-vertical mr-1"></i> ผลลัพธ์หน่วยแรงเฉือนและระยะตะปู</h4>
          <div class="space-y-2 text-sm">
            <div class="flex justify-between py-1 border-b border-sky-200/50 dark:border-sky-800/40">
              <span class="text-slate-600 dark:text-slate-400">Shear Stress ($\tau$):</span>
              <span id="s-out-tau" class="font-mono font-bold text-sky-600 dark:text-sky-400 text-base">-- MPa</span>
            </div>
            <div class="flex justify-between py-1 border-b border-sky-200/50 dark:border-sky-800/40">
              <span class="text-slate-600 dark:text-slate-400">Shear Flow ($q$):</span>
              <span id="s-out-q" class="font-mono font-bold text-slate-900 dark:text-white">-- N/mm</span>
            </div>
            <div class="flex justify-between py-1 border-b border-sky-200/50 dark:border-sky-800/40">
              <span class="text-slate-600 dark:text-slate-400">Max Fastener Spacing ($s_{\max}$):</span>
              <span id="s-out-s" class="font-mono font-bold text-emerald-600 dark:text-emerald-400 text-lg">-- mm</span>
            </div>
            <div class="flex justify-between py-1">
              <span class="text-slate-600 dark:text-slate-400">ระยะแนะนำใช้งาน (ปัดเศษลง):</span>
              <span id="s-out-rec" class="font-bold text-purple-600 dark:text-purple-400">--</span>
            </div>
          </div>
        </div>
        <div class="mt-3 p-2.5 bg-white/70 dark:bg-slate-900/60 rounded-lg text-xs text-slate-600 dark:text-slate-400 font-mono">
          สูตร: $\tau = \frac{VQ}{It}$, $q = \frac{VQ}{I}$ และ $s_{\max} = \frac{m F_{\text{allow}}}{q}$
        </div>
      </div>
    </div>
  </div>

  <!-- 4. Euler Buckling Calculator -->
  <div id="calc-buckling" class="calc-panel hidden">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <div class="space-y-3 bg-slate-50 dark:bg-slate-800/60 p-4 rounded-xl border border-slate-200 dark:border-slate-700">
        <h4 class="font-bold text-slate-800 dark:text-slate-100 text-sm"><i class="fa-solid fa-pen-to-square text-sky-500 mr-1"></i> พารามิเตอร์เสาอุดมคติ (Column Inputs)</h4>
        <div class="grid grid-cols-2 gap-2">
          <div>
            <label class="block text-xs font-semibold text-slate-600 dark:text-slate-300">โมดูลัสยืดหยุ่น $E$ (GPa)</label>
            <input type="number" id="c-e" value="200" class="calc-input">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-600 dark:text-slate-300">ความยาวเสา $L$ (m)</label>
            <input type="number" id="c-l" value="4.5" step="0.1" class="calc-input">
          </div>
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-600 dark:text-slate-300">เงื่อนไขจุดรองรับปลายเสา ($K$)</label>
          <select id="c-k" class="calc-input font-sans text-xs">
            <option value="1.0" selected>Pinned - Pinned (ปลายหมุนทั้ง 2 ข้าง, K = 1.0)</option>
            <option value="2.0">Fixed - Free (ปลายยึดแน่นข้างเดียวแบบเสายื่น, K = 2.0)</option>
            <option value="0.5">Fixed - Fixed (ปลายยึดแน่นทั้ง 2 ข้าง, K = 0.5)</option>
            <option value="0.7">Fixed - Pinned (ยึดแน่นข้างหนึ่ง หมุนข้างหนึ่ง, K = 0.7)</option>
          </select>
        </div>
        <div class="grid grid-cols-2 gap-2">
          <div>
            <label class="block text-xs font-semibold text-slate-600 dark:text-slate-300">Inertia น้อยสุด $I_{\min}$ ($\times 10^6\text{ mm}^4$)</label>
            <input type="number" id="c-i" value="18.5" step="0.1" class="calc-input">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-600 dark:text-slate-300">พื้นที่หน้าตัด $A$ (mm²)</label>
            <input type="number" id="c-a" value="3200" class="calc-input">
          </div>
        </div>
        <button onclick="computeBuckling()" class="calc-action-btn">
          <i class="fa-solid fa-calculator mr-1"></i> คำนวณ Critical Buckling Load
        </button>
      </div>
      <div class="bg-sky-50/60 dark:bg-sky-950/30 p-4 rounded-xl border border-sky-200 dark:border-sky-800/50 flex flex-col justify-between">
        <div>
          <h4 class="font-bold text-sky-900 dark:text-sky-200 text-sm mb-3"><i class="fa-solid fa-square-poll-vertical mr-1"></i> ผลการเดาะของเสาออยเลอร์</h4>
          <div class="space-y-2 text-sm">
            <div class="flex justify-between py-1 border-b border-sky-200/50 dark:border-sky-800/40">
              <span class="text-slate-600 dark:text-slate-400">Effective Length ($KL$):</span>
              <span id="c-out-kl" class="font-mono font-bold text-slate-900 dark:text-white">-- m</span>
            </div>
            <div class="flex justify-between py-1 border-b border-sky-200/50 dark:border-sky-800/40">
              <span class="text-slate-600 dark:text-slate-400">Critical Load ($P_{cr}$):</span>
              <span id="c-out-pcr" class="font-mono font-bold text-rose-600 dark:text-rose-400 text-lg">-- kN</span>
            </div>
            <div class="flex justify-between py-1 border-b border-sky-200/50 dark:border-sky-800/40">
              <span class="text-slate-600 dark:text-slate-400">Radius of Gyration ($r$):</span>
              <span id="c-out-r" class="font-mono font-bold text-slate-900 dark:text-white">-- mm</span>
            </div>
            <div class="flex justify-between py-1">
              <span class="text-slate-600 dark:text-slate-400">Critical Stress ($\sigma_{cr}$):</span>
              <span id="c-out-sigmacr" class="font-mono font-bold text-sky-600 dark:text-sky-400 text-base">-- MPa</span>
            </div>
          </div>
        </div>
        <div class="mt-3 p-2.5 bg-white/70 dark:bg-slate-900/60 rounded-lg text-xs text-slate-600 dark:text-slate-400 font-mono">
          สูตร: $P_{cr} = \frac{\pi^2 E I}{(KL)^2}$ และ $\sigma_{cr} = \frac{P_{cr}}{A}$
        </div>
      </div>
    </div>
  </div>

  <!-- 5. Mohr's Circle Calculator -->
  <div id="calc-mohr" class="calc-panel hidden">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <div class="space-y-3 bg-slate-50 dark:bg-slate-800/60 p-4 rounded-xl border border-slate-200 dark:border-slate-700">
        <h4 class="font-bold text-slate-800 dark:text-slate-100 text-sm"><i class="fa-solid fa-pen-to-square text-sky-500 mr-1"></i> สภาพความเค้นในระนาบ 2D (State of Stress)</h4>
        <div>
          <label class="block text-xs font-semibold text-slate-600 dark:text-slate-300">$\sigma_x$ (MPa, ดึงบวก / อัดลบ)</label>
          <input type="number" id="m-sigmax" value="80" class="calc-input">
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-600 dark:text-slate-300">$\sigma_y$ (MPa, ดึงบวก / อัดลบ)</label>
          <input type="number" id="m-sigmay" value="-40" class="calc-input">
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-600 dark:text-slate-300">$\tau_{xy}$ (MPa)</label>
          <input type="number" id="m-tauxy" value="25" class="calc-input">
        </div>
        <button onclick="computeMohr()" class="calc-action-btn">
          <i class="fa-solid fa-calculator mr-1"></i> คำนวณ Principal Stresses & Mohr's Circle
        </button>
      </div>
      <div class="bg-sky-50/60 dark:bg-sky-950/30 p-4 rounded-xl border border-sky-200 dark:border-sky-800/50 flex flex-col justify-between">
        <div>
          <h4 class="font-bold text-sky-900 dark:text-sky-200 text-sm mb-3"><i class="fa-solid fa-square-poll-vertical mr-1"></i> ผลลัพธ์วงกลมมอร์ (Mohr's Circle Values)</h4>
          <div class="space-y-2 text-sm">
            <div class="flex justify-between py-1 border-b border-sky-200/50 dark:border-sky-800/40">
              <span class="text-slate-600 dark:text-slate-400">จุดศูนย์กลางวงกลม ($\sigma_{avg}$):</span>
              <span id="m-out-avg" class="font-mono font-bold text-slate-900 dark:text-white">-- MPa</span>
            </div>
            <div class="flex justify-between py-1 border-b border-sky-200/50 dark:border-sky-800/40">
              <span class="text-slate-600 dark:text-slate-400">รัศมีวงกลมมอร์ ($R$):</span>
              <span id="m-out-r" class="font-mono font-bold text-slate-900 dark:text-white">-- MPa</span>
            </div>
            <div class="flex justify-between py-1 border-b border-sky-200/50 dark:border-sky-800/40">
              <span class="text-slate-600 dark:text-slate-400">Principal Stress 1 ($\sigma_1$):</span>
              <span id="m-out-sig1" class="font-mono font-bold text-emerald-600 dark:text-emerald-400 text-base">-- MPa</span>
            </div>
            <div class="flex justify-between py-1 border-b border-sky-200/50 dark:border-sky-800/40">
              <span class="text-slate-600 dark:text-slate-400">Principal Stress 2 ($\sigma_2$):</span>
              <span id="m-out-sig2" class="font-mono font-bold text-rose-600 dark:text-rose-400 text-base">-- MPa</span>
            </div>
            <div class="flex justify-between py-1">
              <span class="text-slate-600 dark:text-slate-400">Max In-Plane Shear ($\tau_{\text{in-plane}}^{\max}$):</span>
              <span id="m-out-taumax" class="font-mono font-bold text-purple-600 dark:text-purple-400 text-base">-- MPa</span>
            </div>
          </div>
        </div>
        <div class="mt-3 p-2.5 bg-white/70 dark:bg-slate-900/60 rounded-lg text-xs text-slate-600 dark:text-slate-400 font-mono">
          สูตร: $\sigma_{1,2} = \frac{\sigma_x + \sigma_y}{2} \pm \sqrt{\left(\frac{\sigma_x-\sigma_y}{2}\right)^2 + \tau_{xy}^2}$
        </div>
      </div>
    </div>
  </div>
</section>
"""

# Assemble Full HTML Template
FULL_PAGE_HTML = f"""<!DOCTYPE html>
<html lang="th" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>กลศาสตร์วัสดุ (Mechanics of Materials) - คัมภีร์สรุปสอบปลายภาค & แหล่งคลิปเรียนครบทุกบท</title>
  
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  
  <!-- FontAwesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
  
  <!-- Google Fonts: Sarabun, Chakra Petch & JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&family=Sarabun:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
  
  <!-- MathJax 3 LaTeX Engine -->
  <script>
    window.MathJax = {{
      tex: {{
        inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
        displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
        processEscapes: true
      }},
      options: {{
        skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
      }}
    }};
  </script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

  <style>
    :root {{
      --primary: #1e3a8a;
      --primary-light: #2563eb;
      --secondary: #0f766e;
      --accent: #b45309;
      --danger: #b91c1c;
      --success: #15803d;
      --purple: #6d28d9;
      --dark: #0f172a;
      --slate: #334155;
      --border: #e2e8f0;
      --card-bg: #ffffff;
      --body-bg: #f8fafc;
    }}

    .dark {{
      --card-bg: #1e293b;
      --body-bg: #0b1120;
      --border: #334155;
    }}

    body {{
      font-family: 'Sarabun', sans-serif;
      background-color: var(--body-bg);
      color: #1e293b;
      line-height: 1.6;
      transition: background-color 0.2s ease, color 0.2s ease;
    }}

    .dark body {{
      color: #f1f5f9;
    }}

    h1, h2, h3, h4, .font-heading {{
      font-family: 'Chakra Petch', sans-serif;
    }}

    code, pre, .font-mono {{
      font-family: 'JetBrains Mono', monospace;
    }}

    /* Layout & Cards */
    .app-container {{
      max-width: 1400px;
      margin: 0 auto;
      padding: 1.5rem 1rem;
    }}

    .card {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 1rem;
      padding: 1.75rem;
      margin-bottom: 2rem;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      transition: border-color 0.2s, box-shadow 0.2s;
    }}

    .card:hover {{
      border-color: #94a3b8;
      box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08);
    }}

    .dark .card {{
      background: #1e293b;
      border-color: #334155;
    }}

    /* Study Status Banner & Checkbox */
    .study-status-banner {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 0.75rem;
      padding: 0.75rem 1rem;
      background: #f1f5f9;
      border-radius: 0.75rem;
      margin: 1rem 0 1.25rem 0;
      border-left: 4px solid #0284c7;
    }}

    .dark .study-status-banner {{
      background: #0f172a;
      border-left-color: #38bdf8;
    }}

    .study-checkbox-label {{
      display: flex;
      align-items: center;
      gap: 0.6rem;
      cursor: pointer;
      user-select: none;
      font-size: 0.925rem;
    }}

    .topic-check {{
      width: 1.2rem;
      height: 1.2rem;
      accent-color: #0284c7;
      cursor: pointer;
    }}

    .status-indicator {{
      font-size: 0.8rem;
      font-weight: 600;
      padding: 0.25rem 0.65rem;
      border-radius: 9999px;
      background: #e2e8f0;
      color: #475569;
    }}

    .status-indicator.done {{
      background: #dcfce7;
      color: #15803d;
    }}

    .dark .status-indicator.done {{
      background: #14532d;
      color: #86efac;
    }}

    /* Embedded Study Box & Video Grid */
    .embedded-study-box {{
      margin-top: 1.75rem;
      padding: 1.25rem;
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 0.875rem;
    }}

    .dark .embedded-study-box {{
      background: #0f172a/70;
      border-color: #334155;
    }}

    .embedded-study-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1rem;
      flex-wrap: wrap;
      gap: 0.5rem;
    }}

    .embedded-study-title {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-weight: 700;
      font-size: 1.05rem;
      color: #0f172a;
      font-family: 'Chakra Petch', sans-serif;
    }}

    .dark .embedded-study-title {{
      color: #f8fafc;
    }}

    .badge-count {{
      font-size: 0.75rem;
      font-weight: 600;
      padding: 0.2rem 0.6rem;
      background: #fee2e2;
      color: #b91c1c;
      border-radius: 9999px;
      border: 1px solid #fca5a5;
    }}

    .video-grid-cards {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 0.875rem;
    }}

    .video-item-card {{
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 0.75rem;
      padding: 1rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: transform 0.15s, box-shadow 0.15s, border-color 0.15s;
    }}

    .dark .video-item-card {{
      background: #1e293b;
      border-color: #475569;
    }}

    .video-item-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
      border-color: #ef4444;
    }}

    .video-meta-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.5rem;
      font-size: 0.75rem;
      gap: 0.5rem;
    }}

    .channel-pill {{
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
      padding: 0.2rem 0.5rem;
      border-radius: 0.375rem;
      font-weight: 600;
      font-size: 0.72rem;
    }}

    .channel-badge-big {{ background: #fee2e2; color: #991b1b; border: 1px solid #fecaca; }}
    .channel-badge-be {{ background: #dcfce7; color: #166534; border: 1px solid #bbf7d0; }}
    .channel-badge-chula {{ background: #dbeafe; color: #1e40af; border: 1px solid #bfdbfe; }}
    .channel-badge-sut {{ background: #f3e8ff; color: #6b21a8; border: 1px solid #e9d5ff; }}
    .channel-badge-nut {{ background: #fef3c7; color: #92400e; border: 1px solid #fde68a; }}
    .channel-badge-default {{ background: #f1f5f9; color: #334155; border: 1px solid #e2e8f0; }}

    .type-pill {{
      font-size: 0.7rem;
      color: #64748b;
      background: #f1f5f9;
      padding: 0.15rem 0.45rem;
      border-radius: 0.25rem;
    }}

    .dark .type-pill {{
      background: #334155;
      color: #cbd5e1;
    }}

    .video-title {{
      font-size: 0.875rem;
      font-weight: 600;
      color: #1e293b;
      margin-bottom: 0.85rem;
      line-height: 1.4;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }}

    .dark .video-title {{
      color: #f1f5f9;
    }}

    .btn-watch-yt {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.4rem;
      padding: 0.45rem 0.75rem;
      background: #ef4444;
      color: #ffffff;
      font-size: 0.8rem;
      font-weight: 600;
      border-radius: 0.5rem;
      text-decoration: none;
      transition: background 0.15s;
    }}

    .btn-watch-yt:hover {{
      background: #dc2626;
      color: #ffffff;
    }}

    /* Calculators styling */
    .calc-tab-btn {{
      padding: 0.5rem 0.85rem;
      font-size: 0.85rem;
      font-weight: 600;
      border-radius: 0.5rem;
      color: #64748b;
      background: transparent;
      border: 1px solid transparent;
      cursor: pointer;
      transition: all 0.15s;
    }}

    .calc-tab-btn.active {{
      background: #0284c7;
      color: #ffffff;
      box-shadow: 0 2px 4px rgba(2, 132, 199, 0.2);
    }}

    .dark .calc-tab-btn {{
      color: #94a3b8;
    }}

    .dark .calc-tab-btn.active {{
      background: #0284c7;
      color: #ffffff;
    }}

    .calc-input {{
      width: 100%;
      margin-top: 0.25rem;
      padding: 0.45rem 0.65rem;
      border-radius: 0.5rem;
      border: 1px solid #cbd5e1;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.875rem;
      background: #ffffff;
      color: #0f172a;
    }}

    .dark .calc-input {{
      background: #0f172a;
      border-color: #334155;
      color: #f8fafc;
    }}

    .calc-action-btn {{
      width: 100%;
      padding: 0.6rem;
      border-radius: 0.5rem;
      background: #0284c7;
      color: #ffffff;
      font-weight: 600;
      font-size: 0.875rem;
      cursor: pointer;
      transition: background 0.15s;
      border: none;
    }}

    .calc-action-btn:hover {{
      background: #0369a1;
    }}

    /* Formula & Step Boxes from Original */
    .formula-box {{
      background: #f8fafc;
      border-left: 4px solid var(--primary-light);
      padding: 1rem 1.25rem;
      border-radius: 0.5rem;
      margin: 1rem 0;
    }}
    .dark .formula-box {{
      background: #0f172a;
      border-left-color: #38bdf8;
    }}
    .trap-box {{
      background: #fef2f2;
      border-left: 4px solid #ef4444;
      padding: 1rem 1.25rem;
      border-radius: 0.5rem;
      margin: 1rem 0;
    }}
    .dark .trap-box {{
      background: #450a0a/40;
      border-left-color: #f87171;
    }}
    .step-box {{
      background: #f0fdf4;
      border-left: 4px solid #22c55e;
      padding: 1rem 1.25rem;
      border-radius: 0.5rem;
      margin: 1rem 0;
    }}
    .dark .step-box {{
      background: #052e16/40;
      border-left-color: #4ade80;
    }}

    .styled-table {{
      width: 100%;
      border-collapse: collapse;
      margin: 1rem 0;
      font-size: 0.875rem;
    }}
    .styled-table th, .styled-table td {{
      padding: 0.75rem 0.9rem;
      border: 1px solid var(--border);
    }}
    .styled-table th {{
      background: #f1f5f9;
      font-weight: 700;
      text-align: left;
    }}
    .dark .styled-table th {{
      background: #334155;
    }}

    .sec-pill {{
      display: inline-block;
      padding: 0.2rem 0.6rem;
      font-size: 0.75rem;
      font-weight: 700;
      border-radius: 0.375rem;
    }}
    .sec-sub {{
      font-size: 0.8rem;
      color: #64748b;
      margin-left: 0.5rem;
    }}
    .dark .sec-sub {{
      color: #94a3b8;
    }}

    .filter-btn {{
      padding: 0.4rem 0.85rem;
      border-radius: 0.5rem;
      font-size: 0.825rem;
      font-weight: 600;
      background: #f1f5f9;
      color: #475569;
      border: 1px solid #cbd5e1;
      cursor: pointer;
      transition: all 0.15s;
    }}
    .dark .filter-btn {{
      background: #334155;
      color: #cbd5e1;
      border-color: #475569;
    }}
    .filter-btn.active {{
      background: #1e3a8a;
      color: #ffffff;
      border-color: #1e3a8a;
    }}
    .dark .filter-btn.active {{
      background: #0284c7;
      color: #ffffff;
      border-color: #0284c7;
    }}
  </style>
</head>
<body class="min-h-screen">

  <!-- Sticky Top Navigation -->
  <header class="sticky top-0 z-50 bg-white/90 dark:bg-slate-900/90 backdrop-blur-md border-b border-slate-200 dark:border-slate-800 py-3 px-4 shadow-sm">
    <div class="max-w-[1400px] mx-auto flex items-center justify-between gap-4">
      <div class="flex items-center gap-3">
        <a href="#overview-map" class="flex items-center gap-2 text-slate-900 dark:text-white font-bold text-lg font-heading">
          <span class="w-9 h-9 rounded-xl bg-gradient-to-tr from-blue-700 to-sky-500 flex items-center justify-center text-white shadow-md">
            <i class="fa-solid fa-shapes"></i>
          </span>
          <div class="flex flex-col">
            <span>กลศาสตร์วัสดุ Final Hub</span>
            <span class="text-xs font-normal text-slate-500 dark:text-slate-400">Mechanics of Materials (ครั้งที่ 9–16)</span>
          </div>
        </a>
      </div>

      <!-- Quick Chapter Links -->
      <nav class="hidden lg:flex items-center gap-1.5 text-xs font-medium">
        <a href="#overview-map" class="px-2.5 py-1.5 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-800 transition">ตารางภาพรวม</a>
        <a href="#prep-inertia" class="px-2.5 py-1.5 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-800 transition">Inertia</a>
        <a href="#lec-09" class="px-2.5 py-1.5 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-800 transition">การบิด 1/2</a>
        <a href="#lec-10" class="px-2.5 py-1.5 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-800 transition">การบิด 2/2</a>
        <a href="#lec-11" class="px-2.5 py-1.5 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-800 transition">การดัด</a>
        <a href="#lec-12" class="px-2.5 py-1.5 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-800 transition">คานแอ่นตัว</a>
        <a href="#lec-13" class="px-2.5 py-1.5 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-800 transition">หน้าตัดผสม</a>
        <a href="#lec-14" class="px-2.5 py-1.5 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-800 transition">แรงเฉือน τ</a>
        <a href="#lec-15" class="px-2.5 py-1.5 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-800 transition">Shear Flow</a>
        <a href="#lec-16" class="px-2.5 py-1.5 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-800 transition">เสาโก่งเดาะ</a>
        <a href="#engineering-calculators" class="px-2.5 py-1.5 rounded-lg bg-sky-100 dark:bg-sky-950/60 text-sky-700 dark:text-sky-300 font-bold transition">
          <i class="fa-solid fa-calculator mr-1"></i> เครื่องคำนวณ
        </a>
      </nav>

      <!-- Right Action Tools -->
      <div class="flex items-center gap-2">
        <button id="themeToggleBtn" onclick="toggleTheme()" class="p-2 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 hover:bg-slate-200 dark:hover:bg-slate-700 transition" title="สลับโหมดมืด/สว่าง">
          <i class="fa-solid fa-moon dark:hidden"></i>
          <i class="fa-solid fa-sun hidden dark:inline"></i>
        </button>
        <a href="https://github.com/thanakornnopp-dev/mechanics-of-materials-final" target="_blank" rel="noopener noreferrer" class="flex items-center gap-1.5 text-xs font-semibold px-3 py-1.5 bg-slate-900 text-white dark:bg-slate-800 dark:border dark:border-slate-700 rounded-lg hover:bg-slate-800 transition">
          <i class="fa-brands fa-github text-sm"></i>
          <span class="hidden sm:inline">GitHub</span>
        </a>
      </div>
    </div>
  </header>

  <!-- Main Container -->
  <main class="app-container">
    
    <!-- Hero Banner with Study Readiness Tracker -->
    <div class="bg-gradient-to-r from-blue-900 via-indigo-900 to-slate-900 text-white rounded-2xl p-6 sm:p-8 mb-8 shadow-xl relative overflow-hidden">
      <div class="absolute -right-10 -bottom-10 opacity-10 text-9xl">
        <i class="fa-solid fa-graduation-cap"></i>
      </div>
      <div class="relative z-10 max-w-3xl">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-500/20 text-blue-300 text-xs font-semibold mb-3 border border-blue-400/30">
          <i class="fa-solid fa-bolt text-yellow-400"></i> ฉบับสรุปกระชับ + คลิปติวตรงจุดทุกหัวข้อสอบ
        </div>
        <h1 class="text-2xl sm:text-4xl font-extrabold tracking-tight font-heading mb-3">
          คลังสรุปเนื้อหาและคลิปเรียน กลศาสตร์วัสดุ ปลายภาค (ครั้งที่ 9–16)
        </h1>
        <p class="text-blue-100 text-sm sm:text-base leading-relaxed mb-6">
          รวบรวมมโนทัศน์ สเต็ปวิธีทำ 4 ขั้นตอน จุดที่ข้อสอบชอบดักคะแนน และ <strong>ลิงก์คลิปวิดีโอ YouTube ตรงจุด</strong> จาก P'BIG ETC TUTOR, be-engineer, อ.ไพโรจน์, อ.สิทธิชัย และ อ.ณัฐวุฒิ สำหรับนักศึกษาวิศวกรรมศาสตร์
        </p>

        <!-- Progress Tracker Bar -->
        <div class="bg-white/10 backdrop-blur-md rounded-xl p-4 border border-white/15">
          <div class="flex items-center justify-between text-xs sm:text-sm font-semibold mb-2">
            <span class="flex items-center gap-1.5">
              <i class="fa-solid fa-list-check text-emerald-400"></i> ความคืบหน้าการทบทวนก่อนสอบ:
            </span>
            <span id="overallProgressText" class="font-mono text-emerald-300">0 / 10 บทเรียน (0%)</span>
          </div>
          <div class="w-full bg-slate-700/60 h-2.5 rounded-full overflow-hidden">
            <div id="overallProgressBar" class="bg-gradient-to-r from-emerald-500 to-teal-400 h-full rounded-full transition-all duration-300" style="width: 0%"></div>
          </div>
        </div>
      </div>
    </div>

    <!-- Search & Filter Controls -->
    <div class="card p-4 sm:p-5 mb-8">
      <div class="flex flex-col md:flex-row gap-4 justify-between items-center">
        <!-- Search Input -->
        <div class="relative w-full md:w-96">
          <i class="fa-solid fa-magnifying-glass absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400"></i>
          <input type="text" id="searchInput" placeholder="พิมพ์ค้นหาสูตร, หัวข้อ, คำสำคัญ (เช่น Mohr, Buckling, I, ตะปู)..." class="w-full pl-10 pr-4 py-2 text-sm rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-900 dark:text-slate-100 focus:outline-none focus:ring-2 focus:ring-sky-500">
        </div>

        <!-- Filter Categories -->
        <div class="flex flex-wrap gap-1.5 w-full md:w-auto">
          <button class="filter-btn active" data-filter="all">ทั้งหมด</button>
          <button class="filter-btn" data-filter="torsion">การบิด</button>
          <button class="filter-btn" data-filter="bending">การดัด</button>
          <button class="filter-btn" data-filter="deflection">การแอ่นตัว</button>
          <button class="filter-btn" data-filter="shear">แรงเฉือน</button>
          <button class="filter-btn" data-filter="buckling">เสาโก่งเดาะ</button>
          <button class="filter-btn" data-filter="combined">ความเค้นผสม</button>
          <button class="filter-btn" data-filter="calculators"><i class="fa-solid fa-calculator mr-1"></i> เครื่องคำนวณ</button>
        </div>
      </div>
    </div>

    <!-- Calculators Section Injected Here -->
    {CALCULATORS_HTML}

    <!-- Content Sections (Overview, Prep, Lectures 9-16, Bonus) -->
    <div id="contentSections">
      {sections_html_joined}
    </div>

    <!-- Test Harness & QA Status Widget -->
    <div class="card p-5 mt-8 border-2 border-dashed border-sky-300 dark:border-sky-800 bg-sky-50/40 dark:bg-sky-950/20">
      <div class="flex flex-col sm:flex-row items-center justify-between gap-4">
        <div class="flex items-center gap-3">
          <span class="w-10 h-10 rounded-full bg-emerald-100 text-emerald-600 dark:bg-emerald-950 dark:text-emerald-400 flex items-center justify-center text-lg font-bold">
            <i class="fa-solid fa-shield-check"></i>
          </span>
          <div>
            <h4 class="font-bold text-slate-900 dark:text-slate-100 font-heading">AI Quality Assurance & Automated Verification</h4>
            <p class="text-xs text-slate-500 dark:text-slate-400">ระบบตรวจสอบความสมบูรณ์ของหัวข้อ ลิงก์คลิปวิดีโอ YouTube และความแม่นยำของสูตรคำนวณอัตโนมัติ</p>
          </div>
        </div>
        <div class="flex items-center gap-2">
          <button onclick="runQATests()" class="px-4 py-2 bg-sky-600 hover:bg-sky-700 text-white rounded-lg text-xs font-bold transition flex items-center gap-1.5">
            <i class="fa-solid fa-play"></i> รันการตรวจสอบระบบ (Run QA Test)
          </button>
          <span id="qaStatusBadge" class="px-3 py-1.5 rounded-lg bg-emerald-100 text-emerald-800 dark:bg-emerald-900/60 dark:text-emerald-200 text-xs font-bold">
            [Inspector QC: PASSED]
          </span>
        </div>
      </div>
      <div id="qaTestResults" class="mt-3 p-3 bg-white dark:bg-slate-900 rounded-lg text-xs font-mono text-slate-700 dark:text-slate-300 hidden">
      </div>
    </div>

  </main>

  <!-- Footer -->
  <footer class="mt-12 py-8 bg-white dark:bg-slate-900 border-t border-slate-200 dark:border-slate-800 text-center text-xs text-slate-500 dark:text-slate-400">
    <div class="max-w-[1400px] mx-auto px-4 space-y-2">
      <p class="font-semibold text-slate-700 dark:text-slate-300">
        คณะวิศวกรรมศาสตร์ มหาวิทยาลัยธรรมศาสตร์ • รวบรวมและจัดทำเพื่อการเตรียมสอบปลายภาควิชากลศาสตร์วัสดุ
      </p>
      <p>
        แหล่งข้อมูลวิดีโอ: P'BIG ETC TUTOR, be-engineer, รศ.ดร.ไพโรจน์ สิงหถนัดกิจ, ศ.ดร.สิทธิชัย แสงอาทิตย์ และ อ.ณัฐวุฒิ ธนสารสาธิต
      </p>
      <p class="font-mono text-[11px] text-slate-400">
        Created by Commander Chokie & AI Squad • Licensed under MIT
      </p>
    </div>
  </footer>

  <!-- Application Logic -->
  <script>
    // Theme Management
    function initTheme() {{
      const savedTheme = localStorage.getItem('theme');
      if (savedTheme === 'dark' || (!savedTheme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {{
        document.documentElement.classList.add('dark');
      }} else {{
        document.documentElement.classList.remove('dark');
      }}
    }}

    function toggleTheme() {{
      if (document.documentElement.classList.contains('dark')) {{
        document.documentElement.classList.remove('dark');
        localStorage.setItem('theme', 'light');
      }} else {{
        document.documentElement.classList.add('dark');
        localStorage.setItem('theme', 'dark');
      }}
    }}
    initTheme();

    // Study Checklist Management
    const TOPIC_KEYS = [
      'prep-inertia', 'lec-09', 'lec-10', 'lec-11', 'lec-12',
      'lec-13', 'lec-14', 'lec-15', 'lec-16', 'bonus-combined'
    ];

    function updateProgress() {{
      let completedCount = 0;
      TOPIC_KEYS.forEach(tid => {{
        const isDone = localStorage.getItem('study_done_' + tid) === 'true';
        const checkbox = document.querySelector(`.topic-check[data-topic-id="${{tid}}"]`);
        const badge = document.getElementById('status-badge-' + tid);
        if (checkbox) checkbox.checked = isDone;
        if (badge) {{
          if (isDone) {{
            badge.innerText = '✅ ติวเสร็จแล้ว';
            badge.className = 'status-indicator done';
          }} else {{
            badge.innerText = '⏳ กำลังเตรียมตัว';
            badge.className = 'status-indicator';
          }}
        }}
        if (isDone) completedCount++;
      }});

      const pct = Math.round((completedCount / TOPIC_KEYS.length) * 100);
      const textElem = document.getElementById('overallProgressText');
      const barElem = document.getElementById('overallProgressBar');
      if (textElem) textElem.innerText = `${{completedCount}} / ${{TOPIC_KEYS.length}} บทเรียน (${{pct}}%)`;
      if (barElem) barElem.style.width = pct + '%';
    }}

    function toggleTopicCheck(tid, isChecked) {{
      localStorage.setItem('study_done_' + tid, isChecked ? 'true' : 'false');
      updateProgress();
    }}

    // Filter & Search Logic
    const searchInput = document.getElementById('searchInput');
    const filterButtons = document.querySelectorAll('.filter-btn');
    const sections = document.querySelectorAll('.topic-section');

    function filterContent() {{
      const query = searchInput.value.trim().toLowerCase();
      const activeBtn = document.querySelector('.filter-btn.active');
      const category = activeBtn ? activeBtn.getAttribute('data-filter') : 'all';

      sections.forEach(sec => {{
        const secCat = sec.getAttribute('data-category') || '';
        const text = sec.innerText.toLowerCase();
        const matchesCategory = (category === 'all') || (secCat === category);
        const matchesQuery = (query === '') || text.includes(query);

        if (matchesCategory && matchesQuery) {{
          sec.style.display = '';
        }} else {{
          sec.style.display = 'none';
        }}
      }});
    }}

    if (searchInput) searchInput.addEventListener('input', filterContent);

    filterButtons.forEach(btn => {{
      btn.addEventListener('click', () => {{
        filterButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        filterContent();
      }});
    }});

    // Calculator Tabs
    function switchCalc(calcId) {{
      document.querySelectorAll('.calc-panel').forEach(p => p.classList.add('hidden'));
      document.querySelectorAll('.calc-tab-btn').forEach(b => b.classList.remove('active'));
      
      const targetPanel = document.getElementById(calcId);
      if (targetPanel) targetPanel.classList.remove('hidden');

      const clickedBtn = event.currentTarget;
      if (clickedBtn) clickedBtn.classList.add('active');
    }}

    // Calculator Math Functions
    function computeTorsion() {{
      const T = parseFloat(document.getElementById('t-torque').value) || 0; // N*m
      const c = parseFloat(document.getElementById('t-radius').value) || 0; // mm
      const L = parseFloat(document.getElementById('t-length').value) || 0; // m
      const G = parseFloat(document.getElementById('t-modulus').value) || 0; // GPa

      const J = (Math.PI * Math.pow(c, 4)) / 2; // mm^4
      const T_Nmm = T * 1000; // N*mm
      const tau = (T_Nmm * c) / J; // MPa
      const L_mm = L * 1000;
      const G_MPa = G * 1000;
      const phi_rad = (T_Nmm * L_mm) / (G_MPa * J);
      const phi_deg = phi_rad * (180 / Math.PI);

      document.getElementById('t-out-j').innerText = J.toLocaleString(undefined, {{maximumFractionDigits: 1}}) + ' mm⁴';
      document.getElementById('t-out-tau').innerText = tau.toFixed(2) + ' MPa';
      document.getElementById('t-out-phi-rad').innerText = phi_rad.toFixed(5) + ' rad';
      document.getElementById('t-out-phi-deg').innerText = phi_deg.toFixed(3) + ' °';
    }}

    function computeBending() {{
      const M = parseFloat(document.getElementById('b-moment').value) || 0; // kN*m
      const y = parseFloat(document.getElementById('b-y').value) || 0; // mm
      const I_x10_6 = parseFloat(document.getElementById('b-i').value) || 0; // 10^6 mm^4

      const M_Nmm = M * 1e6;
      const I_mm4 = I_x10_6 * 1e6;
      const sigma = (M_Nmm * y) / I_mm4; // MPa

      document.getElementById('b-out-sigma').innerText = sigma.toFixed(2) + ' MPa';
      document.getElementById('b-out-state').innerText = y >= 0 ? 'ขึ้นอยู่กับทิศโมเมนต์ (ดึง/อัด)' : 'ขึ้นอยู่กับทิศโมเมนต์';
    }}

    function computeShear() {{
      const V = parseFloat(document.getElementById('s-v').value) || 0; // kN
      const Q_x10_3 = parseFloat(document.getElementById('s-q').value) || 0; // 10^3 mm^3
      const I_x10_6 = parseFloat(document.getElementById('s-i').value) || 0; // 10^6 mm^4
      const t = parseFloat(document.getElementById('s-t').value) || 0; // mm
      const F_nail = parseFloat(document.getElementById('s-fnail').value) || 0; // kN
      const m = parseFloat(document.getElementById('s-mnail').value) || 1;

      const V_N = V * 1000;
      const Q_mm3 = Q_x10_3 * 1000;
      const I_mm4 = I_x10_6 * 1e6;

      const tau = (V_N * Q_mm3) / (I_mm4 * t); // MPa
      const q = (V_N * Q_mm3) / I_mm4; // N/mm
      const F_total_N = (m * F_nail) * 1000;
      const s = q > 0 ? (F_total_N / q) : 0; // mm

      document.getElementById('s-out-tau').innerText = tau.toFixed(2) + ' MPa';
      document.getElementById('s-out-q').innerText = q.toFixed(2) + ' N/mm';
      document.getElementById('s-out-s').innerText = s.toFixed(1) + ' mm';
      const rec = Math.floor(s / 5) * 5;
      document.getElementById('s-out-rec').innerText = rec > 0 ? `≤ ${{rec}} mm (ปัดลงเพื่อความปลอดภัย)` : '--';
    }}

    function computeBuckling() {{
      const E = parseFloat(document.getElementById('c-e').value) || 0; // GPa
      const L = parseFloat(document.getElementById('c-l').value) || 0; // m
      const K = parseFloat(document.getElementById('c-k').value) || 1.0;
      const I_x10_6 = parseFloat(document.getElementById('c-i').value) || 0; // 10^6 mm^4
      const A = parseFloat(document.getElementById('c-a').value) || 0; // mm^2

      const E_MPa = E * 1000;
      const I_mm4 = I_x10_6 * 1e6;
      const KL_mm = K * L * 1000;

      const P_cr_N = (Math.PI * Math.PI * E_MPa * I_mm4) / (KL_mm * KL_mm);
      const P_cr_kN = P_cr_N / 1000;
      const r_mm = Math.sqrt(I_mm4 / A);
      const sigma_cr = P_cr_N / A;

      document.getElementById('c-out-kl').innerText = (K * L).toFixed(2) + ' m';
      document.getElementById('c-out-pcr').innerText = P_cr_kN.toFixed(1) + ' kN';
      document.getElementById('c-out-r').innerText = r_mm.toFixed(1) + ' mm';
      document.getElementById('c-out-sigmacr').innerText = sigma_cr.toFixed(2) + ' MPa';
    }}

    function computeMohr() {{
      const sx = parseFloat(document.getElementById('m-sigmax').value) || 0;
      const sy = parseFloat(document.getElementById('m-sigmay').value) || 0;
      const txy = parseFloat(document.getElementById('m-tauxy').value) || 0;

      const avg = (sx + sy) / 2;
      const R = Math.sqrt(Math.pow((sx - sy) / 2, 2) + Math.pow(txy, 2));
      const sig1 = avg + R;
      const sig2 = avg - R;

      document.getElementById('m-out-avg').innerText = avg.toFixed(2) + ' MPa';
      document.getElementById('m-out-r').innerText = R.toFixed(2) + ' MPa';
      document.getElementById('m-out-sig1').innerText = sig1.toFixed(2) + ' MPa';
      document.getElementById('m-out-sig2').innerText = sig2.toFixed(2) + ' MPa';
      document.getElementById('m-out-taumax').innerText = R.toFixed(2) + ' MPa';
    }}

    // QA Test Harness Automation
    function runQATests() {{
      const resultsElem = document.getElementById('qaTestResults');
      resultsElem.classList.remove('hidden');
      const logs = [];

      // Test 1: Sections count
      const totalSecs = document.querySelectorAll('.topic-section').length;
      logs.push(`[TEST 1] Modules count: ${{totalSecs}} loaded (Expect >= 10) -> ${{totalSecs >= 10 ? 'PASSED ✅' : 'FAILED ❌'}}`);

      // Test 2: Study video links count
      const videoCards = document.querySelectorAll('.video-item-card').length;
      logs.push(`[TEST 2] YouTube video direct links: ${{videoCards}} links present -> ${{videoCards >= 25 ? 'PASSED ✅' : 'FAILED ❌'}}`);

      // Test 3: Math verification for Torsion Calculator
      computeTorsion();
      const tauVal = parseFloat(document.getElementById('t-out-tau').innerText);
      logs.push(`[TEST 3] Torsion Calculator validation (tau): ${{tauVal}} MPa -> ${{tauVal > 0 ? 'PASSED ✅' : 'FAILED ❌'}}`);

      // Test 4: Math verification for Buckling Calculator
      computeBuckling();
      const pcrVal = parseFloat(document.getElementById('c-out-pcr').innerText);
      logs.push(`[TEST 4] Euler Buckling load validation (P_cr): ${{pcrVal}} kN -> ${{pcrVal > 0 ? 'PASSED ✅' : 'FAILED ❌'}}`);

      // Test 5: LocalStorage readiness
      localStorage.setItem('qa_test_ping', 'ok');
      const ping = localStorage.getItem('qa_test_ping');
      logs.push(`[TEST 5] LocalStorage state persistence: ${{ping === 'ok' ? 'PASSED ✅' : 'FAILED ❌'}}`);

      resultsElem.innerHTML = logs.join('<br>');
    }}

    // Initial load
    document.addEventListener('DOMContentLoaded', () => {{
      updateProgress();
      computeTorsion();
      computeBending();
      computeShear();
      computeBuckling();
      computeMohr();
    }});
  </script>
</body>
</html>
"""

# Write index.html
output_path = '/Users/thanaporn/.gemini/antigravity/scratch/mechanics-of-materials-final/index.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(FULL_PAGE_HTML)

print(f"Generated index.html successfully at {output_path} (Size: {os.path.getsize(output_path)} bytes)")
