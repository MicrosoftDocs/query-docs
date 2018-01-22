---
title: "List.Accumulate | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 795da002-244b-47be-b6e6-c29d228d03f8
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
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
