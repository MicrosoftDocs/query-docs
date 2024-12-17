---
description: "Learn more about: Duration.Seconds"
title: "Duration.Seconds"
ms.subservice: m-source
---
# Duration.Seconds

## Syntax

<pre>
Duration.Seconds(<b>duration</b> as nullable duration) as nullable number
</pre>
  
## About

Returns the seconds portion of `duration`.

## Example 1

Extract the seconds from a duration value.

**Usage**

```powerquery-m
Duration.Seconds(#duration(5, 4, 3, 2))
```

**Output**

`2`
