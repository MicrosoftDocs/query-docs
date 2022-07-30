---
description: "Learn more about: Text.From"
title: "Text.From"
ms.date: 3/14/2022
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

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

**Usage**

```powerquery-m
Text.From(3)
```

**Output**

`"3"`
