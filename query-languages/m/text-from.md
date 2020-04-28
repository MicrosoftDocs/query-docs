---
title: "Text.From | Microsoft Docs"
ms.date: 4/21/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Text.From

## Syntax

<pre>
Text.From(<b>value</b> as any, optional <b>culture</b> as nullable text) as nullable text
</pre>
  
## About  
Returns the text representation of `value`. The `value` can be a `number`, `date`, `time`, `datetime`, `datetimezone`, `logical`, `duration` or `binary` value. If the given value is null, `Text.From` returns null. An optional `culture` may also be provided (for example, "en-US").

## Example 1
Create a text value from the number 3.

```powerquery-m
Text.From(3)
```

`"3"`
