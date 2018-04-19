---
title: "Combiner.CombineTextByPositions | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Combiner.CombineTextByPositions

  
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
  
