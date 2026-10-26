# HX-Redirect

The `HX-Redirect` response header redirects to a new URL with a full page reload.

Use it for non-htmx endpoints or pages that require a full browser load.

For AJAX navigation inside an htmx application, use [`HX-Location`](https://four.htmx.org/reference/headers/HX-Location).

Response headers are not processed on 3xx response codes. Return a 2xx status when using this header.

## Example

```http
HX-Redirect: /dashboard
```

```python
return Response(
    "Redirecting...",
    headers={'HX-Redirect': '/dashboard'}
)
```

## See Also

- [`HX-Location`](https://four.htmx.org/reference/headers/HX-Location)