# 🚀 Trading Menu Bar

แอปแสดงราคา **Crypto + ทองคำ + ดัชนีหุ้น** บน macOS Menu Bar สำหรับคุณเก้ 💕

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-macOS-lightgrey.svg)
![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-brightgreen.svg)

## 🌐 Live Website

**[ดูเว็บไซต์ →](https://yourusername.github.io/trading-menu-bar)**

Landing page สวยๆ สไตล์ pricebar.coinbx.com พร้อมให้ deploy บน GitHub Pages แล้ว!

## ✨ ฟีเจอร์

- 📊 **แสดงราคา Real-time** - Crypto จาก Binance, ทอง/ดัชนีจาก Yahoo Finance
- 🔔 **แจ้งเตือนราคา** - ตั้งเป้าหมายราคาแล้วแจ้งเตือน
- ⚡ **เบา + เร็ว** - ใช้ Python ไม่หนักเครื่อง
- 🎯 **เลือกแสดงได้** - สูงสุด 3 รายการบน Menu Bar

## 📦 รายการที่รองรับ

### 🪙 Crypto (Binance)
| เหรียญ | สัญลักษณ์ |
|--------|----------|
| Bitcoin | ₿ |
| Ethereum | Ξ |
| Solana | ◎ |
| BNB | 🔶 |
| XRP | ✕ |
| Cardano | ₳ |
| Dogecoin | Ð |
| Avalanche | 🔺 |

### 📈 Forex & Indices (Yahoo Finance)
| รายการ | สัญลักษณ์ | รายละเอียด |
|--------|----------|-----------|
| **XAUUSD** | 🥇 | ทองคำ Spot (Gold) |
| **US30** | 📊 | Dow Jones Industrial |
| **NAS100** | 📈 | Nasdaq 100 |

> 💡 **หมายเหตุ**: COMEX:GC1! คือ Gold Futures เหมือน XAUUSD ค่ะ ใช้ `GC=F` จาก Yahoo Finance

## 🛠️ วิธีติดตั้ง

### 1. ติดตั้ง Python (ถ้ายังไม่มี)
```bash
brew install python3
```

### 2. ติดตั้ง Dependencies
```bash
cd crypto-menu-bar
pip3 install -r requirements.txt
```

### 3. รันแอป
```bash
python3 main.py
```

แอปจะขึ้นที่ Menu Bar (ขวาบน) ค่ะ ✨

## 📱 วิธีใช้งาน

### เลือกรายการแสดง
- คลิกที่ icon บน Menu Bar
- เลือก/ยกเลิกจากเมนู (✅ = แสดง, ⬜️ = ไม่แสดง)
- สูงสุด 3 รายการพร้อมกัน

### ตั้งค่าแจ้งเตือน
1. คลิก "🔔 ตั้งค่าแจ้งเตือน"
2. พิมพ์รูปแบบ:
   - `XAUUSD 2800` (ทองคำ)
   - `BTC 85000` (บิทคอยน์)
   - `US30 42000` (ดาวโจนส์)
   - `NAS100 19500` (แนสแด็ก)
3. รอแจ้งเตือนเมื่อถึงราคา!

### ดูการแจ้งเตือน
- คลิก "📋 ดูการแจ้งเตือน" เพื่อดูรายการที่ตั้งไว้

## 📦 Build เป็น .app (optional)

```bash
pip3 install py2app
python3 setup.py py2app
```

ไฟล์จะอยู่ที่ `dist/Trading Menu Bar.app` ค่ะ

## 🌐 Deploy GitHub Pages

โฟลเดอร์ `web/` คือ Landing Page สวยๆ สำหรับโปรเจกต์

### วิธี Deploy:

1. **Push ขึ้น GitHub:**
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/danupolai-alt/pulsebar.git
git push -u origin main
```

2. **ตั้งค่า GitHub Pages:**
   - ไปที่ Settings → Pages
   - Source: Deploy from a branch
   - Branch: main / root
   - กด Save

3. **รอ 1-2 นาที** แล้วเข้า `https://yourusername.github.io/trading-menu-bar`

> 💡 **Tip**: ถ้าอยากให้ URL เป็น `username.github.io` ให้ตั้งชื่อ repo เป็น `yourusername.github.io`

## 📝 โครงสร้างไฟล์

```
crypto-menu-bar/
├── main.py              # โค้ดหลัก
├── requirements.txt     # Dependencies
├── setup.py            # สำหรับ build .app
├── README.md           # ไฟล์นี้
└── web/                # 🌐 Landing Page
    ├── index.html      # หน้าเว็บหลัก
    ├── styles.css      # สไตล์ (Dark theme)
    └── script.js       # Animation & interaction
```

## 🎨 Customization

### แก้ไขเว็บไซต์:
- แก้ชื่อ/ข้อความใน `web/index.html`
- แก้สี/สไตล์ใน `web/styles.css` (CSS Variables ที่ `:root`)
- แก้ลิงก์ GitHub ใน `index.html` และ `script.js`

### แก้ไขแอป:
- เพิ่มเหรียญ: แก้ `self.crypto` ใน `main.py`
- เพิ่มดัชนี: แก้ `self.forex` ใน `main.py`

## ⚠️ หมายเหตุ

- ต้องเชื่อมต่ออินเทอร์เน็ตตลอดเวลา
- **Crypto**: Binance Public API (ไม่ต้องใส่ API Key)
- **Forex/Indices**: Yahoo Finance (ใช้ yfinance)
- ราคาอาจมีความล่าช้าเล็กน้อย (ไม่เหมาะกับเทรด high-frequency)
- อัปเดตทุก 15 วินาที (ป้องกัน rate limit)

## 📄 License

MIT License - ใช้ฟรี แก้ไขได้ แจกจ่ายได้!

---

สร้างด้วย 💕 โดยคิม สำหรับคุณเก้
