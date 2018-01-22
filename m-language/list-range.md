---
title: "List.Range | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 7401f23d-0515-4b01-9866-dd08d2602bee
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.Range

  
## About  
Returns a count items starting at an offset.  
  
```  
List.Range(list as list, offset as number, optional count as number) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|offset|The index to start at.|  
|optional count|Count of items to return.|  
  
## <a name="__goback"></a>Example  
  
```  
List.Range({1..10}, 3, 5)  equals  {4, 5, 6, 7, 8}  
```  
