---
title: "List.Last | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 0af144d6-8046-41c1-b8d4-8325c7c39507
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# List.Last
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns the last set of items in the list by specifying how many items to return or a qualifying condition provided by **countOrCondition**.  
  
```  
List.Last(list as list, optional defaultValue as any) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|optional defaultValue|Default value if list is empty.|  
  
## <a name="__toc360789237"></a>Remarks  
  
-   If a number is specified, up to that many items are returned.  
  
-   If a condition is specified, all items are returned that initially meet the condition. Once an item fails the condition, no further items are considered.  
  
## Examples  
  
```  
List.Last({1, 2, 3}) equals 3  
```  
