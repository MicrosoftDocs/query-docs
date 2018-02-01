---
title: "Splitter.SplitTextByLengths | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
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
manager: "kfile"
---
# Splitter.SplitTextByLengths

  
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
  
