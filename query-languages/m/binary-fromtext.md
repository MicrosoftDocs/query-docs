---
description: "Learn more about: Binary.FromText"
title: "Binary.FromText"
ms.date: 12/2/2022
---
# Binary.FromText

## Syntax

<pre>
Binary.FromText(<b>text</b> as nullable text, optional <b>encoding</b> as nullable number) as nullable binary
</pre>

## About

Returns the result of converting text value `text` to a binary (list of `number`). `encoding` may be specified to indicate the encoding used in the text value. The following `BinaryEncoding` values may be used for `encoding`.

* [BinaryEncoding.Base64](binaryencoding-type.md): Base 64 encoding
* [BinaryEncoding.Hex](binaryencoding-type.md): Hex encoding

## Example 1

Decode `"1011"` into binary.

**Usage**

```powerquery-m
Binary.FromText("1011")
```

**Output**

```powerquery-m
Binary.FromText("1011", BinaryEncoding.Base64)
```

## Example 2

Decode `"1011"` into binary with Hex encoding.

**Usage**

```powerquery-m
Binary.FromText("1011", BinaryEncoding.Hex)
```

**Output**

```powerquery-m
Binary.FromText("EBE=", BinaryEncoding.Base64)
```
