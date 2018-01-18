---
title: "Time.EndOfHour | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 1c75b7d9-a238-4bb9-bd98-f5b7edac6d3d
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Time.EndOfHour
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a DateTime value from the end of the hour.  
  
```  
Time.EndOfHour(dateTime as datetime) as nullable datetime  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check against.|  
  
## Remarks  
  
-   The time portion is reset to its terminating values for the hour.  
  
-   The timezone information is persisted.  
  
## Example  
  
```  
dateTime = DateTimeZone.FromText("2011-02-21T12:30:00-08:00");   
Time.EndOfHour(dateTime) equals 2011-02-21T12:59:59-08:00  
```  
