---
description: "Learn more about: Binary.ToText"
title: "Binary.ToText"
ms.subservice: m-source
---
# Binary.ToText

## Syntax

<pre>
Binary.ToText(<b>binary</b> as nullable binary, optional <b>encoding</b> as nullable number) as nullable text
</pre>

## About

Returns the result of converting a binary list of numbers `binary` into a text value. Optionally, `encoding` may be specified to indicate the encoding to be used in the text value produced The following `BinaryEncoding` values may be used for `encoding`.

* `BinaryEncoding.Base64`: Base 64 encoding
* `BinaryEncoding.Hex`: Hex encoding
