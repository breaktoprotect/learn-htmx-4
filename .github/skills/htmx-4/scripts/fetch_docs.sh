#!/usr/bin/env bash
# Fetch htmx 4 docs into references/ as byte-faithful markdown.
#
#   bash scripts/fetch_docs.sh                 # refresh the whole mirror
#   bash scripts/fetch_docs.sh /docs/quirks    # fetch one page
#
# Site markdown export is https://four.htmx.org/<path>.md .
# It 404s for the 10 /docs/* guide pages, so those fall back to the source
# markdown each guide page links to (bigskysoftware/htmx @ four-dev).
# The list of bundled pages is references/SOURCES.txt.
set -uo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.." || exit 1   # skill root

SITE=https://four.htmx.org
GH=https://raw.githubusercontent.com/bigskysoftware/htmx/four-dev/www/src/content/docs

fetch_page() {
  local path="${1#/}" out="${1#/}.md" code tmp
  [ "$path" = "docs" ] && out="docs.md"
  mkdir -p "references/$(dirname "$out")"
  tmp=$(mktemp)
  # Download to a temp file and only move it into place on HTTP 200, so a
  # failed or 404 fetch can never leave an HTML error page in references/.
  code=$(curl -sL -o "$tmp" -w '%{http_code}' "$SITE/$path.md")
  if [ "$code" != 200 ] && [ "${path#docs/}" != "$path" ]; then
    code=$(curl -sL -o "$tmp" -w '%{http_code}' "$GH/${path#docs/}.md")
  fi
  if [ "$code" = 200 ]; then
    mv "$tmp" "references/$out"; echo "ok   references/$out"
  else
    rm -f "$tmp"; echo "FAIL references/$out (HTTP $code, nothing written)"
  fi
}

if [ $# -ge 1 ]; then
  fetch_page "$1"
else
  echo "Refreshing mirror from $SITE ($(wc -l < references/SOURCES.txt) pages)"
  while read -r p; do [ -n "$p" ] && fetch_page "$p"; done < references/SOURCES.txt
fi
