---
title: "Number.IsOdd | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 1f1931d5-d29d-4fd2-81ae-65eb38ebd373
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Number.IsOdd
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns true if a value is an odd number.  
  
```  
Number.IsOdd(value as number) as logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|Value to evaluate.|  
  
## Examples  
  
```  
Number.IsOdd(3) equals true  
```  
  
```  
Number.IsOdd(4) equals false  
```  
