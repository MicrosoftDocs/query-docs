---
title: "List.Numbers | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 4f89a4ac-acf9-4c8c-918b-36705798cc02
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# List.Numbers
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a list of numbers from size count starting at initial, and adds an increment.  The increment defaults to 1.  
  
```  
List.Numbers(start as number, count as number, optional increment as nullable number) as { Number }  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|start|The first number in the sequence.|  
|count|How many numbers to return.|  
|optional increment|The number to increment each number.|  
  
## Examples  
  
```  
List.Numbers(1, 5) equals {1, 2, 3, 4, 5}  
```  
  
```  
List.Numbers(1, 8, 3) equals {1, 4, 7, 10, 13, 16, 19, 22}  
```  
