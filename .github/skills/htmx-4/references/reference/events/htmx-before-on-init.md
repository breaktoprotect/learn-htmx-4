# htmx:before:on:init

The `htmx:before:on:init` event fires before htmx binds the [`hx-on`](https://four.htmx.org/reference/attributes/hx-on) attributes on an element.

Cancel it to leave those attributes unbound.

## When It Fires

During [`htmx.process()`](https://four.htmx.org/reference/methods/htmx-process), after [`htmx:before:process`](https://four.htmx.org/reference/events/htmx-before-process) and before element initialization.

htmx fires it once for the processed root, and once for each descendant that carries an `hx-on` attribute.

## Event Detail

Empty - no additional context provided.

## Example

```javascript
htmx.on('htmx:before:on:init', (evt) => {
  if (evt.target.closest('.no-inline-handlers')) {
    evt.preventDefault();
  }
});
```

## Notes

* The event bubbles and is cancelable.
* `preventDefault()` stops htmx from binding the `hx-on` attributes on that element only. Processing continues for the rest of the tree.

## See Also

* [`hx-on`](https://four.htmx.org/reference/attributes/hx-on)
* [`htmx:before:process`](https://four.htmx.org/reference/events/htmx-before-process)
* [`htmx:before:init`](https://four.htmx.org/reference/events/htmx-before-init)