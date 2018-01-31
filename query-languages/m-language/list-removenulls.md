---
title: "List.RemoveNulls | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: fc0d6b62-d2a4-43c5-88df-04317683f821
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.RemoveNulls

  
## About  
Removes null values from a list.  
  
```  
List.RemoveNulls(list as list) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to modify.|  
  
## Example  
  
```  
List.RemoveNulls({1, null, 2}) equals {1, 2}  
```  
