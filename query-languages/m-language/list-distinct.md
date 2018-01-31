---
title: "List.Distinct | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 0b557e3e-ea59-4a8f-a443-54f85686fc1a
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.Distinct

  
## About  
Filters a list down by removing duplicates. An optional equation criteria value can be specified to control equality comparison.  The first value from each equality group is chosen.  
  
For more information about equationCriteria, see Parameter Values.  
  
```  
List.Distinct(list as list, optional equationCriteria as any, criteria as any) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|optional equationCriteria|An equality group equation.|  
|criteria|Filter criteria.|  
  
## Examples  
  
```  
List.Distinct({1, 2, 3, 2, 3}) equals {1, 2, 3}  
```  
  
```  
List.Distinct({"a","b","A"}, each _) equals {"a", "b", "A"}  
```  
  
```  
List.Distinct({"a","b","A"}, Comparer.FromCulture("en",true)) equals {"a", "b"}  
```  
  
```  
List.Distint({[a="a",b=2],[a="b",b=3],[a="A",b=4]},   
{ each [a] , Comparer.FromCulture("en", true) } )   
equals { [ a = "a", b = 2 ],   
//   [a = "b",  b = 3 ] }  
```  
