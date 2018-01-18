---
title: "Date.StartOfDay | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: ebb58e60-4cc8-46fc-8cdf-b7e00026dd04
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Date.StartOfDay
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a DateTime value for the start of the day.  
  
```  
Date.StartOfDay(dateTime as nullable datetime) as nullable datetime  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check against.|  
  
## Remarks  
  
-   The date and time portions are reset to their initial values for the day.  
  
-   The timezone information is persisted.  
  
## <a name="__goback"></a>Example  
  
```  
dateTime = DateTimeZone.FromText("2011-02-21T12:30:00-08:00");   
Date.StartOfDay(dateTime) equals 2011-02-21T00:00:00-08:00  
```  
