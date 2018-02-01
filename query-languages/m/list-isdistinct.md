---
title: "List.IsDistinct | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: a06f9a08-0cae-4344-b4d6-83f01eaeda99
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.IsDistinct

  
## About  
Returns whether a list is distinct.  
  
```  
List.IsDistinct(list as list, optional equationCriteria as any) as logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|optional equationCriteria|Equation criteria value used to control equality comparison. For more information about equationCriteria, see Parameter Values.|  
  
## Examples  
  
```  
List.IsDistinct({1, 2, 3, 2, 3}) equals false  
```  
  
```  
List.IsDistinct({"a","b","A"}, Comparer.FromCulture("en",false) equals true  
```  
  
```  
List.IsDistinct({"a","b","A"}, Comparer.FromCulture("en",true) equals false  
```  
