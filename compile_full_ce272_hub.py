# -*- coding: utf-8 -*-
import os
import json
from make_solid_ja_html import PROBLEMS

html_parts = []

# ==========================================
# PART 1: Head & Setup
# ==========================================
html_parts.append(r'''<!doctype html>
<html lang="th" data-theme="light">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>CE 211 กลศาสตร์วัสดุ ปลายภาค (Mechanics of Materials) · มหาวิทยาลัยธรรมศาสตร์</title>
  <meta name="description" content="สรุปสูตร ที่มา สเต็ปวิธีทำ จุดดักข้อสอบ และเฉลยชีทข้อสอบจริง Solid Ja E Here ครบทั้ง 21 หน้า กลศาสตร์วัสดุ CE 211 วิศวกรรมโยธา มหาวิทยาลัยธรรมศาสตร์">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Sarabun:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css">
  <link rel="stylesheet" href="assets/style.css?v=20261123">
  <script>
    (function(){
      var t = null;
      try { t = localStorage.getItem('theme'); } catch(e){}
      if (t !== 'light' && t !== 'dark') {
        t = matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
      }
      document.documentElement.setAttribute('data-theme', t);
    })();
  </script>
</head>
<body>

<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <defs>
    <marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0 0L10 5L0 10z" fill="context-stroke"/>
    </marker>
  </defs>
</svg>

<nav class="toc" aria-label="สารบัญนำทาง">
  <a href="#sum" aria-current="page">สรุปภาพรวม</a>
  <a href="#plan">แผนอ่าน 7 วัน</a>
  <a href="#lec9">ครั้ง 9 การบิด 1/2</a>
  <a href="#lec10">ครั้ง 10 การบิด 2/2</a>
  <a href="#lec11">ครั้ง 11 การดัด</a>
  <a href="#lec12">ครั้ง 12 คานแอ่นตัว</a>
  <a href="#lec13">ครั้ง 13 หน้าตัดผสม</a>
  <a href="#lec14">ครั้ง 14 แรงเฉือน τ</a>
  <a href="#lec15">ครั้ง 15 Shear Flow</a>
  <a href="#lec16">ครั้ง 16 เสาโก่งเดาะ</a>
  <a href="#bonus">โบนัส ความเค้นผสม</a>
  <a href="#solidja" class="gap">ชีท Solid Ja (10 ข้อ)</a>
  <a href="#calc" class="gap">คิดเลข</a>
  <a href="#ref">คำศัพท์ &amp; จุดดัก</a>
  <span class="sp"></span>
  <span class="tools">
    <button class="th" id="practice" type="button" aria-pressed="false" aria-label="โหมดฝึก ซ่อนวิธีทำ">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20h4L19 9l-4-4L4 16z"/><path d="M13.5 6.5l4 4"/></svg>
      <span class="lbl">ฝึก</span>
    </button>
    <button class="th" id="theme" type="button" aria-label="สลับโหมดสว่าง/มืด">
      <svg class="sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
      <svg class="moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4 8 8 0 1 0 20 14.5z"/></svg>
      <span class="lbl" id="thl">โหมดมืด</span>
    </button>
  </span>
</nav>

<main>
<noscript><p style="padding:20px;color:red;text-align:center;">กรุณาเปิดการทำงานของ JavaScript เพื่อแสดงสูตรคณิตศาสตร์และใช้งานระบบ</p></noscript>
''')

