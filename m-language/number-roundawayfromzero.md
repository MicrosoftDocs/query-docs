---
title: "Number.RoundAwayFromZero | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 25a06bf2-acdd-4a5b-acb5-b7e08223f30b
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Number.RoundAwayFromZero
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns Number.RoundUp(value) when value &gt;= 0 and Number.RoundDown(value) when value &lt; 0.  
  
```  
Number.RoundAwayFromZero(value as nullable number) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|Value to round away from zero.|  
  
## Examples  
  
```  
Number.RoundAwayFromZero(-1.2) equals -2  
```  
  
```  
Number.RoundAwayFromZero(1.2) equals 2  
```  
