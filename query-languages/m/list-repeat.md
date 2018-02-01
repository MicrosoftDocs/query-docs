---
title: "List.Repeat | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 27540b78-1510-4926-b59f-e0548c9b99a6
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.Repeat

  
## About  
Returns a list that repeats the contents of an input list count times.  
  
```  
List.Repeat(list as list, count as number) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to repeat.|  
|count|The number of times to repeat.|  
  
## <a name="__goback"></a>Example  
  
```  
List.Repeat({1, 2, 3}, 3) equals {1, 2, 3, 1, 2, 3, 1, 2, 3}  
```  
