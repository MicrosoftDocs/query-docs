---
description: "Learn more about: Time.Minute"
title: "Time.Minute"
---
# Time.Minute

## Syntax

<pre> 
Time.Minute(<b>dateTime</b> as any) as nullable number
</pre>
  
## About

Returns the minute component of the provided `time`, `datetime`, or `datetimezone` value, `dateTime`.

## Example 1

Find the minute in #datetime(2011, 12, 31, 9, 15, 36).

**Usage**

```powerquery-m
Time.Minute(#datetime(2011, 12, 31, 9, 15, 36))
```

**Output**

`15`
