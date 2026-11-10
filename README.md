# 📚 กลศาสตร์วัสดุ (Mechanics of Materials) - คัมภีร์สรุปสอบปลายภาค & รวมคลิปเรียนตรงจุด

> 🏛️ **คณะวิศวกรรมศาสตร์ มหาวิทยาลัยธรรมศาสตร์ (Thammasat University)**  
> 🎯 **เนื้อหาสอบปลายภาค ครอบคลุมครั้งที่ 9 ถึง 16 และโบนัสความเค้นผสม 3 มิติ**  
> 🌐 **Live Web Hub:** [ดูผ่าน GitHub Pages หรือเปิดไฟล์ `index.html`](./index.html)

---

## 📌 สารบัญเนื้อหาและคลิปเรียน (Lectures 9–16)

| ครั้งที่ | หัวข้อสอบ | บทที่ | สูตรหัวใจสำคัญ | แหล่งเรียนรู้ YouTube แนะนำ |
| :---: | :--- | :---: | :--- | :--- |
| **ปูพื้น** | เซนทรอยด์ ($\bar{y}$) & โมเมนต์ความเฉื่อย ($I$) | พื้นฐาน | $\bar{y} = \frac{\sum Ay}{\sum A}$, $I = \sum (\bar{I} + Ad^2)$ | P'BIG ETC TUTOR, be-engineer |
| **9** | การบิด (1/2): เพลากลม มุมบิด และระบบเฟืองทด | 4 | $\tau = \frac{Tr}{J}$, $\phi = \sum \frac{TL}{GJ}$, $P = T\omega$ | be-engineer, อ.ไพโรจน์, อ.สิทธิชัย |
| **10** | การบิด (2/2): ปัญหาอินดีเทอร์มิเนตเชิงสถิต | 4 | $\sum T = 0$ คู่กับ $\phi_{\text{left}} = \phi_{\text{right}}$ | อ.สิทธิชัย, อ.ไพโรจน์ |
| **11** | การดัด: หน่วยแรงดัด และสูตรการดัด | 5 | $\sigma = -\frac{My}{I}$, $\sigma_{\max} = \frac{Mc}{I}$ | be-engineer, อ.ไพโรจน์, อ.สิทธิชัย, อ.ณัฐวุฒิ |
| **12** | การแอ่นตัวของคาน (Beam Deflection) | 5 | $EI v'' = M(x)$, Moment-Area Theorem | P'BIG ETC TUTOR, อ.ไพโรจน์, อ.ณัฐวุฒิ |
| **13** | การดัดหน้าตัดผสม (Transformed-Section Method) | 5 | $b' = n \cdot b$, $\sigma_2 = n \frac{My}{I_T}$ | อ.ไพโรจน์, อ.สิทธิชัย |
| **14** | แรงเฉือนตามขวาง และสูตรการเฉือน | 6 | $\tau = \frac{VQ}{It}$, $Q = A' \bar{y}'$ | be-engineer, อ.ไพโรจน์, P'BIG ETC TUTOR |
| **15** | การเฉือนไหลของหน้าตัดประกอบ & รอยต่อตะปู | 6 | $q = \frac{VQ}{I}$, $s_{\max} \le \frac{m F_{\text{allow}}}{q}$ | อ.สิทธิชัย, อ.ไพโรจน์, P'BIG ETC TUTOR |
| **16** | การโก่งเดาะของเสาอุดมคติ (Euler Buckling) | 7 | $P_{cr} = \frac{\pi^2 EI}{(KL)^2}$, $\sigma_{cr} = \frac{\pi^2 E}{(KL/r)^2}$ | อ.ไพโรจน์, อ.สิทธิชัย, อ.ณัฐวุฒิ |
| **โบนัส** | ความเค้นผสม 3 มิติ & วงกลมมอร์ (Mohr's Circle) | รวม | $\sigma_{1,2} = \sigma_{\text{avg}} \pm R$, $\tau_{\max} = R$ | P'BIG ETC TUTOR, be-engineer, etctutor |

---

## ⚡ ฟีเจอร์เด่นของเว็บแอปพลิเคชัน (`index.html`)

1. **Direct Learning Links:** คลิกเดียวเปิดดูคลิปติวตรงจุดใน YouTube กว่า 30 คลิป พร้อมแท็กแยกช่องติวเตอร์และอาจารย์ผู้สอน
2. **Interactive Study Checklist:** บันทึกความคืบหน้าการอ่านหนังสือในเครื่อง (`localStorage`) พร้อม Progress Bar แสดง % ความพร้อมก่อนเข้าห้องสอบ
3. **5 Engineering Quick Calculators:**
   * Torsion Calculator ($\tau, \phi$)
   * Flexure Stress Calculator ($\sigma = My/I$)
   * Transverse Shear & Nail Pitch Calculator ($\tau, q, s_{\max}$)
   * Euler Buckling Critical Load Calculator ($P_{cr}, \sigma_{cr}$)
   * Mohr's Circle Principal Stresses Calculator ($\sigma_1, \sigma_2, \tau_{\max}$)
4. **MathJax 3 LaTeX Math:** แสดงสูตรและสมการคณิตศาสตร์คมชัดตามมาตรฐานวิศวกรรม
5. **Dark / Light Mode:** สลับธีมถนอมสายตาสำหรับอ่านทบทวนตอนกลางคืน

---

## 🚀 วิธีเปิดใช้งาน

เพียงเปิดไฟล์ `index.html` บนเว็บเบราว์เซอร์ใดก็ได้ (Chrome, Safari, Edge, Firefox) หรือเปิดผ่าน GitHub Pages:
```bash
open index.html
```
