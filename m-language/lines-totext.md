---
title: "Lines.ToText | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: fb35019a-493e-46a8-9680-05b5db534b94
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Lines.ToText

  
## About  
Converts a list of text into a single text. The specified lineSeparator is appended to each line. If not specified then the carriage return and line feed characters are used.  
  
```  
Lines.ToText (lines as list,  optional lineSeparator as nullable text) as text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|lines|The list of lines to convert.|  
|optional lineSeparator|Determines whether the line break characters are included in the line.  This is useful when the actual line break is significant and needs to be preserved.  If not specified, then it defaults to false.If includeLineSeparators is true, then the line break characters are included in the text.|  
  
## Examples  
  
```  
Lines.FromText("A,""B#(cr)C""#(cr)#(lf)1,2", true, null)  
{  
"A,""B#(cr)",  
"C""#(cr)#(lf)",  
"1,2"  
}  
```  
  
```  
Lines.FromText("A,""B#(cr)C""#(cr)#(lf)1,2")  
{  
"A,""B",  
"C""",  
"1,2"  
}  
```  
  
```  
Lines.FromText("A,""B#(cr)C""#(cr)#(lf)1,2", null, ",")  
{  
"A,""B#(cr)C""",  
"1,2"  
}  
```  
