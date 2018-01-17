---
title: "List.IsDistinct | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: a06f9a08-0cae-4344-b4d6-83f01eaeda99
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# List.IsDistinct
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns whether a list is distinct.  
  
```  
List.IsDistinct(list as list, optional equationCriteria as any) as logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|optional equationCriteria|Equation criteria value used to control equality comparison. For more information about equationCriteria, see Parameter Values.|  
  
## Examples  
  
```  
List.IsDistinct({1, 2, 3, 2, 3}) equals false  
```  
  
```  
List.IsDistinct({"a","b","A"}, Comparer.FromCulture("en",false) equals true  
```  
  
```  
List.IsDistinct({"a","b","A"}, Comparer.FromCulture("en",true) equals false  
```  
