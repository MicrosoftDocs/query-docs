---
title: "List.RemoveRange | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: b857c6b8-d94e-4283-8cd6-bf57bab68a81
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# List.RemoveRange
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a list that removes count items starting at offset.  The default count is 1.  
  
```  
List.RemoveRange(list as list, offset as number, optional count as nullable number) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to remove items from.|  
|offset|The index to start at.|  
|optional count|The number of items to remove.|  
  
## Examples  
  
```  
List.RemoveRange({"A", "B", "C", "D"}, 2) equals {"A", "B", "D"}  
```  
  
```  
List.RemoveRange({"A", "B", "C", "D"}, 1, 2) equals {"A", "D"}  
```  
