---
title: "List.Max | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: b86fe33c-d704-45fc-8e95-b7660f371d2c
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.Max

  
## About  
Returns the maximum item in a list, or the optional default value if the list is empty.  
  
```  
List.Max(list as list, optional default as any, optional comparisonCriteria as any, optional includeNulls as nullable logical) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|optional default|The default value to return.|  
|optional comparisonCriteria|An optional comparison criteria value to control equality testing. If this argument is null, the default comparer is used.|  
|optional includeNulls|The Logical value whether or not to include null values in the return list.|  
  
## Example  
  
```  
List.Max({1, 4, 7, 3, -2, 5}, 1) equals 7  
```  
