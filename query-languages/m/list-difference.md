---
title: "List.Difference | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: be9f7055-9a9c-4ae7-b8de-c207dc80f0df
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.Difference

  
## About  
Returns the items in list 1 that do not appear in list 2. Duplicate values are supported.  
  
```  
List.Difference(list1 as list, list2 as list,optional equationCriteria as any) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list1|The List to check with.|  
|list2|The List to check against.|  
|optional equationCriteria|An optional equation criteria value to control equality comparisons. For more information about equality comparisons, see Parameter Values.|  
  
## Examples  
  
```  
List.Difference({1..10}, {2..3,5..7}) equals {1,4,8,9,10}  
```  
  
```  
List.Difference({1}, {1,2,3}) equals {}  
```  
  
```  
List.Difference({1, 1, 1}, {1}) equals {1, 1}  
```  
