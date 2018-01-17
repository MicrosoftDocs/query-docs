---
title: "DateTime.LocalNow | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 567827c0-d7d8-441b-9369-9993aabb64fd
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# DateTime.LocalNow
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a datetime value set to the current date and time on the system.  
  
```  
DateTime.LocalNow() as datetime  
```  
  
## Remarks  
  
-   The returned value does not contain timezone information.  
  
## Example  
  
```  
DateTime.LocalNow()equals 2013-03-08T14:22:42  
```  
