---
title: "List.ContainsAny | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: ab1f5410-2c84-4e8b-afed-67fab729ca5e
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.ContainsAny

  
## About  
Returns true if any item in values is found in a list.  
  
```  
List.ContainsAny(list as list, values as list,optional equationCriteria as any) as logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|values|The list of values to check for.|  
|optional equationCriteria|An optional equation criteria value to control equality comparisons. For more information about equality comparisons, see Parameter Values.|  
  
## Examples  
  
```  
List.ContainsAny({1, 2, 3}, {2, 4}) equals true  
```  
  
```  
List.ContainsAny({1, 2, 3}, {4, 5}) equals false  
```  
