---
description: "Learn more about: List.Random"
title: "List.Random | Microsoft Docs"
ms.date: 3/8/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# List.Random

## Syntax

<pre>
List.Random(<b>count</b> as number, optional <b>seed</b> as nullable number) as list
</pre>
  
## About

Returns a list of random numbers between 0 and 1, given the number of values to generate and an optional seed value.

* `count`: The number of random values to generate.
* `seed`: _[Optional]_ A numeric value used to seed the random number generator. If omitted a unique list of random numbers is generated each time you call the function. If you specify the seed value with a number every call to the function generates the same list of random numbers.

## Example 1

Create a list of 3 random numbers.

**Usage**

```powerquery-m
List.Random(3)
```

**Output**

`{0.992332, 0.132334, 0.023592}`

## Example 2

Create a list of 3 random numbers, specifying seed value.

**Usage**

```powerquery-m
List.Random(3, 2)
```

**Output**

`{0.883002, 0.245344, 0.723212}`
