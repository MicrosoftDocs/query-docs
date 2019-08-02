---
title: "Text.From | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.From

## Syntax

<pre>
Text.From(<b>value</b> as any, optional <b>culture</b> as nullable text) as nullable text
</pre>
  
## About  
Returns the text representation of `value`. The `value` can be a `number`, `date`, `time`, `datetime`, `datetimezone`, `logical`, `duration` or `binary` value. If the given value is null, `Text.From` returns null. An optional `culture` may also be provided.

## Example 1
Create a text value from the number 3.

```powerquery-m
Text.From(3)
```

`"3"`
