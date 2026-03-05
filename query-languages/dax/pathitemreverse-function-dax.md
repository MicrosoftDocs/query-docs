---
description: "Learn more about: PATHITEMREVERSE"
title: "PATHITEMREVERSE function (DAX)"
ms.topic: reference
---
# PATHITEMREVERSE

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the item at the specified `position` from a string resulting from evaluation of a PATH function. Positions are counted backwards from right to left.

## Syntax

```dax
PATHITEMREVERSE(<path>, <position>[, <type>])
```

### Parameters

|Term|Definition|
|--------|--------------|
|`path`| A text string resulting from evaluation of a PATH function.      |
|`position`|  An integer expression with the position of the item to be returned. Position is counted backwards from right to left.    |
|`type`|  (Optional)An enumeration that defines the data type of the result:  |

#### type enumeration

|Enumeration|Alternate Enumeration|Description|
|-----|-----|-----|
|`TEXT`|0|Results are returned with the data type text. (default).|
|`INTEGER`|1|Results are returned as integers.|

## Return value

The n-position ascendant in the given path, counting from current to the oldest.

## Remarks

- This function can be used to get an individual item from a hierarchy resulting from a PATH function.

- This function reverses the standard order of the hierarchy, so that closest items are listed first, For example, if the PATh function returns a list of managers above an employee in a hierarchy, the PATHITEMREVERSE function returns the employee's immediate manager in position 2 because position 1 contains the employee's id.

- If the number specified for `position` is less than one (1) or greater than the number of elements in `path`, the PATHITEM function  returns BLANK.

- If `type` is not a valid enumeration element an error is returned.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following example takes an employee ID column as the input to a PATH function, and reverses the list of grandparent elements that are returned. The position specified is 3 and the return type is 1; therefore, the PATHITEMREVERSE function returns an integer representing the manager two levels up from the employee.

```dax
= PATHITEMREVERSE(PATH(Employee[EmployeeKey], Employee[ParentEmployeeKey]), 3, 1)
```
