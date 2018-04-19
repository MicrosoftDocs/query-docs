---
title: "Date.StartOfWeek | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.StartOfWeek

  
## About  
Returns a DateTime value representing the start of the week.  
  
```  
Date.StartOfWeek(dateTime as nullable datetime, optional firstDay as nullable number) as nullable datetime  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check against.|  
|optional firstDay|An optional argument to set the first day of the week.|  
  
### Enum Values  
  
-   Day.Sunday = 0;  
  
-   Day.Monday = 1;  
  
-   Day.Tuesday = 2;  
  
-   Day.Wednesday = 3;  
  
-   Day.Thursday = 4;  
  
-   Day.Friday = 5;  
  
-   Day.Saturday = 6;  
  
## Remarks  
  
-   The date and time portions are reset to their initial values for the week.  
  
-   The timezone information is persisted.  
  
## Example  
  
```  
dateTime = DateTimeZone.FromText("2011-02-24T12:30:00-08:00");   
Date.StartOfWeek(dateTime, Day.Monday) equals 2011-02-21T00:00:00-08:00  
```  
