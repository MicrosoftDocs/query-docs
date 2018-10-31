---
title: "Text.Range | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.Range

  
## About  
Returns the substring from the text `text` found at the offset `offset`. An optional parameter, `count`, can be included to specify how many characters to return. Throws an error if there aren't enough characters.  

## Syntax

<pre>
Text.Range(text as nullable text, offset as number, optional count as nullable number) as nullable text  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|The text to parse.|  
|offset|The index to start parsing at.|  
|count|The number of characters to return.|  
  
## Example 1  
  
Find the substring from the text "Hello World" starting at index 6.  
  
```powerquery-m
Text.Range("Hello World", 6) equals "World"  
```  
  
## Example 2  
  
Find the substring from the text "Hello World Hello" starting at index 6 spanning 5 characters.  
  
```powerquery-m
Text.Range("Hello World Hello", 6, 5) equals "World"  
```
  
