# Infinite Scroll

<div id="demo-content" class="not-prose demo-container min-h-[380px]"></div>

## Basic usage

On the client, put a placeholder row at the end of your table.

```html
<tr hx-get="/contacts?page=2"
    hx-swap="outerHTML"
    hx-trigger="revealed">
  <td>Loading more...</td>
</tr>
```

- [`hx-get`](https://four.htmx.org/reference/attributes/hx-get) requests `/contacts?page=2`.
- [`hx-swap`](https://four.htmx.org/reference/attributes/hx-swap)=[`"outerHTML"`](https://four.htmx.org/reference/attributes/hx-swap#outerhtml) sets the strategy to replace the target.
- [`hx-trigger`](https://four.htmx.org/reference/attributes/hx-trigger)=[`"revealed"`](https://four.htmx.org/reference/attributes/hx-trigger#revealed) fires when the element scrolls into view. Use [`intersect`](https://four.htmx.org/reference/attributes/hx-trigger#intersect) [`once`](https://four.htmx.org/reference/attributes/hx-trigger#once) instead if your container has `overflow-y: scroll`.

On the server, respond with the next rows plus a fresh placeholder pointing to `?page=3`:

```html
<tr><td>Agent Smith</td><td>agent10@smith.org</td></tr>
<tr><td>Agent Smith</td><td>agent11@smith.org</td></tr>
<tr><td>Agent Smith</td><td>agent12@smith.org</td></tr>

<!-- When there are no more pages, just omit this row -->
<tr hx-get="/contacts?page=3"
    hx-swap="outerHTML"
    hx-trigger="revealed">
  <td>Loading more...</td>
</tr>
```

Because [`outerHTML`](https://four.htmx.org/reference/attributes/hx-swap#outerhtml) replaces the old placeholder, the new one takes its place, creating a self-extending chain.