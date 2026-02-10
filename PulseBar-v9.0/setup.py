"""
Setup script for PulseBar - macOS Menu Bar App
"""

from setuptools import setup

APP = ['main.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'CFBundleName': 'PulseBar',
        'CFBundleDisplayName': 'PulseBar',
        'CFBundleIdentifier': 'com.danupolai.pulsebar',
        'CFBundleVersion': '9.0.0',
        'CFBundleShortVersionString': '9.0',
        'LSUIElement': True,
        'NSHumanReadableCopyright': '© 2024 danupolai-alt',
    },
    'packages': ['rumps', 'requests', 'yfinance'],
    'includes': ['ctypes', 'datetime', 'threading', 'time'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
