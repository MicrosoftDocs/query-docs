---
title: "Duration.From | Microsoft Docs"
ms.date: 7/30/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Duration.From

## Syntax

<pre>
Duration.From(<b>value</b> as any) as nullable duration
</pre>
  
## About  
Returns a `duration` value from the given `value`. If the given `value` is `null`, `Duration.From` returns `null`. If the given `value` is `duration`, `value` is returned. Values of the following types can be converted to a `duration` value: <ul> <li><code>text</code>: A <code>duration</code> value from textual elapsed time forms (d.h:m:s). See <code>Duration.FromText</code> for details.</li> <li><code>number</code>: A <code>duration</code> equivalent to the number of whole and fractional days expressed by <code>value</code>.</li> </ul> If <code>value</code> is of any other type, an error is returned.

## Example 1
Convert `2.525` into a `duration` value.

```powerquery-m
Duration.From(2.525)
```

`#duration(2, 12, 36, 0)`
