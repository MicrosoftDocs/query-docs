---
title: "DateTime.IsInCurrentSecond | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTime.IsInCurrentSecond
DateTime.IsInCurrentSecond(dateTime as any) as nullable logical  
  
## About  
Indicates whether the given datetime value occurs during the current second, as determined by the current date and time on the system.  
  
|Value|  
|---------|  
|dateTime: A datetime, or datetimezone value to be evaluated.|  
  
### Example 1  
Determine if the current system time is in the current second.  
  
```  
DateTime.IsInCurrentSecond(DateTime.FixedLocalNow())  
```  
  
```  
Equals: true  
```  
