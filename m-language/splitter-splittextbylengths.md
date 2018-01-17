---
title: "Splitter.SplitTextByLengths | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: a39d5968-55cd-4fee-a061-f222dd1622da
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Splitter.SplitTextByLengths
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a function that splits text according to the specified lengths.  
  
```  
Splitter.SplitTextByLengths(lengths as list) as function  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|lengths|The lengths to split on.|  
  
## <a name="__toc360789931"></a>Remarks  
  
-   Each item in lengths should be a non-negative number indicating the number of characters to use for each item.  SplitTextByLengths works by computing a set of ranges by adding each subsequent length to compute the next position, and delegating to SplitTextByRanges.  The list returned will have the same cardinality as that of the positions.  
  
