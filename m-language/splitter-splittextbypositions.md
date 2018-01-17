---
title: "Splitter.SplitTextByPositions | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: ed28c1e2-ac00-4136-92f6-09824f7b70db
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Splitter.SplitTextByPositions
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a function that splits text according to the specified positions.  
  
```  
Splitter.SplitTextByPositions(positions as list) as function  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|positions|The positions to split on.|  
  
## <a name="__toc360789928"></a>Remarks  
  
-   Each item in positions should be a non-negative number indicating the position at which to break the text, and each item must be greater than or equal to the previous.  SplitTextByPositions works by computing a set of ranges by using the difference between subsequent positions as lengths (with the last position of effectively infinite length) and delegating to SplitTextByRanges.  The list returned will have the same cardinality as that of the positions.  
  
