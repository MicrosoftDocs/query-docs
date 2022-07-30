---
description: "Learn more about: Time.ToRecord"
title: "Time.ToRecord"
ms.date: 3/11/2022
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Time.ToRecord

## Syntax

<pre>
Time.ToRecord(<b>time</b> as time) as record
</pre>
  
## About

Returns a record containing the parts of the given Time value, `time`.

* `time`: A `time` value for from which the record of its parts is to be calculated.

## Example 1

Convert the `#time(11, 56, 2)` value into a record containing Time values.

**Usage**

```powerquery-m
Time.ToRecord(#time(11, 56, 2))
```

**Output**

```powerquery-m
[
      Hour = 11,
      Minute = 56,
      Second = 2
]
```
