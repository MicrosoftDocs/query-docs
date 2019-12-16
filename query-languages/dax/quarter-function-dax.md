---
title: "QUARTER function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 12/05/2019
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

See related DAX functions: [YEAR](year-function-dax.md), [MONTH](month-function-dax.md), [DAY](day-function-dax.md).   

If the input value is BLANK, the output value is also BLANK.


## Example   

The following DAX query:
  
```dax
EVALUATE { QUARTER(DATE(2019, 2, 1)), QUARTER(DATE(2018, 12, 31)) } 
```

Returns:

|[Value]  |
|---------|
|1    |
|4    |

## Example   

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