# ==========================================
# PART 2: Section #sum (Overview)
# ==========================================
html_parts.append(r'''
<section id="sum" class="on">
  <header class="top">
    <p class="kick">แนวทางการเตรียมสอบปลายภาคกลศาสตร์วัสดุสำหรับวิศวกรโยธา</p>
    <h1>CE 211 กลศาสตร์วัสดุ ปลายภาค</h1>
    <p class="sub">สรุปเนื้อหา · สมการควบคุม · สเต็ปวิธีทำ 4 ขั้นตอน · จุดดักคะแนน ครบครั้งที่ 9–16</p>
    <p class="by">ภาควิชาวิศวกรรมโยธา คณะวิศวกรรมศาสตร์ มหาวิทยาลัยธรรมศาสตร์<br>อ้างอิงเนื้อหาหลักสูตรและชีทข้อสอบจริง Solid Ja E Here (21 หน้า) · จัดทำโดย ธนภรณ์ นพรัตน์</p>
    <p class="pracnote">โหมดฝึกเปิดอยู่: ซ่อนวิธีทำไว้ แตะแต่ละขั้นเพื่อดู (ลองเขียนเองก่อน) กดปุ่ม "ฝึก" อีกครั้งเพื่อปิด</p>
  </header>

  <h2 class="prob"><span class="tag">ภาพรวม</span>สรุปมโนทัศน์สำคัญและการสอบปลายภาค</h2>
  <div class="stmt">
    <p>คู่มือนี้สรุปเนื้อหากลศาสตร์วัสดุ (Mechanics of Materials) ปลายภาค ครบทุกบท (ครั้งที่ 9 ถึง 16 และโบนัสความเค้นผสม 3 มิติ) พร้อมถอดรหัสเฉลยข้อสอบจริงจากชีท <b>"Solid Ja E Here-" (21 หน้าเต็ม)</b> แปลงเป็นสูตรคณิตศาสตร์ \(\LaTeX\) คมชัด 100% แสดงวิธีทำตามมาตรฐาน 4 ขั้นตอนของอาจารย์ เพื่อให้นักศึกษาสามารถทบทวนและซ้อมทำข้อสอบได้อย่างรวดเร็ว ถูกต้อง และแม่นยำ</p>
  </div>

  <div class="jump">
    <a href="#sum-matrix">ตารางสมการ 9–16</a>
    <a href="#sum-cards">การ์ดสรุปสูตร</a>
    <a href="#plan">แผนอ่าน 7 วัน</a>
    <a href="#lec9">ครั้ง 9 การบิด 1/2</a>
    <a href="#lec10">ครั้ง 10 การบิด 2/2</a>
    <a href="#lec11">ครั้ง 11 การดัด</a>
    <a href="#lec12">ครั้ง 12 คานแอ่นตัว</a>
    <a href="#lec13">ครั้ง 13 หน้าตัดผสม</a>
    <a href="#lec14">ครั้ง 14 แรงเฉือน τ</a>
    <a href="#lec15">ครั้ง 15 Shear Flow</a>
    <a href="#lec16">ครั้ง 16 เสาโก่งเดาะ</a>
    <a href="#solidja">ชีท Solid Ja (10 ข้อ)</a>
    <a href="#calc">คิดเลข</a>
  </div>

  <h3 class="grp" id="sum-matrix">ก. สรุปสมการควบคุมหลักครั้งที่ 9–16 (Governing Formulas Matrix)</h3>
  <div class="tw">
    <table>
      <caption>ตารางสรุปสมการควบคุมและหัวใจสำคัญ ข้อสอบปลายภาค ครบทุกบท (เลื่อนแนวนอนเพื่อดูคอลัมน์เต็ม)</caption>
      <thead>
        <tr>
          <th class="td-num">ครั้ง</th>
          <th class="td-name">หัวข้อสอบตามตาราง</th>
          <th class="td-eq">สมการสำคัญ (\(\LaTeX\))</th>
          <th class="td-vars">ตัวแปรหลักที่ต้องหา</th>
          <th class="td-tools">คลิปติวตรงจุด</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="td-num"><b>9</b></td>
          <td class="td-name">การบิด (1/2)<small>ดีเทอร์มิเนต &amp; เฟืองทด</small></td>
          <td class="td-eq">
            <div class="eq-row">
              <div class="eq-pill">\(\tau = \frac{Tr}{J}\)</div>
              <div class="eq-pill">\(\phi = \sum \frac{T_i L_i}{G_i J_i}\)</div>
              <div class="eq-subnote">เฟืองทด: \(T_2 = T_1(r_2/r_1), \phi_2 = \phi_1(r_1/r_2)\)</div>
            </div>
          </td>
          <td class="td-vars">\(T_i, J = \frac{\pi c^4}{2}, \tau_{\max}, \phi\)</td>
          <td class="td-tools"><a href="https://www.youtube.com/results?search_query=ติวสดฟรี+Strength+-+Torsion+be-engineer" target="_blank">be-engineer &amp; อ.ไพโรจน์</a></td>
        </tr>
        <tr>
          <td class="td-num"><b>10</b></td>
          <td class="td-name">การบิด (2/2)<small>อินดีเทอร์มิเนต &amp; สวมซ้อน</small></td>
          <td class="td-eq">
            <div class="eq-row">
              <div class="eq-pill">\(\sum T = 0\) คู่กับ \(\phi_{A/D} = \sum \frac{T_i L_i}{GJ} = 0\)</div>
              <div class="eq-pill">เพลาสวมซ้อน: \(\phi_s = \phi_b \implies \frac{T_s}{T_b} = \frac{G_s J_s}{G_b J_b}\)</div>
            </div>
          </td>
          <td class="td-vars">\(T_A, T_D, \tau_{\max}, \tau_{\min}\)</td>
          <td class="td-tools"><a href="https://www.youtube.com/results?search_query=บทที่+5+การบิด+Part+2%2F2+Indeterminate+สิทธิชัย+แสงอาทิตย์" target="_blank">อ.สิทธิชัย &amp; อ.ไพโรจน์</a></td>
        </tr>
        <tr>
          <td class="td-num"><b>11</b></td>
          <td class="td-name">การดัด<small>หน่วยแรงดัดในคาน</small></td>
          <td class="td-eq">
            <div class="eq-row">
              <div class="eq-pill">\(\sigma = -\frac{My}{I}\), \(\sigma_{\max} = \frac{Mc}{I}\)</div>
              <div class="eq-subnote">แกนสะเทิน NA: \(\bar{y} = \frac{\sum Ay}{\sum A}, I = \sum (\bar{I} + Ad^2)\)</div>
            </div>
          </td>
          <td class="td-vars">\(\bar{y}, I, M_{\max}, \sigma_{\text{top}}, \sigma_{\text{bot}}\)</td>
          <td class="td-tools"><a href="https://www.youtube.com/results?search_query=การหา+Bending+Stress+โดยละเอียด+be-engineer" target="_blank">be-engineer &amp; อ.ไพโรจน์</a></td>
        </tr>
        <tr>
          <td class="td-num"><b>12</b></td>
          <td class="td-name">คานแอ่นตัว<small>Deflection of Beams</small></td>
          <td class="td-eq">
            <div class="eq-row">
              <div class="eq-pill">\(EI \frac{d^2v}{dx^2} = M(x)\)</div>
              <div class="eq-pill">Moment-Area: \(\theta_{B/A} = \text{Area}\left(\frac{M}{EI}\right), t_{B/A} = \text{Area}\cdot\bar{x}_B\)</div>
            </div>
          </td>
          <td class="td-vars">สมการ Slope \(v'(x)\), Deflection \(v(x), v_{\max}\)</td>
          <td class="td-tools"><a href="https://www.youtube.com/results?search_query=DOUBLE+INTEGRATION+By+P%27BIG+ETC+TUTOR" target="_blank">P'BIG &amp; อ.ไพโรจน์</a></td>
        </tr>
        <tr>
          <td class="td-num"><b>13</b></td>
          <td class="td-name">หน้าตัดผสม<small>Transformed Section</small></td>
          <td class="td-eq">
            <div class="eq-row">
              <div class="eq-pill">\(n = \frac{E_2}{E_1}, b' = n \cdot b\) (ความสูง \(h\) ห้ามเปลี่ยน!)</div>
              <div class="eq-pill">\(\sigma_1 = -\frac{My}{I_T}, \sigma_2 = -n \frac{My}{I_T}\) (คูณ \(n\) กลับ)</div>
            </div>
          </td>
          <td class="td-vars">\(n, \bar{y}_T, I_T, \sigma_w, \sigma_s\)</td>
          <td class="td-tools"><a href="https://www.youtube.com/results?search_query=โจทย์ตัวอย่าง+Bending+of+beam+Pairod+Singhatanadgid" target="_blank">อ.ไพโรจน์ &amp; อ.สิทธิชัย</a></td>
        </tr>
        <tr>
          <td class="td-num"><b>14</b></td>
          <td class="td-name">แรงเฉือนตามขวาง<small>Transverse Shear</small></td>
          <td class="td-eq">
            <div class="eq-row">
              <div class="eq-pill">\(\tau = \frac{VQ}{It}, Q = A' \bar{y}'\)</div>
              <div class="eq-subnote">\(\tau\) กระโดดที่รอยต่อปีกกับเอวตามอัตราส่วนความหนา \(t_f/t_w\)</div>
            </div>
          </td>
          <td class="td-vars">\(Q_{\text{junc}}, Q_{\text{NA}}, \tau_{\text{flange}}, \tau_{\text{web}}, \tau_{\max}\)</td>
          <td class="td-tools"><a href="https://www.youtube.com/results?search_query=Shear+Center+P%27BIG+ETC+TUTOR" target="_blank">P'BIG &amp; อ.ไพโรจน์</a></td>
        </tr>
        <tr>
          <td class="td-num"><b>15</b></td>
          <td class="td-name">การเฉือนไหล<small>Shear Flow &amp; Fasteners</small></td>
          <td class="td-eq">
            <div class="eq-row">
              <div class="eq-pill">\(q = \frac{VQ}{I}, s_{\max} \le \frac{m F_{\text{allow}}}{q}\)</div>
              <div class="eq-subnote">ถอนตะปูแผ่นไหนหลุดคิด \(A'\) แผ่นนั้น · ปัดเศษ \(s\) ลงเสมอ</div>
            </div>
          </td>
          <td class="td-vars">\(q, s_{\max}\) (ระยะห่างตะปู), \(m\) (จำนวนแถว)</td>
          <td class="td-tools"><a href="https://www.youtube.com/results?search_query=16+บทที่+7+การเฉือนตามขวาง+Shear+flow+สิทธิชัย+แสงอาทิตย์" target="_blank">อ.สิทธิชัย &amp; P'BIG</a></td>
        </tr>
        <tr>
          <td class="td-num"><b>16</b></td>
          <td class="td-name">เสาโก่งเดาะ<small>Euler Buckling</small></td>
          <td class="td-eq">
            <div class="eq-row">
              <div class="eq-pill">\(P_{cr} = \frac{\pi^2 EI}{(KL)^2}, \sigma_{cr} = \frac{\pi^2 E}{(KL/r)^2}\)</div>
              <div class="eq-subnote">ตรวจ 2 ระนาบ \(x, y\) · แกนที่ \(\lambda = \frac{KL}{r}\) สูงกว่าจะเดาะก่อน</div>
            </div>
          </td>
          <td class="td-vars">\(r = \sqrt{I/A}, \lambda = \frac{KL}{r}, \left(\frac{KL}{r}\right)_c, P_{cr}\)</td>
          <td class="td-tools"><a href="https://www.youtube.com/results?search_query=โจทย์ตัวอย่าง+Buckling+Pairod+Singhatanadgid" target="_blank">อ.ไพโรจน์ &amp; อ.สิทธิชัย</a></td>
        </tr>
        <tr>
          <td class="td-num"><b>โบนัส</b></td>
          <td class="td-name">ความเค้นผสม 3 มิติ<small>Combined Stress &amp; Mohr</small></td>
          <td class="td-eq">
            <div class="eq-row">
              <div class="eq-pill">\(\sigma_{\text{total}} = \frac{P}{A} \pm \frac{My}{I}, \tau_{\text{total}} = \frac{Tr}{J} \pm \frac{VQ}{It}\)</div>
              <div class="eq-pill">\(\sigma_{1,2} = \sigma_{\text{avg}} \pm R, \tau_{\max} = R = \sqrt{\left(\frac{\sigma_x-\sigma_y}{2}\right)^2 + \tau_{xy}^2}\)</div>
            </div>
          </td>
          <td class="td-vars">\(\sigma_1, \sigma_2, \tau_{\max}, \theta_p\)</td>
          <td class="td-tools"><a href="https://www.youtube.com/results?search_query=การใช้+Mohr%27s+Circle+หา+Principal+Stress+be-engineer" target="_blank">be-engineer &amp; P'BIG</a></td>
        </tr>
      </tbody>
    </table>
  </div>

  <h3 class="grp" id="sum-cards">ข. การ์ดสรุปสูตรหัวใจหลัก 8 บท</h3>
  <div class="formula-grid">
    <div class="formula-card">
      <div class="formula-card-head">
        <span class="formula-card-title">1. การบิดเพลากลม (Torsion)</span>
        <span class="formula-card-badge">ครั้งที่ 9–10</span>
      </div>
      <div class="formula-card-body">
        \(\tau = \frac{Tr}{J}, \quad \phi = \sum \frac{TL}{GJ}, \quad J = \frac{\pi c^4}{2}\)
      </div>
      <div class="formula-card-desc">ตัด FBD หาแรงบิดภายใน \(T\) ทีละช่วง หากยึดแน่นสองปลายใช้ Compatibility \(\phi_{\text{ซ้าย}} = \phi_{\text{ขวา}}\)</div>
      <div class="formula-card-trap">⚠️ จุดดัก: แปลง \(T\) เป็น \(\text{N}\cdot\text{mm}\) และเพลากลวง \(\tau_{\min}\) ที่ผิวในไม่เท่ากับศูนย์</div>
    </div>

    <div class="formula-card">
      <div class="formula-card-head">
        <span class="formula-card-title">2. สูตรการดัด (Flexure Formula)</span>
        <span class="formula-card-badge">ครั้งที่ 11</span>
      </div>
      <div class="formula-card-body">
        \(\sigma = -\frac{My}{I}, \quad \sigma_{\max} = \frac{Mc}{I}, \quad I = \sum (\bar{I} + Ad^2)\)
      </div>
      <div class="formula-card-desc">หาจุดเซนทรอยด์ \(\bar{y}\) เพื่อกำหนดแกนสะเทิน (NA) ความเค้นดัดที่แกน NA เป็นศูนย์เสมอ</div>
      <div class="formula-card-trap">⚠️ จุดดัก: ดูทิศโมเมนต์ให้ถูก โซนหัวลูกศรเป็นอัด \((-)\) โซนตูดลูกศรเป็นดึง \((+)\)</div>
    </div>

    <div class="formula-card">
      <div class="formula-card-head">
        <span class="formula-card-title">3. หน้าตัดผสม (Transformed Section)</span>
        <span class="formula-card-badge">ครั้งที่ 13</span>
      </div>
      <div class="formula-card-body">
        \(n = \frac{E_2}{E_1}, \quad b' = n \cdot b, \quad \sigma_2 = n \frac{My}{I_T}\)
      </div>
      <div class="formula-card-desc">แปลงวัสดุแข็งให้เป็นวัสดุอ่อนเสมือน โดยขยายเฉพาะความกว้าง \(b\) ความสูง \(h\) คงเดิม</div>
      <div class="formula-card-trap">⚠️ จุดดัก: ห้ามเปลี่ยนความสูง \(h\) เด็ดขาด และเมื่อคิดความเค้นในเหล็กจริงต้องคูณ \(n\) กลับเสมอ</div>
    </div>

    <div class="formula-card">
      <div class="formula-card-head">
        <span class="formula-card-title">4. การเฉือนตามขวาง &amp; ตะปู (Shear Flow)</span>
        <span class="formula-card-badge">ครั้งที่ 14–15</span>
      </div>
      <div class="formula-card-body">
        \(\tau = \frac{VQ}{It}, \quad q = \frac{VQ}{I}, \quad s_{\max} \le \frac{m F_{\text{allow}}}{q}\)
      </div>
      <div class="formula-card-desc">\(Q = A'\bar{y}'\) คือโมเมนต์พื้นที่ส่วนที่ตัดขาด และระยะห่างตะปูคำนวณจากแรงต้านทานตะปู</div>
      <div class="formula-card-trap">⚠️ จุดดัก: ห้ามตัดแรเงาข้ามแกน NA และระยะห่างตะปูต้องปัดเศษลง (Round Down) เสมอ</div>
    </div>

    <div class="formula-card">
      <div class="formula-card-head">
        <span class="formula-card-title">5. เสาโก่งเดาะ (Euler Buckling)</span>
        <span class="formula-card-badge">ครั้งที่ 16</span>
      </div>
      <div class="formula-card-body">
        \(P_{cr} = \frac{\pi^2 EI}{(KL)^2}, \quad \lambda = \frac{KL}{r}, \quad r = \sqrt{\frac{I}{A}}\)
      </div>
      <div class="formula-card-desc">เสาจะโก่งเดาะรอบแกนที่มีความชะลูด \(\lambda\) สูงกว่าเสมอ ค่า \(K\) ขึ้นกับเงื่อนไขจุดรองรับ</div>
      <div class="formula-card-trap">⚠️ จุดดัก: ต้องคำนวณเปรียบเทียบทั้งแกน \(x\) และแกน \(y\) เสมอ ระวังกรณีมีค้ำยันด้านข้าง</div>
    </div>

    <div class="formula-card">
      <div class="formula-card-head">
        <span class="formula-card-title">6. การแอ่นตัวของคาน (Deflection)</span>
        <span class="formula-card-badge">ครั้งที่ 12</span>
      </div>
      <div class="formula-card-body">
        \(EI v''(x) = M(x), \quad \theta_{B/A} = \text{Area}_{A-B}(M/EI)\)
      </div>
      <div class="formula-card-desc">อินทิเกรตสองชั้นหาฟังก์ชันเส้นแอ่นตัว \(v(x)\) หรือใช้ทฤษฎีพื้นที่โมเมนต์สำหรับคานยื่น</div>
      <div class="formula-card-trap">⚠️ จุดดัก: ระวังเงื่อนไขขอบเขตที่จุดรองรับ คานยื่น \(v(0)=0, v'(0)=0\) คานช่วงเดียว \(v(0)=0, v(L)=0\)</div>
    </div>
  </div>

  <div class="pn">
    <span></span>
    <a href="#plan">ถัดไป: แผนการอ่านหนังสือ 7 วัน →</a>
  </div>
</section>
''')

