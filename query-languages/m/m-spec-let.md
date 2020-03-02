---
title: M Language Let | Microsoft Docs
description: Use the "create from blank" option to create a custom connector for Power Automate and Power Apps
author: dougklopfenstein

ms.service: powerquery

ms.topic: article
ms.date: 02/28/2020
ms.author: v-douklo
---


# Let

## Let expression

A let expression can be used to capture a value from an intermediate calculation in a variable.

<em>let-expression:</em> `let` <em>variable-list</em> `in`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>expression</em><br/>
<em>variable-list: variable</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>variable , variable-list</em><br/> 
<em>variable: variable-name =</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>expression</em><br/>
<em>variable-name: identifier</em>

The following example shows intermediate results being calculated and stored in variables `x`, `y`, and `z` which are then used in a subsequent calculation `x + y + z`:

```
let     x = 1 + 1,
        y = 2 + 2,     
        z = y + 1 
in      x + y + z
```

The result of this expression is:

```
11  // (1 + 1) + (2 + 2) + (2 + 2 + 1)
```

The following holds when evaluating expressions within the _let-expression_:

* The expressions in the variable list define a new scope containing the identifiers from the _variable-list_ production and must be present when evaluating the expressions within the _variable-list_ productions. Expressions within the _variable-list_ may refer to one-another.

* The expressions within the _variable-list_ must be evaluated before the expression in the _let-expression_ is evaluated.

* Unless the expressions in the _variable-list_ are accessed, they must not be evaluated.

* Errors that are raised during the evaluation of the expressions in the _let-expression_ are propagated.

A let expression can be seen as syntactic sugar over an implicit record expression. The following expression is equivalent to the example above:

```
[     x = 1 + 1,
      y = 2 + 2,
      z = y + 1,
      result = x + y + z ]
[result]
```

