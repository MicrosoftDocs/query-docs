---
title: "List.Sum | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: f4e7ed91-e432-49e4-a976-0733279f4ee0
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.Sum

  
## About  
Returns the sum from a list.  
  
```  
List.Sum(list as list) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
  
## <a name="__toc360789389"></a>Remarks  
  
-   If the list is empty, an Expression.Error is thrown.  
  
## Examples  
  
```  
List.Sum({1, 2, 3}) equals 6  
```  
  
```  
List.Sum({#duration(0, 0, 0, 15), #duration(0, 0, 0, 30)}) equals #duration(0, 0, 0, 45)  
```  
  
```  
List.Sum({}) equals error  
```  
