# htmx.config.implicitInheritance

The `htmx.config.implicitInheritance` option, when set to `true`, causes child elements to implicitly inherit htmx attributes from parent elements.

**Default:** `false`

## Example

```javascript
htmx.config.implicitInheritance = true;
```

```html
<meta name="htmx-config" content='{"implicitInheritance":true}'>
```

When enabled, attributes like [`hx-target`](https://four.htmx.org/reference/attributes/hx-target) on a parent apply to all child elements unless overridden.