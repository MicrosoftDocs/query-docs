---
title: "Combiner.CombineTextByPositions | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 6d3a53e9-c5cc-4f6f-a224-c779312b9812
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Combiner.CombineTextByPositions
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a function that merges a list of text into a single text.  
  
```  
Combiner.CombineTextByPositions(positions as list, optional template as nullable text) as function  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|positions|The positions to combine at.|  
|optional template|The Combiner template.|  
  
## <a name="__toc360789944"></a>Remarks  
  
-   This function behaves similar to CombineTextByRanges, except that the positions are used to determine the locations of the text.  As in Splitter.SplitTextByRanges, each position must be non-negative and larger than the previous position.   As in SplitTextByPositions, CombineTextByPositions works by delegating to CombineTextByRanges.  
  
