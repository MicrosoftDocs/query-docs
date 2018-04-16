---
title: "DateTime.IsInNextMinute | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTime.IsInNextMinute
DateTime.IsInNextMinute(dateTime as any) as nullable logical  
  
## About  
Indicates whether the given datetime value occurs during the next minute, as determined by the current date and time on the system.  
  
|Value|  
|---------|  
|dateTime: A datetime, or datetimezone value to be evaluated.|  
  
### Example 1  
Determine if the minute after the current system time is in the next minute.  
  
```  
DateTime.IsInNextMinute(DateTime.LocalNow() + #duration(0,0,1,0))  
```  
  
```  
Equals: true  
```  
