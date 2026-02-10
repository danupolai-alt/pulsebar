#!/usr/bin/env python3
"""
🚀 Trading Menu Bar - แอปแสดงราคา Crypto & ทองคำ/ดัชนี บน macOS Menu Bar
สำหรับคุณเก้ 💕
"""

import rumps
import requests
import threading
import time
import yfinance as yf
from datetime import datetime

class TradingMenuBarApp(rumps.App):
    def __init__(self):
        super().__init__(
            name="TradingBar",
            title="⏳ โหลด...",
            icon=None
        )
        
        # 🪙 Crypto - จาก Binance
        self.crypto = {
            "BTCUSDT": ("BTC", "₿", "crypto"),
            "ETHUSDT": ("ETH", "Ξ", "crypto"),
            "SOLUSDT": ("SOL", "◎", "crypto"),
            "BNBUSDT": ("BNB", "🔶", "crypto"),
            "XRPUSDT": ("XRP", "✕", "crypto"),
            "ADAUSDT": ("ADA", "₳", "crypto"),
            "DOGEUSDT": ("DOGE", "Ð", "crypto"),
            "AVAXUSDT": ("AVAX", "🔺", "crypto"),
        }
        
        # 📈 Forex/Indices - จาก Yahoo Finance
        self.forex = {
            "GC=F": ("XAUUSD", "🥇", "forex"),      # ทองคำ (Gold Futures)
            "^DJI": ("US30", "📊", "forex"),        # Dow Jones
            "^NDX": ("NAS100", "📈", "forex"),      # Nasdaq 100
        }
        
        # รวมทั้งหมด
        self.all_assets = {**self.crypto, **self.forex}
        
        # รายการที่เลือกแสดงบน Menu Bar (สูงสุด 3 ตัว)
        self.selected = ["BTCUSDT", "ETHUSDT", "GC=F"]
        
        # ราคาล่าสุด
        self.prices = {}
        self.price_changes = {}
        
        # Alert settings
        self.alerts = {}  # symbol -> target_price
        
        # สร้างเมนู
        self.build_menu()
        
        # เริ่ม thread ดึงราคา
        self.running = True
        self.price_thread = threading.Thread(target=self.price_updater, daemon=True)
        self.price_thread.start()
    
    def build_menu(self):
        """สร้างเมนู"""
        menu_items = []
        
        # Header
        menu_items.append(rumps.MenuItem("🚀 ราคาตลาด", callback=None))
        menu_items.append(rumps.MenuItem("─" * 30, callback=None))
        
        # === Crypto Section ===
        menu_items.append(rumps.MenuItem("🪙 Crypto", callback=None))
        for symbol, (name, icon, type_) in self.crypto.items():
            is_selected = "✅ " if symbol in self.selected else "⬜️ "
            price_str = "---"
            if symbol in self.prices:
                price = self.prices[symbol]
                if price >= 1000:
                    price_str = f"{price:,.0f}"
                elif price >= 100:
                    price_str = f"{price:,.1f}"
                else:
                    price_str = f"{price:,.2f}"
            
            change = self.price_changes.get(symbol, 0)
            change_icon = "🟢" if change > 0 else "🔴" if change < 0 else "⚪️"
            
            item = rumps.MenuItem(
                f"{is_selected}{icon} {name}: ${price_str} {change_icon}",
                callback=lambda sender, sym=symbol: self.toggle_asset(sym)
            )
            menu_items.append(item)
        
        menu_items.append(rumps.MenuItem("─" * 30, callback=None))
        
        # === Forex/Indices Section ===
        menu_items.append(rumps.MenuItem("📈 Forex & Indices", callback=None))
        for symbol, (name, icon, type_) in self.forex.items():
            is_selected = "✅ " if symbol in self.selected else "⬜️ "
            price_str = "---"
            if symbol in self.prices:
                price = self.prices[symbol]
                # จัดรูปแบบตามชนิด
                if "XAU" in name:  # ทองคำ 2 ทศนิยม
                    price_str = f"{price:,.2f}"
                elif "US30" in name or "NAS" in name:  # ดัชนีไม่มีทศนิยม
                    price_str = f"{price:,.0f}"
                else:
                    price_str = f"{price:,.2f}"
            
            change = self.price_changes.get(symbol, 0)
            change_icon = "🟢" if change > 0 else "🔴" if change < 0 else "⚪️"
            
            item = rumps.MenuItem(
                f"{is_selected}{icon} {name}: {price_str} {change_icon}",
                callback=lambda sender, sym=symbol: self.toggle_asset(sym)
            )
            menu_items.append(item)
        
        menu_items.append(rumps.MenuItem("─" * 30, callback=None))
        
        # เมนู Alert
        menu_items.append(rumps.MenuItem("🔔 ตั้งค่าแจ้งเตือน", callback=self.set_alert))
        menu_items.append(rumps.MenuItem("📋 ดูการแจ้งเตือน", callback=self.view_alerts))
        
        menu_items.append(rumps.MenuItem("─" * 30, callback=None))
        
        # Refresh
        menu_items.append(rumps.MenuItem("🔄 รีเฟรช", callback=self.manual_refresh))
        menu_items.append(rumps.MenuItem("❌ ออก", callback=self.quit_app))
        
        self.menu = menu_items
    
    def toggle_asset(self, symbol):
        """เลือก/ยกเลิกรายการที่จะแสดง"""
        if symbol in self.selected:
            self.selected.remove(symbol)
        else:
            if len(self.selected) < 3:  # จำกัดแค่ 3 ตัว
                self.selected.append(symbol)
            else:
                rumps.notification(
                    title="⚠️ จำกัด 3 รายการ",
                    subtitle="กรุณายกเลิกรายการอื่นก่อน",
                    message="",
                    sound=False
                )
        self.build_menu()
        self.update_title()
    
    def update_title(self):
        """อัปเดตข้อความบน Menu Bar"""
        if not self.selected:
            self.title = "📊"
            return
        
        titles = []
        for symbol in self.selected:
            if symbol in self.prices:
                name = self.all_assets[symbol][0]
                price = self.prices[symbol]
                
                # จัดรูปแบบราคาตามชนิด
                if "XAU" in name:  # ทองคำ
                    price_str = f"{price:,.0f}"
                elif "US30" in name or "NAS" in name:  # ดัชนี
                    price_str = f"{price:,.0f}"
                elif price >= 1000:  # Crypto ใหญ่
                    price_str = f"{price:,.0f}"
                elif price >= 100:
                    price_str = f"{price:,.1f}"
                else:
                    price_str = f"{price:,.2f}"
                
                titles.append(f"{name} {price_str}")
        
        self.title = " | ".join(titles) if titles else "⏳"
    
    def price_updater(self):
        """Thread สำหรับดึงราคา"""
        while self.running:
            try:
                self.fetch_crypto_prices()
                self.fetch_forex_prices()
                self.check_alerts()
                rumps.deferred_call(self.update_title)
                rumps.deferred_call(self.build_menu)
                time.sleep(15)  # อัปเดตทุก 15 วินาที (Yahoo จำกัด rate)
            except Exception as e:
                print(f"Error: {e}")
                time.sleep(5)
    
    def fetch_crypto_prices(self):
        """ดึงราคา Crypto จาก Binance API"""
        try:
            url = "https://api.binance.com/api/v3/ticker/24hr"
            response = requests.get(url, timeout=10)
            data = response.json()
            
            for item in data:
                symbol = item['symbol']
                if symbol in self.crypto:
                    self.prices[symbol] = float(item['lastPrice'])
                    self.price_changes[symbol] = float(item['priceChangePercent'])
                    
        except Exception as e:
            print(f"Error fetching crypto prices: {e}")
    
    def fetch_forex_prices(self):
        """ดึงราคา Forex/Indices จาก Yahoo Finance"""
        try:
            for symbol in self.forex.keys():
                try:
                    ticker = yf.Ticker(symbol)
                    data = ticker.fast_info  # เร็วกว่า .info
                    
                    if hasattr(data, 'last_price') and data.last_price:
                        self.prices[symbol] = float(data.last_price)
                    elif hasattr(data, 'previous_close') and data.previous_close:
                        # คำนวณ % เปลี่ยนแปลง
                        current = data.last_price if hasattr(data, 'last_price') else data.regular_market_price
                        prev = data.previous_close
                        self.prices[symbol] = float(current) if current else float(prev)
                        change_pct = ((self.prices[symbol] - prev) / prev) * 100 if prev else 0
                        self.price_changes[symbol] = change_pct
                    
                    # ดึงข้อมูลเพิ่มเติม
                    hist = ticker.history(period="2d", interval="1d")
                    if len(hist) >= 2:
                        current_price = hist['Close'].iloc[-1]
                        prev_price = hist['Close'].iloc[-2]
                        change_pct = ((current_price - prev_price) / prev_price) * 100
                        
                        self.prices[symbol] = current_price
                        self.price_changes[symbol] = change_pct
                        
                except Exception as e:
                    print(f"Error fetching {symbol}: {e}")
                    continue
                    
        except Exception as e:
            print(f"Error fetching forex prices: {e}")
    
    def check_alerts(self):
        """ตรวจสอบการแจ้งเตือน"""
        for symbol, target_price in list(self.alerts.items()):
            if symbol in self.prices:
                current_price = self.prices[symbol]
                name = self.all_assets[symbol][0]
                
                # ถึงเป้าหมาย (บวกลบ 0.5%)
                if abs(current_price - target_price) / target_price < 0.005:
                    rumps.notification(
                        title=f"🚨 {name} ถึงเป้าหมาย!",
                        subtitle=f"ราคา: {current_price:,.2f}",
                        message=f"เป้าหมาย: {target_price:,.2f}",
                        sound=True
                    )
                    # ลบ alert หลังแจ้งเตือน
                    del self.alerts[symbol]
    
    def set_alert(self, sender):
        """ตั้งค่าแจ้งเตือน"""
        # รวมชื่อที่ใช้ได้
        all_names = []
        for symbol, (name, icon, type_) in self.all_assets.items():
            all_names.append(f"{name}({icon})")
        
        window = rumps.Window(
            title="🔔 ตั้งค่าแจ้งเตือน",
            message=f"เลือกรายการและใส่ราคาเป้าหมาย\n\nที่มี: {', '.join(all_names[:6])}...\n\nตัวอย่าง: XAUUSD 2800",
            default_text="",
            ok="ตั้งค่า",
            cancel="ยกเลิก"
        )
        response = window.run()
        
        if response.clicked:
            try:
                parts = response.text.strip().upper().split()
                if len(parts) == 2:
                    asset_name = parts[0]
                    target = float(parts[1])
                    
                    # หา symbol จากชื่อ
                    symbol = None
                    for sym, (name, _, _) in self.all_assets.items():
                        if name == asset_name:
                            symbol = sym
                            break
                    
                    if symbol:
                        self.alerts[symbol] = target
                        rumps.notification(
                            title=f"✅ ตั้งค่าสำเร็จ",
                            subtitle=f"{asset_name} ที่ {target:,.2f}",
                            message="จะแจ้งเตือนเมื่อถึงราคา",
                            sound=False
                        )
                    else:
                        rumps.alert("❌ ไม่พบรายการ", f"ไม่มี {asset_name} ในระบบ\n\nลอง: BTC, ETH, XAUUSD, US30, NAS100")
            except ValueError:
                rumps.alert("❌ รูปแบบไม่ถูกต้อง", "กรุณาใส่ในรูปแบบ: XAUUSD 2800")
    
    def view_alerts(self, sender):
        """ดูการแจ้งเตือนที่ตั้งไว้"""
        if not self.alerts:
            rumps.alert("📋 การแจ้งเตือน", "ไม่มีการตั้งค่าแจ้งเตือน")
            return
        
        alert_list = []
        for symbol, price in self.alerts.items():
            name = self.all_assets[symbol][0]
            current = self.prices.get(symbol, 0)
            alert_list.append(f"• {name}: {price:,.2f} (ตอนนี้: {current:,.2f})")
        
        rumps.alert("📋 การแจ้งเตือนที่ตั้งไว้", "\n".join(alert_list))
    
    def manual_refresh(self, sender):
        """รีเฟรชข้อมูลด้วยตนเอง"""
        threading.Thread(target=self.fetch_crypto_prices, daemon=True).start()
        threading.Thread(target=self.fetch_forex_prices, daemon=True).start()
        self.update_title()
        rumps.notification(
            title="🔄 รีเฟรชแล้ว",
            subtitle="อัปเดตราคาล่าสุด",
            message="",
            sound=False
        )
    
    def quit_app(self, sender):
        """ปิดแอป"""
        self.running = False
        rumps.quit_application()


if __name__ == "__main__":
    app = TradingMenuBarApp()
    app.run()
