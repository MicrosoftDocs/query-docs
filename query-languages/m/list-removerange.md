---
title: "List.RemoveRange | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: b857c6b8-d94e-4283-8cd6-bf57bab68a81
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.RemoveRange

  
## About  
Returns a list that removes count items starting at offset.  The default count is 1.  
  
```  
List.RemoveRange(list as list, offset as number, optional count as nullable number) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to remove items from.|  
|offset|The index to start at.|  
|optional count|The number of items to remove.|  
  
## Examples  
  
```  
List.RemoveRange({"A", "B", "C", "D"}, 2) equals {"A", "B", "D"}  
```  
  
```  
List.RemoveRange({"A", "B", "C", "D"}, 1, 2) equals {"A", "D"}  
```  
