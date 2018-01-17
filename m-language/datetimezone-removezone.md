---
title: "DateTimeZone.RemoveZone | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: aa2f84ae-dcb8-485c-981f-76d8377289fe
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# DateTimeZone.RemoveZone
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a datetime value with the zone information removed from the input datetimezone value.  
  
```  
DateTimeZone.RemoveZone(dateTimeZone as datetimezone) as nullable datetime  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTimeZone|The DateTimeZone to modify.|  
  
## Example  
  
```  
DateTimeZone.RemoveZone(#datetimezone(2010, 5, 4, 14, 5, 5, 8, 0)) equals #datetime(2010, 5, 4, 14, 5, 5)  
```  
