---
title: "List.Modes | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: c9a4c869-0d1d-414b-86fe-4a69f34c89c7
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# List.Modes
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns all items that appear with the same maximum frequency.  
  
```  
List.Modes(list as list, optional equationCriteria as any)as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|optional equationCriteria|Controls the sort order. For more information about equality comparisons, see Parameter Values.|  
  
## <a name="__toc360789384"></a>Remarks  
  
-   If the list is empty, an Expression.Error is thrown.  
  
## <a name="__goback"></a>Example  
  
```  
List.Modes({"A", 1, 4, 5, 2, "B", 3, 5, 5, "A", 4, 4, "A"}) equals {"A", 4, 5}  
```  
