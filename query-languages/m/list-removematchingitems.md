---
title: "List.RemoveMatchingItems | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# List.RemoveMatchingItems

## Syntax

<pre>
List.RemoveMatchingItems(<b>list1</b> as list, <b>list2</b> as list, optional <b>equationCriteria</b> as any) as list
</pre>
  
## About  
Removes all occurrences of the given values in `list2` from the list `list1`. If the values in `list2` don't exist in `list1`, the original list is returned. An optional equation criteria value, `equationCriteria`, can be specified to control equality testing. 

## Example 1
Create a list from {1, 2, 3, 4, 5, 5} without {1, 5}.

```powerquery-m
List.RemoveMatchingItems({1, 2, 3, 4, 5, 5}, {1, 5})
```

<table> <tr><td>2</td></tr> <tr><td>3</td></tr> <tr><td>4</td></tr> </table>
