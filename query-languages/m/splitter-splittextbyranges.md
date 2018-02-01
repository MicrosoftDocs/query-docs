---
title: "Splitter.SplitTextByRanges | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 30588a7c-d53f-4c8b-803e-86f5de981c8e
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Splitter.SplitTextByRanges

  
## About  
Returns a function that splits text according to the specified ranges.  
  
```  
Splitter.SplitTextByRanges(ranges as list) as function  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|ranges|The ranges to split on.|  
  
## <a name="__toc360789925"></a>Remarks  
  
-   Each item in ranges should specify a tuple of offset and length (where offset zero refers to the first character).  The subset of characters of the line denoted by each tuple is returned as a separate item.  If the offset or length is less than zero, an error is thrown.   Otherwise, if the tuple is out of range of the line, spaces are used to fill out the value.  Therefore, the list returned will have the same cardinality as ranges, and each item will be of the length specified in the corresponding tuple.  There is no checking for overlap of tuple ranges.  
  
