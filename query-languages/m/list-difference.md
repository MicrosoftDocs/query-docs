---
title: "List.Difference | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
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
