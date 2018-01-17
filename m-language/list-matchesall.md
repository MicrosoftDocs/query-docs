---
title: "List.MatchesAll | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: d4223e95-586a-45f8-8af8-05581f8666da
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# List.MatchesAll
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns true if all items in a list meet a condition.  
  
```  
List.MatchesAll(list as list, condition as Function) as logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|condition|The condition to qualify against.|  
  
## Examples  
  
```  
List.MatchesAll({2, 4, 6}, each Number.Mod(_,2) = 0) equals true  
```  
  
```  
List.MatchesAll({2, 4, 5}, each Number.Mod(_,2) = 0) equals false  
```  
