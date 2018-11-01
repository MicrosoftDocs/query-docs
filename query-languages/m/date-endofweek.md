---
title: "Date.EndOfWeek | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.EndOfWeek

  
## About  
Returns a date, datetime, or datetimezone value for the end of the week.  
  
## Syntax

<pre>
Date.StartOfWeek(dateTime as any, optional firstDayOfWeek as nullable number) as any   
</pre>  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The date, datetime, or datetimezone to check against.|  
|optional firstDayOfWeek|A number value as an enum value to set the last day of the week. The default value for firstDayOfWeek is Day.Sunday.|  
  
### Day Enum Values  
  
-   Day.Sunday = 0;  
  
-   Day.Monday = 1;  
  
-   Day.Tuesday = 2;  
  
-   Day.Wednesday = 3;  
  
-   Day.Thursday= 4;  
  
-   Day.Friday = 5;  
  
-   Day.Saturday= 6;  
  
## Remarks  
  
-   The date and time portions are reset to their initial values for the week.  
  
-   The timezone information is persisted.  
  
## <a name="__goback"></a>Example  
  
```powerquery-m  
let dateTime = DateTimeZone.FromText("2011-02-24T12:30:00-08:00") in  
Date.EndOfWeek(dateTime, Day.Sunday) equals 2011-02-26T23:59:59.9999999-08:00  
```  
