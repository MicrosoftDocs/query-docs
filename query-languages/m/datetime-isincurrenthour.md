---
title: "DateTime.IsInCurrentHour | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: f27f5ada-eb34-405e-a65b-b52246837b37
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# DateTime.IsInCurrentHour
DateTime.IsInCurrentHour(dateTime as any) as nullable logical  
  
## About  
Indicates whether the given datetime value occurs during the current hour, as determined by the current date and time on the system.  
  
|Value|  
|---------|  
|dateTime: A datetime, or datetimezone value to be evaluated.|  
  
### Example 1  
Determine if the current system time is in the current hour.  
  
```  
DateTime.IsInCurrentHour(DateTime.LocalNow())  
```  
  
```  
Equals: true  
```  
