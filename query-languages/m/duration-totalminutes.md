---
description: "Learn more about: Duration.TotalMinutes"
title: "Duration.TotalMinutes"
---
# Duration.TotalMinutes

## Syntax

<pre>
Duration.TotalMinutes(<b>duration</b> as nullable duration) as nullable number 
</pre>
  
## About

Returns the total minutes spanned by `duration`.

## Example 1

Find the total minutes spanned by a duration value.

**Usage**

```powerquery-m
Duration.TotalMinutes(#duration(5, 4, 3, 2))
```

**Output**

`7443.0333333333338`
