"""
สำหรับ build เป็น .app บน macOS
ใช้คำสั่ง: python setup.py py2app
"""

from setuptools import setup

APP = ['main.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': None,
    'plist': {
        'CFBundleName': 'Crypto Menu Bar',
        'CFBundleDisplayName': 'Crypto Menu Bar',
        'CFBundleIdentifier': 'com.yourname.cryptomenubar',
        'CFBundleVersion': '1.0.0',
        'LSUIElement': True,  # สำคัญ! ทำให้ไม่แสดง dock icon
    },
    'packages': ['rumps', 'requests'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
