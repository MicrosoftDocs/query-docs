---
title: "Number.RoundDown | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: cf4bd4c6-6f8d-4ee7-ac59-b945ccbe175f
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Number.RoundDown
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns the largest integer less than or equal to a number value.  
  
```  
Number.RoundDown(value as nullable number) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|Value to round down.|  
  
## Examples  
  
```  
Number.RoundDown(-1.2) equals -2  
```  
  
```  
Number.RoundDown(1.2) equals 1  
```  
