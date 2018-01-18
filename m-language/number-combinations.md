---
title: "Number.Combinations | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 79a36f60-291c-45da-9f42-d2df864b08ff
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Number.Combinations
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns the number of combinations of a given number of items for the optional combination size.  
  
```  
Number.Combinations (setSize as nullable number,  combinationSize as nullable number)  as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|setSize|Number of combination items.|  
|combinationSize|Size of combinations.|  
  
## Example  
  
```  
Number.Combinations(5, 3) equals 10  
```  
