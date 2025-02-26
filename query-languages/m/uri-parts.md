---
description: "Learn more about: Uri.Parts"
title: "Uri.Parts"
ms.subservice: m-source
---
# Uri.Parts

## Syntax

<pre>
Uri.Parts(<b>absoluteUri</b> as text) as record
</pre>

## About

Returns the parts of the input `absoluteUri` as a record, containing values such as Scheme, Host, Port, Path, Query, Fragment, UserName and Password.

## Example 1

Find the parts of the absolute URI "www.adventure-works.com".

**Usage**

```powerquery-m
Uri.Parts("www.adventure-works.com")
```

**Output**

```powerquery-m
[
    Scheme = "http",
    Host = "www.adventure-works.com",
    Port = 80,
    Path = "/",
    Query = [],
    Fragment = "",
    UserName = "",
    Password = ""
]
```

## Example 2

Decode a percent-encoded string.

**Usage**

```powerquery-m
let
    UriUnescapeDataString = (data as text) as text => Uri.Parts("http://contoso?a=" & data)[Query][a]
in
    UriUnescapeDataString("%2Bmoney%24")
```

**Output**

`"+money$"`
