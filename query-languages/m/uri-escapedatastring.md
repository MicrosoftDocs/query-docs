---
description: "Learn more about: Uri.EscapeDataString"
title: "Uri.EscapeDataString | Microsoft Docs"
ms.date: 3/14/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

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