# ==========================================
# PART 3: Section #plan (Study Schedule)
# ==========================================
html_parts.append(r'''
<section id="plan">
  <header class="top">
    <p class="kick">ยุทธศาสตร์การพิชิตข้อสอบปลายภาคแบบมีวินัย</p>
    <h1>แผนการอ่านหนังสือและพิชิตข้อสอบ 7 วัน</h1>
    <p class="sub">แบ่งเป้าหมายรายวัน · คลิปเรียนตรงจุด · แบบฝึกหัดที่ต้องผ่าน</p>
    <p class="by">CE 211 กลศาสตร์วัสดุ · ภาควิชาวิศวกรรมโยธา มหาวิทยาลัยธรรมศาสตร์</p>
  </header>

  <h2 class="prob"><span class="tag">ตารางติว</span>Sprint 7 วัน สำหรับช่วงโค้งสุดท้าย</h2>
  <div class="stmt">
    <p>แผนการอ่านหนังสือนี้จัดทำขึ้นสำหรับเตรียมตัวสอบปลายภาคโดยเฉพาะ จัดสรรเวลาวันละ 2.5–3 ชั่วโมง พร้อมระบุคลิปติวและข้อสอบเก่าที่ต้องฝึกทำในแต่ละวัน เมื่อทำสำเร็จสามารถติ๊กช่องบันทึกสถานะได้ทันที</p>
  </div>

  <div class="plan">
    <p><b class="l">DAY 1:</b><b>ปูพื้นฐาน Inertia &amp; การบิดเพลาขั้น (ชีทข้อ 1)</b><br>
    หาแกนสะเทิน NA, โมเมนต์ความเฉื่อย \(I\), ตัด FBD หาแรงบิดภายใน และอัตราทดฟันเฟือง<br>
    📺 คลิป: <a href="https://www.youtube.com/results?search_query=Centroid+P%27BIG+ETC+TUTOR" target="_blank">Centroid P'BIG</a> · <a href="https://www.youtube.com/results?search_query=ติวสดฟรี+Strength+-+Torsion+be-engineer" target="_blank">Torsion be-engineer</a><br>
    ✍️ โจทย์: ฝึกทำข้อที่ 1 จากชีท Solid Ja E Here</p>

    <p><b class="l">DAY 2:</b><b>การบิดอินดีเทอร์มิเนต &amp; เพลาสวมซ้อน (ชีทข้อ 2 &amp; 3)</b><br>
    ตั้งสมการ Compatibility \(\phi_{A/D} = 0\) และเพลาสองวัสดุสวมซ้อนกัน \(\phi_s = \phi_b\)<br>
    📺 คลิป: <a href="https://www.youtube.com/results?search_query=บทที่+5+การบิด+Part+2%2F2+Indeterminate+สิทธิชัย+แสงอาทิตย์" target="_blank">Indeterminate Torsion อ.สิทธิชัย</a><br>
    ✍️ โจทย์: ฝึกทำข้อที่ 2 และ 3 จากชีท Solid Ja E Here</p>

    <p><b class="l">DAY 3:</b><b>ความเค้นดัด &amp; หน้าตัดผสมไม้ประกบเหล็ก (ชีทข้อ 5 &amp; 7)</b><br>
    สูตร \(\sigma = My/I\), แปลงความกว้าง \(b' = nb\) (ห้ามเปลี่ยนความสูง) และคูณ \(n\) กลับในเหล็ก<br>
    📺 คลิป: <a href="https://www.youtube.com/results?search_query=การหา+Bending+Stress+โดยละเอียด+be-engineer" target="_blank">Bending be-engineer</a> · <a href="https://www.youtube.com/results?search_query=โจทย์ตัวอย่าง+Bending+of+beam+Pairod+Singhatanadgid" target="_blank">หน้าตัดผสม อ.ไพโรจน์</a><br>
    ✍️ โจทย์: ฝึกทำข้อที่ 5 และ 7 จากชีท Solid Ja E Here</p>

    <p><b class="l">DAY 4:</b><b>การแอ่นตัวของคาน Deflection (ชีทข้อ 6)</b><br>
    ตั้งสมการ \(EI v''(x) = M(x)\), อินทิเกรต 2 รอบแทนค่าเงื่อนไขขอบเขต และวิธี Moment-Area<br>
    📺 คลิป: <a href="https://www.youtube.com/results?search_query=DOUBLE+INTEGRATION+By+P%27BIG+ETC+TUTOR" target="_blank">Double Integration P'BIG</a> · <a href="https://www.youtube.com/results?search_query=Deflection+of+Beam+Pairod+Singhatanadgid" target="_blank">Deflection อ.ไพโรจน์</a><br>
    ✍️ โจทย์: ฝึกทำข้อที่ 6 จากชีท Solid Ja E Here</p>

    <p><b class="l">DAY 5:</b><b>แรงเฉือนตามขวาง &amp; ระยะห่างตะปู (ชีทข้อ 8 &amp; 9)</b><br>
    สูตร \(\tau = VQ/It\) การกระโดดของหน่วยแรง, Shear Flow \(q = VQ/I\) และระยะห่างตะปู \(s \le mF/q\) (ปัดเศษลง)<br>
    📺 คลิป: <a href="https://www.youtube.com/results?search_query=Shear+Center+P%27BIG+ETC+TUTOR" target="_blank">Shear Center P'BIG</a> · <a href="https://www.youtube.com/results?search_query=16+บทที่+7+การเฉือนตามขวาง+Shear+flow+สิทธิชัย+แสงอาทิตย์" target="_blank">Shear Flow อ.สิทธิชัย</a><br>
    ✍️ โจทย์: ฝึกทำข้อที่ 8 และ 9 จากชีท Solid Ja E Here</p>

    <p><b class="l">DAY 6:</b><b>เสาโก่งเดาะ Euler Buckling &amp; วงกลมมอร์ (ชีทข้อ 10)</b><br>
    สูตร Euler Buckling ตรวจสอบ 2 แกน (\(x, y\)) ความชะลูด \(\lambda = KL/r\) และทบทวน Combined Stress<br>
    📺 คลิป: <a href="https://www.youtube.com/results?search_query=โจทย์ตัวอย่าง+Buckling+Pairod+Singhatanadgid" target="_blank">Buckling อ.ไพโรจน์</a> · <a href="https://www.youtube.com/results?search_query=การใช้+Mohr%27s+Circle+หา+Principal+Stress+be-engineer" target="_blank">Mohr's Circle be-engineer</a><br>
    ✍️ โจทย์: ฝึกทำข้อที่ 10 จากชีท Solid Ja E Here</p>

    <p><b class="l">DAY 7:</b><b style="color:var(--gold);">ซ้อมสอบเสมือนจริง (Mock Exam 3 ชั่วโมงเต็ม)</b><br>
    ปิดตำราจับเวลาทำโจทย์ทั้ง 10 ข้อในชีท ตรวจสอบเครื่องหมายดึง/อัด และหน่วยวิศวกรรมให้ครบถ้วน 100%</p>
  </div>

  <div class="pn">
    <a href="#sum">← สรุปภาพรวม</a>
    <a href="#lec9">ครั้งที่ 9 การบิด 1/2 →</a>
  </div>
</section>
''')

