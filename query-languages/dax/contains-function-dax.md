---
description: "Learn more about: CONTAINS"
title: "CONTAINS function (DAX) | Microsoft Docs"
---
# CONTAINS

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns true if values for all referred columns exist, or are contained, in those columns; otherwise, the function returns false.  
  
## Syntax  
  
```dax
CONTAINS(<table>, <columnName>, <value>[, <columnName>, <value>]…)  
```
  
### Parameters  

|Term|Definition|  
|--------|--------------|  
|table|Any DAX expression that returns a table of data.|  
|columnName|The name of an existing column, using standard DAX syntax. It cannot be an expression. |  
|value|Any DAX expression that returns a single scalar value, that is to be sought in *columnName*. The expression is to be evaluated exactly once and before it is passed to the argument list.  |  

## Return value

A value of **TRUE** if each specified *value* can be found in the corresponding *columnName*, or are contained, in those columns; otherwise, the function returns **FALSE**.  
  
## Remarks  
  
- The arguments *columnName* and *value* must come in pairs; otherwise an error is returned.  
  
- *columnName* must belong to the specified *table*, or to a table that is related to *table*.  
  
- If *columnName* refers to a column in a related table then it must be fully qualified; otherwise, an error is returned.  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following example creates a measure that tells you whether there were any Internet sales of product 214 and to customer 11185 at the same time.  
  
```dax
= CONTAINS(InternetSales, [ProductKey], 214, [CustomerKey], 11185)  
```
