---
title: "List.Accumulate | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Accumulate

  
## About  
Accumulates a result from the list. Starting from the initial value seed this function applies the **accumulator** function and returns the final result.  
  
```  
List.Accumulate(list as list, seed as any, accumulator as function)as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|seed|The initial value seed.|  
|accumulator|The value accumulator function.|  
  
## Example  
  
```  
// This accumulates the sum of the numbers in the list provided.  
List.Accumulate({1, 2, 3, 4, 5}, 0, (state, current) => state + current) equals 15  
```  
