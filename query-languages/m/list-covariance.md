---
title: "List.Covariance | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Covariance

## Syntax

<pre>
List.Covariance(<b>numberList1</b> as list, <b>numberList2</b> as list) as nullable number 
</pre>
  
## About  
Returns the covariance between two lists, `numberList1` and `numberList2`. `numberList1` and `numberList2` must contain the same number of `number` values.

## Example 1
Calculate the covariance between two lists.

```powerquery-m
List.Covariance({1, 2, 3},{1, 2, 3})
```

`0.66666666666666607`
