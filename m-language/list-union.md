---
title: "List.Union | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: bc144ab1-21b5-4335-b054-f2a8b18d3e71
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# List.Union
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a list from a list of lists and unions the items in the individual lists. The returned list contains all items in any input lists. Duplicate values are matched as part of the Union.  
  
```  
List.Union(list as list,optional equationCriteria as any) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List of lists to check.|  
|optional equationCriteria|An optional equation criteria value to control equality comparisons. For more information about equality comparisons, see Parameter Values.|  
  
## Examples  
  
```  
List.Union({ {1..5}, {2..6}, {3..7} }) equals {1..7}  
```  
  
```  
List.Union({ {1..5}, {4..8}, {7..11} }) equals {1..11}  
```  
  
```  
List.Union({ {1, 1, 1, 2}, {1, 1, 2, 2} }) equals {1, 1, 1, 2, 2}  
```  
