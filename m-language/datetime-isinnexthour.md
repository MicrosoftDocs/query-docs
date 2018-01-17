---
title: "DateTime.IsInNextHour | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 305d04b2-68f3-4e3d-a6cf-891c6ec04d9f
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# DateTime.IsInNextHour
DateTime.IsInNextHour(dateTime as any) as nullable logical  
  
## About  
Indicates whether the given datetime value occurs during the next hour, as determined by the current date and time on the system.  
  
|Value|  
|---------|  
|dateTime: A datetime, or datetimezone value to be evaluated.|  
  
### Example 1  
Determine if the hour after the current system time is in the next hour.  
  
```  
DateTime.IsInNextHour(DateTime.LocalNow() + #duration(0,1,0,0))  
```  
  
```  
Equals: true  
```  
