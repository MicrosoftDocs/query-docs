---
description: "Learn more about: Uri.EscapeDataString"
title: "Uri.EscapeDataString"
ms.date: 3/14/2022
---
# Uri.EscapeDataString

## Syntax

<pre>
Uri.EscapeDataString(<b>data</b> as text) as text
</pre>

## About

Encodes special characters in the input `data` according to the rules of RFC 3986.

## Example 1

Encode the special characters in "+money$".

**Usage**

```powerquery-m
Uri.EscapeDataString("+money$")
```

**Output**

`"%2Bmoney%24"`
