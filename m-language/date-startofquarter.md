---
title: "Date.StartOfQuarter | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 80488daf-07d9-4cb6-99c9-e952d65cc3a3
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Date.StartOfQuarter
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a Date/DateTime/DateTimeZone value representing the start of the quarter. The date and time portions are reset to their initial values for the quarter. The timezone information is persisted.  
  
```  
Date.StartOfQuarter(dateTime)  
```  
  
## <a name="__goback"></a>Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime whose date and time portions are to be reset to their initial values for the quarter.|  
  
