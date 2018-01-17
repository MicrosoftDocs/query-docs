---
title: "DateTimeZone.FromFileTime | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 565684a8-f1a3-442c-83e3-80bc06388d3c
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# DateTimeZone.FromFileTime
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a DateTimeZone from a number value.  
  
```  
DateTimeZone.FromFileTime(fileTime as nullable number) as nullable datetimezone  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|fileTime|The fileTime is a Windows file time value that represents the number of 100-nanoseconds intervals that have elapsed since 12:00 midnight, January 1, 1601 A.D. (C.E.) Coordinated Universal Time (UTC).|  
  
## <a name="__goback"></a>Example  
  
```  
DateTimeZone.FromFileTime(12987640252984224) equals #datetimezone(2012, 7, 24, 14, 50, 52.9842245, -7, 0)  
```  
