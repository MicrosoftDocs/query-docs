---
title: "CROSSJOIN  function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 12/10/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# CROSSJOIN

Returns a table that contains the Cartesian product of all rows from all tables in the arguments. The columns in the new table are all the columns in all the argument tables.  
  
## Syntax  
  
```dax
CROSSJOIN(<table>, <table>[, <table>]…)  
```
  
### Parameters  

|Term|Definition|  
|--------|--------------|  
|table|Any DAX expression that returns a table of data|  
  
## Return value

A table that contains the Cartesian product of all rows from all tables in the arguments.  
  
## Remarks  
  
- Column names from *table* arguments must all be different in all tables or an error is returned.  
  
- The total number of rows returned by CROSSJOIN() is equal to the product of the number of rows from all tables in the arguments; also, the total number of columns in the result table is the sum of the number of columns in all tables. For example, if **TableA** has **rA** rows and **cA** columns, and **TableB** has **rB** rows and **cB** columns, and **TableC** has **rC** rows and **cC** column; then, the resulting table has **rA × rb × rC** rows and **cA + cB + cC** columns.  
  
## Example

The following example shows the results of applying CROSSJOIN() to two tables: **Colors** and **Stationery**.  
  
The table **Colors** contains colors and patterns:  
  
|Color|Pattern|  
|---------|-----------|  
|Red|Horizontal Stripe|  
|Green|Vertical Stripe|  
|Blue|Crosshatch|  
  
The table **Stationery** contains fonts and presentation:  
  
|Font|Presentation|  
|--------|----------------|  
|serif|embossed|  
|sans-serif|engraved|  
  
The expression to generate the cross join is presented below:  
  
```dax
CROSSJOIN( Colors, Stationery)  
```

When the above expression is used wherever a table expression is expected, the results of the expression would be as follows:  
  
|Color|Pattern|Font|Presentation|  
|---------|-----------|---------|-----------|  
|Red|Horizontal Stripe|serif|embossed|  
|Green|Vertical Stripe|serif|embossed|  
|Blue|Crosshatch|serif|embossed|  
|Red|Horizontal Stripe|sans-serif|engraved|  
|Green|Vertical Stripe|sans-serif|engraved|  
|Blue|Crosshatch|sans-serif|engraved|  
