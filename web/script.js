// ===== Language Management =====
const LangManager = {
    currentLang: 'en',
    
    init() {
        const savedLang = localStorage.getItem('lang') || 'en';
        this.setLang(savedLang);
        this.setupEventListeners();
    },
    
    setupEventListeners() {
        const langToggle = document.getElementById('langToggle');
        if (langToggle) {
            langToggle.addEventListener('click', () => {
                const newLang = this.currentLang === 'en' ? 'th' : 'en';
                this.setLang(newLang);
            });
        }
    },
    
    setLang(lang) {
        this.currentLang = lang;
        localStorage.setItem('lang', lang);
        this.updateUI(lang);
    },
    
    updateUI(lang) {
        // อัปเดตปุ่มภาษา
        const langToggle = document.getElementById('langToggle');
        if (langToggle) {
            const current = langToggle.querySelector('.lang-current');
            const option = langToggle.querySelector('.lang-option');
            if (lang === 'en') {
                current.textContent = 'EN';
                option.textContent = 'TH';
            } else {
                current.textContent = 'TH';
                option.textContent = 'EN';
            }
        }
        
        // อัปเดตเนื้อหาทั้งหมด
        document.querySelectorAll('[data-en][data-th]').forEach(el => {
            const newContent = lang === 'en' ? el.dataset.en : el.dataset.th;
            if (el.hasAttribute('data-html')) {
                el.innerHTML = newContent;
            } else if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
                el.placeholder = newContent;
            } else {
                // ถ้ามี HTML tag ข้างใน ใช้ innerHTML ระวัง
                if (newContent.includes('<')) {
                    el.innerHTML = newContent;
                } else {
                    el.textContent = newContent;
                }
            }
        });
        
        // อัปเดตทิศทาง (ถ้ามีภาษาอาหรับในอนาคต)
        document.documentElement.setAttribute('lang', lang);
    }
};

// เริ่มต้น Language Manager
LangManager.init();

// ===== Theme Management =====
const ThemeManager = {
    currentTheme: 'auto',
    
    init() {
        // โหลด theme ที่บันทึกไว้
        const savedTheme = localStorage.getItem('theme') || 'auto';
        this.setTheme(savedTheme);
        
        // ตั้งค่า event listeners
        this.setupEventListeners();
        
        // ตรวจสอบเวลาทุกนาที (สำหรับ auto theme)
        setInterval(() => this.checkAutoTheme(), 60000);
    },
    
    setupEventListeners() {
        const themeToggle = document.getElementById('themeToggle');
        const themeDropdown = document.getElementById('themeDropdown');
        const themeOptions = document.querySelectorAll('.theme-option');
        
        // Toggle dropdown
        themeToggle.addEventListener('click', (e) => {
            e.stopPropagation();
            themeDropdown.classList.toggle('active');
        });
        
        // Close dropdown เมื่อคลิกข้างนอก
        document.addEventListener('click', () => {
            themeDropdown.classList.remove('active');
        });
        
        // เลือก theme
        themeOptions.forEach(option => {
            option.addEventListener('click', (e) => {
                e.stopPropagation();
                const theme = option.dataset.theme;
                this.setTheme(theme);
                themeDropdown.classList.remove('active');
            });
        });
    },
    
    setTheme(theme) {
        this.currentTheme = theme;
        
        // บันทึกลง localStorage
        localStorage.setItem('theme', theme);
        
        // อัปเดต UI
        this.updateUI(theme);
        
        // ใช้ theme
        if (theme === 'auto') {
            this.applyAutoTheme();
        } else {
            document.documentElement.setAttribute('data-theme', theme);
        }
        
        // อัปเดต icon
        this.updateThemeIcon(theme);
    },
    
    updateUI(selectedTheme) {
        // อัปเดต active state ใน dropdown
        document.querySelectorAll('.theme-option').forEach(option => {
            option.classList.toggle('active', option.dataset.theme === selectedTheme);
        });
    },
    
    applyAutoTheme() {
        const hour = new Date().getHours();
        // 6:00 - 18:00 = Light, 18:00 - 6:00 = Dark
        const isDaytime = hour >= 6 && hour < 18;
        const autoTheme = isDaytime ? 'light' : 'dark';
        
        document.documentElement.setAttribute('data-theme', autoTheme);
        
        // อัปเดต badge ใน dropdown
        const autoOption = document.querySelector('[data-theme="auto"]');
        if (autoOption) {
            const badge = autoOption.querySelector('.auto-badge');
            if (badge) {
                badge.textContent = isDaytime ? 'Light' : 'Dark';
            }
        }
    },
    
    checkAutoTheme() {
        if (this.currentTheme === 'auto') {
            this.applyAutoTheme();
        }
    },
    
    updateThemeIcon(theme) {
        const icon = document.getElementById('currentThemeIcon');
        const icons = {
            'auto': '🌓',
            'dark': '🌙',
            'light': '☀️',
            'minimal': '⚪'
        };
        if (icon) {
            icon.textContent = icons[theme] || '🌙';
        }
    }
};

// เริ่มต้น Theme Manager
ThemeManager.init();