# ==========================================
# PART 4: Sections #lec9 to #lec16 & #bonus
# ==========================================
LECTURES = [
    {
        "id": "lec9",
        "title": "ครั้งที่ 9: การบิด (1/2) - เพลากลมตันและระบบส่งกำลังด้วยเฟือง",
        "sub": "สมการการบิด · ความเค้นเฉือนสูงสุด · มุมบิดสะสม · การถ่ายทอดแรงข้ามฟันเฟือง",
        "principles": "เมื่อเพลากลมรับแรงบิดภายใน \(T\) หน้าตัดจะหมุนบิดโดยที่หน้าตัดยังคงรักษารูปร่างระนาบเดิม ความเครียดและความเค้นเฉือนจะแปรผันตรงกับระยะห่างจากแกนศูนย์กลางเพลา (\(\tau \propto r\)) และมีค่าสูงสุดที่ผิวนอกสุดเสมอ",
        "formulas": r"""
\begin{aligned}
\text{Polar Moment: } & J = \frac{\pi c^4}{2} = \frac{\pi d^4}{32} \\
\text{Torsion Formula: } & \tau = \frac{Tr}{J}, \quad \tau_{\max} = \frac{Tc}{J} \\
\text{Angle of Twist: } & \phi = \sum \frac{T_i L_i}{G_i J_i} \\
\text{Gear Transmission: } & F = \frac{T_1}{r_1} = \frac{T_2}{r_2} \implies T_2 = T_1\left(\frac{r_2}{r_1}\right), \quad \phi_2 = \phi_1\left(\frac{r_1}{r_2}\right)
\end{aligned}
""",
        "traps": "ระวังการลืมคูณ 1000 เพื่อแปลง \(T\) จาก \(\text{N}\cdot\text{m}\) เป็น \(\text{N}\cdot\text{mm}\) ก่อนแทนในสูตร และการหมุนข้ามเฟืองมุมบิดจะมีทิศทางตรงกันข้ามเสมอ",
        "prob_idx": 0
    },
    {
        "id": "lec10",
        "title": "ครั้งที่ 10: การบิด (2/2) - ปัญหาอินดีเทอร์มิเนตเชิงสถิตและเพลาสวมซ้อน",
        "sub": "เพลายึดแน่นหัวท้าย · สมการความเข้ากันได้ Compatibility · เพลาสวมซ้อน Coaxial Shafts",
        "principles": "เมื่อเพลาถูกยึดแน่นทั้งสองปลาย (Fixed-Fixed) จำนวนแรงบิดต้านทานที่จุดรองรับจะเกินจำนวนสมการสมดุลสถิตยศาสตร์ (\(\sum T = 0\)) จึงต้องใช้สมการความเข้ากันได้ของการเสียรูปว่ามุมบิดรวมระหว่างจุดรองรับต้องเป็นศูนย์ (\(\phi_{A/D} = 0\))",
        "formulas": r"""
\begin{aligned}
\text{Compatibility: } & \phi_{A/D} = 0 \implies \phi_{AB} + \phi_{BC} + \phi_{CD} = 0 \\
\text{Equilibrium: } & \sum T_x = 0 \implies T_A + T_D = \sum T_{\text{applied}} \\
\text{Composite Shaft: } & \phi_s = \phi_b \implies \frac{T_s L}{G_s J_s} = \frac{T_b L}{G_b J_b} \implies \frac{T_s}{T_b} = \frac{G_s J_s}{G_b J_b}
\end{aligned}
""",
        "traps": "สำหรับเพลากลวง หน่วยแรงเฉือนต่ำสุดที่ผิวด้านในไม่เท่ากับศูนย์ แต่คำนวณจาก \(\tau_{\min} = \frac{T c_i}{J}\) ห้ามตอบศูนย์เด็ดขาด",
        "prob_idx": 1
    },
    {
        "id": "lec11",
        "title": "ครั้งที่ 11: การดัดและสูตรการดัด (Flexure Formula)",
        "sub": "แกนสะเทิน NA · โมเมนต์ความเฉื่อย \(I\) · หน่วยแรงดึงและหน่วยแรงอัดในคาน",
        "principles": "เมื่อคานรับโมเมนต์ดัด \(M\) เส้นใยด้านหนึ่งจะถูกยืด (เกิดแรงดึง) และอีกด้านจะถูกอัด โดยมีแกนกึ่งกลางที่ไม่ยืดไม่หดตัวเลย เรียกว่า แกนสะเทิน (Neutral Axis: NA) ซึ่งผ่านจุดเซนทรอยด์ของหน้าตัดเสมอ",
        "formulas": r"""
\begin{aligned}
\text{Centroid (NA): } & \bar{y} = \frac{\sum A_i y_i}{\sum A_i} \\
\text{Parallel Axis Theorem: } & I = \sum (\bar{I}_i + A_i d_i^2), \quad \bar{I} = \frac{bh^3}{12} \\
\text{Flexure Formula: } & \sigma = -\frac{My}{I}, \quad \sigma_{\max} = \frac{Mc}{I}
\end{aligned}
""",
        "traps": "ดูทิศโมเมนต์ให้ถูกต้อง: โมเมนต์บวก (คานแอ่นลง) ด้านบนเป็นอัด \((-)\) ด้านล่างเป็นดึง \((+)\) แต่ถ้าโมเมนต์ลบ (คานโก่งขึ้น) ด้านบนจะเป็นดึงและด้านล่างจะเป็นอัด",
        "prob_idx": 4
    },
    {
        "id": "lec12",
        "title": "ครั้งที่ 12: การดัดและการแอ่นตัวของคาน (Deflection of Beams)",
        "sub": "วิธีอินทิเกรตสองชั้น Double Integration · ทฤษฎีพื้นที่โมเมนต์ Moment-Area",
        "principles": "ความโค้งของเส้นแอ่นตัวอิลาสติกแปรผันตรงกับโมเมนต์ดัดภายในและแปรผกผันกับ Flexural Rigidity (\(EI\)) การอินทิเกรตสมการโมเมนต์ดัดสองครั้งจะให้สมการความลาดชัน (Slope) และสมการการแอ่นตัว (Deflection) ตามลำดับ",
        "formulas": r"""
\begin{aligned}
\text{Governing ODE: } & EI \frac{d^2v}{dx^2} = M(x) \\
\text{Slope: } & EI \frac{dv}{dx} = \int M(x) dx + C_1 \\
\text{Deflection: } & EI v(x) = \iint M(x) dx dx + C_1 x + C_2 \\
\text{Moment-Area: } & \theta_{B/A} = \text{Area}_{A-B}\left(\frac{M}{EI}\right), \quad t_{B/A} = \text{Area}_{A-B}\left(\frac{M}{EI}\right) \cdot \bar{x}_B
\end{aligned}
""",
        "traps": "แทนเงื่อนไขขอบเขต (Boundary Conditions) ให้ตรงกับจุดรองรับ: จุดยึดแน่น Fixed \(v=0, v'=0\), จุดหมุน Pinned \(v=0\) (แต่ \(v' \ne 0\))",
        "prob_idx": 5
    },
    {
        "id": "lec13",
        "title": "ครั้งที่ 13: หน้าตัดผสมและการแปลงหน้าตัด (Transformed-Section Method)",
        "sub": "โมดูลัสเรโช \(n = E_2/E_1\) · การขยายความกว้าง \(b' = nb\) · การหาความเค้นจริง",
        "principles": "เพื่อแก้ปัญหาคานที่ประกอบด้วยวัสดุมากกว่าหนึ่งชนิด (เช่น คานไม้ประกบเหล็ก) เราจะแปลงหน้าตัดของวัสดุแข็งให้เสมือนเป็นวัสดุอ่อน โดยขยายเฉพาะความกว้าง \(b\) เป็นสัดส่วน \(n\) เท่า เพื่อให้ความสัมพันธ์ของหน่วยแรงกระจายเป็นเส้นตรงเส้นเดียว",
        "formulas": r"""
\begin{aligned}
\text{Modular Ratio: } & n = \frac{E_{\text{strong}}}{E_{\text{weak}}} = \frac{E_s}{E_w} > 1 \\
\text{Transformed Width: } & b_s' = n \cdot b_s \quad (\text{ความสูง } h \text{ ห้ามเปลี่ยน!}) \\
\text{Weak Material Stress: } & \sigma_w = -\frac{My}{I_T} \\
\text{Strong Material Stress: } & \sigma_s = -n \frac{My}{I_T} \quad (\text{ต้องคูณ } n \text{ กลับเสมอ!})
\end{aligned}
""",
        "traps": "กฎเหล็ก: แปลงเฉพาะความกว้าง \(b' = nb\) ห้ามขยายความสูง \(h\) และในเนื้อเหล็กต้องจำให้ขึ้นใจว่า \(\sigma_{\text{จริง}} = n \times \sigma_{\text{แปลง}}\)",
        "prob_idx": 6
    },
    {
        "id": "lec14",
        "title": "ครั้งที่ 14: แรงเฉือนตามขวางและสูตรการเฉือน (Transverse Shear Stress)",
        "sub": "First Moment of Area \(Q = A'\bar{y}'\) · การกระโดดของหน่วยแรงเฉือน · \(\tau_{\max}\) ที่แกน NA",
        "principles": "แรงเฉือนในแนวขวางทำให้เกิดหน่วยแรงเฉือนทั้งในระนาบขวางและระนาบตามยาวของคาน โดยหน่วยแรงเฉือนแปรผกผันกับความหนาแนวตัด \(t\) ทำให้ที่รอยต่อระหว่างปีก (Flange) และเอว (Web) หน่วยแรงเฉือนจะกระโดดขึ้นทันที",
        "formulas": r"""
\begin{aligned}
\text{Shear Formula: } & \tau = \frac{VQ}{It} \\
\text{First Moment: } & Q = A' \bar{y}' = \int_y^c \eta \, dA \\
\text{At Flange Junction: } & \tau_{\text{flange}} = \frac{VQ}{I t_f}, \quad \tau_{\text{web}} = \frac{VQ}{I t_w} \\
\text{Max Shear Stress: } & \tau_{\max} = \frac{V Q_{\text{NA}}}{I t_w} \quad (\text{เกิดขึ้นที่แกนสะเทิน NA เสมอ})
\end{aligned}
""",
        "traps": "การหาพื้นที่ \(A'\) ต้องตัดระนาบขนานกับแกน NA และคิดพื้นที่ส่วนที่อยู่เหนือรอยตัดขึ้นไปถึงขอบนอกสุด ห้ามแรเงาข้ามแกนสะเทินเด็ดขาด",
        "prob_idx": 7
    },
    {
        "id": "lec15",
        "title": "ครั้งที่ 15: การเฉือนไหลและรอยต่อของหน้าตัดประกอบ (Shear Flow & Fasteners)",
        "sub": "Shear Flow \(q = VQ/I\) · ระยะห่างตะปูหรือสลักเกลียว · กฎการปัดเศษลง",
        "principles": "คานที่สร้างขึ้นจากการนำแผ่นไม้หรือเหล็กหลายแผ่นมาประกบกัน แรงเฉือนตามยาวจะพยายามทำให้แผ่นเลื่อนไถลหลุดออกจากกัน ตะปูหรือสลักเกลียวที่ตอกยึดจะต้องรับแรงเฉือนไหล \(q\) ต่อหนึ่งหน่วยความยาว",
        "formulas": r"""
\begin{aligned}
\text{Shear Flow: } & q = \frac{VQ}{I} \quad (\text{หน่วย N/mm หรือ kN/m}) \\
\text{Fastener Capacity: } & F_{\text{resistance}} = m \cdot F_{\text{allow}} \quad (m = \text{จำนวนแถวของตะปู}) \\
\text{Nail Pitch: } & s_{\max} \le \frac{m F_{\text{allow}}}{q} \quad (\text{ปัดเศษลงเสมอ!})
\end{aligned}
""",
        "traps": "หากคำนวณระยะห่างตะปูได้ \(94.7\text{ mm}\) ต้องปัดเศษลงเป็น \(90\text{ mm}\) ห้ามปัดขึ้นเป็น \(100\text{ mm}\) เพราะจะทำให้ตะปูรับแรงเกินกำลังวิกฤต",
        "prob_idx": 8
    },
    {
        "id": "lec16",
        "title": "ครั้งที่ 16: การโก่งเดาะของเสาอุดมคติ (Euler Buckling of Columns)",
        "sub": "แรงเดาะวิกฤต \(P_{cr}\) · อัตราส่วนความชะลูด \(\lambda = KL/r\) · การตรวจสอบ 2 แกน \(x, y\)",
        "principles": "เสายาวที่รับแรงอัดตามแนวแกนจะพังทลายจากการสูญเสียเสถียรภาพทางเรขาคณิต (โก่งงอด้านข้าง) ก่อนที่หน่วยแรงจะถึงขีดจำกัดความแข็งแรงของวัสดุ ตามทฤษฎีเสาของออยเลอร์",
        "formulas": r"""
\begin{aligned}
\text{Critical Buckling Load: } & P_{cr} = \frac{\pi^2 EI}{(KL)^2} \\
\text{Critical Stress: } & \sigma_{cr} = \frac{P_{cr}}{A} = \frac{\pi^2 E}{(KL/r)^2} \\
\text{Radius of Gyration: } & r = \sqrt{\frac{I}{A}} \\
\text{Effective Length Factor: } & K = 1.0\text{ (Pin-Pin)}, 0.5\text{ (Fix-Fix)}, 0.7\text{ (Fix-Pin)}, 2.0\text{ (Fix-Free)}
\end{aligned}
""",
        "traps": "ต้องตรวจสอบทั้งแกน \(x\) และแกน \(y\) เสมอ เสาจะโก่งเดาะรอบแกนที่มีความชะลูด \(\frac{KL}{r}\) สูงกว่าเสมอ (แกนอ่อน)",
        "prob_idx": 9
    },
    {
        "id": "bonus",
        "title": "โบนัส: ความเค้นผสม 3 มิติ และวงกลมมอร์ (Combined Stress & Mohr's Circle)",
        "sub": "การรวมความเค้นตั้งฉากและเฉือน · Principal Stresses · Maximum In-Plane Shear",
        "principles": "ชิ้นส่วนวิศวกรรมที่รับแรงหลายรูปแบบพร้อมกัน (แรงตามแนวแกน โมเมนต์ดัด แรงบิด และแรงเฉือน) จะต้องรวมหน่วยแรงที่ระนาบพิจารณา แล้วหมุนแกนเพื่อหาหน่วยแรงหลักดึง/อัดสูงสุดและหน่วยแรงเฉือนสูงสุด",
        "formulas": r"""
\begin{aligned}
\text{Normal Stress Sum: } & \sigma_{\text{total}} = \frac{P}{A} \pm \frac{My}{I} \\
\text{Shear Stress Sum: } & \tau_{\text{total}} = \frac{Tr}{J} \pm \frac{VQ}{It} \\
\text{Principal Stresses: } & \sigma_{1,2} = \frac{\sigma_x + \sigma_y}{2} \pm \sqrt{\left(\frac{\sigma_x-\sigma_y}{2}\right)^2 + \tau_{xy}^2} \\
\text{Max Shear Stress: } & \tau_{\max} = R = \sqrt{\left(\frac{\sigma_x-\sigma_y}{2}\right)^2 + \tau_{xy}^2}
\end{aligned}
""",
        "traps": "ระวังการรวมเครื่องหมายของ \(\sigma\) จากแรงดึง \(P/A\) และโมเมนต์ดัด \(My/I\) ต้องเช็กว่าเป็นดึงหรืออัดที่จุดที่กำลังพิจารณา",
        "prob_idx": -1
    }
]

