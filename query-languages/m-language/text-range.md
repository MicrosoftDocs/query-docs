---
title: "Text.Range | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: edec4521-270e-4f56-8188-3e8f435ae607
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
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
  
