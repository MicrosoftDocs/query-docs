---
title: "Date.AddWeeks | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: d271c85b-18bc-43d1-998a-9272d1c29a0d
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Date.AddWeeks
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a Date/DateTime/DateTimeZone value incremented by the number of weeks provided. Each week is defined as a duration of seven days. It also handles incrementing the month and year potions of the value as appropriate.  
  
```  
Date.AddWeeks(dateTime, weeks as number)  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to add weeks to.|  
|weeks|The number of weeks to add.|  
  
## Examples  
  
```  
Date.AddWeeks(DateTime.FromText("2011-02-19"), 1) equals 2011-02-26  
```  
  
```  
Date.AddWeeks(DateTime.FromText("2011-02-19"), -2) equals 2011-02-05  
```  
  
```  
Date.AddWeeks(DateTime.FromText("2011-12-31"), 1) equals 2012-01-07  
```  
