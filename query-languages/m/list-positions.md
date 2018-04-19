---
title: "List.Positions | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Positions

  
## About  
Returns a list of positions for an input list.  
  
```  
List.Positions(list as list) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
  
## <a name="__toc360789251"></a>Remarks  
  
-   When using `List.Transform` to modify a list, the list of positions can be used to give the transform access to the positions.  
  
## <a name="__goback"></a>Example  
  
```  
List.Positions({4, 5, 6}) equals {0, 1, 2}  
```  
