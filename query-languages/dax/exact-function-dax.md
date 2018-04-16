---
title: "EXACT Function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 4/13/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# EXACT Function (DAX)
Compares two text strings and returns TRUE if they are exactly the same, FALSE otherwise. EXACT is case-sensitive but ignores formatting differences. You can use EXACT to test text being entered into a document.  
  
## Syntax  
  
```  
EXACT(<text1>,<text2>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**text1**|The first text string or column that contains text.|  
|**text2**|The second text string or column that contains text.|  
  
## Property Value/Return Value  
True or false. (Boolean)  
  
## Example  
The following formula checks the value of Column1 for the current row against the value of Column2 for the current row, and returns TRUE if they are the same, and returns FALSE if they are different.  
  
```  
=EXACT([Column1],[Column2])  
```  
  
## See Also  
[Text Functions &#40;DAX&#41;](text-functions-dax.md)  
  
