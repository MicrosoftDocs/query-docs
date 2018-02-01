---
title: "List.Min | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: b4eac522-4ef3-4077-b5e4-94bc96358e40
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.Min

  
## About  
Returns the minimum item in a list, or the optional default value if the list is empty.  
  
```  
List.Min(list as list, optional default as any, optional comparisonCriteria as any, optional includeNulls as nullable logical) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|optional default|The default value to return.|  
|optional comparisonCriteria|Specifies how to compare values in the list. If this argument is null, the default comparer is used.|  
|optional includeNulls|The Logical value whether or not to include null values in the return list.|  
  
## Example  
  
```  
List.Min({1, 4, 7, 3, -2, 5}) equals -2  
```  
