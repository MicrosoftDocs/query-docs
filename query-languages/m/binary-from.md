---
title: "Binary.From | Microsoft Docs"
ms.date: 12/12/2018
ms.service: powerquery
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Binary.From

## Syntax  

<pre>
Binary.From(<b>value</b> as any, optional <b>encoding</b> as nullable number) as nullable binary
</pre>

## About
Returns a `binary` value from the given `value`. If the given `value` is `null`, `Binary.From` returns `null`. If the given `value` is `binary`, `value` is returned. Values of the following types can be converted to a `binary` value: <ul> <li>`text`: A `binary` value from the text representation. See `Binary.FromText` for details.</li> </ul> If `value` is of any other type, an error is returned.

## Example 1
Get the `binary` value of `"1011"`.

```powerquery-m
Binary.From("1011")
```

`Binary.FromText("1011", BinaryEncoding.Base64)`