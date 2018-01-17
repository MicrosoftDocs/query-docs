---
title: "Comparer.Ordinal | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 89a9b474-5f98-4f82-bfe5-0ce55df055a2
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Comparer.Ordinal
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a comparer function which uses Ordinal rules to compare values.  
  
```  
Comparer.Ordinal(x as any, y as any) as number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|x|The left value to compare.|  
|y|The right value to compare.|  
  
## Examples  
  
```  
Comparer.Equals(Comparer.Ordinal, "a","A")equals false  
```  
