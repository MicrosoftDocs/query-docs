---
title: "List.Split | Microsoft Docs"
ms.date: 5/22/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Split

## Syntax

<pre>
List.Split(<b>list</b> as list, <b>pageSize</b> as number) as list
</pre>

## About
Splits `list` into a list of lists where the first element of the output list is a list containing the first `pageSize` elements from the source list, the next element of the output list is a list containing the next `pageSize` elements from the source list, etc.