for l in LECTURES:
    prob_html = ""
    if l["prob_idx"] >= 0 and l["prob_idx"] < len(PROBLEMS):
        p = PROBLEMS[l["prob_idx"]]
        # Build exam rows
        prob_html = f'''
  <h3 class="grp">ตัวอย่างโจทย์สอบจริงและวิธีทำ 4 ขั้นตอน (จากชีท Solid Ja E Here)</h3>
  <div class="exam">
    <div class="row">
      <div class="lab">โจทย์และข้อมูล</div>
      <div>
        <p><b>{p['topic']}</b></p>
        <p class="given">{p['given'].strip()}</p>
      </div>
    </div>
    <div class="row">
      <div class="lab">วิธีทำทีละขั้น</div>
      <div>
        <div class="math-content overflow-x-auto text-[15px]">
          {p['solution'].strip()}
        </div>
      </div>
    </div>
    <div class="row">
      <div class="lab">คำตอบสุดท้าย</div>
      <div>
        <div class="fin">ตรวจสอบคำตอบและหน่วยตามมาตรฐานวิศวกรรมเรียบร้อย</div>
      </div>
    </div>
  </div>
'''

    sec_html = f'''
<section id="{l['id']}">
  <header class="top">
    <p class="kick">วิศวกรรมโยธา · เนื้อหาสอบปลายภาค</p>
    <h1>{l['title']}</h1>
    <p class="sub">{l['sub']}</p>
    <p class="by">CE 211 กลศาสตร์วัสดุ · มหาวิทยาลัยธรรมศาสตร์</p>
    <p class="pracnote">โหมดฝึกเปิดอยู่: ซ่อนวิธีทำไว้ แตะแต่ละขั้นเพื่อดู (ลองเขียนเองก่อน) กดปุ่ม "ฝึก" อีกครั้งเพื่อปิด</p>
  </header>

  <h2 class="prob"><span class="tag">แก่นแท้</span>มโนทัศน์และเหตุผลทางฟิสิกส์ (First Principles)</h2>
  <div class="stmt">
    <p>{l['principles']}</p>
  </div>

  <h3 class="grp">สมการควบคุมหลัก (Governing Formulas)</h3>
  <div class="formula-card-body" style="padding:14px 18px;margin:12px 0;">
    {l['formulas'].strip()}
  </div>

  <div class="formula-card-trap" style="margin:16px 0;font-size:14px;">
    {l['traps']}
  </div>

  {prob_html}

  <div class="pn">
    <a href="#sum">← สรุปภาพรวม</a>
    <a href="#solidja">ไปที่ชีท Solid Ja E Here รวม 10 ข้อ →</a>
  </div>
</section>
'''
    html_parts.append(sec_html)

