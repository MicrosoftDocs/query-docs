---
title: "List.IsEmpty | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: ceaa4f2d-0de4-4983-a4ae-c0c9ffd7c6db
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.IsEmpty

  
## About  
Returns whether a list is empty.  
  
```  
List.IsEmpty(list as list) as logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
  
## Examples  
  
```  
List.IsEmpty({}) equals true  
```  
  
```  
List.IsEmpty({1, 2, 3}) equals false  
```  
