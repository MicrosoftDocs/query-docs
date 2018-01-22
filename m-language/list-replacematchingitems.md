---
title: "List.ReplaceMatchingItems | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 0ab144d3-7c08-4b3a-9955-101311566763
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.ReplaceMatchingItems

  
## About  
Replaces occurrences of existing values in the list with new values using the provided equationCriteria. Old and new values are provided by the replacements parameters. An optional equation criteria value can be specified to control equality comparisons. For details of replacement operations and equation criteria, see Parameter Values.  
  
```  
List.ReplaceMatchingItems(list as list, replacements as any ,optional equationCriteria as any) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to modify.|  
|replacements|The replacements to make.|  
|optional equationCriteria|An optional equation criteria value to control equality testing.|  
  
## Examples  
  
```  
List.ReplaceMatchingItems ({1, 2, 3, 4, 5}, {{2, -2}}) equals { 1, -2, 3, 4, 5}  
```  
  
```  
List.ReplaceMatchingItems ({1, 2, 3, 4, 5}, {{2, -2}, {3, -3}}) equals { 1, -2, -3, 4, 5}  
```  
