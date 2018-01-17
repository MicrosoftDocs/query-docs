---
title: "Uri.Combine | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 8c928dd2-057f-4f6d-98fa-d1c24cb9c675
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Uri.Combine
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a Uri based on the combination of the base and relative parts.  
  
```  
Uri.Combine(baseUri as text, relativeUri as text) as text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|baseUri|The left part of the URI to combine.|  
|relativeUri|The right part of the URI to combine.|  
  
