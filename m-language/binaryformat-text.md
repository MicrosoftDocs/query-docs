---
title: "BinaryFormat.Text | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: bc061c05-be96-4df2-b74d-2b7bbf67e9a5
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# BinaryFormat.Text
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a binary format that reads a text value.  The optional encoding value specifies the encoding of the text.  
  
```  
BinaryFormat.Text(length as number, optional encoding as nullable number) as function  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|length|The number of bytes to decode.|  
|optional encoding|The encoding of the text.|  
  
## Remarks  
  
-   If the encoding is not specified, then the encoding is determined from the Unicode byte order marks.  
  
-   If no byte order marks are present, then TextEncoding.Utf8 is used.  
  
## Example  
  
```  
// Decode two bytes as ASCII text.  
let  
binaryData = #binary({65, 66, 67}),  
textFormat = BinaryFormat.Text(2, TextEncoding.Ascii)  
in  
textFormat(binaryData)   
equals "AB"  
```  