# ==========================================
# PART 5: Section #solidja (10 Master Problems)
# ==========================================
solid_prob_cards = []
for idx, p in enumerate(PROBLEMS):
    sheet_no = idx + 1
    # Build scanned image tags
    img_tags = []
    for img_name in p["pages"]:
        img_tags.append(f'''
        <div style="background:var(--hover);padding:10px;border-radius:4px;border:1px solid var(--rule);text-align:center;">
          <div style="font-size:12px;color:var(--gray);margin-bottom:6px;">ต้นฉบับชีท: {img_name}</div>
          <a href="assets/pages/{img_name}" target="_blank" rel="noopener noreferrer">
            <img src="assets/pages/{img_name}" alt="ต้นฉบับ {p['num']}" style="width:100%;max-height:450px;object-fit:contain;border:1px solid var(--rule);border-radius:3px;">
          </a>
        </div>
        ''')

    card = f'''
  <h3 class="grp" id="{p['id']}">[{p['num']}] {p['topic']} <small style="color:var(--gray);font-weight:400;">(ชีทหน้า {', '.join([x.replace('page_', '').replace('.png', '') for x in p['pages']])})</small></h3>
  <p style="font-size:15px;color:var(--gray);margin-bottom:12px;">{p['summary']}</p>
  
  <div class="exam">
    <div class="row">
      <div class="lab">1. ข้อมูลที่กำหนด</div>
      <div>
        <p class="given" style="white-space:pre-line;">{p['given'].strip()}</p>
      </div>
    </div>
    <div class="row">
      <div class="lab">2. สเต็ปวิธีทำ</div>
      <div>
        <div class="math-content overflow-x-auto text-[15px]">
          {p['solution'].strip()}
        </div>
      </div>
    </div>
    <div class="row">
      <div class="lab">3. จุดดักคะแนน</div>
      <div>
        <div class="formula-card-trap" style="margin:4px 0;">{p['exam_trap']}</div>
      </div>
    </div>
    <div class="row">
      <div class="lab">4. ต้นฉบับลายมือ</div>
      <div>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:12px;margin-top:6px;">
          {''.join(img_tags)}
        </div>
      </div>
    </div>
  </div>
'''
    solid_prob_cards.append(card)

