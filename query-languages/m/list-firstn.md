---
description: "Learn more about: List.FirstN"
title: "List.FirstN"
ms.date: 3/8/2022
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# List.FirstN

## Syntax

<pre>
List.FirstN(<b>list</b> as list, <b>countOrCondition</b> as any) as any
</pre>
  
## About

* If a number is specified, up to that many items are returned.
* If a condition is specified, all items are returned that initially meet the condition. Once an item fails the condition, no further items are considered.

## Example 1

Find the intial values in the list {3, 4, 5, -1, 7, 8, 2} that are greater than 0.

**Usage**

```powerquery-m
List.FirstN({3, 4, 5, -1, 7, 8, 2}, each _ > 0)
```

**Output**

`{3, 4, 5}`
