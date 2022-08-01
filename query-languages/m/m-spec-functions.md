---
title: M Language Functions 
description: Describes using functions in the Power Query M formula language
ms.topic: article
ms.date: 4/7/2020
---


# Functions

A _function_ is a value that represents a mapping from a set of argument values to a single value. A function is invoked by provided a set of input values (the argument values), and produces a single output value (the return value).

## Writing functions

Functions are written using a _function-expression_:

_function-expression:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`(`  _parameter-list<sub>opt</sub>_  `)`  _function-return-type<sub>opt</sub>_  `=>`  _function-body<br/>
function-body:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expression<br/>
parameter-list:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fixed-parameter-list<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fixed-parameter-list_  `,`  _optional-parameter-list<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;optional-parameter-list<br/>
fixed-parameter-list:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;parameter<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;parameter_  `,`  _fixed-parameter-list<br/> 
parameter:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;parameter-name parameter-type<sub>opt</sub><br/>
parameter-name:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier<br/>
parameter-type:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assertion<br/>
function-return-type:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assertion<br/>
assertion:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`as`  _nullable-primiitve-type<br/>
optional-parameter-list:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;optional-parameter<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;optional-parameter_  `,`  _optional-parameter-list<br/>
optional-parameter:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`optional` _parameter<br/>
nullable-primitve-type<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`nullable`_<sub>opt</sub> primitive-type_

The following is an example of a function that requires exactly two values `x` and `y`, and produces the result of applying the `+` operator to those values. The `x` and `y` are _parameters_ that are part of the _formal-parameter-list_ of the function, and the `x + y` is the _function body_:

```
(x, y) => x + y
```

The result of evaluating a _function-expression_ is to produce a function value (not to evaluate the _function-body_). As a convention in this document, function values (as opposed to function expressions) are shown with the _formal-parameter-list_ but with an ellipsis (`...`) instead of the _function-body_. For example, once the function expression above has been evaluated, it would be shown as the following function value:

```
 (x, y) => ...
 ```

The following operators are defined for function values:

| Operator | Result |
| -------- | ------ |
| `x = y` | Equal |
| `x <> y` | Not equal |
| | |

