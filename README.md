## Telegram Microservice

I created this to fulfil my own requirement.
It's a simple micrsoservice send message to a telegram group using [Telegram API](https://core.telegram.org/api).

Methods:

  1.`GET /`
    
    Response a JSON object
    { telegram_bot: "Hello There! }

  2. `POST /send`

    Request (JSON object)
    {
      name: String,   // Alphabets and spaces only
      email: String,  // A valid email id.
      message: String // Message to send (ASCII characters are allowed only).
    }

    Response (JSON object)
    {
      ok: boolean,
      result: {...}
    }
