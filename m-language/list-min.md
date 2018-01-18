---
title: "List.Min | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: b4eac522-4ef3-4077-b5e4-94bc96358e40
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# List.Min
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns the minimum item in a list, or the optional default value if the list is empty.  
  
```  
List.Min(list as list, optional default as any, optional comparisonCriteria as any, optional includeNulls as nullable logical) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|optional default|The default value to return.|  
|optional comparisonCriteria|Specifies how to compare values in the list. If this argument is null, the default comparer is used.|  
|optional includeNulls|The Logical value whether or not to include null values in the return list.|  
  
## Example  
  
```  
List.Min({1, 4, 7, 3, -2, 5}) equals -2  
```  
