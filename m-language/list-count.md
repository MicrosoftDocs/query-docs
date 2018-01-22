---
title: "List.Count | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 4071c145-7b8c-4c30-b211-ebdb05ac17b1
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.Count

  
## About  
Returns the number of items in a list.  
  
```  
List.Count(list as list) as number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
  
## Examples  
  
```  
List.Count({1,2,3}) equals 3  
```  
  
```  
List.Count({}) equals 0  
```  
