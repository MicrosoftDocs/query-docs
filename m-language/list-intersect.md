---
title: "List.Intersect | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: e0b4a862-edcf-46f3-95c7-74f56e31c77e
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# List.Intersect
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a list from a list of lists and intersects common items in individual lists. Duplicate values are supported.  
  
```  
List.Intersect(list as list /* { List } */,optional equationCriteria as any) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List of lists to check.|  
|optional equationCriteria|An optional equation criteria value to control equality comparisons. For more information about equality comparisons, see Parameter Values.|  
  
## <a name="__toc360789342"></a>Remarks  
  
-   If nothing is common in all lists, an empty list is returned.  
  
## Examples  
  
```  
List.Intersect({ {1..5}, {2..6}, {3..7} }) equals {3..5}  
```  
  
```  
List.Intersect({ {1..5}, {4..8}, {7..11} }) equals {}  
```  
  
```  
List.Intersect({ {1, 1, 1, 2}, {1, 1, 2, 2} }) equals {1, 1, 2}  
```  
