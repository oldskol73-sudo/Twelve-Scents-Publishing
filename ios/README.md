# Twelve Scents – iOS app

SwiftUI shell that hosts the Twelve Scents shop design (`../app-design`) full-screen in a `WKWebView`.
Everything (React, Babel, fonts, screens) is bundled, so it runs fully offline.

## Open in Xcode
1. Open `TwelveScents.xcodeproj` (Xcode 15+).
2. Target **TwelveScents → Signing & Capabilities**: pick your Team and change the bundle id (`com.twelvescents.app`) if needed.
3. Choose a simulator or device and press Run.

## Change the design
Edit the sources in `../app-design`, then rebuild the bundle and re-run in Xcode:

    python3 build_web.py              # dark theme (default)
    python3 build_web.py ShopGrey     # light grey theme
    python3 build_web.py ShopHeather  # heather/plum theme

This regenerates `TwelveScents/Web`. `ios-frame.js` here replaces the design's fake phone bezel,
so the app draws edge to edge and iOS supplies the real status bar and home indicator.

## Notes
- Pages are served from the bundle via an `app://` URL scheme (`WebContainer.swift`), because the design runtime `fetch()`es its files.
- The app icon is a placeholder (brass "12"); replace `Assets.xcassets/AppIcon.appiconset/icon-1024.png`.
- The Debug build enables Safari Web Inspector (iOS 16.4+).
- Cart, checkout and account screens are the design's prototype flows, not a real store backend.
