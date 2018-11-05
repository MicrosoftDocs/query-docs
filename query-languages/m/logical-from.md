---
title: "Logical.From | Microsoft Docs"
ms.date: 8/30/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Logical.From

## Syntax

<pre>
Logical.From(<b>value</b> as any) as nullable logical
</pre>


## About

Returns a `logical` value from the given `value`. If the given `value` is `null`, `Logical.From` returns `null`. If the given `value` is `logical`, `value` is returned. 

Values of the following types can be converted to a `logical` value: <ul> <li>`text`: A `logical` value from the text value, either `"true"` or `"false"`. See `Logical.FromText` for details.</li> <li>`number`: `false` if `value` equals `0`, `true` otherwise.</li> </ul> If `value` is of any other type, an error is returned.

## Example 1
Convert `2` to a `logical` value.

```powerquery-m
Logical.From(2)
```

`true`
