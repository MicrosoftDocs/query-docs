---
title: "List.ContainsAll | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 80a7ab13-ca7d-43b5-b6fe-0d8d66c27082
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.ContainsAll

  
## About  
Returns true if all items in values are found in a list.  
  
```  
List.ContainsAll(list as list, values as list,optional equationCriteria as any) as logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|values|The list of values to check for.|  
|optional equationCriteria|An optional equation criteria value to control equality comparisons. For more information about equality comparisons, see Parameter Values.|  
  
## Examples  
  
```  
List.ContainsAll({1, 2, 3}, {2, 3}) equals true  
```  
  
```  
List.ContainsAll({1, 2, 3}, {2, 4}) equals false  
```  
