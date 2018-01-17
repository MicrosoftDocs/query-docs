---
title: "List.Difference | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: be9f7055-9a9c-4ae7-b8de-c207dc80f0df
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# List.Difference
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns the items in list 1 that do not appear in list 2. Duplicate values are supported.  
  
```  
List.Difference(list1 as list, list2 as list,optional equationCriteria as any) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list1|The List to check with.|  
|list2|The List to check against.|  
|optional equationCriteria|An optional equation criteria value to control equality comparisons. For more information about equality comparisons, see Parameter Values.|  
  
## Examples  
  
```  
List.Difference({1..10}, {2..3,5..7}) equals {1,4,8,9,10}  
```  
  
```  
List.Difference({1}, {1,2,3}) equals {}  
```  
  
```  
List.Difference({1, 1, 1}, {1}) equals {1, 1}  
```  
