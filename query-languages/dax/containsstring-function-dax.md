---
description: "Learn more about: CONTAINSSTRING"
title: "CONTAINSSTRING function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 07/05/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# CONTAINSSTRING

Returns TRUE or FALSE indicating whether one string contains another string.  
  
## Syntax  
  
```dax
CONTAINSSTRING(<within_text>, <find_text>) 
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|within_text|The text in which you want to search for find_text.|  
|find_text|The text you want to find.|
  
## Return value  

TRUE if find_text is a substring of within_text; otherwise FALSE.

## Remarks

- CONTAINSSTRING is not case-sensitive.

- You can use `?` and `*` wildcard characters. Use `~` to escape wildcard characters.

## Example  

DAX query

```DAX
EVALUATE
    ROW(
        "Case 1", CONTAINSSTRING("abcd", "bc"), 
        "Case 2", CONTAINSSTRING("abcd", "BC"),
        "Case 3", CONTAINSSTRING("abcd", "a*d"),
        "Case 4", CONTAINSSTRING("abcd", "ef")
    )
```

Returns

|[Case 1]  |[Case 2]  |[Case 3]  |[Case 4]  |
|---------|---------|---------|---------|
|TRUE     | TRUE         | TRUE         |FALSE          |