html_parts.append(f'''
<section id="solidja">
  <header class="top">
    <p class="kick">ถอดรหัสเฉลยข้อสอบฉบับลายมือ 21 หน้าเต็ม</p>
    <h1>คลังข้อสอบชีท Solid Ja E Here (10 ข้อแม่บท)</h1>
    <p class="sub">แปลงเป็นตัวพิมพ์ดิจิทัลและสูตร \(\LaTeX\) คมชัด 100% พร้อมรูปสแกนต้นฉบับ</p>
    <p class="by">CE 211 กลศาสตร์วัสดุ · ภาควิชาวิศวกรรมโยธา มหาวิทยาลัยธรรมศาสตร์</p>
    <p class="pracnote">โหมดฝึกเปิดอยู่: ซ่อนวิธีทำไว้ แตะแต่ละขั้นเพื่อดู (ลองเขียนเองก่อน) กดปุ่ม "ฝึก" อีกครั้งเพื่อปิด</p>
  </header>

  <h2 class="prob"><span class="tag">ชีทลายมือ</span>รวมเฉลยข้อสอบจริง 10 ข้อหลัก</h2>
  <div class="stmt">
    <p>ถอดรหัสจากชีทข้อสอบจริง 21 หน้าเต็ม แปลงเป็นภาษาเขียนและสูตรคณิตศาสตร์ \(\LaTeX\) ทุกบรรทัด มีระบบโหมดฝึกซ่อนเฉลย และสามารถคลิกดูรูปสแกนต้นฉบับเปรียบเทียบได้ทันที</p>
  </div>

  {''.join(solid_prob_cards)}

  <div class="pn">
    <a href="#sum">← สรุปภาพรวม</a>
    <a href="#calc">ไปที่เครื่องคิดเลขวิศวกรรม →</a>
  </div>
</section>
''')

# ==========================================
# PART 6: Section #calc (Calculators)
# ==========================================
html_parts.append(r'''
<section id="calc">
  <header class="top">
    <p class="kick">เครื่องมือคำนวณและตรวจสอบผลลัพธ์ตัวเลข</p>
    <h1>เครื่องคำนวณสูตรหลักกลศาสตร์วัสดุ</h1>
    <p class="sub">ตรวจคำตอบการบ้าน · ตรวจผลคำนวณข้อสอบ · ทดลองเปลี่ยนตัวแปร</p>
    <p class="by">CE 211 กลศาสตร์วัสดุ · มหาวิทยาลัยธรรมศาสตร์</p>
  </header>

  <h2 class="prob"><span class="tag">คำนวณสด</span>เครื่องคิดเลขวิศวกรรม 5 บทหลัก</h2>
  
  <div class="formula-grid" style="grid-template-columns:1fr;gap:20px;">
    <!-- Torsion Calculator -->
    <div class="formula-card">
      <div class="formula-card-head">
        <span class="formula-card-title">1. เครื่องคำนวณการบิดเพลากลม (Torsion Calculator)</span>
        <span class="formula-card-badge">\(\tau = \frac{Tc}{J}, \phi = \frac{TL}{GJ}\)</span>
      </div>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:10px;padding:10px 0;">
        <div>
          <label style="font-size:13px;font-weight:600;">แรงบิด \(T\) (\(\text{N}\cdot\text{m}\)):</label>
          <input type="number" id="c-tor-t" value="1200" style="width:100%;padding:6px;border:1px solid var(--rule);border-radius:4px;background:var(--bg);color:var(--ink);">
        </div>
        <div>
          <label style="font-size:13px;font-weight:600;">รัศมีเพลา \(c\) (\(\text{mm}\)):</label>
          <input type="number" id="c-tor-c" value="25" style="width:100%;padding:6px;border:1px solid var(--rule);border-radius:4px;background:var(--bg);color:var(--ink);">
        </div>
        <div>
          <label style="font-size:13px;font-weight:600;">ความยาว \(L\) (\(\text{m}\)):</label>
          <input type="number" id="c-tor-l" value="1.5" step="0.1" style="width:100%;padding:6px;border:1px solid var(--rule);border-radius:4px;background:var(--bg);color:var(--ink);">
        </div>
        <div>
          <label style="font-size:13px;font-weight:600;">มอดุลัสเฉือน \(G\) (\(\text{GPa}\)):</label>
          <input type="number" id="c-tor-g" value="77" style="width:100%;padding:6px;border:1px solid var(--rule);border-radius:4px;background:var(--bg);color:var(--ink);">
        </div>
      </div>
      <button onclick="calcTor()" style="padding:8px 16px;background:var(--navy);color:#fff;border:0;border-radius:4px;cursor:pointer;font-weight:600;">คำนวณ \(\tau_{\max}\) และ \(\phi\)</button>
      <div id="res-tor" style="margin-top:10px;font-size:15px;color:var(--blue);font-weight:600;">ผลลัพธ์: \(\tau_{\max} = 39.11\text{ MPa}, \phi = 0.0381\text{ rad} \ (2.18^\circ)\)</div>
    </div>

    <!-- Bending Calculator -->
    <div class="formula-card">
      <div class="formula-card-head">
        <span class="formula-card-title">2. เครื่องคำนวณความเค้นดัด (Flexure Stress Calculator)</span>
        <span class="formula-card-badge">\(\sigma = \frac{My}{I}\)</span>
      </div>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:10px;padding:10px 0;">
        <div>
          <label style="font-size:13px;font-weight:600;">โมเมนต์ \(M\) (\(\text{kN}\cdot\text{m}\)):</label>
          <input type="number" id="c-bnd-m" value="45" style="width:100%;padding:6px;border:1px solid var(--rule);border-radius:4px;background:var(--bg);color:var(--ink);">
        </div>
        <div>
          <label style="font-size:13px;font-weight:600;">ระยะห่าง \(y\) (\(\text{mm}\)):</label>
          <input type="number" id="c-bnd-y" value="120" style="width:100%;padding:6px;border:1px solid var(--rule);border-radius:4px;background:var(--bg);color:var(--ink);">
        </div>
        <div>
          <label style="font-size:13px;font-weight:600;">Inertia \(I\) (\(\times 10^6\text{ mm}^4\)):</label>
          <input type="number" id="c-bnd-i" value="65.4" step="0.1" style="width:100%;padding:6px;border:1px solid var(--rule);border-radius:4px;background:var(--bg);color:var(--ink);">
        </div>
      </div>
      <button onclick="calcBnd()" style="padding:8px 16px;background:var(--navy);color:#fff;border:0;border-radius:4px;cursor:pointer;font-weight:600;">คำนวณ \(\sigma\)</button>
      <div id="res-bnd" style="margin-top:10px;font-size:15px;color:var(--blue);font-weight:600;">ผลลัพธ์: \(\sigma = 82.57\text{ MPa}\)</div>
    </div>
  </div>

  <div class="pn">
    <a href="#solidja">← ชีท Solid Ja E Here</a>
    <a href="#ref">คำศัพท์ &amp; ตารางอ้างอิง →</a>
  </div>
</section>
''')

