---
description: "Learn more about: EVALUATE"
title: "EVALUATE keyword (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 07/08/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# EVALUATE
  
A statement containing a table expression required in a [DAX query](dax-queries.md).

A DAX query can include any number of EVALUATE statements. EVALUATE statements can be preceded by one or more optional DEFINE statements which include VAR, MEASURE, TABLE, COLUMN entity definitions that exist for the entire scope of the query and apply to all EVALUATE statements in the query. An EVALUATE statement can be followed by optional ORDER BY and START AT result modifiers that determine the order and starting point of rows returned.  

## Syntax  
  
```dax
EVALUATE <table>  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|table|A table expression|  
  
### Return value

The result of a table expression.

### Remarks

A DAX query can contain multiple EVALUATE statements.

### Example

```dax
EVALUATE(
    'Internet Sales'
    )
```

Returns all rows and columns from the Internet Sales table, as a table.

## ORDER BY (Optional)

The optional **ORDER BY** keyword defines one or more expressions used to sort query results. Any expression that can be evaluated for each row of the result is valid.  

### Syntax

```dax
EVALUATE <table>  
[ORDER BY {<expression> [{ASC | DESC}]}[, …]  
```

### Arguments

|Term  |Definition  |
|---------|---------|
|  expression     |   Any DAX expression that returns a single scalar value.  |
| ASC  | (default) Ascending sort order. |
| DESC  | Descending sort order. |

### Example

```dax
EVALUATE(
    'Internet Sales'
    )
ORDER BY
    'Internet Sales'[Order Date]
```

Returns all rows and columns from the Internet Sales table, ordered by Order Date, as a table.

## START AT (Optional)

The optional **START AT** keyword is used inside an **ORDER BY** clause. It defines the value at which the query results begin.

### Syntax

```dax
EVALUATE <table>  
[ORDER BY {<expression> [{ASC | DESC}]}[, …]  
[START AT {<value>|<parameter>} [, …]]]  
```

### Arguments

|Term  |Definition  |
|---------|---------|
|  value     |   A constant value. Cannot be an expression.  |
|  parameter     |   The name of a parameter in an XMLA statement prefixed with an `@` character.  |

### Remarks
  
START AT arguments have a one-to-one correspondence with the columns in the ORDER BY clause. There can be as many arguments in the START AT clause as there are in the ORDER BY clause, but not more. The first argument in the START AT defines the starting value in column 1 of the ORDER BY columns. The second argument in the START AT defines the starting value in column 2 of the ORDER BY columns within the rows that meet the first value for column 1.  

### Example

```dax
EVALUATE(
    'Internet Sales'
    )
ORDER BY
    'Internet Sales'[Order Date]
```

Returns all rows and columns from the Internet Sales table, ordered by Order Date, as a table.

## See also

[DAX queries](dax-queries.md)  
[VAR](var-dax.md)  
