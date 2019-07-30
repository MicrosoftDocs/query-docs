---
title: "DateTimeZone.From | Microsoft Docs"
ms.date: 7/30/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTimeZone.From

## Syntax

<pre>
DateTimeZone.From(<b>value</b> as any, optional <b>culture</b> as nullable text) as nullable datetimezone
</pre>
  
## About  
Returns a `datetimezone` value from the given `value`. If the given `value` is `null`, `DateTimeZone.From` returns `null`. If the given `value` is `datetimezone`, `value` is returned. Values of the following types can be converted to a `datetimezone` value: <ul> <li><code>text</code>: A <code>datetimezone</code> value from textual representation. See <code>DateTimeZone.FromText</code> for details.</li> <li><code>date</code>: A <code>datetimezone</code> with <code>value</code> as the date component, <code>12:00:00 AM</code> as the time component and the offset corresponding the local time zone.</li> <li><code>datetime</code>: A <code>datetimezone</code> with <code>value</code> as the datetime and the offset corresponding the local time zone.</li> <li><code>time</code>: A <code>datetimezone</code> with the date equivalent of the OLE Automation Date of <code>0</code> as the date component, <code>value</code> as the time component and the offset corresponding the local time zone.</li> <li><code>number</code>: A <code>datetimezone</code> with the datetime equivalent the OLE Automation Date expressed by <code>value</code> and the offset corresponding the local time zone.</li> </ul> If `value` is of any other type, an error is returned.

## Example 1
Convert `"2020-10-30T01:30:00-08:00"` to a `datetimezone` value.

```powerquery-m
DateTimeZone.From("2020-10-30T01:30:00-08:00")
```

`#datetimezone(2020, 10, 30, 01, 30, 00, -8, 00)`

