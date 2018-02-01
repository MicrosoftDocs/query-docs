---
title: "List.Transform | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 15274b80-cb2d-4e4f-b6a3-7869d3bfe7d9
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.Transform

  
## About  
Performs the function on each item in the list and returns the new list.  
  
```  
List.Transform(list as list, transform as function)  as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to modify.|  
|transform|The transform to apply.|  
  
## <a name="__goback"></a>Example  
  
```  
List.Transform({1, 2}, each _ + 1) equals { 2, 3 }  
```  
