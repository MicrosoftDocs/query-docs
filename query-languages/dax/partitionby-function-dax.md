---
description: "Learn more about: PARTITIONBY"
title: "PARTITIONBY function (DAX) | Microsoft Docs"
---

# PARTITIONBY

Defines the columns that are used to partition a window function’s \<relation> parameter.
  
## Syntax  
  
```dax
PARTITIONBY ( [<partitionBy_columnName>[, partitionBy_columnName [, …]]] )
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|partitionBy_columnName| (Optional) The name of an existing column to be used to partition the window function’s \<relation>.</br> RELATED() may also be used to refer to a column in a table related to \<relation>.|

## Return value

This function does not return a value.  
  
## Remarks

This function can only be used within a window function expression.

## Example

See [OFFSET](offset-function-dax.md).

## Related content

[Understanding ORDERBY, PARTITIONBY, and MATCHBY functions](../dax/best-practices/dax-understand-orderby.md)  
[INDEX](index-function-dax.md)  
[OFFSET](offset-function-dax.md)  
[ORDERBY](orderby-function-dax.md)  
[MATCHBY](matchby-function-dax.md)  
[WINDOW](window-function-dax.md)  
[RANK](rank-function-dax.md)  
[ROWNUMBER](rownumber-function-dax.md)