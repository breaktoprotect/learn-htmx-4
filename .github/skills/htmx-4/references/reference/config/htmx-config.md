# htmx.config

The `htmx.config` object holds the current htmx configuration. You can modify it in JavaScript or set values using a `<meta>` tag.

## Configure via Meta Tag

Set config values with [HCON](https://four.htmx.org/docs/hcon-guide):

```html
<meta name="htmx-config"
      content="defaultSwap:outerHTML defaultTimeout:5000">
```

Or JSON:

```html
<meta name="htmx-config"
      content='{"defaultSwap":"outerHTML","defaultTimeout":5000}'>
```

## Configure via JavaScript

Modify config values directly:

```javascript
htmx.config.defaultSwap = 'outerHTML';
htmx.config.defaultTimeout = 5000;
```

## Available Options

| Option | Default | Description |
|--------|---------|-------------|
| [`logAll`](https://four.htmx.org/reference/config/htmx-config-logAll) | `false` | Log all htmx events |
| [`prefix`](https://four.htmx.org/reference/config/htmx-config-prefix) | `"data-hx-"` | Secondary attribute prefix recognized alongside `hx-` |
| [`metaCharacter`](https://four.htmx.org/reference/config/htmx-config-metaCharacter) | `undefined` | Character used instead of `:` in attribute names |
| [`transitions`](https://four.htmx.org/reference/config/htmx-config-transitions) | `false` | Enable view transitions |
| [`history`](https://four.htmx.org/reference/config/htmx-config-history) | `true` | Enable history support |
| [`mode`](https://four.htmx.org/reference/config/htmx-config-mode) | `"same-origin"` | Request mode for `fetch()` |
| [`defaultSwap`](https://four.htmx.org/reference/config/htmx-config-defaultSwap) | `"innerHTML"` | Default swap style |
| [`allowEmptySwapAfterOOB`](https://four.htmx.org/reference/config/htmx-config-allowEmptySwapAfterOOB) | `false` | Allow empty main swap after OOB extraction |
| [`defaultFocusScroll`](https://four.htmx.org/reference/config/htmx-config-defaultFocusScroll) | `false` | Scroll to a focused element after swapping |
| [`defaultSettleDelay`](https://four.htmx.org/reference/config/htmx-config-defaultSettleDelay) | `1` | Delay before settling in milliseconds |
| [`indicatorClass`](https://four.htmx.org/reference/config/htmx-config-indicatorClass) | `"htmx-indicator"` | CSS class for indicators |
| [`requestClass`](https://four.htmx.org/reference/config/htmx-config-requestClass) | `"htmx-request"` | CSS class during requests |
| [`includeIndicatorCSS`](https://four.htmx.org/reference/config/htmx-config-includeIndicatorCSS) | `true` | Include default indicator CSS |
| [`defaultTimeout`](https://four.htmx.org/reference/config/htmx-config-defaultTimeout) | `60000` | Request timeout in milliseconds |
| [`extensions`](https://four.htmx.org/reference/config/htmx-config-extensions) | `""` | Extensions to load |
| [`morphIgnore`](https://four.htmx.org/reference/config/htmx-config-morphIgnore) | `["data-htmx-powered"]` | Attributes to ignore during morphing |
| [`morphSkip`](https://four.htmx.org/reference/config/htmx-config-morphSkip) | `"[hx-morph-skip]"` | Elements to skip while morphing |
| [`morphSkipChildren`](https://four.htmx.org/reference/config/htmx-config-morphSkipChildren) | `"[hx-morph-skip-children]"` | Elements whose children are not morphed |
| [`morphScanLimit`](https://four.htmx.org/reference/config/htmx-config-morphScanLimit) | `10` | Siblings scanned while matching elements |
| [`noSwap`](https://four.htmx.org/reference/config/htmx-config-noSwap) | `[204, 304]` | HTTP status codes that skip swaps |
| [`implicitInheritance`](https://four.htmx.org/reference/config/htmx-config-implicitInheritance) | `false` | Enable implicit attribute inheritance |
| [`inlineScriptNonce`](https://four.htmx.org/reference/config/htmx-config-inlineScriptNonce) | `undefined` | Nonce added to inline scripts |

## See Also

- [HCON](https://four.htmx.org/docs/hcon-guide)
- [`hx-config`](https://four.htmx.org/reference/attributes/hx-config)