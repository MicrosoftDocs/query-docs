---
title: "DateTime.Date | Microsoft Docs"
ms.date: 7/30/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# DateTime.Date

## Syntax

<pre>
DateTime.Date(<b>dateTime</b> as any) as nullable date 
</pre>
  
## About  
Returns the date component of `dateTime`, the given `date`, `datetime`, or `datetimezone` value.

## Example 1
Find date value of #datetime(2010, 12, 31, 11, 56, 02).

```powerquery-m
DateTime.Date(#datetime(2010, 12, 31, 11, 56, 02))
```

`#date(2010, 12, 31)`
