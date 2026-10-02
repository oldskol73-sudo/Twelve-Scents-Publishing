#!/usr/bin/env python3
"""Builds TwelveScents/Web (the offline web bundle the iOS app loads) from ../app-design.

Usage: python3 build_web.py [Shop|ShopGrey|ShopHeather]   (default: Shop, the dark theme)
Vendor files (React, Babel, fonts) are copied from ./vendor, which is committed.
"""
import re, shutil, sys, pathlib
here = pathlib.Path(__file__).parent
src = here.parent / 'app-design'
out = here / 'TwelveScents' / 'Web'
theme = sys.argv[1] if len(sys.argv) > 1 else 'Shop'
comp = {'Shop': 'TwelveScentsShop', 'ShopGrey': 'TwelveScentsShopGrey', 'ShopHeather': 'TwelveScentsShopHeather'}[theme]

if out.exists(): shutil.rmtree(out)
shutil.copytree(here / 'vendor', out / 'vendor')
shutil.copy(src / 'support.js', out / 'support.js')
shutil.copy(here / 'ios-frame.js', out / 'ios-frame.js')   # full-bleed IOSDevice (no fake bezel)

h = (src / f'{comp}.dc.html').read_text()
# local fonts instead of Google Fonts
h = re.sub(r'<link rel="preconnect"[^>]*>\s*<link href="https://fonts\.googleapis[^>]*>', '<link rel="stylesheet" href="./vendor/fonts.css">', h)
# fill the real screen instead of a fixed 402x874 phone
h = h.replace('position:relative;height:874px;', 'position:relative;height:100vh;height:100dvh;', 1)
# point the runtime at the bundled React/Babel (it reads window.__resources before hitting unpkg)
res = ('<script>window.__resources={'
       '"https://unpkg.com/react@18.3.1/umd/react.production.min.js":"./vendor/react.production.min.js",'
       '"https://unpkg.com/react-dom@18.3.1/umd/react-dom.production.min.js":"./vendor/react-dom.production.min.js",'
       '"https://unpkg.com/@babel/standalone@7.29.0/babel.min.js":"./vendor/babel.min.js"};</script>'
       '<style>html,body{margin:0;height:100%;overflow:hidden;background:#14110e;-webkit-text-size-adjust:100%}'
       'x-dc{display:block;height:100%}</style>')
h = h.replace('<script src="./support.js"></script>', res + '<script src="./support.js"></script>', 1)
h = h.replace('width=device-width, initial-scale=1', 'width=device-width, initial-scale=1, viewport-fit=cover')
(out / 'index.html').write_text(h)
print('wrote', out)
