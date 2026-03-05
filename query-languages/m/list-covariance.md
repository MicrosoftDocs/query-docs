---
description: "Learn more about: List.Covariance"
title: "List.Covariance"
ms.subservice: m-source
ms.topic: reference
---
# List.Covariance

## Syntax

<pre>
List.Covariance(<b>numberList1</b> as list, <b>numberList2</b> as list) as nullable number
</pre>

## About

Returns the covariance between two lists, `numberList1` and `numberList2`. `numberList1` and `numberList2` must contain the same number of `number` values.

## Example 1

Calculate the covariance between two lists.

**Usage**

```powerquery-m
List.Covariance({1, 2, 3}, {1, 2, 3})
```

**Output**

`0.66666666666666607`
