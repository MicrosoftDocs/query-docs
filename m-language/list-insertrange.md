---
title: "List.InsertRange | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 887c2017-9787-4603-b647-457b93257c5d
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# List.InsertRange
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Inserts items from values at the given index in the input list.  
  
```  
List.InsertRange(list as list, offset as number, values as list) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to modify.|  
|offset|The index to insert at.|  
|values|The values to insert.|  
  
## <a name="__goback"></a>Example  
  
```  
List.InsertRange({"A", "B", "D"}, 2, {"C"}) equals {"A", "B", "C", "D"}  
```  
