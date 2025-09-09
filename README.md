# Tweed Cloud

This repository contains the [Hugo](https://gohugo.io/) source for the Tweed Cloud website.

## Development

1. Install Hugo.
2. Run `hugo server` to view the site locally.
3. Run `hugo` to build the static files into the `public/` directory.

The output is ready to deploy on platforms such as Cloudflare Pages.

### Content guidelines

Each page should include the following front matter fields:

```
title: "Page title"
description: "One–sentence summary shown in meta tags."
image: "/images/optional-social.jpg" # used for social cards
```

Use meaningful alt text for all images and keep headings in order. For long articles the automatic table of contents and previous/next links will appear.

### Theme options

This site uses the `tweed-90s` theme. Optional 90s details can be toggled in `hugo.toml`:

```
[params.theme]
  retroMode = true        # underlined links and dotted rules
  showGradients = true    # gradient separators
  showPixelBorders = true # 1–2px borders on cards and nav
```

All features are text-only and rely on system fonts.
