---
title: "Uri.EscapeDataString | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Uri.EscapeDataString

## Syntax

<pre>
Uri.EscapeDataString(<b>data</b> as text) as text
</pre>

## About
Encodes special characters in the input `data` according to the rules of RFC 3986.

## Example 
Encode the special characters in "+money$".

```powerquery-m
Uri.EscapeDataString("+money$")
```

`"%2Bmoney%24"`

