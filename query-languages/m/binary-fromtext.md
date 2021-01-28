---
description: "Learn more about: Binary.FromText"
title: "Binary.FromText | Microsoft Docs"
ms.date: 12/12/2018
ms.service: powerquery
ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Binary.FromText

## Syntax

<pre>
Binary.FromText(<b>text</b> as nullable text, optional <b>encoding</b> as nullable number) as nullable binary
</pre>

## About
Returns the result of converting text value `text` to a binary (list of `number`). `encoding` may be specified to indicate the encoding used in the text value. The following `BinaryEncoding` values may be used for `encoding`. <ul> <li>`BinaryEncoding.Base64`: Base 64 encoding</li> <li>`BinaryEncoding.Hex`: Hex encoding</li> </ul>

## Example 1

Decode `"1011"` into binary.

```powerquery-m
Binary.FromText("1011")
```

```powerquery-m
Binary.FromText("1011", BinaryEncoding.Base64)
```

## Example 2
Decode `"1011"` into binary with Hex encoding.

```powerquery-m
Binary.FromText("1011", BinaryEncoding.Hex)
```

```powerquery-m
Binary.FromText("EBE=", BinaryEncoding.Base64)
```

