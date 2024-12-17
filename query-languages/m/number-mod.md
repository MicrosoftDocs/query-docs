---
description: "Learn more about: Number.Mod"
title: "Number.Mod"
ms.subservice: m-source
---
# Number.Mod

## Syntax

<pre>
Number.Mod(<b>number</b> as nullable number, <b>divisor</b> as nullable number, optional <b>precision</b> as nullable number) as nullable number
</pre>
  
## About

Returns the remainder resulting from the integer division of `number` by `divisor`. If `number` or `divisor` are null, `Number.Mod` returns null.

* `number`: The dividend.
* `divisor`: The divisor.

## Example 1

Find the remainder when you divide 5 by 3.

**Usage**

```powerquery-m
Number.Mod(5, 3)
```

**Output**

`2`
