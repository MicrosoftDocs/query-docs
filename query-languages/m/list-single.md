---
title: "List.Single | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# List.Single

## Syntax

<pre>
List.Single(<b>list</b> as list) as any  
</pre>
  
## About  
If there is only one item in the list `list`, returns that item. If there is more than one item or the list is empty, the function throws an exception.

## Example 1
Find the single value in the list {1}.

```powerquery-m
List.Single({1})
```

`1`

## Example 2
Find the single value in the list {1, 2, 3}.

```powerquery-m
List.Single({1, 2, 3})
```

`[Expression.Error] There were too many elements in the enumeration to complete the operation.`
