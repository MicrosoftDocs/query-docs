---
title: "List.Mode | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 99d4a818-59d4-48ce-90d2-a4e72db67997
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.Mode

  
## About  
Returns an item that appears most commonly in a list.  
  
```  
List.Mode(list as list, optional equationCriteria as any)as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|optional equationCriteria|Controls the sort order. For more information about equality comparisons, see Parameter Values.|  
  
## <a name="__toc360789380"></a>Remarks  
  
-   If more than 1 item appears with the same maximum frequency, the last item in the first appearance order is chosen.  
  
-   If the list is empty, an Expression.Error is thrown.  
  
## <a name="__goback"></a>Example  
  
```  
List.Mode({"A", 1, 4, 5, 2, "B", 3, 5, 5, 4, 4}) equals 5  
```  
