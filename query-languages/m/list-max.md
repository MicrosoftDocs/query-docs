---
title: "List.Max | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# List.Max

## Syntax

<pre>
List.Max(<b>list</b> as list, optional <b>default</b> as any, optional <b>comparisonCriteria</b> as any, optional <b>includeNulls</b> as nullable logical) as any
</pre>
  
## About  
Returns the maximum item in the list `list`, or the optional default value `default` if the list is empty. An optional comparisonCriteria value, `comparisonCriteria`, may be specified to determine how to compare the items in the list. If this parameter is null, the default comparer is used.

## Example 1
Find the max in the list {1, 4, 7, 3, -2, 5}.

```powerquery-m
List.Max({1, 4, 7, 3, -2, 5},1)
```

`7`

## Example 2
Find the max in the list {} or return -1 if it is empty. 

```powerquery-m
List.Max({}, -1)
```

`-1`
