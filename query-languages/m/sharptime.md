---
title: "#time | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# #time
<code>#time(<b>hour</b> as number, <b>minute</b> as number, <b>second</b> as number) as time</code>

## About
Creates a time value from whole numbers hour <code>hour</code>, minute <code>minute</code>, and (fractional) second <code>second</code>. Raises an error if these are not true: <ul> <li> 0 ≤ hour ≤ 24 </li> <li> 0 ≤ minute ≤ 59 </li> <li> 0 ≤ second ≤ 59 </li> <li> if hour is 24, then minute and second must be 0 </li> </ul>