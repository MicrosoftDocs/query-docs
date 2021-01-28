---
description: "Learn more about: Number.Combinations"
title: "Number.Combinations | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Number.Combinations

## Syntax

<pre>
Number.Combinations(<b>setSize</b> as nullable number, <b>combinationSize</b> as nullable number) as nullable number
</pre>
  
## About  
Returns the number of unique combinations from a list of items, `setSize` with specified combination size, `combinationSize`. <ul> <li><code>setSize</code>: The number of items in the list.</li> <li><code>combinationSize</code>: The number of items in each combination.</li> </ul> 

## Example 1
Find the number of combinations from a total of 5 items when each combination is a group of 3.

```powerquery-m
Number.Combinations(5, 3)
```

`10`
