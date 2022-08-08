---
description: "Learn more about: Number.IntegerDivide"
title: "Number.IntegerDivide"
ms.date: 3/11/2022
---
# Number.IntegerDivide

## Syntax

<pre>
Number.IntegerDivide(<b>number1</b> as nullable number, <b>number2</b> as nullable number, optional <b>precision</b> as nullable number) as nullable number
</pre>
  
## About

Returns the integer portion of the result from dividing a number, `number1`, by another number, `number2`. If `number1` or `number2` are null, **Number.IntegerDivide** returns null.

* `number1`: The dividend.
* `number2`: The divisor.

## Example 1

Divide 6 by 4.

**Usage**

```powerquery-m
Number.IntegerDivide(6, 4)
```

**Output**

`1`

## Example 2

Divide 8.3 by 3.

**Usage**

```powerquery-m
Number.IntegerDivide(8.3, 3)
```

**Output**

`2`
