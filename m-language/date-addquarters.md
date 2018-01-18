---
title: "Date.AddQuarters | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 25a4a535-42d2-4c7f-97d4-20e413c24776
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Date.AddQuarters
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a Date/DateTime/DateTimeZone value incremented by the number of quarters provided. Each quarter is defined as a duration of three months. It also handles incrementing the year potion of the value as appropriate.  
  
```  
Date.AddQuarters(dateTime, quarters as number)  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to add quarters to.|  
|quarters|The number of quarters to add.|  
  
## Examples  
  
```  
Date.AddQuarters(DateTime.FromText("2011-02-19"), 1) equals 2011-05-19  
```  
  
```  
Date.AddQuarters(DateTime.FromText("2011-11-30"), 1) equals 2012-02-29  
```  
