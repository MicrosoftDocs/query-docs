---
title: "Expression.Identifier | Microsoft Docs"
ms.date: 7/30/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Expression.Identifier

## Syntax

<pre>
Expression.Identifier(<b>name</b> as text) as text
</pre>
  
## About  
Returns a text value that can be used as an identifier from a text value.  
  

## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|name|The text to identify.|  
  
## Examples  

```powerquery-m
Expression.Identifier("foo") 
```  
equals "foo" 
 
```powerquery-m
Expression.Identifier("10 lbs")  
```  
equals "#""10 lbs""" 

```powerquery-m
Expression.Identifier("try")
``` 
equals "#""try"""  
  
```powerquery-m
Expression.Identifier("")
```  
equals "#"""""   

```powerquery-m
Expression.Identifier(null) 
```  
equals Error  

## Example of combined use  
  
```powerquery-m
Expression.Evaluate(  
// "let x = 1 in x"  
"let " &  
Expression.Identifier("x") & " = " & Expression.Constant(1) &  
" in " &  
Expression.Identifier("x")  
)   
```  
equals 1