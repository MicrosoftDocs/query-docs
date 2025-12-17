---
title: M Language basic concepts 
description: Discusses basic concepts that appear throughout the subsequent sections
ms.topic: language-reference
ms.date: 8/2/2022
ms.custom: nonautomated-date, intro-internal
ms.subservice: m-specification

---

# Basic concepts

This section discusses basic concepts that appear throughout the subsequent sections.

## Values

A single piece of data is called a _value_. Broadly speaking, there are two general categories of values: _primitive values_, which are atomic, and _structured values_, which are constructed out of primitive values and other structured values. For example, the values

```powerquery-m
1 
true
3.14159 
"abc"
```

are primitive in that they are not made up of other values. On the other hand, the values

```powerquery-m
{1, 2, 3} 
[ A = {1}, B = {2}, C = {3} ]
```

are constructed using primitive values and, in the case of the record, other structured values.

## Expressions

An _expression_ is a formula used to construct values. An expression can be formed using a variety of syntactic constructs. The following are some examples of expressions. Each line is a separate expression.

```powerquery-m
"Hello World"             // a text value 
123                       // a number 
1 + 2                     // sum of two numbers 
{1, 2, 3}                 // a list of three numbers 
[ x = 1, y = 2 + 3 ]      // a record containing two fields: 
                          //        x and y 
(x, y) => x + y           // a function that computes a sum 
if 2 > 1 then 2 else 1    // a conditional expression 
let x = 1 + 1  in x * 2   // a let expression 
error "A"                 // error with message "A"
```

The simplest form of expression, as seen above, is a literal representing a value.

More complex expressions are built from other expressions, called _sub-expressions_. For example:

```powerquery-m
1 + 2
```

The above expression is actually composed of three expressions. The `1` and `2` literals are subexpressions of the parent expression `1 + 2`.

Executing the algorithm defined by the syntactic constructs used in an expression is called _evaluating_ the expression. Each kind of expression has rules for how it is evaluated. For example, a literal expression like `1` will produce a constant value, while the expression `a + b` will take the resulting values produced by evaluating two other expressions (`a` and `b`) and add them together according to some set of rules.

## Environments and variables

Expressions are evaluated within a given environment. An _environment_ is a set of named values, called _variables_. Each variable in an environment has a unique name within the environment called an _identifier_.

A top-level (or _root_) expression is evaluated within the _global environment_. The global environment is provided by the expression evaluator instead of being determined from the contents of the expression being evaluated. The contents of the global environment includes the standard library definitions and can be affected by exports from sections from some set of documents. (For simplicity, the examples in this section will assume an empty global environment. That is, it is assumed that there is no standard library and that there are no other section-based definitions.)

The environment used to evaluate a sub-expression is determined by the parent expression. Most parent expression kinds will evaluate a sub-expression within the same environment they were evaluated within, but some will use a different environment. The global environment is the _parent environment_ within which the global expression is evaluated.

For example, the _record-initializer-expression_ evaluates the sub-expression for each field with a modified environment. The modified environment includes a variable for each of the fields of the record, except the one being initialized. Including the other fields of the record allows the fields to depend upon the values of the fields. For example:

```powerquery-m
[  
    x = 1,          // environment: y, z 
    y = 2,          // environment: x, z 
    z = x + y       // environment: x, y
] 
```

Similarly, the _let-expression_ evaluates the sub-expression for each variable with an environment containing each of the variables of the let except the one being initialized. The _let-expression_ evaluates the expression following the in with an environment containing all the variables:

```powerquery-m
let 

    x = 1,          // environment: y, z 
    y = 2,          // environment: x, z 
    z = x + y       // environment: x, y
in
    x + y + z       // environment: x, y, z
```

