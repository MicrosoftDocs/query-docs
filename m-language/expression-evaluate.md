---
title: "Expression.Evaluate | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 06400c08-5977-40e6-b251-cf15e8801de1
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Expression.Evaluate
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Evaluates a Text expression and returns the evaluated value.  
  
```  
Expression.Evaluate(expression as text, optional environment as [...]) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|expression|The expression to evaluate.|  
|optional environment|The expression environment.|  
  
## Examples  
Expression.Evaluate("1 + 1") equals 2  
  
Expression.Evaluate("1 +") equals Error  
  
Expression.Evaluate(  
  
"section Section1; shared X = 1;"  
  
)  equals  Error, only expressions are supported  
  
Expression.Evaluate(  
  
"Record.Field([A=1], ""A"")"  
  
)  equals  error. Unknown identifier "Record.Field".  
  
Expression.Evaluate(  
  
"Record.Field([A=1], ""A"")",  
  
[Record.Field = Record.Field]  
  
)  equals  1  
  
let  
  
x = 1  
  
in  
  
Expression.Evaluate("x") equals Error. Unknown identifier "x".  
  
let  
  
x = 1  
  
in  
  
Expression.Evaluate(  
  
"x",  
  
\#shared  
  
) equals Error. Unknown identifier "x".  
  
let  
  
x = 1  
  
in  
  
Expression.Evaluate("x", [x = x]) equals 1  
  
section;  
  
shared MyText = "ABC";  
  
MyResult = Expression.Evaluate(  
  
"Text.StartsWith(MyText, ""A"")",  
  
\#shared  
  
); // true  
  
section;  
  
MyText = "ABC";  
  
MyResult = Expression.Evaluate(  
  
"Text.StartsWith(MyText, ""A"")",  
  
\#shared  
  
); equals Error. Unknown identifier "MyText" (since MyText isn't shared).  
  
