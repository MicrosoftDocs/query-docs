---
title: "List.IsDistinct | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# List.IsDistinct

## Syntax

<pre>
List.IsDistinct(<b>list</b> as list, optional <b>equationCriteria</b> as any) as logical 
</pre>
  
## About  
Returns a logical value whether there are duplicates in the list `list`; `true` if the list is distinct, `false` if there are duplicate values. 

## Example 1
Find if the list {1, 2, 3} is distinct (i.e. no duplicates).

```powerquery-m
List.IsDistinct({1, 2, 3})
```

`true`

## Example 2
Find if the list {1, 2, 3, 3} is distinct (i.e. no duplicates).

```powerquery-m
List.IsDistinct({1, 2, 3, 3})
```

`false`
