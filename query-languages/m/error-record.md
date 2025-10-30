---
description: "Learn more about: Error.Record"
title: "Error.Record"
ms.subservice: m-source
---
# Error.Record

## Syntax

<pre>
Error.Record(
    <b>reason</b> as text,
    optional <b>message</b> as nullable text,
    optional <b>detail</b> as any,
    optional <b>parameters</b> as nullable list,
    optional <b>errorCode</b> as nullable text
) as record
</pre>

## About

Returns an error record from the provided text values for reason, mesage, detail, and error code.

* `reason`: The high-level cause of the error.
* `message`: (Optional) A description of the error.
* `detail`: (Optional) Additional detailed information about the error.
* `parameters`: (Optional) A list of values that provide additional context for the error, typically used for diagnostics or programmatic handling.
* `errorCode`: (Optional) An identifier for the error.

## Example 1

Handle a divide by zero error.

**Usage**

```powerquery-m
let
    input = 100,
    divisor = 0,
    result = try if divisor = 0 then
        error Error.Record(
            "DivideByZero", 
            "You attempted to divide by zero."
        )
    else
        input / divisor
in
    result
```

**Output**

```powerquery-m
[
    HasError = true,
    Error =
    [
        Reason = "DivideByZero",
        Message = "You attempted to divide by zero.",
        Detail = null,
        Message.Format = null,
        Message.Parameters = null,
        ErrorCode = null
    ]
]
````

## Example 2

Create a log entry for a non-existent customer ID error. If no error occurs, create a successful log entry.

**Usage**

```powerquery-m
let
    CustomerId = 12345,

    result = try if CustomerId > 9999 then
        error Error.Record(
            "CustomerNotFound",
            Text.Format("Customer ID #{0} wasn't found.", {CustomerId}),
            "Customer doesn't exist.",
            {
                Text.Format("Invalid ID = #{0}", {CustomerId}),
                "Valid IDs: https://api.contoso.com/customers"
            },
            "ERR404"
        )

    else CustomerId,

    logEntry = if result[HasError] then [
        Level="Error",
        Source="Customer API",
        Reason=result[Error][Reason],
        Message=result[Error][Message],
        Detail=result[Error][Detail],
        Param1=result[Error][Message.Parameters]{0},
        Param2=result[Error][Message.Parameters]{1},
        Code=result[Error][ErrorCode]
        ]

    else [
        Level="Info",
        Source="Customer API",
        Message=Text.Format("Customer ID #{0} is valid.", {result[Value]})
        ]

in
    logEntry
```

**Output**

```powerquery-m
[
    Level = "Error",
    Source = "Customer API",
    Reason = "CustomerNotFound",
    Message = "Customer ID 12345 wasn't found.",
    Detail = "Customer doesn't exist.",
    Param1 = "Invalid ID = 12345",
    Param2 = "Valid IDs: https://api.contoso.com/customers",
    Code = "ERR404"
]
```
