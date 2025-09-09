# Site Audit

## Pages
See `content-report.csv` for details of each page.

## Observations
- Meta descriptions were missing; now provided.
- No canonical or Open Graph tags were present; a new SEO head partial outputs them consistently.
- Navigation used `<h1>` causing duplicate headings; changed to paragraph to preserve page `<h1>`.
- No schema.org data; added Organization and Article JSON-LD.
- CSS was inline and unminified; moved to Hugo Pipes for minification and caching.
- Robots.txt and sitemap configuration were absent; templates added.

## Recommendations
- Expand thin pages like Contact and Consultation with more useful information.
- Add images with meaningful `alt` text and consider responsive processing.
- Consider adding a blog section to grow organic visibility.
