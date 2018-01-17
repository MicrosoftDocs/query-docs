---
title: "Expression.Constant | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: ba2d990b-142a-4d40-8b1e-e7f3c9c42e31
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Expression.Constant
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a constant text literal from a value.  
  
```  
Expression.Constant(value as any) as text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|Text literal value.|  
  
## Examples  
Expression.Constant(1)  equals  "1"  
  
Expression.Constant(1 + 1)  equals  "2"  
  
Expression.Constant(true)  equals  "true"  
  
Expression.Constant("abc")  equals  """abc"""  
  
Expression.Constant("#(tab)")  equals  """#(#)(tab)"""  
  
Expression.Constant(#date(2011, 1, 1))  equals  "#date(2011, 1, 1)"  
  
Expression.Constant((x) =&gt; x)  equals  Error: Functions not supported  
  
Expression.Constant({1, 2, 3})  equals  Error: Lists not supported  
  
Expression.Constant([a = 1 + 1])  equals  Error: Records not supported  
  
