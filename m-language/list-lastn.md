---
title: "List.LastN | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 42b6fa16-ef37-408b-bd10-1d63d9d0b658
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.LastN

  
## About  
Returns the last set of items in a list by specifying how many items to return or a qualifying condition.  
  
```  
List.LastN(list as list, optional countOrCondition as any) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|optional countOrCondition|Number items to return or a qualifying condition.|  
  
## <a name="__toc360789241"></a>Remarks  
  
-   If a number is specified, up to that many items are returned.  
  
-   If a condition is specified, all items are returned that initially meet the condition.  
  
-   Once an item fails the condition, no further items are considered  
  
## Example  
  
```  
List.LastN({3, 4, 5, -1, 7, 8, 2},1) equals  { 2 }  
```  
