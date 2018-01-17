---
title: "DateTimeZone.ToRecord | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: dafd1b0a-58ee-48fe-ad26-0f1597cad8ca
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# DateTimeZone.ToRecord
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
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
