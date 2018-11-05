---
title: "UNICHAR Function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# UNICHAR Function (DAX)

Returns the Unicode character referenced by the numeric value.
  
## Syntax  
  
```dax
UNICHAR(number)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|The Unicode number that represents the character.|  
  
## Return Value  
A character represented by the Unicode number 
  
## Remarks  

If XML characters are not invalid, UNICHAR returns an error.

If Unicode numbers are partial surrogates and data types are not valid, UNICHAR returns an error.

If numbers are numeric values that fall outside the allowable range, UNICHAR returns an error.

If number is zero (0), UNICHAR returns an error.

The Unicode character returned can be a string of characters, for example in UTF-8 or UTF-16 codes.
  
## Example  

The following example returns the character represented by the Unicode number 66 (uppercase A).  
```dax
=UNICHAR(65)
```

The following example returns the character represented by the Unicode number 32 (space character).
```dax
=UNICHAR(32)
```

The following example returns the character represented by the Unicode number 9733 (&#9733; character).
```dax
=UNICHAR(9733)
```

  
