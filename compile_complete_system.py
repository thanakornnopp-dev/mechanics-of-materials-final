import os
import re
import json
from make_solid_ja_html import PROBLEMS

# Load current index.html
with open('/Users/thanaporn/.gemini/antigravity/scratch/mechanics-of-materials-final/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Build HTML for Solid Ja E Here Workbook Section
prob_cards_html = []
for p in PROBLEMS:
    img_tags = []
    for img_name in p["pages"]:
        img_tags.append(f"""
        <div class="scanned-page-box">
          <div class="text-xs text-slate-500 font-mono mb-1"><i class="fa-solid fa-file-image mr-1"></i> ต้นฉบับชีท: {img_name}</div>
          <a href="assets/pages/{img_name}" target="_blank" rel="noopener noreferrer" title="คลิกเพื่อดูภาพขนาดเต็ม">
            <img src="assets/pages/{img_name}" alt="ต้นฉบับ {p['num']}" class="rounded-lg border border-slate-300 dark:border-slate-700 shadow-sm hover:shadow-md transition max-h-96 object-contain bg-white">
          </a>
        </div>
        """)
    images_block = f"""
    <div class="mt-4 pt-4 border-t border-slate-200 dark:border-slate-700">
      <button onclick="toggleScannedImages('{p['id']}')" class="px-3 py-1.5 rounded-lg bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-300 text-xs font-semibold flex items-center gap-1.5 transition">
        <i class="fa-solid fa-image text-amber-500"></i>
        <span>ดูรูปต้นฉบับลายมือชีท Solid Ja E Here ({len(p['pages'])} หน้า)</span>
        <i class="fa-solid fa-chevron-down text-[10px] ml-1" id="chevron-{p['id']}"></i>
      </button>
      <div id="images-{p['id']}" class="hidden mt-3 grid grid-cols-1 md:grid-cols-2 gap-3 p-3 bg-slate-50 dark:bg-slate-900/60 rounded-xl border border-slate-200 dark:border-slate-700">
        {''.join(img_tags)}
      </div>
    </div>
    """

    card_html = f"""
    <div class="solid-prob-card bg-white dark:bg-slate-800 rounded-2xl p-6 border border-slate-200 dark:border-slate-700 shadow-sm mb-6" id="{p['id']}">
      <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <div class="flex items-center gap-2">
          <span class="px-3 py-1 rounded-full bg-rose-100 dark:bg-rose-950/80 text-rose-700 dark:text-rose-300 text-xs font-bold font-mono">
            {p['num']}
          </span>
          <h3 class="text-lg sm:text-xl font-bold text-slate-900 dark:text-white font-heading">
            {p['topic']}
          </h3>
        </div>
        <span class="text-xs text-slate-500 dark:text-slate-400 font-mono">
          <i class="fa-regular fa-bookmark mr-1 text-sky-500"></i> ชีทหน้า {', '.join([x.replace('page_', '').replace('.png', '') for x in p['pages']])}
        </span>
      </div>

      <p class="text-sm text-slate-600 dark:text-slate-300 mb-4 leading-relaxed">
        {p['summary']}
      </p>

      <!-- Given Box -->
      <div class="formula-box mb-4 text-xs sm:text-sm">
        <div class="font-bold text-sky-800 dark:text-sky-300 mb-1 flex items-center gap-1.5">
          <i class="fa-solid fa-clipboard-list"></i> ข้อมูลที่โจทย์กำหนด (Given Parameters & Geometry)
        </div>
        <div class="text-slate-700 dark:text-slate-300 font-sans whitespace-pre-line">
          {p['given'].strip()}
        </div>
      </div>

      <!-- Step-by-Step LaTeX Solution -->
      <div class="step-box mb-4 overflow-x-auto text-xs sm:text-sm">
        <div class="font-bold text-emerald-800 dark:text-emerald-300 mb-2 flex items-center gap-1.5">
          <i class="fa-solid fa-square-root-variable"></i> ขั้นตอนการพิสูจน์และคำนวณละเอียด (Step-by-Step LaTeX Solution)
        </div>
        <div class="text-slate-800 dark:text-slate-100 font-mono">
          {p['solution'].strip()}
        </div>
      </div>

      <!-- First Principles & Trap Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs sm:text-sm">
        <div class="p-3.5 bg-blue-50/70 dark:bg-blue-950/30 rounded-xl border border-blue-200 dark:border-blue-900/40">
          <div class="font-bold text-blue-900 dark:text-blue-300 mb-1 flex items-center gap-1">
            <i class="fa-regular fa-lightbulb text-amber-500"></i> มโนทัศน์ & เหตุผลทางฟิสิกส์ (First Principles)
          </div>
          <p class="text-slate-700 dark:text-slate-300 text-xs leading-relaxed">
            {p['first_principles']}
          </p>
        </div>
        <div class="p-3.5 bg-rose-50/70 dark:bg-rose-950/30 rounded-xl border border-rose-200 dark:border-rose-900/40">
          <div class="font-bold text-rose-900 dark:text-rose-300 mb-1 flex items-center gap-1">
            <i class="fa-solid fa-triangle-exclamation text-rose-500"></i> จุดดักคะแนนในห้องสอบ (Exam Trap Alert)
          </div>
          <p class="text-slate-700 dark:text-slate-300 text-xs leading-relaxed">
            {p['exam_trap']}
          </p>
        </div>
      </div>

      <!-- Scanned Images Accordion -->
      {images_block}
    </div>
    """
    prob_cards_html.append(card_html)

SOLID_JA_SECTION_HTML = f"""
<!-- Solid Ja E Here Master Workbook Section -->
<section id="solid-ja-workbook" class="topic-section card" data-category="solid-ja">
  <div class="section-badge-header">
    <span class="sec-pill" style="background:#e11d48;color:#fff;"><i class="fa-solid fa-fire mr-1"></i> Original Workbook</span>
    <span class="sec-sub">ถอดรหัสชีทลายมือข้อสอบจริงฉบับเต็ม 21 หน้า</span>
  </div>
  <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 mt-2 mb-4">
    <h2 class="text-2xl sm:text-3xl font-bold text-slate-900 dark:text-white flex items-center gap-2">
      <i class="fa-solid fa-book-open-reader text-rose-500"></i> คลังเฉลยข้อสอบฉบับลายมือ (Solid Ja E Here Workbook)
    </h2>
    <span class="px-3 py-1 rounded-full bg-rose-50 dark:bg-rose-950/60 text-rose-600 dark:text-rose-300 text-xs font-bold border border-rose-200 dark:border-rose-800">
      10 ชุดข้อสอบแม่บท • แปลง LaTeX ละเอียด 100%
    </span>
  </div>
  <p class="text-slate-600 dark:text-slate-300 text-sm mb-6 leading-relaxed">
    รวบรวมและถอดรหัสจากชีทลายมือ <strong>"Solid Ja E Here-" (21 หน้า)</strong> แปลงเป็นสูตรคณิตศาสตร์ LaTeX พร้อมแสดงวิธีทำตามเกณฑ์ตรวจข้อสอบอัตนัยของอาจารย์อย่างละเอียดทุกบรรทัด พร้อมปุ่มกดดูภาพสแกนต้นฉบับประกอบความเข้าใจ
  </p>

  <!-- Problem Cards Grid -->
  <div class="space-y-6">
    {''.join(prob_cards_html)}
  </div>
</section>
"""

# Build Study Plan Section
STUDY_PLAN_HTML = """
<!-- Study Plan Section -->
<section id="study-plan" class="topic-section card" data-category="study-plan">
  <div class="section-badge-header">
    <span class="sec-pill" style="background:#d97706;color:#fff;"><i class="fa-solid fa-calendar-check mr-1"></i> Study Strategy</span>
    <span class="sec-sub">แผนการอ่านหนังสือและการเตรียมตัวสอบปลายภาค</span>
  </div>
  <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 mt-2 mb-4">
    <h2 class="text-2xl sm:text-3xl font-bold text-slate-900 dark:text-white flex items-center gap-2">
      <i class="fa-solid fa-calendar-days text-amber-500"></i> แผนการอ่านหนังสือและพิชิตข้อสอบปลายภาค (Study Roadmap)
    </h2>
    <div class="flex items-center gap-1.5">
      <button class="plan-tab-btn active" onclick="switchPlanTab('plan-7days')">แผนเร่งรัด 7 วัน (Sprint)</button>
      <button class="plan-tab-btn" onclick="switchPlanTab('plan-14days')">แผนเจาะลึก 14 วัน (Mastery)</button>
    </div>
  </div>
  <p class="text-slate-600 dark:text-slate-300 text-sm mb-6">
    ตารางอ่านหนังสือที่ออกแบบตามน้ำหนักคะแนนข้อสอบจริง แบ่งเป้าหมายรายวัน คลิปเรียนที่ต้องดู และโจทย์ที่ต้องฝึกทำ
  </p>

  <!-- 7 Days Sprint Plan -->
  <div id="plan-7days" class="plan-panel">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      
      <div class="p-4 rounded-xl bg-slate-50 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 flex flex-col justify-between">
        <div>
          <div class="flex justify-between items-center mb-2">
            <span class="px-2 py-0.5 rounded bg-blue-100 text-blue-700 dark:bg-blue-900 dark:text-blue-300 text-xs font-bold">DAY 1</span>
            <span class="text-xs text-slate-400">2.5 ชม.</span>
          </div>
          <h4 class="font-bold text-slate-800 dark:text-slate-100 text-sm mb-1">ปูพื้นฐาน Inertia & การบิดพื้นฐาน</h4>
          <p class="text-xs text-slate-600 dark:text-slate-400 mb-3">ทบทวนการหาแกนสะเทิน NA, โมเมนต์ความเฉื่อย $I$, ตัด FBD แรงบิดเพลา และอัตราทดฟันเฟือง</p>
          <div class="text-xs space-y-1 text-slate-700 dark:text-slate-300">
            <div>📺 คลิป: Centroid & Torsion (be-engineer & P'BIG)</div>
            <div>✍️ ฝึกทำ: ข้อที่ 1 จาก Solid Ja E Here</div>
          </div>
        </div>
        <div class="mt-3 pt-2 border-t border-slate-200 dark:border-slate-700 flex items-center justify-between">
          <label class="text-xs flex items-center gap-1 cursor-pointer">
            <input type="checkbox" class="plan-day-check" data-day="day1" onchange="toggleDayCheck('day1', this.checked)">
            <span>สำเร็จภารกิจ</span>
          </label>
        </div>
      </div>

      <div class="p-4 rounded-xl bg-slate-50 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 flex flex-col justify-between">
        <div>
          <div class="flex justify-between items-center mb-2">
            <span class="px-2 py-0.5 rounded bg-blue-100 text-blue-700 dark:bg-blue-900 dark:text-blue-300 text-xs font-bold">DAY 2</span>
            <span class="text-xs text-slate-400">3 ชม.</span>
          </div>
          <h4 class="font-bold text-slate-800 dark:text-slate-100 text-sm mb-1">การบิดขั้นสูง & เพลาสวมซ้อน</h4>
          <p class="text-xs text-slate-600 dark:text-slate-400 mb-3">เพลายึดแน่นหัวท้าย (Indeterminate Torsion) และเพลาสองวัสดุสวมซ้อนกัน</p>
          <div class="text-xs space-y-1 text-slate-700 dark:text-slate-300">
            <div>📺 คลิป: บทที่ 5 การบิด Part 2/2 (อ.สิทธิชัย)</div>
            <div>✍️ ฝึกทำ: ข้อที่ 2 และ ข้อที่ 3 จาก Solid Ja E Here</div>
          </div>
        </div>
        <div class="mt-3 pt-2 border-t border-slate-200 dark:border-slate-700 flex items-center justify-between">
          <label class="text-xs flex items-center gap-1 cursor-pointer">
            <input type="checkbox" class="plan-day-check" data-day="day2" onchange="toggleDayCheck('day2', this.checked)">
            <span>สำเร็จภารกิจ</span>
          </label>
        </div>
      </div>

      <div class="p-4 rounded-xl bg-slate-50 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 flex flex-col justify-between">
        <div>
          <div class="flex justify-between items-center mb-2">
            <span class="px-2 py-0.5 rounded bg-blue-100 text-blue-700 dark:bg-blue-900 dark:text-blue-300 text-xs font-bold">DAY 3</span>
            <span class="text-xs text-slate-400">3 ชม.</span>
          </div>
          <h4 class="font-bold text-slate-800 dark:text-slate-100 text-sm mb-1">ความเค้นดัด & คานหน้าตัดผสม</h4>
          <p class="text-xs text-slate-600 dark:text-slate-400 mb-3">สูตรการดัด $\sigma = My/I$, การแปลงหน้าตัดไม้ประกบเหล็ก $b' = nb$</p>
          <div class="text-xs space-y-1 text-slate-700 dark:text-slate-300">
            <div>📺 คลิป: Bending Stress (be-engineer) & Transformed Section (อ.ไพโรจน์)</div>
            <div>✍️ ฝึกทำ: ข้อที่ 5 และ ข้อที่ 7 จาก Solid Ja E Here</div>
          </div>
        </div>
        <div class="mt-3 pt-2 border-t border-slate-200 dark:border-slate-700 flex items-center justify-between">
          <label class="text-xs flex items-center gap-1 cursor-pointer">
            <input type="checkbox" class="plan-day-check" data-day="day3" onchange="toggleDayCheck('day3', this.checked)">
            <span>สำเร็จภารกิจ</span>
          </label>
        </div>
      </div>

      <div class="p-4 rounded-xl bg-slate-50 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 flex flex-col justify-between">
        <div>
          <div class="flex justify-between items-center mb-2">
            <span class="px-2 py-0.5 rounded bg-blue-100 text-blue-700 dark:bg-blue-900 dark:text-blue-300 text-xs font-bold">DAY 4</span>
            <span class="text-xs text-slate-400">3 ชม.</span>
          </div>
          <h4 class="font-bold text-slate-800 dark:text-slate-100 text-sm mb-1">การแอ่นตัวของคาน (Deflection)</h4>
          <p class="text-xs text-slate-600 dark:text-slate-400 mb-3">วิธีอินทิเกรตสองชั้น $EI v'' = M(x)$ และวิธีพื้นที่โมเมนต์ Moment-Area</p>
          <div class="text-xs space-y-1 text-slate-700 dark:text-slate-300">
            <div>📺 คลิป: Double Integration By P'BIG & Deflection (อ.ไพโรจน์)</div>
            <div>✍️ ฝึกทำ: ข้อที่ 6 จาก Solid Ja E Here</div>
          </div>
        </div>
        <div class="mt-3 pt-2 border-t border-slate-200 dark:border-slate-700 flex items-center justify-between">
          <label class="text-xs flex items-center gap-1 cursor-pointer">
            <input type="checkbox" class="plan-day-check" data-day="day4" onchange="toggleDayCheck('day4', this.checked)">
            <span>สำเร็จภารกิจ</span>
          </label>
        </div>
      </div>

      <div class="p-4 rounded-xl bg-slate-50 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 flex flex-col justify-between">
        <div>
          <div class="flex justify-between items-center mb-2">
            <span class="px-2 py-0.5 rounded bg-blue-100 text-blue-700 dark:bg-blue-900 dark:text-blue-300 text-xs font-bold">DAY 5</span>
            <span class="text-xs text-slate-400">3 ชม.</span>
          </div>
          <h4 class="font-bold text-slate-800 dark:text-slate-100 text-sm mb-1">แรงเฉือนตามขวาง & ระยะห่างตะปู</h4>
          <p class="text-xs text-slate-600 dark:text-slate-400 mb-3">สูตร $\tau = VQ/It$ การกระโดดของหน่วยแรง และการหา Shear Flow $q = VQ/I, s \le mF/q$</p>
          <div class="text-xs space-y-1 text-slate-700 dark:text-slate-300">
            <div>📺 คลิป: Shear Flow & Shear Center (P'BIG & อ.สิทธิชัย)</div>
            <div>✍️ ฝึกทำ: ข้อที่ 8 และ ข้อที่ 9 จาก Solid Ja E Here</div>
          </div>
        </div>
        <div class="mt-3 pt-2 border-t border-slate-200 dark:border-slate-700 flex items-center justify-between">
          <label class="text-xs flex items-center gap-1 cursor-pointer">
            <input type="checkbox" class="plan-day-check" data-day="day5" onchange="toggleDayCheck('day5', this.checked)">
            <span>สำเร็จภารกิจ</span>
          </label>
        </div>
      </div>

      <div class="p-4 rounded-xl bg-slate-50 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 flex flex-col justify-between">
        <div>
          <div class="flex justify-between items-center mb-2">
            <span class="px-2 py-0.5 rounded bg-blue-100 text-blue-700 dark:bg-blue-900 dark:text-blue-300 text-xs font-bold">DAY 6</span>
            <span class="text-xs text-slate-400">3 ชม.</span>
          </div>
          <h4 class="font-bold text-slate-800 dark:text-slate-100 text-sm mb-1">เสาโก่งเดาะออยเลอร์ & วงกลมมอร์</h4>
          <p class="text-xs text-slate-600 dark:text-slate-400 mb-3">สูตร Euler Buckling เช็ก 2 ระนาบแกน $x, y$ และทบทวน Combined Stress</p>
          <div class="text-xs space-y-1 text-slate-700 dark:text-slate-300">
            <div>📺 คลิป: Buckling of Column (อ.ไพโรจน์) & Mohr's Circle (be-engineer)</div>
            <div>✍️ ฝึกทำ: ข้อที่ 10 จาก Solid Ja E Here</div>
          </div>
        </div>
        <div class="mt-3 pt-2 border-t border-slate-200 dark:border-slate-700 flex items-center justify-between">
          <label class="text-xs flex items-center gap-1 cursor-pointer">
            <input type="checkbox" class="plan-day-check" data-day="day6" onchange="toggleDayCheck('day6', this.checked)">
            <span>สำเร็จภารกิจ</span>
          </label>
        </div>
      </div>

      <div class="p-4 rounded-xl bg-gradient-to-br from-amber-50 to-orange-50 dark:from-amber-950/40 dark:to-orange-950/40 border border-amber-300 dark:border-amber-800 flex flex-col justify-between md:col-span-2 lg:col-span-3">
        <div>
          <div class="flex justify-between items-center mb-2">
            <span class="px-2.5 py-0.5 rounded bg-amber-500 text-white text-xs font-bold">DAY 7 (FINAL REVIEW)</span>
            <span class="text-xs font-semibold text-amber-800 dark:text-amber-300">ซ้อมสอบเสมือนจริง 3 ชั่วโมง</span>
          </div>
          <h4 class="font-bold text-slate-900 dark:text-slate-100 text-base mb-1">🎯 ตะลุย Mock Exam ปลายภาคแบบปิดตำรา + สแกนจุดดักคะแนน</h4>
          <p class="text-xs text-slate-700 dark:text-slate-300 mb-3 leading-relaxed">
            เลือกโจทย์สุ่มจากทั้ง 10 ข้อในชีท Solid Ja E Here ทำแบบจับเวลาจริงข้อละ 25 นาที ตรวจเช็กเครื่องหมายดึง/อัด, มิติของหน่วย ($\text{N, mm, MPa}$), และเขียนพิสูจน์ครบ 4 ขั้นตอน
          </p>
        </div>
        <div class="mt-2 pt-2 border-t border-amber-200 dark:border-amber-900/60 flex items-center justify-between">
          <label class="text-xs font-bold text-amber-900 dark:text-amber-200 flex items-center gap-1 cursor-pointer">
            <input type="checkbox" class="plan-day-check" data-day="day7" onchange="toggleDayCheck('day7', this.checked)">
            <span>พร้อมลุยห้องสอบ 100%!</span>
          </label>
        </div>
      </div>

    </div>
  </div>

  <!-- 14 Days Mastery Plan -->
  <div id="plan-14days" class="plan-panel hidden">
    <div class="p-4 bg-slate-50 dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700 text-xs sm:text-sm text-slate-700 dark:text-slate-300 space-y-2">
      <div class="font-bold text-slate-900 dark:text-white text-sm mb-2"><i class="fa-solid fa-route text-amber-500 mr-1"></i> แผน 14 วัน แบบเรียนวันละ 1 คอนเซปต์ + สลับวันฝึกทำโจทย์:</div>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
        <div class="p-2.5 bg-white dark:bg-slate-900 rounded-lg"><strong>Day 1-2:</strong> เซนทรอยด์ & โมเมนต์ความเฉื่อย $I$ (ทำโจทย์หน้าตัดไม่สมมาตร)</div>
        <div class="p-2.5 bg-white dark:bg-slate-900 rounded-lg"><strong>Day 3-4:</strong> การบิดเพลากลมตัน & ระบบเฟืองทด (ฝึกตัด FBD และคิดมุมบิดสะสม)</div>
        <div class="p-2.5 bg-white dark:bg-slate-900 rounded-lg"><strong>Day 5-6:</strong> อินดีเทอร์มิเนตการบิด & เพลาสวมซ้อน (ฝึกตั้งสมการ Compatibility $\phi=0$)</div>
        <div class="p-2.5 bg-white dark:bg-slate-900 rounded-lg"><strong>Day 7-8:</strong> สูตรการดัด $\sigma = My/I$ และการดัดหน้าตัดผสม $b' = nb$</div>
        <div class="p-2.5 bg-white dark:bg-slate-900 rounded-lg"><strong>Day 9-10:</strong> การแอ่นตัวของคาน (Double Integration & Moment-Area Method)</div>
        <div class="p-2.5 bg-white dark:bg-slate-900 rounded-lg"><strong>Day 11-12:</strong> แรงเฉือน $\tau = VQ/It$ และการเฉือนไหลตะปู $q = VQ/I, s \le mF/q$</div>
        <div class="p-2.5 bg-white dark:bg-slate-900 rounded-lg"><strong>Day 13:</strong> การโก่งเดาะของเสาอุดมคติ Euler Buckling (ตรวจ 2 แกน $x, y$)</div>
        <div class="p-2.5 bg-white dark:bg-slate-900 rounded-lg"><strong>Day 14:</strong> ความเค้นผสม 3 มิติ และวงกลมมอร์ (Full Comprehensive Review)</div>
      </div>
    </div>
  </div>
</section>
"""

# Update Navigation in header
nav_insert = """
        <a href="#solid-ja-workbook" class="px-2.5 py-1.5 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-800 transition text-rose-600 dark:text-rose-400 font-bold"><i class="fa-solid fa-fire mr-1"></i> ชีท Solid Ja E Here</a>
        <a href="#study-plan" class="px-2.5 py-1.5 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-800 transition text-amber-600 dark:text-amber-400 font-bold"><i class="fa-solid fa-calendar-days mr-1"></i> แผนอ่านหนังสือ</a>
"""

# Update Filter buttons
filter_insert = """
          <button class="filter-btn text-rose-600 dark:text-rose-400 font-bold" data-filter="solid-ja"><i class="fa-solid fa-fire mr-1"></i> ชีท Solid Ja (10 ข้อ)</button>
          <button class="filter-btn text-amber-600 dark:text-amber-400 font-bold" data-filter="study-plan"><i class="fa-solid fa-calendar-days mr-1"></i> แผนอ่านหนังสือ</button>
"""

# Inject into html
# 1. Add nav items before </nav>
html = html.replace('</nav>', nav_insert + '\n      </nav>')

# 2. Add filter buttons
html = html.replace('<button class="filter-btn" data-filter="calculators">', filter_insert + '\n          <button class="filter-btn" data-filter="calculators">')

# 3. Add styling for study plan tabs and scanned page images
additional_css = """
    /* Solid Ja E Here Scanned Images Box */
    .scanned-page-box {
      background: #ffffff;
      padding: 0.75rem;
      border-radius: 0.75rem;
      border: 1px solid #e2e8f0;
      text-align: center;
    }
    .dark .scanned-page-box {
      background: #1e293b;
      border-color: #334155;
    }
    .plan-tab-btn {
      padding: 0.35rem 0.75rem;
      font-size: 0.75rem;
      font-weight: 700;
      border-radius: 0.5rem;
      color: #64748b;
      background: #f1f5f9;
      border: 1px solid #cbd5e1;
      cursor: pointer;
      transition: all 0.15s;
    }
    .plan-tab-btn.active {
      background: #d97706;
      color: #ffffff;
      border-color: #d97706;
    }
    .dark .plan-tab-btn {
      background: #334155;
      color: #cbd5e1;
      border-color: #475569;
    }
    .dark .plan-tab-btn.active {
      background: #d97706;
      color: #ffffff;
    }
"""

html = html.replace('</style>', additional_css + '\n  </style>')

# 4. Inject Solid Ja and Study Plan sections right before #contentSections
sections_insertion = SOLID_JA_SECTION_HTML + "\n\n" + STUDY_PLAN_HTML + "\n\n"
html = html.replace('<div id="contentSections">', sections_insertion + '<div id="contentSections">')

# 5. Add JavaScript for toggling scanned images and plan tabs
additional_js = """
    // Toggle Scanned Images Accordion
    function toggleScannedImages(probId) {
      const container = document.getElementById('images-' + probId);
      const chevron = document.getElementById('chevron-' + probId);
      if (container) {
        if (container.classList.contains('hidden')) {
          container.classList.remove('hidden');
          if (chevron) chevron.className = 'fa-solid fa-chevron-up text-[10px] ml-1';
        } else {
          container.classList.add('hidden');
          if (chevron) chevron.className = 'fa-solid fa-chevron-down text-[10px] ml-1';
        }
      }
    }

    // Study Plan Tab Switcher
    function switchPlanTab(planId) {
      document.querySelectorAll('.plan-panel').forEach(p => p.classList.add('hidden'));
      document.querySelectorAll('.plan-tab-btn').forEach(b => b.classList.remove('active'));
      const target = document.getElementById(planId);
      if (target) target.classList.remove('hidden');
      if (event && event.currentTarget) event.currentTarget.classList.add('active');
    }

    // Daily Checkboxes Persistence
    function toggleDayCheck(dayId, isChecked) {
      localStorage.setItem('study_day_' + dayId, isChecked ? 'true' : 'false');
    }

    function initDayChecks() {
      ['day1', 'day2', 'day3', 'day4', 'day5', 'day6', 'day7'].forEach(d => {
        const isDone = localStorage.getItem('study_day_' + d) === 'true';
        const checkbox = document.querySelector(`.plan-day-check[data-day="${d}"]`);
        if (checkbox) checkbox.checked = isDone;
      });
    }

    document.addEventListener('DOMContentLoaded', () => {
      initDayChecks();
    });
"""

html = html.replace('</script>\n</body>', additional_js + '\n  </script>\n</body>')

# Save updated index.html
output_path = '/Users/thanaporn/.gemini/antigravity/scratch/mechanics-of-materials-final/index.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Successfully compiled updated portal with Solid Ja E Here and Study Plan! New file size: {os.path.getsize(output_path)} bytes")
