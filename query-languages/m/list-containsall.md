---
description: "Learn more about: List.ContainsAll"
title: "List.ContainsAll"
ms.date: 3/11/2022
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# List.ContainsAll

## Syntax

<pre>
List.ContainsAll(<b>list</b> as list, <b>values</b> as list, optional <b>equationCriteria</b> as any) as logical
</pre>
  
## About

Indicates whether the list `list` includes all the values in another list, `values`. Returns true if value is found in the list, false otherwise. An optional equation criteria value, `equationCriteria`, can be specified to control equality testing.

## Example 1

Find out if the list {1, 2, 3, 4, 5} contains 3 and 4.

**Usage**

```powerquery-m
List.ContainsAll({1, 2, 3, 4, 5}, {3, 4})
```

**Output**

`true`

## Example 2

Find out if the list {1, 2, 3, 4, 5} contains 5 and 6.

**Usage**

```powerquery-m
List.ContainsAll({1, 2, 3, 4, 5}, {5, 6})
```

**Output**

`false`
