# htmx.config.inlineScriptNonce

The `htmx.config.inlineScriptNonce` option sets `nonce` on generated inline scripts.

Use it with a Content Security Policy that requires script nonces.

**Default:** `undefined` (no nonce added)

## Example

```javascript
htmx.config.inlineScriptNonce = "abc123";
```

```html
<meta name="htmx-config" content='{"inlineScriptNonce":"abc123"}'>
```

The nonce value should match the one provided in your `Content-Security-Policy` header.

See also: [`htmx.config`](https://four.htmx.org/reference/config/htmx-config)