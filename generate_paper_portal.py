import os
import json
from make_solid_ja_html import PROBLEMS

print(f"Loaded {len(PROBLEMS)} problems. Generating White Paper Document Layout...")

# Study Links mapping
STUDY_LINKS = {
    "torsion": [
        {"channel": "be-engineer", "title": "ติวสดฟรี Strength - Torsion (การบิด)", "url": "https://www.youtube.com/results?search_query=ติวสดฟรี+Strength+-+Torsion+be-engineer"},
        {"channel": "อ.ไพโรจน์ สิงหถนัดกิจ", "title": "โจทย์ตัวอย่าง Torsion 1-3 & 2-3 (เพลาต่อเฟือง)", "url": "https://www.youtube.com/results?search_query=โจทย์ตัวอย่าง+-+Torsion+Pairod+Singhatanadgid"},
        {"channel": "อ.สิทธิชัย แสงอาทิตย์", "title": "บทที่ 5 การบิด Part 2/2 (Indeterminate)", "url": "https://www.youtube.com/results?search_query=บทที่+5+การบิด+Part+2%2F2+Indeterminate+สิทธิชัย+แสงอาทิตย์"}
    ],
    "bending": [
        {"channel": "be-engineer", "title": "การหา Bending Stress โดยละเอียด", "url": "https://www.youtube.com/results?search_query=การหา+Bending+Stress+โดยละเอียด+be-engineer"},
        {"channel": "อ.ไพโรจน์ สิงหถนัดกิจ", "title": "โจทย์ตัวอย่าง Bending of beam & Transformed Section", "url": "https://www.youtube.com/results?search_query=โจทย์ตัวอย่าง+Bending+of+beam+Pairod+Singhatanadgid"},
        {"channel": "อ.สิทธิชัย แสงอาทิตย์", "title": "บทที่ 6 การดัด (หน้าตัดผสม Transformed Section)", "url": "https://www.youtube.com/results?search_query=14+บทที่+6+การดัด+Part+2%2F2+สิทธิชัย+แสงอาทิตย์"}
    ],
    "deflection": [
        {"channel": "P'BIG ETC TUTOR", "title": "DOUBLE INTEGRATION By P'BIG ETC TUTOR", "url": "https://www.youtube.com/results?search_query=DOUBLE+INTEGRATION+By+P%27BIG+ETC+TUTOR"},
        {"channel": "P'BIG ETC TUTOR", "title": "MOMENT AREA Part 1 & Part 2", "url": "https://www.youtube.com/results?search_query=MOMENT+AREA+P%27BIG+ETC+TUTOR"},
        {"channel": "อ.ไพโรจน์ สิงหถนัดกิจ", "title": "Lecture 18 & 19 Deflection of Beam", "url": "https://www.youtube.com/results?search_query=Deflection+of+Beam+Pairod+Singhatanadgid"}
    ],
    "shear": [
        {"channel": "อ.ไพโรจน์ สิงหถนัดกิจ", "title": "โจทย์ตัวอย่าง Transverse Shear 1-1", "url": "https://www.youtube.com/results?search_query=โจทย์ตัวอย่าง+Transverse+Shear+1-1+Pairod+Singhatanadgid"},
        {"channel": "P'BIG ETC TUTOR", "title": "Shear Center และการหาค่า First Moment Q", "url": "https://www.youtube.com/results?search_query=Shear+Center+P%27BIG+ETC+TUTOR"},
        {"channel": "อ.สิทธิชัย แสงอาทิตย์", "title": "บทที่ 7 การเฉือนตามขวาง [Shear flow & ตะปู]", "url": "https://www.youtube.com/results?search_query=16+บทที่+7+การเฉือนตามขวาง+Shear+flow+สิทธิชัย+แสงอาทิตย์"}
    ],
    "buckling": [
        {"channel": "อ.ไพโรจน์ สิงหถนัดกิจ", "title": "โจทย์ตัวอย่าง Buckling 1-2 & 2-2", "url": "https://www.youtube.com/results?search_query=โจทย์ตัวอย่าง+Buckling+Pairod+Singhatanadgid"},
        {"channel": "อ.สิทธิชัย แสงอาทิตย์", "title": "บทที่ 13 การโก่งเดาะของเสา (Euler Buckling)", "url": "https://www.youtube.com/results?search_query=21+บทที่+13+การโก่งเดาะของเสา+สิทธิชัย+แสงอาทิตย์"}
    ]
}

