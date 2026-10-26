# htmx.config.morphScanLimit

The `htmx.config.morphScanLimit` option limits siblings scanned during morph matching.

Higher values improve accuracy for long lists without IDs at a performance cost.

**Default:** `10`

## Example

```javascript
htmx.config.morphScanLimit = 20;
```

```html
<meta name="htmx-config" content='{"morphScanLimit":20}'>
```

If morphing produces unexpected reorders in long lists, try increasing this limit.

See also: [`htmx.config`](https://four.htmx.org/reference/config/htmx-config)