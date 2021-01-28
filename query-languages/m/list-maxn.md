---
description: "Learn more about: List.MaxN"
title: "List.MaxN | Microsoft Docs"
ms.date: 7/31/2019
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
Returns the maximum value(s) in the list, `list`. After the rows are sorted, optional parameters may be specified to further filter the result. The optional parameter, `countOrCondition`, specifies the number of values to return or a filtering condition. The optional parameter, `comparisonCriteria`, specifies how to compare values in the list. <ul> <li> <code>list</code>: The list of values.</li> <li> <code>countOrCondition</code>: If a number is specified, a list of up to <code>countOrCondition</code> items in ascending order is returned. If a condition is specified, a list of items that initially meet the condition is returned. Once an item fails the condition, no further items are considered.</li> <li><code>comparisonCriteria</code>: <i>[Opional]</i> An optional <code>comparisonCriteria</code> value, may be specified to determine how to compare the items in the list. If this parameter is null, the default comparer is used. </ul>