# Generate Paper Sheets HTML for 10 problems
paper_sheets_html = []
for idx, p in enumerate(PROBLEMS):
    sheet_no = idx + 1
    
    # Scanned images block
    img_tags = []
    for img_name in p["pages"]:
        img_tags.append(f"""
        <div class="scanned-box">
          <div class="text-[11px] text-slate-500 font-mono mb-1"><i class="fa-regular fa-image"></i> ต้นฉบับชีท: {img_name}</div>
          <a href="assets/pages/{img_name}" target="_blank" rel="noopener noreferrer" title="คลิกเพื่อขยายภาพ">
            <img src="assets/pages/{img_name}" alt="ต้นฉบับ {p['num']}" class="w-full rounded border border-slate-300 hover:border-blue-600 transition shadow-sm">
          </a>
        </div>
        """)

    sheet_html = f"""
    <!-- Paper Sheet {sheet_no} -->
    <article class="paper-sheet" id="{p['id']}">
      <!-- Sheet Header -->
      <div class="paper-header">
        <div>
          <span class="paper-course-badge">CE211 MECHANICS OF MATERIALS • FINAL EXAM PREPARATION</span>
          <h2 class="paper-title mt-1">
            <span class="text-blue-800 font-mono">[{p['num']}]</span> {p['topic']}
          </h2>
        </div>
        <div class="paper-page-num text-right">
          <span class="text-xs font-mono font-bold text-slate-400">SHEET {sheet_no:02d} / 10</span>
          <div class="text-[11px] text-slate-500 font-sans">อ้างอิงชีทหน้า {', '.join([x.replace('page_', '').replace('.png', '') for x in p['pages']])}</div>
        </div>
      </div>

      <!-- Problem Overview Note -->
      <div class="paper-desc mb-5">
        <strong>📌 ภาพรวมโจทย์:</strong> {p['summary']}
      </div>

      <!-- Step 1: Given -->
      <section class="paper-step-card step-given mb-5">
        <h3 class="step-heading text-slate-800">
          <i class="fa-solid fa-clipboard-check text-blue-700 mr-1.5"></i> ขั้นตอนที่ 1: สิ่งที่โจทย์กำหนดและพารามิเตอร์ (Given Parameters & Geometry)
        </h3>
        <div class="step-content text-slate-700 whitespace-pre-line text-[15px]">
          {p['given'].strip()}
        </div>
      </section>

      <!-- Step 2: Solution Derivation -->
      <section class="paper-step-card step-solution mb-5">
        <h3 class="step-heading text-slate-900">
          <i class="fa-solid fa-calculator text-emerald-700 mr-1.5"></i> ขั้นตอนที่ 2 & 3: การพิสูจน์และแสดงวิธีทำทีละบรรทัด (Step-by-Step LaTeX Derivation)
        </h3>
        <div class="math-content overflow-x-auto py-2 text-slate-900">
          {p['solution'].strip()}
        </div>
      </section>

      <!-- Step 3: First Principles & Exam Trap -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-5">
        <!-- Principles -->
        <div class="paper-step-card step-principle">
          <h4 class="font-bold text-blue-900 text-sm mb-1.5 flex items-center gap-1.5">
            <i class="fa-regular fa-lightbulb text-amber-500"></i> มโนทัศน์ & เหตุผลทางฟิสิกส์ (First Principles)
          </h4>
          <p class="text-[14px] text-slate-700 leading-relaxed">
            {p['first_principles']}
          </p>
        </div>

        <!-- Exam Trap -->
        <div class="paper-step-card step-trap">
          <h4 class="font-bold text-rose-900 text-sm mb-1.5 flex items-center gap-1.5">
            <i class="fa-solid fa-triangle-exclamation text-rose-600"></i> จุดดักคะแนนในห้องสอบ (Exam Trap Alert)
          </h4>
          <p class="text-[14px] text-rose-950 leading-relaxed">
            {p['exam_trap']}
          </p>
        </div>
      </div>

      <!-- Original Handwritten Scan Accordion -->
      <div class="paper-scan-accordion pt-3 border-t border-slate-200">
        <button onclick="toggleSheetScan('{p['id']}')" class="btn-toggle-scan">
          <i class="fa-regular fa-file-image text-slate-600"></i>
          <span>คลิกเพื่อดูรูปสแกนชีทลายมือต้นฉบับ ({len(p['pages'])} หน้า)</span>
          <i class="fa-solid fa-chevron-down text-xs ml-1" id="chevron-{p['id']}"></i>
        </button>
        <div id="scan-container-{p['id']}" class="hidden mt-3 grid grid-cols-1 md:grid-cols-2 gap-3 p-3 bg-slate-50 rounded border border-slate-200">
          {''.join(img_tags)}
        </div>
      </div>

      <!-- Sheet Footer -->
      <div class="paper-footer mt-6 pt-3 border-t border-slate-200 flex justify-between items-center text-xs text-slate-400">
        <span>ภาควิชาวิศวกรรมโยธา คณะวิศวกรรมศาสตร์ มหาวิทยาลัยธรรมศาสตร์</span>
        <span>หน้า {sheet_no}</span>
      </div>
    </article>
    """
    paper_sheets_html.append(sheet_html)

