---
description: "Learn more about: Number.IsNaN"
title: "Number.IsNaN"
ms.subservice: m-source
ms.topic: reference
---
# Number.IsNaN

## Syntax

<pre>
Number.IsNaN(<b>number</b> as number) as logical
</pre>
  
## About

Indicates if the value is NaN (Not a number). Returns `true` if `number` is equivalent to **Number.IsNaN**, `false` otherwise.

## Example 1

Check if 0 divided by 0 is NaN.

**Usage**

```powerquery-m
Number.IsNaN(0/0)
```

**Output**

`true`

## Example 2

Check if 1 divided by 0 is NaN.

**Usage**

```powerquery-m
Number.IsNaN(1/0)
```

**Output**

`false`
