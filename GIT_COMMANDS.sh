#!/bin/bash
# 🚀 คำสั่งอัปโหลด PulseBar ขึ้น GitHub
# วิธีใช้: เปิด Terminal แล้ววางคำสั่งทีละบรรทัด

cd /Users/tonyk/Documents/AI\ LCI/crypto-menu-bar

# 1. เริ่มต้น Git (ถ้ายังไม่เคยทำ)
git init

# 2. เพิ่มไฟล์ทั้งหมด
git add .

# 3. บันทึกการเปลี่ยนแปลง
git commit -m "🚀 Initial commit: PulseBar v1.0

- Real-time crypto, gold & stock indices tracker
- macOS menu bar app with Python
- Beautiful landing page with 3 themes
- Price alerts & notifications"

# 4. เชื่อมต่อกับ GitHub
git remote add origin https://github.com/danupolai-alt/pulsebar.git

# 5. อัปโหลดขึ้น GitHub
git branch -M main
git push -u origin main

echo "✅ Push เสร็จแล้ว!"
echo "🌐 ไปตั้งค่า GitHub Pages ที่: https://github.com/danupolai-alt/pulsebar/settings/pages"
