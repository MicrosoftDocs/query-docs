---
description: "Learn more about: MEASURE"
title: "Virtual Column (DAX) | Microsoft Docs"
---
# Virtual Column

Introduces a virtual column definition in a DEFINE statement of a [DAX query](dax-queries.md).

## Syntax

```dax
[DEFINE 
    (
      COLUMN <table name>[<column name>] = <scalar expression>
    ) + 
]

(EVALUATE <table expression>) +
```

### Parameters

Scalar expression defines the content of virtual column. The expression is evaluated row by row on the table. The virtual column is only defined in the scope of current query.

## Return value

A virtual column is defined

## Remarks

- Virtual column is computed on-demand even for import model. This behavior is different from calculated column which is processed during refresh time.

- For DirectQuery table, the scalar expression is subject to data source capability. The limitation is the same as DirectQuery calculated column.

- Please carefully evaluate performance impact when defining a virtual column on a table with huge number of rows.

- When defining virtual column over a virtual table with visual shape, this virtual column is considered a visual calculation, and subject to visual calculation limitations.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Related content

[DEFINE](define-statement-dax.md)  
[EVALUATE](evaluate-statement-dax.md)  
[VAR](var-dax.md)  
[Virtual Table](virtual-table-statement-dax.md)
[DAX queries](dax-queries.md)  
