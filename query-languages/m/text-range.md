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
Returns the substring from the text <code>text</code> found at the offset <code>offset</code>. An optional parameter, <code>count</code>, can be included to specify how many characters to return. Throws an error if there aren't enough characters.  
```  
Text.Range(text as nullable text, offset as number, optional count as nullable number) as nullable text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|The text to parse.|  
|offset|The index to start parsing at.|  
|count|The number of characters to return.|  
  
## Example 1  
  
Find the substring from the text "Hello World" starting at index 6.  
  
```  
Text.Range("Hello World", 6) equals "World"  
```  
  
## Example 2  
  
Find the substring from the text "Hello World Hello" starting at index 6 spanning 5 characters.  
  
```  
Text.Range("Hello World Hello", 6, 5) equals "World"  
  
