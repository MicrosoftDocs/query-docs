---
title: "Date.AddMonths | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: ca90ae1f-943d-44cc-82b7-a5abe72c6cfe
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Date.AddMonths
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a DateTime value with the month portion incremented by n months.  
  
```  
Date.AddMonths(dateTime as datetime, numberOfMonths as number) as nullable datetime  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to add months to.|  
|numberOfMonths|The number of months to add.|  
  
## Remarks  
  
-   It also handles incrementing the year portion of the value as appropriate.  
  
## Examples  
  
```  
Date.AddMonths(DateTime.FromText("2011-02-19"), 5) equals 2011-07-19  
```  
  
```  
Date.AddMonths(DateTime.FromText("2010-12-01"), 2) equals 2011-02-01  
```  
