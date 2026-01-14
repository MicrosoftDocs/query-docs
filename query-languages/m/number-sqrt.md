---
description: "Learn more about: Number.Sqrt"
title: "Number.Sqrt"
ms.subservice: m-source
ms.topic: reference
---
# Number.Sqrt

## Syntax

<pre>
Number.Sqrt(<b>number</b> as nullable number) as nullable number
</pre>
  
## About

Returns the square root of `number`. If `number` is null, **Number.Sqrt** returns null. If it is a negative value, [Number.NaN](/powerquery-m/number-nan) is returned (Not a number).

## Example 1

Find the square root of 625.

**Usage**

```powerquery-m
Number.Sqrt(625)
```

**Output**

`25`

## Example 2

Find the square root of 85.

**Usage**

```powerquery-m
Number.Sqrt(85)
```

**Output**

`9.2195444572928871`
