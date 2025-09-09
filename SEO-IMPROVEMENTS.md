# SEO Improvements

The project includes the following SEO and UX enhancements:

- `layouts/partials/seo/head.html` builds dynamic `<title>` and meta tags with Open Graph, Twitter, canonical URLs and `article:modified_time`.
- JSON-LD schema modules for Organization and Article are emitted via `params.seo.organization` toggle.
- Styles moved to `assets/css/main.css` and processed through Hugo Pipes for minification and fingerprinting.
- Descriptions added to all pages; `/about-us` redirect provided via `static/_redirects`.
- Template now uses `<h1>` headings, optional table of contents, and previous/next navigation.
- Automatic `robots.txt` and configured `sitemap.xml`.
- GitHub Actions workflow performs Hugo build, link checking, and spell checking.

These changes aim to improve crawlability, social sharing and Core Web Vitals while keeping URLs stable.
