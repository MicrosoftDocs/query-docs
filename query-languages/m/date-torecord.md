---
description: "Learn more about: Date.ToRecord"
title: "Date.ToRecord"
ms.subservice: m-source
ms.topic: reference
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
