---
description: "Learn more about: CONTAINSSTRINGEXACT"
title: "CONTAINSSTRINGEXACT function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/05/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# CONTAINSSTRINGEXACT

Returns TRUE or FALSE indicating whether one string contains another string.
  
## Syntax  
  
```dax
CONTAINSSTRINGEXACT(<within_text>, <find_text>)
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|within_text|The text in which you want to search for find_text.|  
|find_text|The text you want to find.|
  
## Return value  

TRUE if find_text is a substring of within_text; otherwise FALSE.

## Remarks

CONTAINSSTRINGEXACT is case-sensitive.

## Example  

DAX query

```DAX
EVALUATE
    ROW(
        "Case 1", CONTAINSSTRINGEXACT("abcd", "bc"), 
        "Case 2", CONTAINSSTRINGEXACT("abcd", "BC"),
        "Case 3", CONTAINSSTRINGEXACT("abcd", "a*d"),
        "Case 4", CONTAINSSTRINGEXACT("abcd", "ef")
    )

```

Returns

|[Case 1]  |[Case 2]  |[Case 3]  |[Case 4]  |
|---------|---------|---------|---------|
|TRUE     | FALSE         | FALSE         |FALSE          |
