# Publish the static portfolio website

The portfolio website is a static HTML page. It has not been published automatically.

## Recommended: GitHub Pages from the repository root

A root `index.html` redirects visitors to `website/index.html`, while keeping the project READMEs and evidence files available at the same site origin. After pushing the repository, open **Settings → Pages**, choose **Deploy from a branch**, select the default branch and the `/(root)` folder, then save. Wait for GitHub Pages to finish deploying and open the URL it provides. If the repository is private, confirm your plan supports Pages before relying on it.

### Manual check before publishing

1. Open `website/index.html` locally in a browser.
2. Test the project filters and review/export interaction.
3. Follow every project and evidence link.
4. Confirm the disclosure about synthetic data and AI assistance remains visible.
5. Do not enter personal or confidential information into the local review form; exports are browser-generated and are not independently verified annotations.

### GitHub repository links

The current site links to Markdown files in the repository. On GitHub Pages, check those links after deployment. If any are not rendered as intended, change them to the corresponding GitHub repository file URLs once the repository URL is confirmed.

## Important

A successful local test does not mean the website is live. Add the final deployed URL to LinkedIn and the resume only after you have published and checked it yourself.

## Offline evidence reader
The website includes website/evidence.html with embedded documentation. Project/method/report links open this reader rather than relying on Markdown rendering on GitHub Pages. Rebuild it after document changes with python build_evidence_reader.py.
