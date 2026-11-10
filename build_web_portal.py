import re
import os

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
        # Channel badge color styling
        ch = l['channel']
        ch_badge_style = "background: #fef2f2; color: #b91c1c; border-color: #fecaca;"
        if "be-engineer" in ch:
            ch_badge_style = "background: #f0fdf4; color: #15803d; border-color: #bbf7d0;"
        elif "ไพโรจน์" in ch:
            ch_badge_style = "background: #eff6ff; color: #1d4ed8; border-color: #bfdbfe;"
        elif "สิทธิชัย" in ch:
            ch_badge_style = "background: #faf5ff; color: #7e22ce; border-color: #e9d5ff;"
        elif "ณัฐวุฒิ" in ch:
            ch_badge_style = "background: #fffbeb; color: #b45309; border-color: #fde68a;"
        
        card = f"""
        <div class="video-card">
          <div class="video-card-top">
            <span class="video-channel" style="{ch_badge_style}"><i class="fa-brands fa-youtube" style="margin-right:4px;"></i>{ch}</span>
            <span class="video-type-badge">{l['type']}</span>
          </div>
          <div class="video-card-title">{l['title']}</div>
          <a href="{l['url']}" target="_blank" rel="noopener noreferrer" class="video-watch-btn">
            <i class="fa-solid fa-play"></i> คลิกเปิดดูคลิปติวใน YouTube
          </a>
        </div>
        """
        cards_html.append(card)
    
    return f"""
    <div class="study-links-container">
      <div class="study-links-header">
        <div class="study-links-title">
          <i class="fa-solid fa-circle-play" style="color: #ef4444; font-size: 1.25rem;"></i>
          <span>คลิปเรียน & โจทย์ตัวอย่างสำหรับหัวข้อนี้ (Direct Learning Links)</span>
        </div>
        <span class="study-links-count">{len(links)} วิดีโอแนะนำ</span>
      </div>
      <div class="video-grid">
        {''.join(cards_html)}
      </div>
    </div>
    """

print("Generator helper ready. Processing sections...")
