# Reset on Submit

<div id="demo-content" class="not-prose demo-container min-h-[380px]"></div>

## Basic usage

On the client, wrap your inputs in a `<form>` and use [`hx-on`](https://four.htmx.org/reference/attributes/hx-on) to reset it after each successful request.

```html
<form hx-post="/chat"
      hx-target="#messages"
      hx-swap="beforeend"
      hx-on:htmx:after:request="this.reset()">
    <input type="text" name="message">
    <button>Send</button>
</form>
<div id="messages"></div>
```

- [`hx-post`](https://four.htmx.org/reference/attributes/hx-post) submits the form to `/chat`.
- [`hx-target`](https://four.htmx.org/reference/attributes/hx-target) points at the `#messages` container.
- [`hx-swap`](https://four.htmx.org/reference/attributes/hx-swap)=[`"beforeend"`](https://four.htmx.org/reference/attributes/hx-swap#beforeend--append) appends each new message to the bottom.
- [`hx-on:htmx:after:request`](https://four.htmx.org/reference/attributes/hx-on) listens for the [`htmx:after:request`](https://four.htmx.org/reference/events/htmx-after-request) event and calls `this.reset()` to clear the form.

On the server, respond with the new message:

```html
<div class="message user">Hello!</div>
<div class="message bot">Hi there! How can I help?</div>
```

## Notes

### Without a form element

The `reset()` method is only available on `<form>` elements. For standalone inputs, select the element and clear its value directly:

```html
<input id="chat-input" type="text" name="message">
<button hx-post="/chat"
        hx-target="#messages"
        hx-swap="beforeend"
        hx-include="#chat-input"
        hx-on:htmx:after:request="document.getElementById('chat-input').value = ''">
    Send
</button>
```

- [`hx-include`](https://four.htmx.org/reference/attributes/hx-include) tells the button which input to include in the request, since it is outside the button element.