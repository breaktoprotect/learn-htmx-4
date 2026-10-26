# HX-Replace-Url

The `HX-Replace-Url` response header replaces the current browser history URL.

It does not create a new history entry.

If present, this header overrides any behavior defined with attributes.

## Possible Values

- A URL to replace the current URL in the location bar. May be relative or absolute, as per [`history.replaceState()`](https://developer.mozilla.org/en-US/docs/Web/API/History/replaceState), but must have the same origin as the current URL.
- `false` — prevents the browser's current URL from being updated.

## Example

```http
HX-Replace-Url: /dashboard
```

## Notes

- Response headers are not processed on 3xx response codes.

See also: [`hx-replace-url`](https://four.htmx.org/reference/attributes/hx-replace-url), [`HX-Push-Url`](https://four.htmx.org/reference/headers/HX-Push-Url)