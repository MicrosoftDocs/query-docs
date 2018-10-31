---
title: "#datetimezone | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# #datetimezone

## Syntax

<pre>
#datetimezone(<b>year</b> as number, <b>month</b> as number, <b>day</b> as number, <b>hour</b> as number, <b>minute</b> as number, <b>second</b> as number, <b>offsetHours</b> as number, <b>offsetMinutes</b> as number) as any
</pre>

## About
Creates a datetimezone value from whole numbers year `year`, month `month`, day `day`, hour `hour`, minute `minute`, (fractional) second `second`, (fractional) offset-hours `offsetHours`, and offset-minutes `offsetMinutes`. Raises an error if these are not true: <ul> <li> 1 ≤ year ≤ 9999 </li> <li> 1 ≤ month ≤ 12 </li> <li> 1 ≤ day ≤ 31 </li> <li> 0 ≤ hour ≤ 23 </li> <li> 0 ≤ minute ≤ 59 </li> <li> 0 ≤ second ≤ 59 </li> <li> -14 ≤ offset-hours + offset-minutes / 60 ≤ 14 </li> </ul>

 
