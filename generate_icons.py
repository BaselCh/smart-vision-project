import os
import urllib.request
import json

# Target Desktop folder as explicitly requested by user
DESKTOP_ICONS_DIR = "/Users/basel/Desktop/icons"
os.makedirs(DESKTOP_ICONS_DIR, exist_ok=True)

# List of all icons used in the SMARTVISION dashboard design
LUCIDE_ICONS = [
    "pie-chart",
    "filter-x",
    "user-plus",
    "user-check",
    "award",
    "check-circle-2",
    "facebook",
    "linkedin",
    "gauge",
    "zap",
    "book-open",
    "dollar-sign",
    "layout-dashboard",
    "database",
    "settings",
    "history",
    "download",
    "cpu",
    "tag",
    "upload-cloud",
    "log-out",
    "chevron-down",
    "chevron-right",
    "sparkles",
    "external-link",
    "check",
    "x",
    "bar-chart-2",
    "trending-up",
    "users",
    "refresh-cw"
]

print(f"Exporting icons to: {DESKTOP_ICONS_DIR}")

# 1. Custom Google Ads Icon
google_svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/>
  <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/>
  <path d="M5.84 14.1c-.22-.66-.35-1.36-.35-2.1s.13-1.44.35-2.1V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.62z" fill="#FBBC05"/>
  <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z" fill="#EA4335"/>
</svg>'''
with open(os.path.join(DESKTOP_ICONS_DIR, "google-ads.svg"), "w", encoding="utf-8") as f:
    f.write(google_svg)

# 2. SMARTVISION Geometric Mark SVG
smartvision_mark_svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 100 100" fill="none">
  <polygon points="10,20 40,20 25,60" fill="#0066FF"/>
  <polygon points="40,20 70,20 55,60" fill="#8B5CF6"/>
  <polygon points="70,20 90,20 50,85" fill="#EC4899"/>
  <polygon points="25,60 50,85 10,20" fill="#06B6D4"/>
</svg>'''
with open(os.path.join(DESKTOP_ICONS_DIR, "smartvision-mark.svg"), "w", encoding="utf-8") as f:
    f.write(smartvision_mark_svg)

# 3. Fetch Lucide SVGs from official repository API / unpkg
for icon in LUCIDE_ICONS:
    try:
        url = f"https://unpkg.com/lucide-static@latest/icons/{icon}.svg"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            svg_content = response.read().decode('utf-8')
            filepath = os.path.join(DESKTOP_ICONS_DIR, f"{icon}.svg")
            with open(filepath, "w", encoding="utf-8") as out:
                out.write(svg_content)
            print(f"Saved: {icon}.svg")
    except Exception as e:
        print(f"Error fetching {icon}: {e}")

print("All icons successfully exported!")
