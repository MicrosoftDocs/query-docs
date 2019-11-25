---
title: "List.Mode | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# List.Mode

## Syntax

<pre>
List.Mode(<b>list</b> as list, optional <b>equationCriteria</b> as any) as any 
</pre>
  
## About  
Returns the item that appears most frequently in the list, `list`. If the list is empty an exception is thrown. If multiple items appear with the same maximum frequency, the last one is chosen. An optional `comparisonCriteria` value, `equationCriteria`, can be specified to control equality testing. 

## Example 1
Find the item that appears most frequently in the list `{"A", 1, 2, 3, 3, 4, 5}`.

```powerquery-m
List.Mode({"A", 1, 2, 3, 3, 4, 5})
```

`3`

## Example 2
Find the item that appears most frequently in the list `{"A", 1, 2, 3, 3, 4, 5, 5}`.

```powerquery-m
List.Mode({"A", 1, 2, 3, 3, 4, 5, 5})
```

`5`
