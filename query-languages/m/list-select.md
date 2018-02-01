---
title: "List.Select | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: be46f76c-9288-41dc-aba6-394a3a1a8356
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.Select

  
## About  
Selects the items that match a condition.  
  
```  
List.Select(list as list, condition as function) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|condition|The condition to match against.|  
  
## <a name="__goback"></a>Example  
  
```  
List.Select({1, 3, 5}, each _ > 2) equals {3 ,5}  
```  
