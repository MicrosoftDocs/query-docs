---
title: "DateTimeZone.SwitchZone | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTimeZone.SwitchZone

  
## About  
Changes the timezone information for the input DateTimeZone.  
  
## Syntax

<pre>
DateTimeZone(dateTimeZone as datetimezone, timezoneHours as number,  optional timezoneMinutes as nullablenumber ) as nullable datetimezone  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTimeZone|The DateTimeZone to modify.|  
|timezoneHours|The house to add.|  
|optional timezoneMinutes|The minuts to add.|  
  
## <a name="__toc360789106"></a>Remarks  
  
-   If the input value does not have a timezone component, DateTimeZone.SwitchZone throws Expression.Error.  
  
## Examples  
  
```powerquery-m
DateTimeZone.SwitchZone(#datetimezone(2010, 5, 4, 6, 5, 5, 0, 0), 8) equals #datetimezone(2010, 5, 4, 14, 5, 5, 8, 0)  
```  
  
```powerquery-m
DateTimeZone.SwitchZone(#datetimezone(2010, 12, 31, 11, 56, 02, 7, 30), 0, -30) equals #datetimezone(2010, 12, 31, 3, 56, 2, 0, -30)  
```  
