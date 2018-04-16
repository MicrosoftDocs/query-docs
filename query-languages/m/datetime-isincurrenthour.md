---
title: "DateTime.IsInCurrentHour | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
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
