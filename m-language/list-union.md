---
title: "List.Union | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: bc144ab1-21b5-4335-b054-f2a8b18d3e71
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.Union

  
## About  
Returns a list from a list of lists and unions the items in the individual lists. The returned list contains all items in any input lists. Duplicate values are matched as part of the Union.  
  
```  
List.Union(list as list,optional equationCriteria as any) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List of lists to check.|  
|optional equationCriteria|An optional equation criteria value to control equality comparisons. For more information about equality comparisons, see Parameter Values.|  
  
## Examples  
  
```  
List.Union({ {1..5}, {2..6}, {3..7} }) equals {1..7}  
```  
  
```  
List.Union({ {1..5}, {4..8}, {7..11} }) equals {1..11}  
```  
  
```  
List.Union({ {1, 1, 1, 2}, {1, 1, 2, 2} }) equals {1, 1, 1, 2, 2}  
```  
