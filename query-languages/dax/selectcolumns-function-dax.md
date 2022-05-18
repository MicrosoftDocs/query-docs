---
description: "Learn more about: SELECTCOLUMNS"
title: "SELECTCOLUMNS function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 07/10/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# SELECTCOLUMNS

Adds calculated columns to the given table or table expression.  
  
## Syntax  
  
```dax
SELECTCOLUMNS(<table>, <name>, <scalar_expression> [, <name>, <scalar_expression>]…) 
```
  
### Parameters  

|Term|Definition|  
|--------|--------------|  
|  table|  Any DAX expression that returns a table. |  
| name |  The name given to the column, enclosed in double quotes. |
|expression|Any expression that returns a scalar value like a column reference, integer, or string value.|
  
## Return value

A table with the same number of rows as the table specified as the first argument. The returned table has one column for each pair of \<name>, \<scalar_expression> arguments, and each expression is evaluated in the context of a row from the specified \<table> argument.
  
## Remarks  

SELECTCOLUMNS has the same signature as ADDCOLUMNS, and has the same behavior except that instead of starting with the \<table> specified, SELECTCOLUMNS starts with an empty table before adding columns.

[!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example  

For the following table named **Info**:

Country  |State  |Count  |Total  
---------|---------|---------|---------
IND     |   JK      |    20     |  800
IND     |   MH      |    25     |  1000
IND     |   WB      |    10     |  900
USA     |   CA      |    5     |   500
USA     |   WA      |    10     |  900

```dax
SELECTCOLUMNS(Info, "StateCountry", [State]&", "&[Country])
```

Returns,

|StateCountry |
|---------|
|IND, JK     |
|IND, MH     |
|IND, WB     |
|USA, CA    |
|USA, WA    |
