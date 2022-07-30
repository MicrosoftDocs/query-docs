---
description: "Learn more about: Number.Abs"
title: "Number.Abs"
ms.date: 3/11/2022
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Number.Abs

## Syntax

<pre>
Number.Abs(<b>number</b> as nullable number) as nullable number
</pre>
  
## About

Returns the absolute value of `number`. If `number` is null, **Number.Abs** returns null.

* `number`: A `number` for which the absolute value is to be calculated.

## Example 1

Absolute value of -3.

**Usage**

```powerquery-m
Number.Abs(-3)
```

**Output**

`3`
