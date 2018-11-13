---
title: "Text.Proper | Microsoft Docs"
ms.date: 11/13/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.Proper

  
## About  
Returns a text value with first letters of all words converted to uppercase.  
  
## Syntax

<pre>
Text.Proper(<b>string</b> as nullable text) as nullable text  
</pre> 
  
## Example  

Use `Text.Proper` on a simple sentence.
  
```powerquery-m  
Text.Proper("the QUICK BrOWn fOx jUmPs oVER tHe LAzy DoG")
```  

`"The Quick Brown Fox Jumps Over The Lazy Dog"`