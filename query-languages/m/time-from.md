---
title: "Time.From | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Time.From

## Syntax

<pre> 
Time.From(<b>value</b> as any, optional <b>culture</b> as nullable text) as nullable time 
</pre>
  
## About  
Returns a `time` value from the given `value`. If the given `value` is `null`, `Time.From` returns `null`. If the given `value` is `time`, `value` is returned. Values of the following types can be converted to a `time` value: <ul> <li><code>text</code>: A <code>time</code> value from textual representation. See <code>Time.FromText</code> for details.</li> <li><code>datetime</code>: The time component of the <code>value</code>.</li> <li><code>datetimezone</code>: The time component of the local datetime equivalent of <code>value</code>.</li> <li><code>number</code>: A <code>time</code> equivalent to the number of fractional days expressed by <code>value</code>. If <code>value</code> is negative or greater or equal to 1, an error is returned.</li> </ul> If <code>value</code> is of any other type, an error is returned.

## Example 1
Convert `0.7575` to a `time` value.

```powerquery-m
Time.From(0.7575)
```

`#time(18,10,48)`

## Example 2
Convert `#datetime(1899, 12, 30, 06, 45, 12)` to a `time` value.

```powerquery-m
Time.From(#datetime(1899, 12, 30, 06, 45, 12))
```

`#time(06, 45, 12)`
