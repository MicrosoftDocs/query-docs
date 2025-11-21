---
description: "Learn more about: Errors"
title: "Errors"
ms.date: 10/7/2022
ms.topic: language-reference
ms.custom: "nonautomated-date"
ms.subservice: m-background
---

# Errors

An *error* in Power Query M formula language is an indication that the process of evaluating an expression could not produce a value. Errors are raised by operators and functions encountering **error** conditions or by using the **error** expression. Errors are handled using the **try** expression. When an error is raised, a value is specified that can be used to indicate why the error occurred.

## Try expression

A try expression converts values and errors into a record value that indicates whether the try expression handled an error, or not, and either the proper value or the error record it extracted when handling the error. For example, consider the following expression that raises an error and then handles it right away:

```powerquery-m
try error "negative unit count"
```

This expression evaluates to the following nested record value, explaining the `[HasError], [Error]`, and `[Message]` field lookups in the unit-price example before.

## Error record

```powerquery-m
[
    HasError = true,
    Error =
        [  
            Reason = "Expression.Error",
            Message = "negative unit count",
            Detail = null
        ]
]
```

A common case is to replace errors with default values. The try expression can be used with an optional otherwise clause to achieve just that in a compact form:

```powerquery-m
try error "negative unit count" otherwise 42
// equals 42
```

## Error example

```powerquery-m
let Sales =
        [
        ProductName = "Fishing rod",
            Revenue = 2000,
            Units = 1000,
            UnitPrice = if Units = 0 then error "No Units"
                    else Revenue / Units
        ],

    //Get UnitPrice from Sales record
        textUnitPrice = try Number.ToText(Sales[UnitPrice]),
    Label = "Unit Price: " &
        (if textUnitPrice[HasError] then textUnitPrice[Error][Message]
        //Continue expression flow
            else textUnitPrice[Value])
in
    Label
```

The previous example accesses the `Sales[UnitPrice]` field and formats the value producing the result:

```powerquery-m
"Unit Price: 2"
```

If the Units field had been zero, then the `UnitPrice` field would have raised an error which would have been handled by the try. The resulting value would then have been:

```powerquery-m
"No Units"
```
