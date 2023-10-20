---
description: "Learn more about: GENERATESERIES"
title: "GENERATESERIES function | Microsoft Docs"
---
# GENERATESERIES

Returns a single column table containing the values of an arithmetic series, that is, a sequence of values in which each differs from the preceding by a constant quantity. The name of the column returned is Value.  
  
## Syntax  
  
```dax
GENERATESERIES(<startValue>, <endValue>[, <incrementValue>])
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|startValue|The initial value used to generate the sequence.|
|endValue|The end value used to generate the sequence.|  
|incrementValue|(Optional) The increment value of the sequence. When not provided, the default value is 1.|
  
## Return value

A single column table containing the values of an arithmetic series. The name of the column is Value.
  
## Remarks

- When endValue is less than startValue, an empty table is returned.

- incrementValue must be a positive value.

- The sequence stops at the last value that is less than or equal to endValue.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example 1

The following DAX query:

```dax
EVALUATE GENERATESERIES(1, 5)
```

Returns the following table with a single column:

[Value]  |
---------|
1     |
2     |
3     |
4     |
5     |

## Example 2

The following DAX query:

```dax
EVALUATE GENERATESERIES(1.2, 2.4, 0.4)
```

Returns the following table with a single column:

[Value]  |
---------|
1.2    |
1.6     |
2     |
2.4     |

## Example 3

The following DAX query:

```dax
EVALUATE GENERATESERIES(CURRENCY(10), CURRENCY(12.4), CURRENCY(0.5))
```

Returns the following table with a single column:

[Value]  |
---------|
10    |
10.5     |
11     |
11.5     |
12     |
