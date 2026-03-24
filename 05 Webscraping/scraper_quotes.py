from playwright.sync_api import sync_playwright
import csv

def run_scraper() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Deze pagina laadt quotes via JavaScript — requests geeft hier niets terug!
        page.goto("https://quotes.toscrape.com/js/")
        page.wait_for_selector("div.quote")

        quotes = page.query_selector_all("div.quote span.text")
        auteurs = page.query_selector_all("div.quote small.author")

        resultaten = []

        for quote, auteur in zip(quotes, auteurs):
            tekst = quote.inner_text()
            naam = auteur.inner_text()
            resultaten.append((naam, tekst))
            print(f"✍️  {naam}")
            print(f"   💬 {tekst}\n")

        with open("quotes.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Auteur", "Quote"])
            writer.writerows(resultaten)

        print(f"💾 {len(resultaten)} quotes opgeslagen in quotes.csv")
        browser.close()

run_scraper()