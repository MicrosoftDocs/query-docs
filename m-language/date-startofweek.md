---
title: "Date.StartOfWeek | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: b81b7d9d-972a-4f7a-badc-51a5532a8e82
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Date.StartOfWeek
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
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
