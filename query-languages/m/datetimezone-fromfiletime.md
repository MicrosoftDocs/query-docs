---
title: "DateTimeZone.FromFileTime | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTimeZone.FromFileTime

  
## About  
Returns a DateTimeZone from a number value.  
  
```  
DateTimeZone.FromFileTime(fileTime as nullable number) as nullable datetimezone  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|fileTime|The fileTime is a Windows file time value that represents the number of 100-nanoseconds intervals that have elapsed since 12:00 midnight, January 1, 1601 A.D. (C.E.) Coordinated Universal Time (UTC).|  
  
## <a name="__goback"></a>Example  
  
```  
DateTimeZone.FromFileTime(12987640252984224) equals #datetimezone(2012, 7, 24, 14, 50, 52.9842245, -7, 0)  
```  
