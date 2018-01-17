---
title: "List.RemoveFirstN | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 62c27f37-ab61-47a5-9dbe-c042ced0acf2
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# List.RemoveFirstN
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a list with the specified number of elements removed from the list starting at the first element. The number of elements removed depends on the optional countOrCondition parameter.  
  
```  
List.RemoveFirstN( table as table, optional countOrCondition as any) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to remove items from.|  
|optional countOrCondition|Optional number of elements  or condition to remove elements, default is 1|  
  
## Remarks  
  
-   If countOrCondidtion is omitted only the first element is removed  
  
-   If countOrCondidtion is a number, that many elements (starting from the top) will be removed)  
  
-   If countOrCondidtion is a condition, the elements that meet the condition will be removed until an element does not meet the condition  
  
## Examples  
  
```  
List.RemoveFirstN  
  
    (  
  
    {1, 2, 3, 4, 5},  
  
    3  
  
    )  
  
equals {4, 5}  
  
List.RemoveFirstN  
  
    (  
  
    {5, 4, 2, 6, 1},  
  
    each _ > 3  
  
    )  
  
equals { 2, 6, 1}  
```  
