---
title: "Text.Length | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
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
manager: "kfile"
---
# Text.Length

  
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
