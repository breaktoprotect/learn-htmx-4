# HX-Retarget

The `HX-Retarget` response header overrides the element that will receive the swapped content, replacing whatever `hx-target` was set on the triggering element.

## Syntax

```http
HX-Retarget: #new-target
```

The value is a CSS selector for the new target element.


Redirect a form submission result to a different container:

```python
return Response(
    content,
    headers={'HX-Retarget': '#notifications'}
)
```

## Notes

- Overrides `hx-target` on the source element
- Evaluated after the response is received, before swapping

See also: [`hx-target`](https://four.htmx.org/reference/attributes/hx-target), [`HX-Reswap`](https://four.htmx.org/reference/headers/HX-Reswap)

## See Also

- [`HX-Target`](https://four.htmx.org/reference/headers/HX-Target)