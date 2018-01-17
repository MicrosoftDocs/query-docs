---
title: "Text.Length | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: e86d5f03-1935-4890-b80c-0136b5943583
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Text.Length
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns the number of characters in a text value.  
  
```  
Text.Length(text as nullable text) as nullable number  
```  
  
## <a name="__toc360788812"></a>Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|The input text value|  
  
## Example  
  
```  
Text.Length("abc") equals 3  
```  
  
## <a name="__toc360788813"></a>Text Comparisons  
Text comparisons are performed by obtaining a comparer from **Comparer.FromCulture**. The comparer returns 0, a negative number, or a positive number based on the result of the comparison. The **Comparer.Equals** function is used to compare two text values.  
  
## Example  
  
```  
let  
comparer = Comparer.FromCulture("en-US", false)  
in  
[    
comparisonResult = comparer("a","b"),    
equalityResult   = Comparer.Equals(comparer,"a","b")    
]  
```  
