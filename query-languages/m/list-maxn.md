---
description: "Learn more about: List.MaxN"
title: "List.MaxN | Microsoft Docs"
ms.date: 3/16/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# List.MaxN

## Syntax

<pre>
List.MaxN(<b>list</b> as list, <b>countOrCondition</b> as any, optional <b>comparisonCriteria</b> as any, optional <b>includeNulls</b> as nullable logical) as list
</pre>
  
## About

Returns the maximum value(s) in the list, `list`. After the rows are sorted, optional parameters may be specified to further filter the result. The optional parameter `countOrCondition` specifies the number of values to return or a filtering condition. The optional parameter `comparisonCriteria` specifies how to compare values in the list.

* `list`: The list of values.
* `countOrCondition`: If a number is specified, a list of up to `countOrCondition` items in ascending order is returned. If a condition is specified, a list of items that initially meet the condition is returned. Once an item fails the condition, no further items are considered.
* `comparisonCriteria`: _[Optional]_ An optional `comparisonCriteria` value can be specified to determine how to compare the items in the list. If this parameter is null, the default comparer is used.
