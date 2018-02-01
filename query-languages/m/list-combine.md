---
title: "List.Combine | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 9885c69b-8899-4d9a-9149-9e3de3610d1c
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.Combine

  
## About  
Merges a list of lists into single list.  
  
```  
List.Combine(list as list) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List of lists to merge.|  
  
## Example  
  
```  
List.Combine({ {1, 2, 3, 4}, {5, 6, 7}, {8, 9} }) equals {1, 2, 3, 4, 5, 6, 7, 8, 9}  
```  
