---
title: "List.Positions | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 4b02fbc7-c3d6-43b2-b14a-911a1980af31
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
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
