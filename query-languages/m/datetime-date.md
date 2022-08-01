---
description: "Learn more about: DateTime.Date"
title: "DateTime.Date"
ms.date: 3/11/2022
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

**Usage**

```powerquery-m
DateTime.Date(#datetime(2010, 12, 31, 11, 56, 02))
```

**Output**

`#date(2010, 12, 31)`
