---
title: "List.RemoveItems | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 3312e6aa-acd7-4b1a-99e9-a16429078ca1
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.RemoveItems

  
## About  
Removes items from list1 that are present in list2, and returns a new list.  
  
```  
List.RemoveItems(list1 as list, list2 as list) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list1|The List to modify.|  
|list2|The list of items to remove.|  
  
## Example  
  
```  
List.RemoveItems({1, 2, 3, 3}, {3}) equals { 1, 2}  
```  
