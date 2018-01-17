---
title: "#datetime | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 2c7f080d-26ac-4c3e-a096-2ecfd60d6898
caps.latest.revision: 2
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# #datetime
<code>#datetime(<b>year</b> as number, <b>month</b> as number, <b>day</b> as number, <b>hour</b> as number, <b>minute</b> as number, <b>second</b> as number) as any</code>

## About
Creates a datetime value from whole numbers year <code>year</code>, month <code>month</code>, day <code>day</code>, hour <code>hour</code>, minute <code>minute</code>, and (fractional) second <code>second</code>. Raises an error if these are not true: <ul> <li> 1 ≤ year ≤ 9999 </li> <li> 1 ≤ month ≤ 12 </li> <li> 1 ≤ day ≤ 31 </li> <li> 0 ≤ hour ≤ 23 </li> <li> 0 ≤ minute ≤ 59 </li> <li> 0 ≤ second ≤ 59 </li> </ul>

  
