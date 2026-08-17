---
description: "Learn more about: EXCEPT"
title: "EXCEPT function (DAX)"
ms.topic: reference
---
# EXCEPT

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the rows of the first table in the expression which do not appear in the second table.

## Syntax

```dax
EXCEPT(<tableExpression1>, <tableExpression2>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`tableExpression`|Any DAX expression that returns a table.|

## Return value

A table that contains the rows of one table minus all the rows of another table.

## Remarks

- If a row appears at all in both tables, it and its duplicates are not present in the result set. If a row appears in only tableExpression1, it and its duplicates will appear in the result set.

- The column names will match the column names in tableExpression1.

- The returned table has lineage based on the columns in tableExpression1 , regardless of the lineage of the columns in the second table. For example, if the first column of first tableExpression has lineage to the base column C1 in the model, the Except will reduce the rows based on the availability of values in the first column of second tableExpression and keep the lineage on base column C1 intact.

- The two tables must have the same number of columns.

- Columns are compared based on positioning, and data comparison with no type coercion.

- The set of rows returned depends on the order of the two expressions.

- The returned table does not include columns from tables related to tableExpression1.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

States1

|State|
|---------|
|A|
|B|
|B|
|B|
|C|
|D|
|D|

States2

|State|
|---------|
|B|
|C|
|D|
|D|
|D|
|E|
|E|
|E|

Except(States1, States2)

|State|
|---------|
|A|

Except(States2, States1)

|State|
|---------|
|E|
|E|
|E|
