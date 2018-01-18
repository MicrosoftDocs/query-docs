---
title: "DateTimeZone.ToLocal | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 2d835f91-d6e3-4498-89eb-c2c29c766d0e
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# DateTimeZone.ToLocal
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a DateTime value from the local time zone.  
  
```  
DateTimeZone.ToLocal(dateTime as datetimezone) as nullable datetimezone  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTimeZone to convert.|  
  
## Example  
  
```  
//assuming local as PST   
dateTime  = DateTimeZone.FromText("2011-02-20T22:19:27+03:00")  
localTime=DateTimeZone.ToLocal(dateTime) equals 2011-02-20T11:19:27-08:00  
```  
