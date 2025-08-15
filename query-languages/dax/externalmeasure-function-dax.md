---
description: "Learn more about: EXTERNALMEASURE"
title: "EXTERNALMEASURE function (DAX)"
---
# EXTERNALMEASURE

[!INCLUDE[applies-to-measures-columns-tables](includes/applies-to-measures-columns-tables.md)]

Invokes a measure defined in a remote model and returns its result with the specified `datatype`.

## Syntax

```dax
EXTERNALMEASURE(<measurename>, <datatype>, <connection>)
ms.custom: AW2020Example
```

### Parameters

|Term|Definition|
|--------|--------------|
|`measurename`|Name of the measure as defined in the remote model.|
|`datatype`|An enumeration that includes: BOOLEAN, CURRENCY, DATETIME, DECIMAL, DOUBLE, INT64, INTEGER, LOGICAL, STRING, TEXT.|
|`connection`|The name of the connection to the remote model.|

## Return value

Result of the remote measure with the datatype specified in `datatype`.

## Remarks

- This function can only be used in [composite models that have a remote model connection](/power-bi/transform-model/desktop-composite-models#composite-models-on-power-bi-semantic-models-and-analysis-services).

## Example

If the remote model connection is called **DirectQuery to AS - Adventure Works DW 2020** and the remote model defines a measure called **Total Sales** you can invoke that measure and return its result as **currency** using:

```
Total Sales Remote = EXTERNALMEASURE("Total Sales", CURRENCY, "DirectQuery to AS - Adventure Works DW 2020")
```

## Related content

[Composite models](/power-bi/transform-model/desktop-composite-models)
