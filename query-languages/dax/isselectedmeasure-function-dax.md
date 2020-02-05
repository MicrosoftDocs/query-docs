---
title: "ISSELECTEDMEASURE function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 04/25/2019
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# ISSELECTEDMEASURE

Used by expressions for calculation items to determine the measure that is in context is one of those specified in a list of measures. 

> [!NOTE]
> This function currently applies only to [SQL Server 2019 Analysis Services CTP 2.3](https://docs.microsoft.com/sql/sql-server/what-s-new-in-sql-server-ver15?view=sqlallproducts-allversions#calc-ctp24) and later.
  
## Syntax  
  
```dax
ISSELECTEDMEASURE( M1, M2, ... )  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|M1, M2, ...|A list of measures.|  
  
## Return value  

A Boolean indicating whether the measure that is currently in context is one of those specified in the list of parameters. 

## Remarks

Can only be referenced in the expression for a calculation item. 

## Example  

The following calculation item expression checks if the current measure is one of those specified in the list of parameters. If the measures are renamed, formula fixup will reflect the name changes in the expression.
  
```dax
IF (
    ISSELECTEDMEASURE ( [Expense Ratio 1], [Expense Ratio 2] ),
    SELECTEDMEASURE (),
    DIVIDE ( SELECTEDMEASURE (), COUNTROWS ( DimDate ) )
)

```
  
## See also  
[SELECTEDMEASURE](selectedmeasure-function-dax.md)  
[SELECTEDMEASURENAME](selectedmeasurename-function-dax.md)   
  
