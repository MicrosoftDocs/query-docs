---
description: "Learn more about: SELECTCOLUMNS"
title: "SELECTCOLUMNS function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 06/08/2022
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# SELECTCOLUMNS

Returns a table with selected columns from the table and new columns specified by the DAX expressions.  
  
## Syntax  
  
```dax
SELECTCOLUMNS(<Table>, [<Name>], <Expression>, <Name>], …) 
```
  
### Parameters  

|Term|Definition|  
|--------|--------------|  
| Table|  Any DAX expression that returns a table. |  
| Name |  The name given to the column, enclosed in double quotes. |
| Expression |Any expression that returns a scalar value like a column reference, integer, or string value.|
  
## Return value

A table with the same number of rows as the table specified as the first argument. The returned table has one column for each pair of \<Name>, \<Expression> arguments, and each expression is evaluated in the context of a row from the specified \<Table> argument.
  
## Remarks  

SELECTCOLUMNS has the same signature as ADDCOLUMNS, and has the same behavior except that instead of starting with the \<Table> specified, SELECTCOLUMNS starts with an empty table before adding columns.

[!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example  

For the following table named **Customer**:

Country  |State  |Count  |Total  
---------|---------|---------|---------
IND     |   JK      |    20     |  800
IND     |   MH      |    25     |  1000
IND     |   WB      |    10     |  900
USA     |   CA      |    5     |   500
USA     |   WA      |    10     |  900

```dax
SELECTCOLUMNS(Customer, "Country, State", [Country]&", "&[State])
```

Returns,

|Country, State |
|---------|
|IND, JK     |
|IND, MH     |
|IND, WB     |
|USA, CA    |
|USA, WA    |
