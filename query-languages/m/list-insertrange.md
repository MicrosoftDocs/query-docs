---
title: "List.InsertRange | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 887c2017-9787-4603-b647-457b93257c5d
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.InsertRange

  
## About  
Inserts items from values at the given index in the input list.  
  
```  
List.InsertRange(list as list, offset as number, values as list) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to modify.|  
|offset|The index to insert at.|  
|values|The values to insert.|  
  
## <a name="__goback"></a>Example  
  
```  
List.InsertRange({"A", "B", "D"}, 2, {"C"}) equals {"A", "B", "C", "D"}  
```  
