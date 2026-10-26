# HX-Reswap

The `HX-Reswap` response header overrides the swap style used when inserting the response, replacing whatever `hx-swap` was set on the triggering element.

## Syntax

```http
HX-Reswap: outerHTML
```

Accepts the same values as [`hx-swap`](https://four.htmx.org/reference/attributes/hx-swap), including modifiers.


Force an outer replacement regardless of what the element specified:

```python
return Response(
    content,
    headers={'HX-Reswap': 'outerHTML'}
)
```

With modifiers:

```http
HX-Reswap: innerHTML transition:true
```

## Notes

- Overrides `hx-swap` on the source element
- Evaluated after the response is received, before swapping

See also: [`hx-swap`](https://four.htmx.org/reference/attributes/hx-swap), [`HX-Retarget`](https://four.htmx.org/reference/headers/HX-Retarget)