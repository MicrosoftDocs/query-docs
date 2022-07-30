---
description: "Learn more about: DateTime.ToRecord"
title: "DateTime.ToRecord | Microsoft Docs"
ms.date: 3/8/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# DateTime.ToRecord

## Syntax

<pre>
DateTime.ToRecord(<b>dateTime</b> as datetime) as record
</pre>
  
## About

Returns a record containing the parts of the given datetime value, `dateTime`.

* `dateTime`: A `datetime` value for from which the record of its parts is to be calculated.

## Example 1

Convert the `#datetime(2011, 12, 31, 11, 56, 2)` value into a record containing Date and Time values.

**Usage**

```powerquery-m
DateTime.ToRecord(#datetime(2011, 12, 31, 11, 56, 2))
```

**Output**

```powerquery-m
[
      Year = 2011,
      Month = 12,
      Day = 31,
      Hour = 11,
      Minute = 56,
      Second = 2
]
```
