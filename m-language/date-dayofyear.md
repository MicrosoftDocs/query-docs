---
title: "Date.DayOfYear | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 4548f4fd-2d47-4dc0-a700-422367b6259e
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Date.DayOfYear
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a number that represents the day of the year from a DateTime value.  
  
```  
Date.DayOfYear(dateTime as datetime) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check against.|  
  
## Examples  
  
```  
Date.DayOfYear(DateTime.FromText("2011-03-01")) equals 60  
```  
  
```  
Date.DayOfYear(DateTime.FromText("2012-03-01")) equals 61  
```  
