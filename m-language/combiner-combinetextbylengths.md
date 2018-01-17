---
title: "Combiner.CombineTextByLengths | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 1fecaf7b-a933-4b0d-91a8-12327f166943
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Combiner.CombineTextByLengths
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a function that merges a list of text into a single text.  
  
```  
Combiner.CombineTextByLengths(lengths as list, optional template as nullable text) as function  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|lengths|The lengths to combine on.|  
|optional template|The Combiner template.|  
  
## <a name="__toc360789947"></a>Remarks  
  
-   Combiner.CombineTextByLengths  is similar to CombineTextByRanges, except that the lengths are used to determine the locations of the text.  
  
-   As in Splitter.SplitTextByLengths, each length must be non-negative.  
  
-   As in SplitTextByLengths, CombineTextByLengths works by delegating to CombineTextByRanges.  
  
