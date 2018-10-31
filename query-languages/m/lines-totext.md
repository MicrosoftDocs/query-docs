---
title: "Lines.ToText | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Lines.ToText

  
## About  
Converts a list of text into a single text. The specified lineSeparator is appended to each line. If not specified then the carriage return and line feed characters are used.  
  
## Syntax

<pre>
Lines.ToText (lines as list,  optional lineSeparator as nullable text) as text  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|lines|The list of lines to convert.|  
|optional lineSeparator|Determines whether the line break characters are included in the line.  This is useful when the actual line break is significant and needs to be preserved.  If not specified, then it defaults to false.If includeLineSeparators is true, then the line break characters are included in the text.|  
  
## Examples  
  
```powerquery-m
Lines.FromText("A,""B#(cr)C""#(cr)#(lf)1,2", true, null)  
{  
"A,""B#(cr)",  
"C""#(cr)#(lf)",  
"1,2"  
}  
```  
  
```powerquery-m
Lines.FromText("A,""B#(cr)C""#(cr)#(lf)1,2")  
{  
"A,""B",  
"C""",  
"1,2"  
}  
```  
  
```powerquery-m
Lines.FromText("A,""B#(cr)C""#(cr)#(lf)1,2", null, ",")  
{  
"A,""B#(cr)C""",  
"1,2"  
}  
```  
