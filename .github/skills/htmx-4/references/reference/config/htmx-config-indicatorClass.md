# htmx.config.indicatorClass

The `htmx.config.indicatorClass` option sets the CSS class used to mark loading indicator content.

Add this class in your markup:

```html
<img id="spinner" class="htmx-indicator" alt="Loading">
```

htmx does not add the class. Built-in indicator CSS hides it until [`requestClass`](https://four.htmx.org/reference/config/htmx-config-requestClass) marks the indicator or an ancestor as active.

**Default:** `"htmx-indicator"`

## Syntax

Use a custom class:

```html
<meta name="htmx-config" content='indicatorClass:"loading"'>

<img id="spinner" class="loading" alt="Loading">
```

## See Also

- [`hx-indicator`](https://four.htmx.org/reference/attributes/hx-indicator)
- [`htmx.config.includeIndicatorCSS`](https://four.htmx.org/reference/config/htmx-config-includeIndicatorCSS)
- [`htmx.config.requestClass`](https://four.htmx.org/reference/config/htmx-config-requestClass)