---
title: "Expression.Identifier | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
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
manager: "kfile"
---
# Expression.Identifier

  
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
