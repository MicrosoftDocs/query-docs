---
title: "List.MinN | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: b15bde9a-0b07-482c-b8ab-3cc0c9e625a1
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# List.MinN
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns the minimum values in a list.  
  
```  
List.MinN(list as list, countOrCondition as any,  optional comparisonCriteria as any, optional includeNulls as nullable logical) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|countOrCondition|Specifies the number of values to return or a filtering condition.|  
|optional comparisonCriteria|Specifies how to compare values in the list.|  
|optional includeNulls|The Logical value whether or not to include null values in the return list.|  
  
## Example  
  
```  
List.MinN({3, 4, 5, -1, 7, 8, 2}, 5) equals {-1, 2, 3, 4, 5}  
```  
