---
title: "#date | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# #date

## Syntax

<pre>
#date(<b>year</b> as number, <b>month</b> as number, <b>day</b> as number) as date
</pre>


## About
Creates a date value from year `year`, month `month`, and day `day`. Raises an error if these are not true: <ul> <li> 1 ≤ year ≤ 9999 </li> <li> 1 ≤ month ≤ 12 </li> <li> 1 ≤ day ≤ 31 </li> </ul>
