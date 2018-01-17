---
title: "List.Max | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: b86fe33c-d704-45fc-8e95-b7660f371d2c
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# List.Max
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns the maximum item in a list, or the optional default value if the list is empty.  
  
```  
List.Max(list as list, optional default as any, optional comparisonCriteria as any, optional includeNulls as nullable logical) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|optional default|The default value to return.|  
|optional comparisonCriteria|An optional comparison criteria value to control equality testing. If this argument is null, the default comparer is used.|  
|optional includeNulls|The Logical value whether or not to include null values in the return list.|  
  
## Example  
  
```  
List.Max({1, 4, 7, 3, -2, 5}, 1) equals 7  
```  
