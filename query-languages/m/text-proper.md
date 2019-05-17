---
title: "Text.Proper | Microsoft Docs"
ms.date: 05/17/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.Proper

  
## About  

Returns the result of capitalizing only the first letter of each word in text value `text`. All other letters are returned in lowercase.
  
## Syntax

<pre>
Text.Proper(<b>text</b> as nullable text, optional <b>culture</b> as nullable text) as nullable text
</pre> 
  
## Example  

Use `Text.Proper` on a simple sentence.
  
```powerquery-m  
Text.Proper("the QUICK BrOWn fOx jUmPs oVER tHe LAzy DoG")
```  

`"The Quick Brown Fox Jumps Over The Lazy Dog"`
