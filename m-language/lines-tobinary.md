---
title: "Lines.ToBinary | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 94873491-2e69-4dda-b33f-e9780b400728
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Lines.ToBinary
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Converts a list of text into a binary value using the specified encoding and lineSeparator.The specified lineSeparator is appended to each line. If not specified then the carriage return and line feed characters are used.  
  
```  
Lines.ToBinary(lines as list, optional lineSeparator as nullable text,  optional encoding as nullable number, optional includeByteOrderMark as nullable logical)as binary  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|lines|The list of lines to convert.|  
|optional lineSeparator|Determines whether the line break characters are included in the line.  This is useful when the actual line break is significant and needs to be preserved.  If not specified, then it defaults to false.If includeLineSeparators is true, then the line break characters are included in the text.|  
|optional encoding|The encoding option to apply.|  
|optional includeByteOrderMark|The byte order mark to include.|  
  
**Binary encoding**  
  
-   BinaryEncoding.Base64 = 0;  
  
-   BinaryEncoding.Hex = 1;  
  
