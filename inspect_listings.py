from lab_selectors import extract_listings

with open('sample_merchandise.html', encoding='utf-8') as f:
    html = f.read()

for listing in extract_listings(html):
    print(listing['name'])
