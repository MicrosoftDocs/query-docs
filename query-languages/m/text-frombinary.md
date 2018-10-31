---
title: "Text.FromBinary | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.FromBinary

  
## About  
Decodes data from a binary value in to a text value using an encoding.  
  
## Syntax

<pre>
Text.FromBinary(binary as nullable binary, optional encoding as nullable number) as nullable text  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|binary|The value to decode.|  
|optional encoding|Encoding option to apply.|  
  
Text encoding  
  
TextEncoding.Utf8 = 65001;  
  
TextEncoding.Utf16 = 1200;  
  
TextEncoding.Ascii = 20127;  
  
TextEncoding.Unicode = 1200;  
  
TextEncoding.BigEndianUnicode = 1201,  
  
TextEncoding.Windows = 1252;  
  
