---
description: "Learn more about: DateTime.Date"
title: "DateTime.Date"
---
# DateTime.Date

## Syntax

<pre>
DateTime.Date(<b>dateTime</b> as any) as nullable date 
</pre>
  
## About

Returns the date component of the `dateTime` parameter if the parameter is a `date`, `datetime`, or `datetimezone` value, or `null` if the parameter is `null`.

## Example 1

Find date value of #datetime(2010, 12, 31, 11, 56, 02).

**Usage**

```powerquery-m
DateTime.Date(#datetime(2010, 12, 31, 11, 56, 02))
```

**Output**

`#date(2010, 12, 31)`
