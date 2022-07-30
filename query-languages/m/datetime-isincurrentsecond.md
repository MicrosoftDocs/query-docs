---
description: "Learn more about: DateTime.IsInCurrentSecond"
title: "DateTime.IsInCurrentSecond"
ms.date: 3/11/2022
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# DateTime.IsInCurrentSecond

## Syntax

<pre>
DateTime.IsInCurrentSecond(<b>dateTime</b> as any) as nullable logical
</pre>
  
## About

Indicates whether the given datetime value `dateTime` occurs during the current second, as determined by the current date and time on the system.

* `dateTime`: A `datetime`, or `datetimezone` value to be evaluated.

## Example 1

Determine if the current system time is in the current second.

**Usage**

```powerquery-m
DateTime.IsInCurrentSecond(DateTime.FixedLocalNow())
```

**Output**

`true`
