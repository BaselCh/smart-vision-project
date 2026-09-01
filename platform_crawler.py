import os
import sys
import time
import argparse
from playwright.sync_api import sync_playwright

def crawl_platform(username=None, password=None, company=None, gui=False):
    output_dir = "/Users/basel/.gemini/antigravity/scratch/add_intelligence_redesign/crawled_pages"
    os.makedirs(output_dir, exist_ok=True)
    
    print("Starting Playwright Browser...")
    with sync_playwright() as p:
        # Launch browser (headless=False if gui requested)
        browser = p.chromium.launch(headless=not gui)
        context = browser.new_context(viewport={'width': 1440, 'height': 900})
        page = context.new_page()

        print("Navigating to https://painel.addintelligence.com.br/...")
        page.goto("https://painel.addintelligence.com.br/", wait_until="networkidle")

        if username and password and company:
            print(f"Attempting automatic login for client '{company}'...")
            page.fill("#txtLogin", username)
            page.fill("#txtSenha", password)
            page.fill("#txtCliente", company)
            page.click("#lkbAutenticar")
            page.wait_for_timeout(3000)

        elif gui:
            print("Opened browser window on your desktop! Please log in on the browser window...")
            # Wait for user to log in manually (checking for Dashboard in URL or title)
            for _ in range(120): # Wait up to 2 minutes
                if "Dashboard" in page.url or "Dashboard" in page.title():
                    print("Login detected! Proceeding to crawl platform...")
                    break
                time.sleep(1)

        # Check current URL
        print(f"Current page URL: {page.url}")
        print(f"Current page title: {page.title()}")

        # Take main snapshot
        page.screenshot(path=os.path.join(output_dir, "00_main_dashboard.png"))
        with open(os.path.join(output_dir, "00_main_dashboard.html"), "w", encoding="utf-8") as f:
            f.write(page.content())

        # Find all dashboard links/buttons on page
        print("Extracting dashboard links...")
        links = page.query_selector_all("a, button, .box, div[onclick]")
        print(f"Found {len(links)} clickable elements.")

        browser.close()
        print("Crawling finished successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add Intelligence Platform Crawler")
    parser.add_argument("--user", type=str, help="Username / Login")
    parser.add_argument("--pass", type=str, dest="password", help="Password")
    parser.add_argument("--company", type=str, help="Company / Empresa")
    parser.add_argument("--gui", action="store_true", help="Launch GUI browser on Mac screen")
    args = parser.parse_args()

    crawl_platform(args.user, args.password, args.company, args.gui)
