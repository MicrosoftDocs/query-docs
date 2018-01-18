---
title: "Expression.Identifier | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 411cdb8c-33c6-4096-9f37-b35c1d9efede
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Expression.Identifier
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a text value that can be used as an identifier from a text value.  
  
```  
Expression.Identifier(name as text) as text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|name|The text to identify.|  
  
## Examples  
  
```  
Expression.Identifier("foo") equals "foo"  
```  
  
```  
Expression.Identifier("10 lbs") equals "#""10 lbs"""  
```  
  
```  
Expression.Identifier("try") equals "#""try"""  
```  
  
```  
Expression.Identifier("") equals "#"""""  
```  
  
```  
Expression.Identifier(null) equals Error  
```  
  
## Example of combined use  
  
```  
Expression.Evaluate(  
// "let x = 1 in x"  
"let " &  
Expression.Identifier("x") & " = " & Expression.Constant(1) &  
" in " &  
Expression.Identifier("x")  
) equals 1  
```  
