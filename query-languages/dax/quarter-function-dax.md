---
description: "Learn more about: QUARTER"
title: "QUARTER function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 07/10/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---

# QUARTER

Returns the quarter as a number from 1 (January – March) to 4 (October – December).
  
## Syntax  
  
```dax
QUARTER(<date>)
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|date|A date.|  
  
## Return value  

An integer number from 1 to 4.  
  
## Remarks

If the input value is BLANK, the output value is also BLANK.

## Example 1

The following DAX query:
  
```dax
EVALUATE { QUARTER(DATE(2019, 2, 1)), QUARTER(DATE(2018, 12, 31)) } 
```

Returns:

|[Value]  |
|---------|
|1    |
|4    |

## Example 2

The following DAX query:
  
```dax
EVALUATE
ADDCOLUMNS(
    FILTER(
        VALUES(
            FactInternetSales[OrderDate]), 
            [OrderDate] >= DATE(2008, 3, 31) && [OrderDate] <= DATE(2008, 4, 1)
        ), 
    "Quarter", QUARTER([OrderDate])
)
```

Returns:

|FactInternetSales[OrderDate]  | [Quarter]  |
|---------|---------|
|3/31/2008    |  1  |
|  4/1/2008  |  2   |

## See also

[YEAR](year-function-dax.md)  
[MONTH](month-function-dax.md)  
[DAY](day-function-dax.md)