# ==========================================
# PART 7: Section #ref (Vocabulary & Traps)
# ==========================================
html_parts.append(r'''
<section id="ref">
  <header class="top">
    <p class="kick">คลังคำศัพท์วิศวกรรมและจุดควรระวังในการสอบ</p>
    <h1>คำศัพท์และจุดดักคะแนนสอบปลายภาค</h1>
    <p class="sub">Glossary of Terms · Common Exam Traps Matrix</p>
    <p class="by">CE 211 กลศาสตร์วัสดุ · ภาควิชาวิศวกรรมโยธา มหาวิทยาลัยธรรมศาสตร์</p>
  </header>

  <h2 class="prob"><span class="tag">คำศัพท์</span>ตารางคำศัพท์เทคนิคภาษาไทย-อังกฤษ</h2>
  <div class="tw">
    <table>
      <thead>
        <tr><th>คำศัพท์ภาษาอังกฤษ</th><th>ความหมายภาษาไทย</th><th>บทที่เกี่ยวข้อง</th></tr>
      </thead>
      <tbody>
        <tr><td>Polar Moment of Inertia (\(J\))</td><td>โมเมนต์ความเฉื่อยเชิงขั้ว (ความต้านทานต่อการบิด)</td><td>การบิด (บทที่ 4)</td></tr>
        <tr><td>Angle of Twist (\(\phi\))</td><td>มุมบิดสัมพัทธ์ระหว่างหน้าตัด (เรเดียน)</td><td>การบิด (บทที่ 4)</td></tr>
        <tr><td>Neutral Axis (NA)</td><td>แกนสะเทิน (แกนที่หน่วยแรงดัดเป็นศูนย์)</td><td>การดัด (บทที่ 5)</td></tr>
        <tr><td>Flexure Formula</td><td>สูตรการดัด (\(\sigma = -My/I\))</td><td>การดัด (บทที่ 5)</td></tr>
        <tr><td>Transformed Section</td><td>หน้าตัดแปลง (ขยายความกว้าง \(b'=nb\))</td><td>หน้าตัดผสม (บทที่ 5)</td></tr>
        <tr><td>Modular Ratio (\(n\))</td><td>อัตราส่วนมอดุลัส (\(n = E_2/E_1\))</td><td>หน้าตัดผสม (บทที่ 5)</td></tr>
        <tr><td>First Moment of Area (\(Q\))</td><td>โมเมนต์อันดับหนึ่งของพื้นที่ตัดขาด (\(Q = A'\bar{y}'\))</td><td>แรงเฉือน (บทที่ 6)</td></tr>
        <tr><td>Shear Flow (\(q\))</td><td>การเฉือนไหล (แรงเฉือนต่อความยาวตามแนวแกน)</td><td>แรงเฉือน (บทที่ 6)</td></tr>
        <tr><td>Euler Buckling Load (\(P_{cr}\))</td><td>แรงโก่งเดาะวิกฤตของเสาอุดมคติ</td><td>เสาโก่งเดาะ (บทที่ 7)</td></tr>
        <tr><td>Slenderness Ratio (\(\lambda\))</td><td>อัตราส่วนความชะลูด (\(\lambda = KL/r\))</td><td>เสาโก่งเดาะ (บทที่ 7)</td></tr>
        <tr><td>Radius of Gyration (\(r\))</td><td>รัศมีไจเรชัน (\(r = \sqrt{I/A}\))</td><td>เสาโก่งเดาะ (บทที่ 7)</td></tr>
        <tr><td>Principal Stresses (\(\sigma_1, \sigma_2\))</td><td>หน่วยแรงดึง/อัดหลัก (บนระนาบที่หน่วยแรงเฉือนเป็นศูนย์)</td><td>ความเค้นผสม</td></tr>
      </tbody>
    </table>
  </div>

  <div class="pn">
    <a href="#calc">← คิดเลข</a>
    <a href="#sum">กลับสู่หน้าแรก (สรุปภาพรวม) →</a>
  </div>

  <p class="foot">
    CE 211 กลศาสตร์วัสดุ · ภาควิชาวิศวกรรมโยธา คณะวิศวกรรมศาสตร์ มหาวิทยาลัยธรรมศาสตร์<br>
    จัดทำและเรียบเรียงโดย <b>ธนภรณ์ นพรัตน์ (Thanaporn Nopparat)</b><br>
    เรนเดอร์สูตรคณิตศาสตร์ด้วย KaTeX · ออกแบบอินเทอร์เฟซตามสถาปัตยกรรม CE 272 Portal
  </p>
</section>

</main>

<!-- KaTeX Scripts with Auto-Render -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.js" defer></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/contrib/auto-render.min.js" defer></script>

<script>
  function calcTor() {
    var T = parseFloat(document.getElementById('c-tor-t').value) || 0;
    var c = parseFloat(document.getElementById('c-tor-c').value) || 0;
    var L = parseFloat(document.getElementById('c-tor-l').value) || 0;
    var G = parseFloat(document.getElementById('c-tor-g').value) || 0;
    var J = (Math.PI * Math.pow(c, 4)) / 2;
    var tau = (T * 1000 * c) / J;
    var phi = (T * 1000 * L * 1000) / (G * 1000 * J);
    var deg = phi * 180 / Math.PI;
    document.getElementById('res-tor').innerText = 'ผลลัพธ์: tau = ' + tau.toFixed(2) + ' MPa, phi = ' + phi.toFixed(4) + ' rad (' + deg.toFixed(2) + ' deg)';
  }

  function calcBnd() {
    var M = parseFloat(document.getElementById('c-bnd-m').value) || 0;
    var y = parseFloat(document.getElementById('c-bnd-y').value) || 0;
    var I = parseFloat(document.getElementById('c-bnd-i').value) || 0;
    var sigma = (M * 1e6 * y) / (I * 1e6);
    document.getElementById('res-bnd').innerText = 'ผลลัพธ์: sigma = ' + sigma.toFixed(2) + ' MPa';
  }
</script>

<!-- Main App Logic: Hash Routing, Practice Mode, Theme Switcher -->
<script src="assets/app.js?v=20261123" defer></script>

</body>
</html>
''')

# Write out the new index.html
output_file = '/Users/thanaporn/.gemini/antigravity/scratch/mechanics-of-materials-final/index.html'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(''.join(html_parts))

print(f"Successfully generated CE272-style index.html! Size: {os.path.getsize(output_file)} bytes")
