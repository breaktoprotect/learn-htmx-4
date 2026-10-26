# htmx.config.noSwap

The `htmx.config.noSwap` option is an array of HTTP status codes for which htmx will not perform a content swap.

**Default:** `[204, 304]`

## Example

```javascript
htmx.config.noSwap = [204, 304, 205];
```

```html
<meta name="htmx-config" content='{"noSwap":[204,304,205]}'>
```

Responses with these status codes will trigger events but won't swap content.

## See Also

- [`hx-status`](https://four.htmx.org/reference/attributes/hx-status)
- [`htmx:response:error`](https://four.htmx.org/reference/events/htmx-response-error)