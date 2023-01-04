---
title: M Language Error Handling 
description: Describes error handling in the Power Query M formula language
ms.topic: conceptual
ms.date: 8/2/2022
---

# Error Handling

The result of evaluating an M expression produces one of the following outcomes:

* A single value is produced.

* An _error is raised_, indicating the process of evaluating the expression could not produce a value. An error contains a single record value that can be used to provide additional information about what caused the incomplete evaluation.

Errors can be raised from within an expression, and can be handled from within an expression.

## Raising errors

The syntax for raising an error is as follows:

_error-raising-expression:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`error`  _expression_

Text values can be used as shorthand for error values. For example:

```powerquery-m
error "Hello, world" // error with message "Hello, world"
```

Full error values are records and can be constructed using the `Error.Record` function:

```powerquery-m
error Error.Record("FileNotFound", "File my.txt not found",
     "my.txt")
```

The above expression is equivalent to:

```powerquery-m
error [ 
    Reason = "FileNotFound", 
    Message = "File my.txt not found", 
    Detail = "my.txt" 
]
```

Raising an error will cause the current expression evaluation to stop, and the expression evaluation stack will unwind until one of the following occurs:

* A record field, section member, or let variable&mdash;collectively: an _entry_&mdash;is reached. The entry is marked as having an error, the error value is saved with that entry, and then propagated. Any subsequent access to that entry will cause an identical error to be raised. Other entries of the record, section, or let expression are not necessarily affected (unless they access an entry previously marked as having an error).

* The top-level expression is reached. In this case, the result of evaluating the top-level expression is an error instead of a value.

* A `try` expression is reached. In this case, the error is captured and returned as a value.

## Handling errors

An _error-handling-expression_ (informally known as a "`try` expression") is used to handle an error:

_error-handling-expression:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`try` _protected-expression 
error-handler<sub>opt</sub><br/>
protected-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expression<br/>
_error-handler:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;otherwise-clause<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;catch-function<br/>
otherwise-clause:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`otherwise` _default-expression_<br/>
_default-expression_:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_expression_<br/>
_catch-function:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`(`_parameter-name_<sub>opt</sub>`)` `=>` _function-body_<br/>

The following holds when evaluating an _error-handling-expression_ without an _error-handler_:

* If the evaluation of the _protected-expression_ does not result in an error and produces a value x, the value produced by the _error-handling-expression_ is a record of the following form:

```powerquery-m
    [ HasErrors = false, Value = x ]
```

* If the evaluation of the _protected-expression_ raises an error value e, the result of the _error-handling-expression_ is a record of the following form:

```powerquery-m
    [ HasErrors = true, Error = e ]
```

The following holds when evaluating an _error-handling-expression_ with an _error-handler_:

* The _protected-expression_ must be evaluated before the _error-handler_.

* The _error-handler_ must be evaluated if and only if the evaluation of the _protected-expression_ raises an error.

* If the evaluation of the _protected-expression_ raises an error, the value produced by the _error-handling-expression_ is the result of evaluating the _error-handler_.

* Errors raised during the evaluation of the _error-handler_ are propagated.

* When an _error-handler_ is evaluated that is a _catch-function_, the function defined by the _catch-function_ is invoked. If that function accepts a parameter, the error value will be passed as its value. 

The following example illustrates an _error-handling-expression_ in a case where no error is raised:

```powerquery-m
let
    x = try "A"
in
    if x[HasError] then x[Error] else x[Value] 
// "A"
```

The following example shows raising an error and then handling it:

```powerquery-m
let
    x = try error "A" 
in
    if x[HasError] then x[Error] else x[Value] 
// [ Reason = "Expression.Error", Message = "A", Detail = null ]
```

The preceding effect can be achieved with less syntax by using a _catch-function_ that accepts a parameter:
```powerquery-m
let
    x = try error "A" catch (e) => e
in
    x
// [ Reason = "Expression.Error", Message = "A", Detail = null ]
```

An _otherwise-clause_ can be used to replace errors handled by a try expression with an alternative value:

```powerquery-m
try error "A" otherwise 1 
// 1
```

A _catch-function_ that does not accept a parameter is effectively a long-form alternate syntax for an _otherwise-clause_:

```powerquery-m
try error "A" catch () => 1 
// 1
```

If the _error-handler_ also raises an error, then so does the entire try expression:

```powerquery-m
try error "A" otherwise error "B" 
// error with message "B"
```

```powerquery-m
try error "A" catch () => error "B" 
// error with message "B"
```

```powerquery-m
try error "A" catch (e) => error "B" 
// error with message "B"
```



## Errors in record and let initializers

The following example shows a record initializer with a field `A` that raises an error and is accessed by two other fields `B` and `C`. Field `B` does not handle the error that is raised by `A`, but `C` does. The final field `D` does not access `A` and so it is not affected by the error in `A`.

```powerquery-m
[ 
    A = error "A", 
    B = A + 1,
    C = let x =
            try A in
                if not x[HasError] then x[Value]
                else x[Error], 
    D = 1 + 1 
]
```

The result of evaluating the above expression is:

```powerquery-m
[ 
    A = // error with message "A" 
    B = // error with message "A" 
    C = "A", 
    D = 2 
]
```

Error handling in M should be performed close to the cause of errors to deal with the effects of lazy field initialization and deferred closure evaluations. The following example shows an unsuccessful attempt at handling an error using a `try` expression:

```powerquery-m
let
    f = (x) => [ a = error "bad", b = x ],
    g = try f(42) otherwise 123
in 
    g[a]  // error "bad"
```

In this example, the definition `g` was meant to handle the error raised when calling `f`. However, the error is raised by a field initializer that only runs when needed and thus after the record was returned from f and passed through the `try` expression.

## Not implemented error

While an expression is being developed, an author may want to leave out the implementation for some parts of the expression, but may still want to be able to execute the expression. One way to handle this case is to raise an error for the unimplemented parts. For example:

```powerquery-m
(x, y) =>
     if x > y then
         x - y
     else
         error Error.Record("Expression.Error", 
            "Not Implemented")
```

The ellipsis symbol (`...`) can be used as a shortcut for `error`.

_not-implemented-expression:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`...`

For example, the following is equivalent to the previous example:

```powerquery-m
(x, y) => if x > y then x - y else ...
```
