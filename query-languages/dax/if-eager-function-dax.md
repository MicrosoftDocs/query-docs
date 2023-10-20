---
description: "Learn more about: IF.EAGER"
title: "IF.EAGER function (DAX) | Microsoft Docs"
---
# IF.EAGER

Checks a condition, and returns one value when TRUE, otherwise it returns a second value. It uses an *eager* execution plan which always executes the branch expressions regardless of the condition expression.

## Syntax

```dax
IF.EAGER(<logical_test>, <value_if_true>[, <value_if_false>])
```

### Parameters

|Term|Definition|
|--------|--------------|
|logical_test|Any value or expression that can be evaluated to TRUE or FALSE.|  
|value_if_true|The value that's returned if the logical test is TRUE.|
|value_if_false|(Optional) The value that's returned if the logical test is FALSE. If omitted, BLANK is returned.|

## Return value

Either **value_if_true**, **value_if_false**, or BLANK.

## Remarks

- The IF.EAGER function can return a variant data type if value_if_true and value_if_false are of different data types, but the function attempts to return a single data type if both **value_if_true** and **value_if_false** are of numeric data types. In the latter case, the IF.EAGER function will implicitly convert data types to accommodate both values. 

    For example, the formula `IF.EAGER(<condition>, TRUE(), 0)` returns TRUE or 0, but the formula `IF.EAGER(<condition>, 1.0, 0)` returns only decimal values even though **value_if_false** is of the whole number data type. To learn more about implicit data type conversion, see [Data types](dax-overview.md#data-types).

- IF.EAGER has the same functional behavior as the IF function, but performance may differ due to differences in execution plans. `IF.EAGER(<logical_test>, <value_if_true>, <value_if_false>)` has the same execution plan as the following DAX expression:

    ```dax
    
    VAR _value_if_true = <value_if_true>
    VAR _value_if_false = <value_if_false>
    RETURN
    IF (<logical_test>, _value_if_true, _value_if_false)
    ```

    Note: The two branch expressions are evaluated regardless of the condition expression.

## Examples

See [IF Examples](if-function-dax.md#examples).

## See also

[IF function](if-function-dax.md)  
[Logical functions](logical-functions-dax.md)  
