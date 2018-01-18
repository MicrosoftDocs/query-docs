---
title: "DateTimeZone.ZoneHours | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: dbbb37b5-dd69-42b3-a10b-538eb5829a27
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# DateTimeZone.ZoneHours
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a time zone hour value from a DateTime value.  
  
```  
DateTimeZone.ZoneHours(dateTime as datetimezone) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTimeZone to check against.|  
  
## Example  
  
```  
DateTimeZone.ZoneHours(DateTime.FromText("12:56:20-08:00")) equals -8  
```  
