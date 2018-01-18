---
title: "DateTime.AddZone | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 9db50fd4-3208-4791-98d0-6cf13f2f710c
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# DateTime.AddZone
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Adds the timezonehours as an offset to the input datetime value and returns a new datetimezone value.  
  
```  
DateTime.AddZone(dateTime as nullable datetime, timezoneHours as number, optional timezoneMinutes as nullable number) as nullable datetimezone  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|A DateTime to modify.|  
|timezoneHours|The hours to add.|  
|optional timezoneMinutes|The minuts to add.|  
  
## Example  
  
```  
DateTime.AddZone(#datetime(2010, 5, 4, 6, 5, 5), 8) equals #datetimezone(2010, 5, 4, 6, 5, 5, 8, 0)  
```  
