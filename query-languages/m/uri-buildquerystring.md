---
description: "Learn more about: Uri.BuildQueryString"
title: "Uri.BuildQueryString"
ms.subservice: m-source
---
# Uri.BuildQueryString

## Syntax

<pre>
Uri.BuildQueryString(<b>query</b> as record) as text
</pre>

## About

Assemble the record `query` into a URI query string, escaping characters as necessary.

## Example 1

Encode a query string which contains some special characters.

**Usage**

```powerquery-m
Uri.BuildQueryString([a = "1", b = "+$"])
```

**Output**

`"a=1&b=%2B%24"`
