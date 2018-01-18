---
title: "Date.IsLeapYear | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 00f167b6-38bf-4c9e-a74b-562ff311b437
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Date.IsLeapYear
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a logical value indicating whether the year portion of a DateTime value is a leap year.  
  
```  
Date.IsLeapYear(dateTime as nullable datetime) as nullable logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check.|  
  
## Examples  
`Date.IsLeapYear(DateTime.FromText("2011-01-01")) equals false`  
  
```  
Date.IsLeapYear(DateTime.FromText("2012-01-01")) equals true  
```  
