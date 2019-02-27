# flag-status
flag-status API using Flask

#### How should I display my flag?

This is an attempt to keep you up-to-date as to whether or not a flag should (officially) be flown at half- or full-mast.
First, retrieve a [list of supported flags](https://bluepale.net/flag-status/flags/), and then request the [status of a flag](https://bluepale.net/flag-status/flags/us/). All responses are in valid [json](https://json.org).

#### Example API Request/Response

    curl https://bluepale.net/flag-status/flags/us/

    {
      "half_staff": false,
      "message": "success",
      "reason": "normal operations",
      "until": "indefinitely"
    }
