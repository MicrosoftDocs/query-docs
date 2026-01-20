---
description: "Learn more about: START AT"
title: "START AT keyword (DAX)"
ms.topic: reference
---
# START AT

Introduces a statement that defines the starting value at which the query results of an ORDER BY clause in an EVALUATE statement in a [DAX query](dax-queries.md) are returned.

## Syntax

```dax
[START AT {<value>|<parameter>} [, …]]
```

## Parameters

|Term  |Definition  |
|---------|---------|
|  `value`     |   A constant value. Cannot be an expression.  |
|  `parameter`     |   The name of a parameter in an XMLA statement prefixed with an `@` character.  |

## Remarks

- START AT arguments have a one-to-one correspondence with the columns in the ORDER BY statement. There can be as many arguments in the START AT statement as there are in the ORDER BY statement, but not more. The first argument in the START AT statement defines the starting value in column 1 of the ORDER BY columns. The second argument in the START AT statement defines the starting value in column 2 of the ORDER BY columns within the rows that meet the first value for column 1.

- To learn more about how START AT statements are used, see [DAX queries](dax-queries.md).

## Related content

- [ORDER BY](orderby-statement-dax.md)
- [EVALUATE](evaluate-statement-dax.md)
- [VAR](var-dax.md)
- [DEFINE](define-statement-dax.md)
- [DAX queries](dax-queries.md)
