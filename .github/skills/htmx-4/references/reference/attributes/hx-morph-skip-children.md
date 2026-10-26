# hx-morph-skip-children

The `hx-morph-skip-children` attribute updates an element's attributes during a [morph swap](https://four.htmx.org/reference/attributes/hx-swap#innermorph) but leaves its children alone.

## Syntax

```html
<div hx-morph-skip-children class="chart">
    <!-- htmx morphs the attributes above, but not this content -->
</div>
```

The value of the attribute is ignored.

## Notes

* Use it when the server owns the element's attributes but a script owns its content, for example a chart or an editor.
* To freeze the attributes as well, use [`hx-morph-skip`](https://four.htmx.org/reference/attributes/hx-morph-skip).
* It applies to morph swaps only. It has no effect on `innerHTML`, `outerHTML`, or the other swap styles.
* htmx matches the attribute through the [`htmx.config.morphSkipChildren`](https://four.htmx.org/reference/config/htmx-config-morphSkipChildren) selector, which defaults to `[hx-morph-skip-children]`. If you set that option to another selector, this attribute stops working.
* htmx morphs the attributes first. If the response omits `hx-morph-skip-children`, htmx removes the attribute and later morphs update the children. Send the attribute in the response to keep it.

## See Also

* [`hx-morph-skip`](https://four.htmx.org/reference/attributes/hx-morph-skip)
* [`hx-preserve`](https://four.htmx.org/reference/attributes/hx-preserve)
* [`htmx.config.morphSkipChildren`](https://four.htmx.org/reference/config/htmx-config-morphSkipChildren)