// ===== Smooth Scroll for Navigation Links =====
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// ===== Mobile Menu Toggle =====
const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
const navLinks = document.querySelector('.nav-links');

if (mobileMenuToggle) {
    mobileMenuToggle.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        mobileMenuToggle.classList.toggle('active');
    });
}

// ===== Navbar Scroll Effect =====
const navbar = document.querySelector('.navbar');
let lastScroll = 0;

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    
    // Add/remove scrolled class
    if (currentScroll > 30) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
    
    lastScroll = currentScroll;
});

// ===== Intersection Observer for Animations =====
const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe feature cards, steps, and asset categories
document.querySelectorAll('.feature-card, .step, .asset-category').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
    observer.observe(el);
});

// ===== Dynamic Price Update Animation =====
function animatePriceChange(element) {
    element.style.transition = 'color 0.3s';
    element.style.color = '#10b981'; // Green
    setTimeout(() => {
        element.style.color = ''; // Reset to CSS variable
    }, 500);
}

// Simulate live price updates in the menu bar preview
const priceElements = document.querySelectorAll('.price');
const mockPrices = [
    { base: 84231, variance: 500 },
    { base: 2798, variance: 15 },
    { base: 42156, variance: 200 }
];

function updateMockPrices() {
    priceElements.forEach((el, index) => {
        if (mockPrices[index]) {
            const { base, variance } = mockPrices[index];
            const change = (Math.random() - 0.5) * variance;
            const newPrice = Math.round(base + change);
            
            // Format based on value
            let formatted;
            if (newPrice >= 10000) {
                formatted = newPrice.toLocaleString();
            } else if (newPrice >= 1000) {
                formatted = newPrice.toLocaleString();
            } else {
                formatted = newPrice.toFixed(2);
            }
            
            // Get the prefix (BTC, XAU, US30)
            const prefix = el.textContent.split(' ')[0];
            const oldPrice = parseFloat(el.textContent.split(' ')[1]?.replace(/,/g, ''));
            el.textContent = `${prefix} ${formatted}`;
            
            // Animate if price changed significantly
            if (Math.abs(change) > variance * 0.3) {
                animatePriceChange(el);
            }
        }
    });
}

// Update prices every 3 seconds for demo effect
setInterval(updateMockPrices, 3000);

// ===== Copy Code Block =====
document.querySelectorAll('.code-block').forEach(block => {
    const copyBtn = document.createElement('button');
    copyBtn.className = 'copy-btn';
    copyBtn.innerHTML = '<i class="far fa-copy"></i>';
    copyBtn.title = 'Copy to clipboard';
    
    copyBtn.addEventListener('click', () => {
        const code = block.querySelector('code');
        if (code) {
            navigator.clipboard.writeText(code.textContent).then(() => {
                copyBtn.innerHTML = '<i class="fas fa-check"></i>';
                copyBtn.style.color = '#10b981';
                setTimeout(() => {
                    copyBtn.innerHTML = '<i class="far fa-copy"></i>';
                    copyBtn.style.color = '';
                }, 2000);
            });
        }
    });
    
    block.style.position = 'relative';
    block.appendChild(copyBtn);
});

// Add copy button styles
const copyBtnStyles = document.createElement('style');
copyBtnStyles.textContent = `
    .copy-btn {
        position: absolute;
        top: 12px;
        right: 12px;
        width: 36px;
        height: 36px;
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 8px;
        color: var(--text-secondary);
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: all 0.2s;
        opacity: 0;
    }
    
    .code-block:hover .copy-btn {
        opacity: 1;
    }
    
    .copy-btn:hover {
        background: rgba(255, 255, 255, 0.15);
        color: var(--text-primary);
    }
    
    [data-theme="light"] .copy-btn,
    [data-theme="minimal"] .copy-btn {
        background: rgba(0, 0, 0, 0.05);
        border-color: rgba(0, 0, 0, 0.1);
    }
    
    @media (max-width: 768px) {
        .copy-btn {
            opacity: 1;
        }
    }
`;
document.head.appendChild(copyBtnStyles);

// ===== Reveal on Scroll =====
const revealElements = document.querySelectorAll('.section-header, .download-card');

const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
            revealObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.1 });

revealElements.forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(40px)';
    el.style.transition = 'opacity 0.8s ease-out, transform 0.8s ease-out';
    revealObserver.observe(el);
});

// ===== Console Easter Egg =====
console.log('%c📊 PulseBar', 'font-size: 24px; font-weight: bold; color: #8b5cf6;');
console.log('%cFree & open source macOS menu bar app for tracking crypto, gold & stock indices.', 'font-size: 14px; color: #a0a0b0;');
console.log('%cGitHub: https://github.com/danupolai-alt/pulsebar', 'font-size: 12px; color: #6b6b7b;');

// ===== Time-based greeting (bonus) =====
const hour = new Date().getHours();
let greeting = 'Hello';
if (hour >= 5 && hour < 12) greeting = 'Good morning';
else if (hour >= 12 && hour < 18) greeting = 'Good afternoon';
else greeting = 'Good evening';

console.log(`%c${greeting}! Current theme: ${ThemeManager.currentTheme}`, 'font-size: 12px; color: #8b5cf6;');
