# HX-Reselect

The `HX-Reselect` response header overrides which part of the response is used for swapping, replacing whatever `hx-select` was set on the triggering element.

## Syntax

```http
HX-Reselect: #content
```

The value is a CSS selector applied to the response HTML to extract the content to swap in.


Return a full page but tell htmx to only use a specific fragment:

```python
return Response(
    full_page_html,
    headers={'HX-Reselect': '#main-content'}
)
```

## Notes

- Overrides `hx-select` on the source element
- Evaluated after the response is received, before swapping

See also: [`hx-select`](https://four.htmx.org/reference/attributes/hx-select), [`HX-Retarget`](https://four.htmx.org/reference/headers/HX-Retarget), [`HX-Reswap`](https://four.htmx.org/reference/headers/HX-Reswap)