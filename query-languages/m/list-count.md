---
description: "Learn more about: List.Count"
title: "List.Count | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# List.Count

## Syntax

<pre>
List.Count(<b>list</b> as list) as number  
</pre>
  
## About  
Returns the number of items in the list `list`.

## Example 1
Find the number of values in the list {1, 2, 3}.

```powerquery-m
List.Count({1, 2, 3})
```

`3`
