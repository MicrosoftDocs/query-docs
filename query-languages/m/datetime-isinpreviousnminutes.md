---
title: "DateTime.IsInPreviousNMinutes | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTime.IsInPreviousNMinutes
DateTime.IsInPreviousNMinutes(dateTime as any, minutes as number) as nullable logical  
  
## About  
Indicates whether the given datetime value occurs during the previous number of minutes, as determined by the current date and time on the system.  
  
|Value|  
|---------|  
|dateTime: A datetime, or datetimezone value to be evaluated.|  
|minutes: The number of minutes.|  
  
### Example 1  
Determine if the minute before the current system time is in the previous two minutes.  
  
```  
DateTime.IsInPreviousNMinutes(DateTime.LocalNow() - #duration(0,0,2,0), 2)  
```  
  
```  
Equals: true  
```  
