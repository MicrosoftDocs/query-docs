---
title: "Combiner.CombineTextByRanges | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 3fe14146-f75b-44ce-ba1b-a2d230de68fb
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Combiner.CombineTextByRanges

  
## About  
Returns a function that merges a list of text into a single text.  
  
```  
Combiner.CombineTextByRanges(ranges as list, optional template as nullable text) as function  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|ranges|The ranges to combine at.|  
|optional template|The Combiner template.|  
  
## <a name="__toc360789941"></a>Remarks  
  
-   Each position identifies a tuple of position and length for a line where the text value should be placed.  If the length of a text value for a given tuple exceeds the length specified by that tuple, then the value is truncated to fit.  There is no checking for overlap of tuple ranges.  If there are fewer text items than ranges, empty text will be used.  If there are fewer ranges than text items, then they will not be emitted.  
  
-   The template specifies the default characters over which the individual items are placed.  If not specified empty text is used.  
  
