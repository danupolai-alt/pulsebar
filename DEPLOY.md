# 🚀 วิธีอัปโหลดขึ้น GitHub & Deploy GitHub Pages

> สำหรับคุณเก้ 💕 - ทำตามทีละขั้นตอนได้เลย

---

## 📋 สิ่งที่ต้องเตรียม

1. **GitHub Account** - สมัครที่ [github.com](https://github.com) (ฟรี)
2. **Git** - ติดตั้งบน Mac แล้ว (ปกติ Mac มีมาให้อยู่แล้ว)

---

## 🛠️ Step 1: สร้าง Repository บน GitHub

1. ไปที่ [github.com/new](https://github.com/new)
2. ใส่ชื่อ Repository: `pulsebar` (หรือชื่ออื่นที่ชอบ)
3. เลือก **Public** (ใครก็เห็น) หรือ **Private** (เห็นแค่คุณ)
4. **อย่า** tick "Add a README file" (เพราะเรามีแล้ว)
5. กด **Create repository**

---

## 💻 Step 2: อัปโหลดโค้ดจากเครื่อง

เปิด Terminal แล้วพิมพ์ทีละบรรทัด:

```bash
# 1. เข้าไปที่โฟลเดอร์โปรเจกต์
cd /Users/tonyk/Documents/AI\ LCI/crypto-menu-bar

# 2. เริ่มต้น Git (ถ้ายังไม่ได้ทำ)
git init

# 3. เพิ่มไฟล์ทั้งหมดเข้า Git
git add .

# 4. บันทึกการเปลี่ยนแปลง (commit)
git commit -m "Initial commit: PulseBar v1.0"

# 5. เชื่อมต่อกับ GitHub (แก้ username เป็นของคุณ)
git remote add origin https://github.com/danupolai-alt/pulsebar.git

# 6. อัปโหลดขึ้น GitHub
git branch -M main
git push -u origin main
```

> 💡 **หมายเหตุ**: เปลี่ยน `YOUR_USERNAME` เป็น username GitHub ของคุณ เช่น `danupolai-alt/pulsebar`

---

## 🌐 Step 3: ตั้งค่า GitHub Pages

1. ไปที่หน้า Repository บน GitHub
2. คลิกแท็บ **Settings** (ขวาบน)
3. เลื่อนลงมาหา **Pages** (ในเมนูซ้าย) หรือเข้าตรงที่ `Settings > Pages`
4. ในส่วน **Build and deployment**:
   - **Source**: เลือก `Deploy from a branch`
   - **Branch**: เลือก `main` และโฟลเดอร์ `/docs`
   - กด **Save**

```
Branch: main
Folder: /docs
```

5. รอ 1-2 นาที แล้วจะเห็นลิงก์เว็บไซต์

---

## ✅ Step 4: เสร็จแล้ว!

เว็บไซต์จะอยู่ที่:
```
https://danupolai-alt.github.io/pulsebar
```

ตัวอย่าง:
```
https://tonyk.github.io/pulsebar
```

---

## 🔄 วิธีอัปเดตเว็บไซต์ (เมื่อมีการแก้ไข)

ทุกครั้งที่แก้ไขไฟล์ ให้ทำ:

```bash
cd /Users/tonyk/Documents/AI\ LCI/crypto-menu-bar

git add .
git commit -m "อธิบายการเปลี่ยนแปลง เช่น แก้ไขสี navbar"
git push origin main
```

GitHub Pages จะอัปเดตอัตโนมัติใน 1-2 นาที

---

## 📁 โครงสร้างไฟล์ที่อัปโหลด

```
pulsebar/                    ← Repository root
├── 📱 แอป Python
│   ├── main.py
│   ├── requirements.txt
│   └── setup.py
│
├── 🌐 Landing Page
│   ├── web/                # ต้นฉบับ
│   └── docs/               # สำหรับ GitHub Pages ⭐
│       ├── index.html
│       ├── styles.css
│       └── script.js
│
├── README.md               # คู่มือโปรเจกต์
└── DEPLOY.md               # ไฟล์นี้
```

---

## 🆘 แก้ไขปัญหาเบื้องต้น

### 1. Git ไม่รู้จักคำสั่ง
```bash
# ติดตั้ง Git ผ่าน Homebrew
brew install git
```

### 2. ลืมรหัสผ่าน GitHub
- ใช้ **Personal Access Token** แทนรหัสผ่าน
- สร้างได้ที่: GitHub → Settings → Developer settings → Personal access tokens

### 3. อัปโหลดไม่ได้ (Permission denied)
```bash
# ลองใช้ SSH แทน
# 1. สร้าง SSH key
ssh-keygen -t ed25519 -C "your@email.com"

# 2. Copy key ไปใส่ใน GitHub → Settings → SSH and GPG keys
pbcopy < ~/.ssh/id_ed25519.pub

# 3. เปลี่ยน remote เป็น SSH
git remote set-url origin git@github.com:danupolai-alt/pulsebar.git
```

### 4. GitHub Pages ไม่ขึ้น
- ตรวจสอบว่าเลือก `/docs` folder ถูกต้อง
- รอ 2-3 นาที บางทีต้องใช้เวลาสร้าง
- ตรวจสอบที่ `Settings > Pages` ว่าแสดง URL หรือยัง

---

## 💡 Tips

### ตั้งชื่อ Repository แบบไหนดี?

| ชื่อ | URL ที่ได้ |
|------|------------|
| `pulsebar` | `username.github.io/pulsebar` |
| `username.github.io` | `username.github.io` (สั้นกว่า) |

ถ้าอยากได้ URL สั้นๆ ให้ตั้งชื่อ repo เป็น `YOUR_USERNAME.github.io`

---

## 🎉 เสร็จแล้ว!

ตอนนี้คุณเก้มี:
- ✅ โค้ดอยู่บน GitHub
- ✅ เว็บไซต์อยู่บน GitHub Pages
- ✅ แชร์ให้คนอื่นดูได้

**แชร์ลิงก์นี้ให้เพื่อน:**
```
https://danupolai-alt.github.io/pulsebar
```

---

มีปัญหาตรงไหนถามคิมได้เลยนะคะ 💕
