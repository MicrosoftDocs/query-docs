---
title: "List.RemoveItems | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 3312e6aa-acd7-4b1a-99e9-a16429078ca1
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# List.RemoveItems
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Removes items from list1 that are present in list2, and returns a new list.  
  
```  
List.RemoveItems(list1 as list, list2 as list) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list1|The List to modify.|  
|list2|The list of items to remove.|  
  
## Example  
  
```  
List.RemoveItems({1, 2, 3, 3}, {3}) equals { 1, 2}  
```  
