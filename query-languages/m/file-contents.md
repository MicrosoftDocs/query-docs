---
title: "File.Contents | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# File.Contents

  
## About  
Returns the binary contents of the file located at a path.  
  
## Syntax

<pre>
File.Contents(path as text) as binary  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|path|The path to the file to retrieve contents for.|  
  
## Example  
  
```powerquery-m
File.Contents("c:\users\myuser\Desktop\file.txt")  
```  
