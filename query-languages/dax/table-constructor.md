---
description: "Learn more about: Table constructor"
title: "Table constructor"
---
# Table constructor

Returns a table of one or more columns.
  
## Syntax  
  
```dax
{ <scalarExpr1>, <scalarExpr2>, … } 
{ ( <scalarExpr1>, <scalarExpr2>, … ), ( <scalarExpr1>, <scalarExpr2>, … ), … }
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|`scalarExprN`|Any DAX expression that returns a scalar value.|  
  
## Return value

A table of one or more columns. When there is only one column, the name of the column is Value. When there are N columns where N > 1, the names of the columns from left to right are Value1, Value2, …, ValueN.
  
## Remarks

- The first syntax returns a table of a single column. The second syntax returns a table of one or more columns.

- The number of scalar expressions must be the same for all rows.

- When the data types of the values for a column are different in different rows, all values are converted to a common data type.

## Example 1

The following DAX queries:

```dax
EVALUATE { 1, 2, 3 }
```

and

```dax
EVALUATE { (1), (2), (3) }
```

Return the following table of a single column:

|[Value]  |
|---------|
|1     |
|2     |
|3     |

### Example 2

The following DAX query:

```dax
EVALUATE
    {
        (1.5, DATE(2017, 1, 1), CURRENCY(199.99), "A"),
        (2.5, DATE(2017, 1, 2), CURRENCY(249.99), "B"),
        (3.5, DATE(2017, 1, 3), CURRENCY(299.99), "C")
    }
```

Returns,

[Value1]  |[Value2]  |[Value3]  |[Value4]  
---------|---------|---------|---------
1.5    |    1/1/2017     |   199.99      |     A
2.5     |   1/2/2017      |    249.99     |         B
3.5     |   1/3/2017      |    299.99     |         C

### Example 3

The following DAX query:

```dax
EVALUATE { 1, DATE(2017, 1, 1), TRUE, "A" }
```

Returns the following table of a single column of String data type:

|[Value]  |
|---------|
|1     |
|1/1/2017     |
|``TRUE``    |
|A  |
