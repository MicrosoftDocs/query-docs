---
title: "List.Median | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Median
<code>List.Median(**list** as list, optional **comparisonCriteria** as any) as any</code>

## About
Returns the median item of the list <code>list</code>. This function returns <code>null</code> if the list contains no non-<code>null</code> values. If there is an even number of items, the function chooses the smaller of the two median items unless the list is comprised entirely of datetimes, durations, numbers or times, in which case it returns the average of the two items.

## Example 1
Find the median of the list <code>{5, 3, 1, 7, 9}</code>.

<code>List.Median({5, 3, 1, 7, 9})</code>

<code>5</code>  
