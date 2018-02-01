---
title: "List.Alternate | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: db6d13c4-b206-4a30-b9e7-730776706210
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.Alternate

  
## About  
Returns a list with the items alternated from the original list based on a count, optional repeatInterval, and an optional offset.  
  
```  
List.Alternate(list as list, count as number,  optional repeatInterval as nullable number,  optional offset as nullable number) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to modify.|  
|count|Alternate count.|  
|optional repeatInterval|Alternate repeat interval.|  
|optional offset|Alternation offset.|  
  
## <a name="__toc360789215"></a>Remarks  
If the repeatInterval and offset are not provided then List.Alternate is equivalent to List.Skip.  
  
## Example  
  
```  
List.Alternate({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 2, 2, 0) equals {3, 4, 7, 8}  
```  