(It turns out that both _record-initializer-expression_ and _let-expression_ actually define _two_ environments, one of which does include the variable being initialized. This is useful for advanced recursive definitions and is covered in [Identifier references ](#identifier-references).

To form the environments for the sub-expressions, the new variables are "merged" with the variables in the parent environment. The following example shows the environments for nested records:

```powerquery-m
[
    a = 
    [ 

        x = 1,      // environment: b, y, z 
        y = 2,      // environment: b, x, z 
        z = x + y   // environment: b, x, y 
    ], 
    b = 3           // environment: a
]  
```

The following example shows the environments for a record nested within a let:

```powerquery-m
Let
    a =
    [
        x = 1,       // environment: b, y, z 
        y = 2,       // environment: b, x, z 
        z = x + y    // environment: b, x, y 
    ], 
    b = 3            // environment: a 
in 
    a[z] + b         // environment: a, b
```

Merging variables with an environment may introduce a conflict between variables (since each variable in an environment must have a unique name). The conflict is resolved as follows: if the name of a new variable being merged is the same as an existing variable in the parent environment, then the new variable will take precedence in the new environment. In the following example, the inner (more deeply nested) variable `x` will take precedence over the outer variable `x`.

```powerquery-m
[
    a =
    [ 
        x = 1,       // environment: b, x (outer), y, z 
        y = 2,       // environment: b, x (inner), z 
        z = x + y    // environment: b, x (inner), y 
    ], 
    b = 3,           // environment: a, x (outer) 
    x = 4            // environment: a, b
]  

```

### Identifier references

An _identifier-reference_ is used to refer to a variable within an environment.

_identifier-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier-reference<br/> 
identifier-reference:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;exclusive-identifier-reference<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inclusive-identifier-reference_

The simplest form of identifier reference is an _exclusive-identifier-reference_:

_exclusive-identifier-reference:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier_

It is an error for an _exclusive-identifier-reference_ to refer to a variable that is not part of the environment of the expression that the identifier appears within. 

It is an error for an _exclusive-identifier-reference_ to refer to an identifier that is currently being initialized if the referenced identifier is defined inside a _record-initializer-expression_ or _let-expression_. Instead, an _inclusive-identifier-reference_ can be used to gain access to the environment that includes the identifier being initialized. If an _inclusive-identifier-reference_ is used in any other situation, then it is equivalent to an _exclusive-identifier-reference_.

_inclusive-identifier-reference:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`@`  _identifier_

This is useful when defining recursive functions since the name of the function would normally not be in scope.

```powerquery-m
[ 
    Factorial = (n) =>
        if n <= 1 then
            1
        else
            n * @Factorial(n - 1),  // @ is scoping operator

    x = Factorial(5) 
]
```

As with a _record-initializer-expression_, an _inclusive-identifier-reference_ can be used within a _let-expression_ to access the environment that includes the identifier being initialized.

## Order of evaluation

Consider the following expression which initializes a record:

```powerquery-m
[ 
    C = A + B, 
    A = 1 + 1, 
    B = 2 + 2 
]
```

When evaluated, this expression produces the following record value:

```powerquery-m
[ 
    C = 6, 
    A = 2, 
    B = 4 
]
```

The expression states that in order to perform the `A + B` calculation for field `C`, the values of both field `A` and field `B` must be known. This is an example of a _dependency ordering_ of calculations that is provided by an expression. The M evaluator abides by the dependency ordering provided by expressions, but is free to perform the remaining calculations in any order it chooses. For example, the computation order could be:

```powerquery-m
A = 1 + 1 
B = 2 + 2 
C = A + B
```

Or it could be:

```powerquery-m
B = 2 + 2 
A = 1 + 1 
C = A + B
```

Or, since `A` and `B` do not depend on each other, they can be computed concurrently:

&nbsp;&nbsp;&nbsp;&nbsp;`B = 2 + 2`   _concurrently with_   `A = 1 + 1`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;`C = A + B`

## Side effects

Allowing an expression evaluator to automatically compute the order of calculations for cases where there are no explicit dependencies stated by the expression is a simple and powerful computation model.

It does, however, rely on being able to reorder computations. Since expressions can call functions, and those functions could observe state external to the expression by issuing external queries, it is possible to construct a scenario where the order of calculation does matter, but is not captured in the partial order of the expression. For example, a function may read the contents of a file. If that function is called repeatedly, then external changes to that file can be observed and, therefore, reordering can cause observable differences in program behavior. Depending on such observed evaluation ordering for the correctness of an M expression causes a dependency on particular implementation choices that might vary from one evaluator to the next or may even vary on the same evaluator under varying circumstances.

## Immutability

Once a value has been calculated, it is _immutable_, meaning it can no longer be changed. This simplifies the model for evaluating an expression and makes it easier to reason about the result since it is not possible to change a value once it has been used to evaluate a subsequent part of the expression. For instance, a record field is only computed when needed. However, once computed, it remains fixed for the lifetime of the record. Even if the attempt to compute the field raised an error, that same error will be raised again on every attempt to access that record field.

An important exception to the immutable-once-calculated rule applies to list, table, and binary values, which have _streaming semantics_. Streaming semantics allow M to transform data sets that don't fit into memory all at once. With streaming, the values returned when enumerating a given table, list, or binary value are produced on demand each time they're requested. Since the expressions defining the enumerated values are evaluated each time they're enumerated, the output they produce can be different across multiple enumerations. This doesn't mean that multiple enumerations always results in different values, just that they can be different if the data source or M logic being used is non-deterministic.

Also, note that function application is _not_ the same as value construction. Library functions may expose external state (such as the current time or the results of a query against a database that evolves over time), rendering them _non-deterministic_. While functions defined in M will not, as such, expose any such non-deterministic behavior, they can if they are defined to invoke other functions that are non-deterministic.

A final source of non-determinism in M are _errors_. Errors stop evaluations when they occur (up to the level where they are handled by a try expression). It is not normally observable whether `a + b` caused the evaluation of `a` before `b` or `b` before `a` (ignoring concurrency here for simplicity). However, if the subexpression that was evaluated first raises an error, then it can be determined which of the two expressions was evaluated first.
