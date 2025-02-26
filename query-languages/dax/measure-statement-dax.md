---
description: "Learn more about: MEASURE"
title: "MEASURE keyword (DAX)"
---
# MEASURE

Introduces a measure definition in a DEFINE statement of a [DAX query](dax-queries.md).

## Syntax

```dax
[DEFINE 
    (
      MEASURE <table name>[<measure name>] = <scalar expression>
    ) + 
]

(EVALUATE <table expression>) +
```

### Parameters

|Term|Definition|
|---------|---------|
|`table name`|   The name of a table containing the measure.  |
|`measure name`|  The name of the measure. It cannot be an expression. The name does not have to be unique. The name exists only for the duration of the query.   |
|`scalar expression`| A DAX expression that returns a scalar value.  |

## Return value

The calculated result of the measure expression.

## Remarks

- Measure definitions for a query override model measures of the same name for the duration of the query. They will not affect the model measure.

- The measure expression can be used with any other expression in the same query.

- To learn more about how MEASURE statements are used, see [DAX queries](dax-queries.md).

## Related content

[DEFINE](define-statement-dax.md)
[EVALUATE](evaluate-statement-dax.md)
[VAR](var-dax.md)
[DAX queries](dax-queries.md)
