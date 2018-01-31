---
title: "List.Single | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: e2bc83c7-ecab-4332-b144-c6a8334a8230
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.Single

  
## About  
Returns the single item of the list or throws an Expression.Error if the list has more than one item.  
  
```  
List.Single(list as list) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
  
## Examples  
  
```  
List.Single({1}) equals 1  
```  
  
```  
List.Single({1, 2, 3}) equals error  
```  
