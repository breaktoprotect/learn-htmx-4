# htmx.config.includeIndicatorCSS

The `htmx.config.includeIndicatorCSS` option controls whether htmx adds built-in loading indicator styles.

The styles hide [`indicatorClass`](https://four.htmx.org/reference/config/htmx-config-indicatorClass) content until [`requestClass`](https://four.htmx.org/reference/config/htmx-config-requestClass) marks it as active.

**Default:** `true`

## Syntax

Disable built-in styles when providing your own:

```html
<meta name="htmx-config" content="includeIndicatorCSS:false">
```

## See Also

- [`hx-indicator`](https://four.htmx.org/reference/attributes/hx-indicator)
- [`htmx.config.indicatorClass`](https://four.htmx.org/reference/config/htmx-config-indicatorClass)
- [`htmx.config.requestClass`](https://four.htmx.org/reference/config/htmx-config-requestClass)