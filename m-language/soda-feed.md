---
title: "Soda.Feed | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: fa2509e0-f237-4fe9-a6e7-eec379f329c0
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Soda.Feed
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns the resulting table of a CSV file that can be accessed using the SODA 2.0 API.  The URL must point to a valid SODA-compliant source that ends in a .csv extension.  
  
```  
Soda.Feed(url as text) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|url|The URL pointing to the SODA compliant .csv source|  
  
