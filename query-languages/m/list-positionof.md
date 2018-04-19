---
title: "List.PositionOf | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.PositionOf

  
## About  
Finds the first occurrence of a value in a list and returns its position.  
  
```  
List.PositionOf(list as list, value as any, optional occurrence as nullable number,optional equationCriteria as any) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|value|The value to check for.|  
|optional occurrence|An enum that controls the scope of operation.|  
|optional equationCriteria|An optional equation criteria value to control equality comparisons. For more information about equality comparisons, see Parameter Values.|  
  
## Occurrence settings  
  
|**Setting**|**Description**|  
|---------------|-------------------|  
|Occurrence.First and Occurrence.Last|Returns a single position.|  
|Occurrence.All|Returns a list of positions with all occurrences.|  
  
## <a name="__toc360789324"></a>Remarks  
  
-   If the value is not found in the list, -1 is returned  
  
## Examples  
  
```  
List.PositionOf({"A", "B", "C", "D"}, "C") equals 2  
```  
  
```  
List.PositionOf({"A", "B", "C", "B", "A"}, "A", Occurrence.First)  equals 0  
```  
  
```  
List.PositionOf({"A", "B", "C", "B", "A"}, "A", Occurrence.Last) equals 4  
```  
  
```  
List.PositionOf({"A", "B", "C", "B", "A"}, "A", Occurrence.All) equals {0, 4}  
```  
