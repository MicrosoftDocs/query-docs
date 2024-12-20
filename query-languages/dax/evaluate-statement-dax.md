---
description: "Learn more about: EVALUATE"
title: "EVALUATE keyword (DAX)"
---
# EVALUATE

Introduces a statement containing a table expression required in a [DAX query](dax-queries.md).

## Syntax

```dax
EVALUATE <table>
```

## Parameters

|Term|Definition|
|--------|--------------|
|`table`|A table expression|

## Return value

The result of a table expression.

## Remarks

- A DAX query can contain multiple EVALUATE statements.

- To learn more about how EVALUATE statements are used, see [DAX queries](dax-queries.md).

## Example

```dax
EVALUATE
    'Internet Sales'
```

Returns all rows and columns from the Internet Sales table, as a table.

## Related content

[ORDER BY](orderby-statement-dax.md)
[START AT](startat-statement-dax.md)
[DEFINE](define-statement-dax.md)
[VAR](var-dax.md)
[DAX queries](dax-queries.md)
