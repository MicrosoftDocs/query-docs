---
title: "List.Difference | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# List.Difference

<pre>
List.Difference(<b>list1</b> as list, <b>list2</b> as list, optional <b>equationCriteria</b> as any) as list
</pre>
  
## About  
Returns the items in list `list1` that do not appear in list `list2`. Duplicate values are supported. An optional equation criteria value, `equationCriteria`, can be specified to control equality testing. 

## Example 1
Find the items in list {1, 2, 3, 4, 5}that do not appear in {4, 5, 3}.

```powerquery-m
List.Difference({1, 2, 3, 4, 5}, {4, 5, 3}
```

<table> <tr><td>1</td></tr> <tr><td>2</td></tr> </table>

## Example 2
Find the items in the list {1, 2} that do not appear in {1, 2, 3}.

```powerquery-m
List.Difference({1, 2}, {1, 2, 3})
```

<table> </table>
