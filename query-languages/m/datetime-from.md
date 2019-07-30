---
title: "DateTime.From | Microsoft Docs"
ms.date: 7/30/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTime.From

## Syntax

<pre>
DateTime.From(<b>value</b> as any, optional <b>culture</b> as nullable text) as nullable datetime
</pre>
  
## About  
Returns a `datetime` value from the given `value`. If the given `value` is `null`, `DateTime.From` returns `null`. If the given `value` is `datetime`, `value` is returned. Values of the following types can be converted to a `datetime` value: <ul> <li><code>text</code>: A <code>datetime</code> value from textual representation. See <code>DateTime.FromText</code> for details.</li> <li><code>date</code>: A <code>datetime</code> with <code>value</code> as the date component and <code>12:00:00 AM</code> as the time component.</li> <li><code>datetimezone</code>: The local <code>datetime</code> equivalent of <code>value</code>.</li> <li><code>time</code>: A <code>datetime</code> with the date equivalent of the OLE Automation Date of <code>0</code> as the date component and <code>value</code> as the time component.</li> <li><code>number</code>: A <code>datetime</code> equivalent the OLE Automation Date expressed by <code>value</code>. </li> </ul> If `value` is of any other type, an error is returned.

## Example 1
Convert `#time(06, 45, 12)` to a `datetime` value.

```powerquery-m
DateTime.From(#time(06, 45, 12))
```

```powerquery-m
#datetime(1899, 12, 30, 06, 45, 12)
```

## Example 2
Convert `#date(1975, 4, 4)` to a `datetime` value.

```powerquery-m
DateTime.From(#date(1975, 4, 4))
```

```powerquery-m
#datetime(1975, 4, 4, 0, 0, 0)
```
