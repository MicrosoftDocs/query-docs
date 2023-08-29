---
description: "Learn more about: Number.Sign"
title: "Number.Sign"
---
# Number.Sign

## Syntax

<pre>
Number.Sign(<b>number</b> as nullable number) as nullable number
</pre>
  
## About

Returns 1 for if `number` is a positive number, -1 if it is a negative number, and 0 if it is zero. If `number` is null, `Number.Sign` returns null.

## Example 1

Determine the sign of 182.

**Usage**

```powerquery-m
Number.Sign(182)
```

**Output**

`1`

## Example 2

Determine the sign of -182.

**Usage**

```powerquery-m
Number.Sign(-182)
```

**Output**

`-1`

## Example 3

Determine the sign of 0.

**Usage**

```powerquery-m
Number.Sign(0)
```

**Output**

`0`
