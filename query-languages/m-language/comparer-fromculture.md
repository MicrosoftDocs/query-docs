---
title: "Comparer.FromCulture | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 67b7970d-84e0-4e7b-bf9d-d67218a6f980
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Comparer.FromCulture

  
## About  
Returns a comparer function given the culture and a logical value for case sensitivity for the comparison. The default value for ignoreCase is false. The value for culture are well known text representations of locales used in the .NET framework.  
  
```  
Comparer.FromCulture(culture as text, optional ignoreCase as nullable logical) as function  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|culture|A text value corresponding to the culture values supported on your version of Windows, such as "en-US". If the culture is not specified, the current user culture is used. For a list of culture names, see [National Language Support (NLS) API Reference](http://msdn.microsoft.com/en-us/goglobal/bb896001.aspx).|  
|optional ignoreCase|Logical value whether or not to ignore the case.|  
  
## Example  
  
```  
let  
comparer1 = Comparer.FromCulture("en-us", false),  
comparer2 = Comparer.FromCulture("en-us", true)      
in       
[         
Test1 =  comparer1("a","A"), equals  -1   
Test2 =  comparer2("a","A") equals  0    
]  
```  
