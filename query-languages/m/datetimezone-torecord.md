---
title: "DateTimeZone.ToRecord | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTimeZone.ToRecord

  
## About  
Returns a record containing parts of a DateTime value.  
  
```  
DateTimeZone.ToRecord(dateTimeZone as datetimezone) as record  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTimeZone|The DateTimeZone to convert.|  
  
## <a name="__toc360789084"></a>Remarks  
  
-   If a portion of the DateTime value is not specified with date, time or timezone, the corresponding part in the output record is not present.  
  
## Example  
  
```  
DateTime.ToRecord(DateTime.FromText("2011-02-02T11:56:02-08:00")) equals  
Year = 2011, Month = 2, Day = 2,  
Hour = 11, Minute = 56, Second = 2,  
Hours = -8, Minutes = 0  
]  
DateTime.ToParts(DateTime.From("11:56:02-05"))  
[  
Time = [Hour = 11, Minute = 56, Second = 2],  
Timezone = [Hours = -5]  
]  
```  
