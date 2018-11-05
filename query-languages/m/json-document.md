---
title: "Json.Document | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Json.Document

  
## About  
Returns the contents of a JSON document.  The contents may be directly passed to the function as text, or it may be the binary value returned by a function like File.Contents.  
  
## Syntax

<pre>
Json.Document(jsonText as any, optional encoding as nullable number) as any  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|jsonText|Json formatted text.|  
|optional encoding|The encoding value.|  
  
## Example  
  
```powerquery-m
Json.Document("{""glossary"": { ""title"": ""Example glossary"" } }")    
equals  [glossary = [title = "Example glossary"]]  
```  
