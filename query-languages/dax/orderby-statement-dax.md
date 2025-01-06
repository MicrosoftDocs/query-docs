---
description: "Learn more about: ORDER BY"
title: "ORDER BY keyword (DAX)"
---
# ORDER BY

Introduces a statement that defines sort order of query results returned by an EVALUATE statement in a [DAX query](dax-queries.md).

## Syntax

```dax
[ORDER BY {<expression> [{ASC | DESC}]}[, …]]
```

### Parameters

|Term|Definition|
|--------|--------------|
|`expression`|Any DAX expression that returns a single scalar value.|
|`ASC`|(default) Ascending sort order.|
|`DESC`|Descending sort order.|

## Return value

The result of an EVALUATE statement in ascending (ASC) or descending (DESC) order.

## Remarks

To learn more about how ORDER BY statements are used, see [DAX queries](dax-queries.md).

## Related content

[START AT](startat-statement-dax.md)
[EVALUATE](evaluate-statement-dax.md)
[VAR](var-dax.md)
[DEFINE](define-statement-dax.md)
[DAX queries](dax-queries.md)