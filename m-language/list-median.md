---
title: "List.Median | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 0970a43a-9693-4552-b0cf-7d1b36f6f5fb
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# List.Median
<code>List.Median(**list** as list, optional **comparisonCriteria** as any) as any</code>

## About
Returns the median item of the list <code>list</code>. This function returns <code>null</code> if the list contains no non-<code>null</code> values. If there is an even number of items, the function chooses the smaller of the two median items unless the list is comprised entirely of datetimes, durations, numbers or times, in which case it returns the average of the two items.

## Example 1
Find the median of the list <code>{5, 3, 1, 7, 9}</code>.

<code>List.Median({5, 3, 1, 7, 9})</code>

<code>5</code>  
