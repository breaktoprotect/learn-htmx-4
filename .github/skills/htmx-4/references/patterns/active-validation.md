# Active Validation

<div id="demo-content" class="not-prose demo-container flex items-center justify-center min-h-[400px]"></div>

## Basic usage

On the client, the input validates on each keystroke (debounced).

```html
<input name="username"
       hx-post="/check-username"
       hx-trigger="input changed delay:300ms"
       hx-target="next span">

<span></span>
```

- [`hx-post`](https://four.htmx.org/reference/attributes/hx-post) sends the value to `/check-username`.
- [`hx-trigger`](https://four.htmx.org/reference/attributes/hx-trigger) fires on [`input`](https://developer.mozilla.org/en-US/docs/Web/API/Element/input_event) after a 300ms [`delay`](https://four.htmx.org/reference/attributes/hx-trigger#delaytime), and only when the value has [`changed`](https://four.htmx.org/reference/attributes/hx-trigger#changed).
- [`hx-target`](https://four.htmx.org/reference/attributes/hx-target)=[`"next span"`](https://four.htmx.org/reference/attributes/hx-target#extended-selectors) puts the response into the next sibling `<span>`.

On the server, respond with a validation message:

```html
<span class="error">That username is taken.</span>
```

Or an empty `<span>` when valid.