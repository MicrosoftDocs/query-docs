---
description: "Learn more about: Virtual Table"
title: "Virtual Table (DAX) | Microsoft Docs"
---
# Virtual Table

Introduces a virtual table definition in a DEFINE statement of a [DAX query](dax-queries.md).

## Syntax

```dax
[DEFINE 
    (
      TABLE <table name> = <table expression>
        [WITH VISUAL SHAPE
          (AXIS <axis name>
            (GROUP <column>[, <column>] + TOTAL <column>) +
            ORDER BY <column>[, <column>] +
          ) +
          [DENSIFY <string literal>]
        ]
    ) + 
]

(EVALUATE <table expression>) +
```

### Parameters

Table expression defines the content of the virtual table. The virtual table is only defined in the scope of current query.

Optionally a visual shape can be defined on the virtual table. Visual shape is used for visual calculation. A visual shape consists of axes with optionally a Boolean DENSIFY column.

Axis is defined to be a list of rollup groups followed by a list of order by columns to specify how the axis is ordered. A rollup group consists of one or more group by columns and then one Boolean TOTAL column indicating whether each row is subtotal of the current rollup group. FALSE value indicates that current row is detail row (grouping by current rollup group). TRUE value indicates current row is rolled up (not grouping by current rollup group).

If DENSIFY column is requested, then the visual shape performs a densification. This means in addition to the rows from original table expression, we also add combination of axes values that do not exist in the original table expression. In other words, we do a left outer join from the cross join of axes with the original table expression. A TRUE value in DENSIFY column indicates the current row is not in the original table expression and added by the densification process. Such row should have empty value in all measure columns (columns outside axes definitions). A FALSE value in DENSIFY column indicates the current row is from the original table expression.

## Return value

A virtual table is defined

## Remark

Unlike variables, virtual table has lineage of its own, and does not carry the lineage from the table expression it's defined from.

## Example

Assume a table T has following rows:

|Year|Product|SalesAmount|
|----------|---------|---------|
|2000|Apple|$  10.1|
|2000|Banana|$  10.2|
|2001|Apple|$  20.3|

```dax
DEFINE TABLE data = SUMMARIZECOLUMNS(ROLLUPADDISSUBTOTAL(T[Year], "IsYearTotal"), ROLLUPADDISSUBTOTAL(T[Product], "IsProductTotal"), "Meausre", SUM(T[SalesAmount]))
  WITH VISUAL SHAPE
    AXIS ROWS GROUP [Year] TOTAL [IsYearTotal] ORDER BY [Year]
    AXIS COLUMNS GROUP [Product] TOTAL [IsProductTotal] ORDER BY [Product]
    DENSIFY "IsDensified"
EVALUATE data
```

The returned result is

|data[Year]|data[Product]|data[IsYearTotal]|data[IsProductTotal]|data[Measure]|data[IsDensified]|
|----------|---------|---------|---------|---------|---------|
|||true|true|$ 40.6|false|
|2000||false|true|$ 20.3|false|
|2001||false|true|$ 20.3|false|
||Apple|true|false|$ 30.4|false|
|2000|Apple|false|false|$ 10.1|false|
|2001|Apple|false|false|$ 20.3|false|
||Banana|true|false|$ 10.2|false|
|2000|Banana|false|false|$ 10.2|false|
|2001|Banana|false|false||true|


## Related content

[DEFINE](define-statement-dax.md)  
[EVALUATE](evaluate-statement-dax.md)  
[VAR](var-dax.md)  
[Virtual Column](virtual-column-statement-dax.md)
[DAX queries](dax-queries.md)  
