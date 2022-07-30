---
description: "Learn more about: Date.ToRecord"
title: "Date.ToRecord | Microsoft Docs"
ms.date: 3/8/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Date.ToRecord

## Syntax

<pre>
Date.ToRecord(<b>date</b> as date) as record
</pre>
  
## About

Returns a record containing the parts of the given date value, `date`.

* `date`: A `date` value for from which the record of its parts is to be calculated.

## Example 1

Convert the `#date(2011, 12, 31)` value into a record containing parts from the date value.

**Usage**

```powerquery-m
Date.ToRecord(#date(2011, 12, 31))
```

**Output**

```powerquery-m
[
      Year = 2011,
      Month = 12,
      Day = 31
]
```