The native type of function values is a custom function type (derived from the intrinsic type `function`) that lists the parameter names and specifies all parameter types and the return type to be `any`. (See [Function types](m-spec-types.md#function-types) for details on function types.)

## Invoking functions

The _function-body_ of a function is executed by _invoking_ the function value using an _invokeexpression_. Invoking a function value means the _function-body_ of the function value is evaluated and a value is returned or an error is raised.

_invoke-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;primary-expression_  `(`  _argument-list<sub>opt</sub>_  `)`<br/>
_argument-list:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expression-list_

Each time a function value is invoked, a set of values are specified as an _argument-list_, called the _arguments_ to the function.

An _argument-list_ is used to specify a fixed number of arguments directly as a list of expressions. The following example defines a record with a function value in a field, and then invokes the function from another field of the record:

```
[ 
    MyFunction = (x, y, z) => x + y + z, 
    Result1 = MyFunction(1, 2, 3)           // 6
]
```

The following holds when invoking a function:

* The environment used to evaluate the _function-body_ of the function includes a variable that corresponds to each parameter, with the same name as the parameter. The value of each parameter corresponds to a value constructed from the _argument-list_ of the _invokeexpression_, as defined in [Parameters](#parameters). 
* All of the expressions corresponding to the function arguments are evaluated before the _function-body_ is evaluated.

* Errors raised when evaluating the expressions in the _expression-list_ or _functionexpression_ are propagated.

* The number of arguments constructed from the _argument-list_ must be compatible with the formal parameters of the function, or an error is raised with reason code `"Expression.Error"`. The process for determining compatibility is defined in [Parameters](#parameters).

## Parameters

There are two kinds of formal parameters that may be present in a _formal-parameter-list_:

* A _required_ parameter indicates that an argument corresponding to the parameter must always be specified when a function is invoked. Required parameters must be specified first in the _formal-parameter-list_. The function in the following example defines required parameters `x` and `y`:

```
    [ 
        MyFunction = (x, y) => x + y, 

        Result1 = MyFunction(1, 1),     // 2 
        Result2 = MyFunction(2, 2)      // 4
    ] 
```

* An _optional_ parameter indicates that an argument corresponding to the parameter may be specified when a function is invoked, but is not required to be specified. If an argument that corresponds to an optional parameter is not specified when the function is invoked, then the value `null` is used instead. Optional parameters must appear after any required parameters in a _formal-parameter-list_. The function in the following example defines a fixed parameter `x` and an optional parameter `y`:

```
    [ 
        MyFunction = fn(x, optional y) =>
                          if (y = null) x else x + y, 
        Result1 = MyFunction(1),        // 1 
        Result2 = MyFunction(1, null),  // 1 
        Result3 = MyFunction(2, 2),     // 4
    ] 
```

The number of arguments that are specified when a function is invoked must be compatible with the formal parameter list. Compatibility of a set of arguments `A` for a function `F` is computed as follows:

* Let the value _N_ represent the number of arguments `A` constructed from the _argumentlist_. For example:

```
    MyFunction()             // N = 0 
    MyFunction(1)            // N = 1 
    MyFunction(null)         // N = 1 
    MyFunction(null, 2)      // N = 2 
    MyFunction(1, 2, 3)      // N = 3 
    MyFunction(1, 2, null)   // N = 3 
    MyFunction(1, 2, {3, 4}) // N = 3
```

* Let the value _Required_ represent the number of fixed parameters of `F` and _Optional_ the number of optional parameters of `F`. For example:

```
()               // Required = 0, Optional = 0 
(x)              // Required = 1, Optional = 0 
(optional x)     // Required = 0, Optional = 1 
(x, optional y)  // Required = 1, Optional = 1
```

* Arguments `A` are compatible with function `F` if the following are true:

   * (_N >= Fixed_) and (_N <= (Fixed + Optional_)) 
   * The argument types are compatible with `F`'s corresponding parameter types

* If the function has a declared return type, then the result value of the body of function `F` is compatible with `F`'s return type if the following is true:

   * The value yielded by evaluating the function body with the supplied arguments for the function parameters has a type that is compatible with the return type.

* If the function body yields a value incompatible with the function's return type, an error with reason code `"Expression.Error"` is raised.

## Recursive functions

In order to write a function value that is recursive, it is necessary to use the scoping operator (`@`) to reference the function within its scope. For example, the following record contains a field that defines the `Factorial` function, and another field that invokes it:

```
[ 
    Factorial = (x) => 
                if x = 0 then 1 else x * @Factorial(x - 1), 
    Result = Factorial(3)  // 6 
]
```

Similarly, mutually recursive functions can be written as long as each function that needs to be accessed has a name. In the following example, part of the `Factorial` function has been refactored into a second `Factorial2` function.

```
[ 
    Factorial = (x) => if x = 0 then 1 else Factorial2(x), 
    Factorial2 = (x) => x * Factorial(x - 1), 
    Result = Factorial(3)     // 6 
]
```

## Closures

A function can return another function as a value. This function can in turn depend on one or more parameters to the original function. In the following example, the function associated with the field `MyFunction` returns a function that returns the parameter specified to it:

```
[ 
    MyFunction = (x) => () => x, 
    MyFunction1 = MyFunction(1), 
    MyFunction2 = MyFunction(2), 
    Result = MyFunction1() + MyFunction2()  // 3 
]
```

Each time the function is invoked, a new function value will be returned that maintains the value of the parameter so that when it is invoked, the parameter value will be returned.

## Functions and environments

In addition to parameters, the _function-body_ of a _function-expression_ can reference variables that are present in the environment when the function is initialized. For example, the function defined by the field `MyFunction` accesses the field `C` of the enclosing record `A`:

```
[ 
A =  
    [ 
        MyFunction = () => C, 
        C = 1 
    ], 
B = A[MyFunction]()           // 1 
]
```

When `MyFunction` is invoked, it accesses the value of the variable `C`, even though it is being invoked from an environment (`B`) that does not contain a variable `C`.

## Simplified declarations

The _each-expression_ is a syntactic shorthand for declaring untyped functions taking a single formal parameter named `_` (underscore).

_each-expression:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`each` _each-expression-body<br/>
each-expression-body:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;function-body_

Simplified declarations are commonly used to improve the readability of higher-order function invocation.

For example, the following pairs of declarations are semantically equivalent:

```
each _ + 1 
(_) => _ + 1  
each [A] 
(_) => _[A] 
 
Table.SelectRows( aTable, each [Weight] > 12 ) 
Table.SelectRows( aTable, (_) => _[Weight] > 12 ) 
```

