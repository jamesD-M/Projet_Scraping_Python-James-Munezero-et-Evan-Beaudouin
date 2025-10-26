import os
import argparse
import time
from parsers import get_category_links, parse_list_page, parse_product_page
from utils import ensure_dir, write_csv, download_file

def main(categories_filter=None, max_pages=None, delay=0, outdir="outputs"):
    categories = get_category_links()
    if categories_filter:
        categories = {name: url for name, url in categories.items() if name in categories_filter}
    output_csv = os.path.join(outdir, "csv")
    output_img = os.path.join(outdir, "images")
    ensure_dir(output_csv)
    ensure_dir(output_img)
    print("Nombre de catégorie trouvées:",len(categories))
    for name, cat_url in categories.items():
        print(f"Scraping catégorie : {name}")
        urls = parse_list_page(cat_url)
        if max_pages is not None:
            urls = urls[:max_pages]
        print(f"  → {len(urls)} livres trouvés")
        data = []

        cat_img = os.path.join(output_img, name)
        ensure_dir(cat_img)

        for url in urls:
            book = parse_product_page(url)
            data.append(book)
            title_clean = "".join(c if c.isalnum() else "_" for c in book["titre"]).strip("_")
            filename = f"{book['upc']}_{title_clean}.jpg"
            image_path = os.path.join(cat_img, filename)
            download_file(book["image"], image_path)

            if delay > 0:
                time.sleep(delay)

        csv_path = os.path.join(output_csv, f"category_{name}.csv")
        write_csv(data, csv_path)
        print(f"Saved {len(data)} books for {name}")
    print("Fin du scraping")
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scraper Books to Scrape")
    parser.add_argument("--categories", type=str, help="Liste de catégories séparées par des virgules")
    parser.add_argument("--max-pages", type=int, help="Nombre maximum de livres à scraper par catégorie")
    parser.add_argument("--delay", type=float, default=0, help="Délai entre les requêtes (en secondes)")
    parser.add_argument("--outdir", type=str, default="outputs", help="Dossier de sortie pour CSV et images")
    args = parser.parse_args()

    categories_list = args.categories.split(",") if args.categories else None

    main(categories_filter=categories_list, max_pages=args.max_pages, delay=args.delay, outdir=args.outdir)



