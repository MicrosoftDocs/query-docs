---
title: "BinaryFormat.Text | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# BinaryFormat.Text

  
## About  
Returns a binary format that reads a text value.  The optional encoding value specifies the encoding of the text.  
  
## Syntax

<pre>   
BinaryFormat.Text(length as number, optional encoding as nullable number) as function  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|length|The number of bytes to decode.|  
|optional encoding|The encoding of the text.|  
  
## Remarks  
  
-   If the encoding is not specified, then the encoding is determined from the Unicode byte order marks.  
  
-   If no byte order marks are present, then TextEncoding.Utf8 is used.  
  
## Example  
  
```powerquery-m  
// Decode two bytes as ASCII text.  
let  
binaryData = #binary({65, 66, 67}),  
textFormat = BinaryFormat.Text(2, TextEncoding.Ascii)  
in  
textFormat(binaryData)   
equals "AB"  
```  
