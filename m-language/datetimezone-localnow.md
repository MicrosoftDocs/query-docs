---
title: "DateTimeZone.LocalNow | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 75d1b8d1-9ddf-492f-a599-33c967a303f6
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# DateTimeZone.LocalNow
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a DateTime value set to the current system date and time.  
  
```  
DateTimeZone.LocalNow() as datetimezone  
```  
  
## Remarks  
  
-   The return value contains timezone information representing the local timezone.  
  
## Example  
  
```  
DateTimeZone.LocalNow() equals 2011-02-20T22:19:38-08:00  
```  
