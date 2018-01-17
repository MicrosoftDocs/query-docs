---
title: "List.RemoveLastN | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 48856cb1-8f6b-4d62-95a6-660ab93417e4
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# List.RemoveLastN
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a list with the specified number of elements removed from the list starting at the last element. The number of elements removed depends on the optional countOrCondition parameter.  
  
```  
List.RemoveRange(list as list, offset as number, optional count as nullable number) as list  
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
List.RemoveLastN  
  
    (  
  
    {1, 2, 3, 4, 5},  
  
    3  
  
    )  
  
equals {1, 2}  
  
List.RemoveLastN  
  
    (  
  
    {5, 4, 2, 6, 4},  
  
    each _ > 3  
  
    )  
  
equals {5, 4, 2}  
```  
