---
title: M Language Let 
description: Describes using the let expression in the Power Query M formula language
ms.topic: language-reference
ms.date: 10/7/2022
ms.custom: "nonautomated-date"
ms.subservice: m-specification
---


# Let

## Let expression

A let expression can be used to capture a value from an intermediate calculation in a variable.

_let-expression:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`let` _variable-list_ `in` _expression<br/>
variable-list:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;variable<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;variable_ `,` _variable-list<br/> 
variable:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;variable-name_ `=` _expression<br/>
variable-name:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier_

The following example shows intermediate results being calculated and stored in variables `x`, `y`, and `z` which are then used in a subsequent calculation `x + y + z`:

```powerquery-m
let     x = 1 + 1,
        y = 2 + 2,
        z = y + 1 
in
        x + y + z
```

The result of this expression is:

```powerquery-m
11  // (1 + 1) + (2 + 2) + (2 + 2 + 1)
```

The following holds when evaluating expressions within the _let-expression_:

* The expressions in the variable list define a new scope containing the identifiers from the _variable-list_ production and must be present when evaluating the expressions within the _variable-list_ productions. Expressions within the _variable-list_ may refer to one-another.

* The expressions within the _variable-list_ must be evaluated before the expression in the _let-expression_ is evaluated.

* Unless the expressions in the _variable-list_ are accessed, they must not be evaluated.

* Errors that are raised during the evaluation of the expressions in the _let-expression_ are propagated.

A let expression can be seen as syntactic sugar over an implicit record expression. The following expression is equivalent to the example above:

```powerquery-m
[     x = 1 + 1,
      y = 2 + 2,
      z = y + 1,
      result = x + y + z 
][result]
```
