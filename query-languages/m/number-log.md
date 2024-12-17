---
description: "Learn more about: Number.Log"
title: "Number.Log"
ms.subservice: m-source
---
# Number.Log

## Syntax

<pre>
Number.Log(<b>number</b> as nullable number, optional <b>base</b> as nullable number) as nullable number
</pre>

## About

Returns the logarithm of a number, `number`, to the specified `base` base. If `base` is not specified, the default value is Number.E. If `number` is null **Number.Log** returns null.

## Example 1

Get the base 10 logarithm of 2.

**Usage**

```powerquery-m
Number.Log(2, 10)
```

**Output**

`0.3010299956639812`

## Example 2

Get the base e logarithm of 2.

**Usage**

```powerquery-m
Number.Log(2)
```

**Output**

`0.69314718055994529`
