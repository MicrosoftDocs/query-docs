---
title: "DateTime.Date | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 903181a7-eee6-4ea5-8a9a-87445cc494fe
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# DateTime.Date
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a date part from a DateTime value  
  
```  
DateTime.Date(dateTime as datetime) as nullable datetime  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to parse.|  
  
## Example  
  
```  
DateTime.Date(#datetime(2010, 5, 4, 6, 5, 4)) equals #date(2010, 5, 4)  
```  
