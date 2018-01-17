---
title: "Number.IntegerDivide | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 1af4109a-2b61-4b7d-bf68-0e2f654149f9
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Number.IntegerDivide
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Divides two numbers and returns the whole part of the resulting number.  
  
```  
Number.IntegerDivide (number1 as nullable number,  number2 as nullable number,  optional precision as nullable number) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|number1|The Dividend.|  
|number2|The Divisor.|  
|optional precision|Precision of the result.|  
  
## Example  
  
```  
Number.IntegerDivide(9.2, 3.1) equals 2  
```  