ALL_SHEETS_JOINED = "\n\n".join(paper_sheets_html)

# Build Full HTML with White Paper Layout
HTML_PAGE = f"""<!DOCTYPE html>
<html lang="th" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>กลศาสตร์วัสดุ (Mechanics of Materials) - คัมภีร์สรุปเตรียมสอบปลายภาค & เฉลยชีท Solid Ja E Here</title>
  
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  
  <!-- FontAwesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
  
  <!-- Google Fonts: Sarabun, Chakra Petch & JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@500;600;700&family=JetBrains+Mono:wght@400;500;600;700&family=Sarabun:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
  
  <!-- MathJax 3 LaTeX Math Engine -->
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
    /* White Paper Aesthetic Standards */
    body {{
      background-color: #e2e8f0; /* Drafting desk neutral background */
      color: #0f172a;
      font-family: 'Sarabun', sans-serif;
      line-height: 1.75;
      font-size: 16px;
      -webkit-font-smoothing: antialiased;
    }}

    h1, h2, h3, h4, .font-heading {{
      font-family: 'Chakra Petch', sans-serif;
    }}

    .font-mono, code, pre {{
      font-family: 'JetBrains Mono', monospace;
    }}

    /* Paper Page Container */
    .paper-sheet {{
      background: #ffffff;
      max-width: 900px;
      margin: 2.5rem auto;
      padding: 3.5rem 3.5rem;
      border-radius: 4px;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.06), 0 0 0 1px rgba(0, 0, 0, 0.08);
      position: relative;
      border-top: 6px solid #1e3a8a; /* Engineering Dark Blue Header */
    }}

    @media (max-width: 768px) {{
      .paper-sheet {{
        padding: 2rem 1.25rem;
        margin: 1rem auto;
      }}
    }}

    /* Paper Sheet Header */
    .paper-header {{
      border-bottom: 2px solid #0f172a;
      padding-bottom: 1rem;
      margin-bottom: 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      flex-wrap: wrap;
      gap: 0.5rem;
    }}

    .paper-course-badge {{
      display: inline-block;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.72rem;
      font-weight: 700;
      color: #1e3a8a;
      letter-spacing: 0.05em;
    }}

    .paper-title {{
      font-size: 1.35rem;
      font-weight: 700;
      color: #0f172a;
      line-height: 1.3;
    }}

    .paper-desc {{
      background: #f8fafc;
      border-left: 3px solid #64748b;
      padding: 0.65rem 1rem;
      font-size: 0.925rem;
      color: #334155;
    }}

    /* Step Cards */
    .paper-step-card {{
      padding: 1.15rem 1.25rem;
      border-radius: 6px;
      border: 1px solid #e2e8f0;
    }}

    .step-given {{
      background: #f8fafc;
      border-left: 4px solid #3b82f6;
    }}

    .step-solution {{
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-left: 4px solid #10b981;
    }}

    .step-principle {{
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      border-left: 4px solid #2563eb;
    }}

    .step-trap {{
      background: #fffbeb;
      border: 1px solid #fde68a;
      border-left: 4px solid #f59e0b;
    }}

    .step-heading {{
      font-size: 0.95rem;
      font-weight: 700;
      margin-bottom: 0.65rem;
      font-family: 'Chakra Petch', sans-serif;
    }}

    /* Scanned image preview button */
    .btn-toggle-scan {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      font-size: 0.8rem;
      font-weight: 600;
      color: #475569;
      background: #f1f5f9;
      padding: 0.4rem 0.85rem;
      border-radius: 4px;
      border: 1px solid #cbd5e1;
      cursor: pointer;
      transition: background 0.15s, color 0.15s;
    }}

    .btn-toggle-scan:hover {{
      background: #e2e8f0;
      color: #0f172a;
    }}

    /* Print media optimization */
    @media print {{
      body {{
        background: #ffffff !important;
        color: #000000 !important;
        font-size: 14px;
      }}
      .no-print, header, .sticky-nav, footer {{
        display: none !important;
      }}
      .paper-sheet {{
        box-shadow: none !important;
        border: none !important;
        border-top: 2px solid #000000 !important;
        margin: 0 !important;
        padding: 1.5cm 1cm !important;
        page-break-after: always;
        max-width: 100% !important;
      }}
    }}
  </style>
</head>
<body class="min-h-screen pb-16">

  <!-- Sticky Top Quick-Navigation Desk -->
  <header class="sticky top-0 z-50 bg-slate-900 text-white shadow-md border-b border-slate-800 py-2.5 px-4 no-print">
    <div class="max-w-[1200px] mx-auto flex items-center justify-between gap-4">
      <div class="flex items-center gap-3">
        <span class="w-8 h-8 rounded bg-blue-600 flex items-center justify-center text-white font-bold text-sm shadow">
          <i class="fa-solid fa-file-lines"></i>
        </span>
        <div>
          <h1 class="font-heading font-bold text-sm sm:text-base tracking-tight leading-tight">
            คัมภีร์แผ่นกระดาษข้อสอบ กลศาสตร์วัสดุ (Solid Ja E Here)
          </h1>
          <p class="text-[11px] text-slate-400 font-sans">
            ถอดรหัสเฉลยข้อสอบ 21 หน้าเต็ม • สเต็ปวิธีทำคณิตศาสตร์ $\LaTeX$ ชัดเจน 100%
          </p>
        </div>
      </div>

      <!-- Quick Nav Buttons -->
      <div class="flex items-center gap-2">
        <a href="#study-schedule" class="px-2.5 py-1.5 rounded bg-amber-500 hover:bg-amber-600 text-slate-950 font-bold text-xs transition flex items-center gap-1">
          <i class="fa-solid fa-calendar-check"></i> ตารางอ่านหนังสือ 7 วัน
        </a>
        <button onclick="window.print()" class="px-2.5 py-1.5 rounded bg-slate-800 hover:bg-slate-700 text-white font-medium text-xs transition border border-slate-700 flex items-center gap-1" title="พิมพ์เป็นเอกสาร PDF">
          <i class="fa-solid fa-print"></i> พิมพ์ A4 (PDF)
        </button>
        <a href="https://github.com/thanakornnopp-dev/mechanics-of-materials-final" target="_blank" rel="noopener noreferrer" class="px-2.5 py-1.5 rounded bg-slate-800 hover:bg-slate-700 text-white font-medium text-xs transition border border-slate-700 flex items-center gap-1">
          <i class="fa-brands fa-github"></i> GitHub
        </a>
      </div>
    </div>
  </header>

  <!-- Main Container holding paper sheets -->
  <main class="max-w-[1200px] mx-auto px-3 sm:px-6 mt-6">

    <!-- Paper Sheet: Cover & Quick Jump Directory -->
    <article class="paper-sheet mb-10">
      <div class="text-center border-b-2 border-slate-900 pb-6 mb-6">
        <div class="inline-block px-3 py-1 bg-slate-100 text-slate-800 rounded text-xs font-mono font-bold mb-2 border border-slate-300">
          FACULTY OF ENGINEERING • THAMMASAT UNIVERSITY
        </div>
        <h1 class="text-2xl sm:text-4xl font-extrabold text-slate-950 font-heading mb-2">
          คัมภีร์สรุปเตรียมสอบปลายภาค กลศาสตร์วัสดุ
        </h1>
        <p class="text-sm sm:text-base text-slate-600 max-w-2xl mx-auto">
          ถอดรหัสเฉลยข้อสอบจริงจากชีท <strong>"Solid Ja E Here-" (21 หน้าเต็ม)</strong> แปลงเป็นสูตรคณิตศาสตร์ $\LaTeX$ ละเอียดทุกบรรทัด พร้อมจุดดักคะแนนและภาพสแกนต้นฉบับ
        </p>
      </div>

      <!-- Quick Jump Table -->
      <h3 class="font-heading font-bold text-base text-slate-900 mb-3 flex items-center gap-2">
        <i class="fa-solid fa-list-ol text-blue-700"></i> สารบัญข้อสอบแม่บททั้ง 10 ข้อ (คลิกเพื่อกระโดดไปยังแผ่นนั้นได้ทันที)
      </h3>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 text-xs sm:text-sm font-sans mb-6">
        <a href="#prob-01" class="p-2.5 rounded bg-slate-50 hover:bg-blue-50 border border-slate-200 transition flex items-center justify-between">
          <span><strong>ข้อ 1:</strong> การบิดเพลาขั้น & ระบบเฟืองทด</span>
          <span class="text-blue-700 font-mono font-bold text-xs">Sheet 01 &rarr;</span>
        </a>
        <a href="#prob-02" class="p-2.5 rounded bg-slate-50 hover:bg-blue-50 border border-slate-200 transition flex items-center justify-between">
          <span><strong>ข้อ 2:</strong> การบิดอินดีเทอร์มิเนต ยึดแน่นหัวท้าย</span>
          <span class="text-blue-700 font-mono font-bold text-xs">Sheet 02 &rarr;</span>
        </a>
        <a href="#prob-03" class="p-2.5 rounded bg-slate-50 hover:bg-blue-50 border border-slate-200 transition flex items-center justify-between">
          <span><strong>ข้อ 3:</strong> เพลาสวมซ้อนกัน (แกนเหล็ก-ปลอกทองเหลือง)</span>
          <span class="text-blue-700 font-mono font-bold text-xs">Sheet 03 &rarr;</span>
        </a>
        <a href="#prob-04" class="p-2.5 rounded bg-slate-50 hover:bg-blue-50 border border-slate-200 transition flex items-center justify-between">
          <span><strong>ข้อ 4:</strong> การออกแบบเพลาตัน vs เพลากลวง</span>
          <span class="text-blue-700 font-mono font-bold text-xs">Sheet 04 &rarr;</span>
        </a>
        <a href="#prob-05" class="p-2.5 rounded bg-slate-50 hover:bg-blue-50 border border-slate-200 transition flex items-center justify-between">
          <span><strong>ข้อ 5:</strong> ความเค้นดัดในคานหน้าตัดไม่สมมาตร (ตัว T / กล่อง)</span>
          <span class="text-blue-700 font-mono font-bold text-xs">Sheet 05 &rarr;</span>
        </a>
        <a href="#prob-06" class="p-2.5 rounded bg-slate-50 hover:bg-blue-50 border border-slate-200 transition flex items-center justify-between">
          <span><strong>ข้อ 6:</strong> การแอ่นตัวของคาน Double Integration</span>
          <span class="text-blue-700 font-mono font-bold text-xs">Sheet 06 &rarr;</span>
        </a>
        <a href="#prob-07" class="p-2.5 rounded bg-slate-50 hover:bg-blue-50 border border-slate-200 transition flex items-center justify-between">
          <span><strong>ข้อ 7:</strong> คานหน้าตัดผสมไม้ประกบเหล็ก ($b' = nb$)</span>
          <span class="text-blue-700 font-mono font-bold text-xs">Sheet 07 &rarr;</span>
        </a>
        <a href="#prob-08" class="p-2.5 rounded bg-slate-50 hover:bg-blue-50 border border-slate-200 transition flex items-center justify-between">
          <span><strong>ข้อ 8:</strong> แรงเฉือนตามขวางและการกระโดดของ $\\tau$</span>
          <span class="text-blue-700 font-mono font-bold text-xs">Sheet 08 &rarr;</span>
        </a>
        <a href="#prob-09" class="p-2.5 rounded bg-slate-50 hover:bg-blue-50 border border-slate-200 transition flex items-center justify-between">
          <span><strong>ข้อ 9:</strong> การเฉือนไหลและระยะห่างตะปูยึดแผ่นไม้</span>
          <span class="text-blue-700 font-mono font-bold text-xs">Sheet 09 &rarr;</span>
        </a>
        <a href="#prob-10" class="p-2.5 rounded bg-slate-50 hover:bg-blue-50 border border-slate-200 transition flex items-center justify-between">
          <span><strong>ข้อ 10:</strong> การโก่งเดาะของเสาอุดมคติ Euler Buckling 2 แกน</span>
          <span class="text-blue-700 font-mono font-bold text-xs">Sheet 10 &rarr;</span>
        </a>
      </div>

      <!-- Quick Tips -->
      <div class="p-4 bg-blue-50 rounded border border-blue-200 text-xs text-blue-900 leading-relaxed">
        <strong>💡 คำแนะนำในการอ่าน:</strong> แต่ละแผ่นพิมพ์แยกเป็นข้ออย่างชัดเจนตามมาตรฐาน 4 ขั้นตอนของอาจารย์ สามารถกดปุ่มด้านล่างเพื่อเปิดดูภาพสแกนชีทลายมือต้นฉบับประกอบได้ตลอดเวลา
      </div>
    </article>

    <!-- Paper Sheet: 7-Day Sprint Study Schedule -->
    <article class="paper-sheet mb-10" id="study-schedule">
      <div class="paper-header">
        <div>
          <span class="paper-course-badge">STRATEGIC STUDY PLAN • 7-DAY REVISION SPRINT</span>
          <h2 class="paper-title mt-1">
            <i class="fa-solid fa-calendar-days text-amber-600 mr-1.5"></i> ตารางอ่านหนังสือและพิชิตข้อสอบ 7 วัน
          </h2>
        </div>
        <div class="paper-page-num text-right">
          <span class="text-xs font-mono font-bold text-slate-400">PLANNER</span>
        </div>
      </div>

      <p class="text-sm text-slate-600 mb-5">
        แผนอ่านหนังสือแบบเข้มข้น 7 วัน แบ่งเวลาวันละ 2.5–3 ชั่วโมง พร้อมคลิปวิดีโอที่ต้องดูและโจทย์ที่ต้องทำให้ได้:
      </p>

      <div class="space-y-3.5 text-xs sm:text-sm">
        
        <div class="p-3.5 bg-slate-50 rounded border border-slate-200 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2">
          <div>
            <div class="font-bold text-blue-900">DAY 1: ปูพื้นฐาน Inertia & การบิดเพลาขั้น (โจทย์ข้อ 1)</div>
            <div class="text-slate-600 text-xs mt-0.5">หาแกนสะเทิน NA, โมเมนต์ความเฉื่อย $I$, ตัด FBD หาแรงบิดภายใน และอัตราทดฟันเฟือง</div>
            <div class="mt-1 flex gap-2">
              <a href="https://www.youtube.com/results?search_query=Centroid+P%27BIG+ETC+TUTOR" target="_blank" class="text-red-600 hover:underline"><i class="fa-brands fa-youtube"></i> Centroid P'BIG</a>
              <a href="https://www.youtube.com/results?search_query=ติวสดฟรี+Strength+-+Torsion+be-engineer" target="_blank" class="text-red-600 hover:underline"><i class="fa-brands fa-youtube"></i> Torsion be-engineer</a>
            </div>
          </div>
          <label class="flex items-center gap-1.5 cursor-pointer font-bold text-slate-700">
            <input type="checkbox" class="w-4 h-4 rounded text-blue-600" onchange="localStorage.setItem('sprint_d1', this.checked)">
            <span>เสร็จแล้ว</span>
          </label>
        </div>

        <div class="p-3.5 bg-slate-50 rounded border border-slate-200 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2">
          <div>
            <div class="font-bold text-blue-900">DAY 2: อินดีเทอร์มิเนตการบิด & เพลาสวมซ้อน (โจทย์ข้อ 2 & 3)</div>
            <div class="text-slate-600 text-xs mt-0.5">สมการ Compatibility $\\phi_{{A/D}} = 0$ และเพลาแกนเหล็ก-ปลอกทองเหลือง $\\phi_s = \\phi_b$</div>
            <div class="mt-1 flex gap-2">
              <a href="https://www.youtube.com/results?search_query=บทที่+5+การบิด+Part+2%2F2+Indeterminate+สิทธิชัย+แสงอาทิตย์" target="_blank" class="text-red-600 hover:underline"><i class="fa-brands fa-youtube"></i> Indeterminate อ.สิทธิชัย</a>
            </div>
          </div>
          <label class="flex items-center gap-1.5 cursor-pointer font-bold text-slate-700">
            <input type="checkbox" class="w-4 h-4 rounded text-blue-600" onchange="localStorage.setItem('sprint_d2', this.checked)">
            <span>เสร็จแล้ว</span>
          </label>
        </div>

        <div class="p-3.5 bg-slate-50 rounded border border-slate-200 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2">
          <div>
            <div class="font-bold text-blue-900">DAY 3: ความเค้นดัด & คานหน้าตัดผสมไม้ประกบเหล็ก (โจทย์ข้อ 5 & 7)</div>
            <div class="text-slate-600 text-xs mt-0.5">สูตร $\\sigma = My/I$, การแปลงความกว้าง $b' = nb$ (ห้ามเปลี่ยนความสูง) และคูณ $n$ กลับในเหล็ก</div>
            <div class="mt-1 flex gap-2">
              <a href="https://www.youtube.com/results?search_query=การหา+Bending+Stress+โดยละเอียด+be-engineer" target="_blank" class="text-red-600 hover:underline"><i class="fa-brands fa-youtube"></i> Bending be-engineer</a>
              <a href="https://www.youtube.com/results?search_query=โจทย์ตัวอย่าง+Bending+of+beam+Pairod+Singhatanadgid" target="_blank" class="text-red-600 hover:underline"><i class="fa-brands fa-youtube"></i> หน้าตัดผสม อ.ไพโรจน์</a>
            </div>
          </div>
          <label class="flex items-center gap-1.5 cursor-pointer font-bold text-slate-700">
            <input type="checkbox" class="w-4 h-4 rounded text-blue-600" onchange="localStorage.setItem('sprint_d3', this.checked)">
            <span>เสร็จแล้ว</span>
          </label>
        </div>

        <div class="p-3.5 bg-slate-50 rounded border border-slate-200 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2">
          <div>
            <div class="font-bold text-blue-900">DAY 4: การแอ่นตัวของคาน Double Integration (โจทย์ข้อ 6)</div>
            <div class="text-slate-600 text-xs mt-0.5">ตั้งสมการ $EI v''(x) = M(x)$, แทนเงื่อนไขขอบเขตหา $C_1, C_2$ และทฤษฎี Moment-Area</div>
            <div class="mt-1 flex gap-2">
              <a href="https://www.youtube.com/results?search_query=DOUBLE+INTEGRATION+By+P%27BIG+ETC+TUTOR" target="_blank" class="text-red-600 hover:underline"><i class="fa-brands fa-youtube"></i> Double Integration P'BIG</a>
              <a href="https://www.youtube.com/results?search_query=Deflection+of+Beam+Pairod+Singhatanadgid" target="_blank" class="text-red-600 hover:underline"><i class="fa-brands fa-youtube"></i> Deflection อ.ไพโรจน์</a>
            </div>
          </div>
          <label class="flex items-center gap-1.5 cursor-pointer font-bold text-slate-700">
            <input type="checkbox" class="w-4 h-4 rounded text-blue-600" onchange="localStorage.setItem('sprint_d4', this.checked)">
            <span>เสร็จแล้ว</span>
          </label>
        </div>

        <div class="p-3.5 bg-slate-50 rounded border border-slate-200 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2">
          <div>
            <div class="font-bold text-blue-900">DAY 5: แรงเฉือนตามขวาง & ระยะห่างตะปู (โจทย์ข้อ 8 & 9)</div>
            <div class="text-slate-600 text-xs mt-0.5">สูตร $\\tau = VQ/It$ การกระโดดของ $\\tau$ ในเอว, Shear Flow $q = VQ/I$, และระยะตะปู $s \\le mF/q$ (ปัดเศษลง)</div>
            <div class="mt-1 flex gap-2">
              <a href="https://www.youtube.com/results?search_query=Shear+Center+P%27BIG+ETC+TUTOR" target="_blank" class="text-red-600 hover:underline"><i class="fa-brands fa-youtube"></i> Shear Center P'BIG</a>
              <a href="https://www.youtube.com/results?search_query=16+บทที่+7+การเฉือนตามขวาง+Shear+flow+สิทธิชัย+แสงอาทิตย์" target="_blank" class="text-red-600 hover:underline"><i class="fa-brands fa-youtube"></i> Shear Flow อ.สิทธิชัย</a>
            </div>
          </div>
          <label class="flex items-center gap-1.5 cursor-pointer font-bold text-slate-700">
            <input type="checkbox" class="w-4 h-4 rounded text-blue-600" onchange="localStorage.setItem('sprint_d5', this.checked)">
            <span>เสร็จแล้ว</span>
          </label>
        </div>

        <div class="p-3.5 bg-slate-50 rounded border border-slate-200 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2">
          <div>
            <div class="font-bold text-blue-900">DAY 6: เสาโก่งเดาะออยเลอร์ & วงกลมมอร์ (โจทย์ข้อ 10)</div>
            <div class="text-slate-600 text-xs mt-0.5">สูตร Euler Buckling เช็ก 2 แกน ($x, y$) อัตราส่วนความชะลูด $\\lambda = KL/r$ และทบทวน Combined Stress</div>
            <div class="mt-1 flex gap-2">
              <a href="https://www.youtube.com/results?search_query=โจทย์ตัวอย่าง+Buckling+Pairod+Singhatanadgid" target="_blank" class="text-red-600 hover:underline"><i class="fa-brands fa-youtube"></i> Buckling อ.ไพโรจน์</a>
              <a href="https://www.youtube.com/results?search_query=การใช้+Mohr%27s+Circle+หา+Principal+Stress+be-engineer" target="_blank" class="text-red-600 hover:underline"><i class="fa-brands fa-youtube"></i> Mohr's Circle be-engineer</a>
            </div>
          </div>
          <label class="flex items-center gap-1.5 cursor-pointer font-bold text-slate-700">
            <input type="checkbox" class="w-4 h-4 rounded text-blue-600" onchange="localStorage.setItem('sprint_d6', this.checked)">
            <span>เสร็จแล้ว</span>
          </label>
        </div>

        <div class="p-4 bg-amber-50 rounded border border-amber-300 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2">
          <div>
            <div class="font-bold text-amber-950 text-base">DAY 7 (FINAL REVIEW): ซ้อมสอบเสมือนจริง 3 ชั่วโมงเต็ม</div>
            <div class="text-amber-900 text-xs mt-0.5">ปิดตำราจับเวลาทำโจทย์ทั้ง 10 ข้อในชีท ตรวจสอบเครื่องหมายดึง/อัด และหน่วยวิศวกรรมให้ครบถ้วน</div>
          </div>
          <label class="flex items-center gap-1.5 cursor-pointer font-bold text-amber-950">
            <input type="checkbox" class="w-5 h-5 rounded text-amber-600" onchange="localStorage.setItem('sprint_d7', this.checked)">
            <span>พร้อมลุยสอบ 100%!</span>
          </label>
        </div>

      </div>
    </article>

    <!-- The 10 Paper Sheets -->
    {ALL_SHEETS_JOINED}

  </main>

  <!-- Clean Footer -->
  <footer class="mt-16 text-center text-xs text-slate-500 no-print">
    <div class="max-w-[900px] mx-auto border-t border-slate-300 pt-6">
      <p class="font-semibold text-slate-700">
        คณะวิศวกรรมศาสตร์ มหาวิทยาลัยธรรมศาสตร์ • CE211 กลศาสตร์วัสดุ (Mechanics of Materials)
      </p>
      <p class="mt-1">
        จัดทำและเรียบเรียงใหม่อัตโนมัติด้วยระบบ White Paper Document Standard • ปรับปรุงล่าสุด 2026
      </p>
    </div>
  </footer>

  <!-- Script for Toggling Original Scanned Sheets -->
  <script>
    function toggleSheetScan(probId) {{
      const container = document.getElementById('scan-container-' + probId);
      const chevron = document.getElementById('chevron-' + probId);
      if (container) {{
        if (container.classList.contains('hidden')) {{
          container.classList.remove('hidden');
          if (chevron) chevron.className = 'fa-solid fa-chevron-up text-xs ml-1';
        }} else {{
          container.classList.add('hidden');
          if (chevron) chevron.className = 'fa-solid fa-chevron-down text-xs ml-1';
        }}
      }}
    }}

    // Restore checkboxes on page load
    document.addEventListener('DOMContentLoaded', () => {{
      for (let i = 1; i <= 7; i++) {{
        const isChecked = localStorage.getItem('sprint_d' + i) === 'true';
        const cb = document.querySelector(`input[onchange*="sprint_d${{i}}"]`);
        if (cb) cb.checked = isChecked;
      }}
    }});
  </script>
</body>
</html>
"""

# Write to index.html
output_file = '/Users/thanaporn/.gemini/antigravity/scratch/mechanics-of-materials-final/index.html'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(HTML_PAGE)

print(f"✅ Generated White Paper Document Portal successfully! Size: {os.path.getsize(output_file)} bytes")
