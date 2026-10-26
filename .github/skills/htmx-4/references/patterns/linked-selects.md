# Linked Selects

<div id="demo-content" class="not-prose demo-container min-h-[240px]"></div>

## Basic usage

On the client, set the first select to request new options whenever its value changes.

```html
<select name="make"
        hx-get="/models"
        hx-target="#models"
        hx-indicator="#models-indicator">
  <option value="audi">Audi</option>
  <option value="toyota">Toyota</option>
  <option value="bmw">BMW</option>
</select>

<select id="models" name="model">
  <option value="A4">A4</option>
  ...
</select>
<span id="models-indicator" class="htmx-indicator">Loading...</span>
```

- [`hx-get`](https://four.htmx.org/reference/attributes/hx-get) requests `/models` with the current `make` value as a query parameter.
- [`hx-target`](https://four.htmx.org/reference/attributes/hx-target)=`"#models"` swaps the response into the second select.
- [`hx-indicator`](https://four.htmx.org/reference/attributes/hx-indicator)=`"#models-indicator"` shows a loading message while the request is in flight.
- No [`hx-trigger`](https://four.htmx.org/reference/attributes/hx-trigger) is needed: htmx defaults to `change` for `<select>` elements.

On the server, respond with a new set of `<option>` elements matching the selected make:

```html
<option value="M3">M3</option>
<option value="X5">X5</option>
<option value="i4">i4</option>
```

Because the default [`hx-swap`](https://four.htmx.org/reference/attributes/hx-swap) strategy is [`innerHTML`](https://four.htmx.org/reference/attributes/hx-swap#innerhtml), the options replace the contents of the `#models` select.