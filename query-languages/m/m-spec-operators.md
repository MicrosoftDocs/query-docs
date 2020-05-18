---
title: M Language Operators | Microsoft Docs
description: Use the "create from blank" option to create a custom connector for Power Automate and Power Apps
author: dougklopfenstein

ms.service: powerquery

ms.topic: article
ms.date: 4/7/2020
ms.author: v-douklo
---

# Operators

This section defines the behavior of the various M operators.

## Operator precedence

When an expression contains multiple operators, the _precedence_ of the operators controls the order in which the individual operators are evaluated. For example, the expression `x + y * z` is evaluated as `x + (y * z)` because the `*` operator has higher precedence than the binary `+` operator. The precedence of an operator is established by the definition of its associated grammar production. For example, an _additive-expression_ consists of a sequence of _multiplicative-expression's_ separated by `+` or `-` operators, thus giving the `+` and `-` operators lower precedence than the `*` and `/` operators.

The _parenthesized-expression_ production can be used to change the default precedence ordering.

_parenthesized-expression:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`(`  _expression_  `)`

For example:

```
1 + 2 * 3       // 7 
(1 + 2) * 3     // 9
```

The following table summarizes the M operators, listing the operator categories in order of precedence from highest to lowest. Operators in the same category have equal precedence.

<table>
    <tr>
        <th align="left">Category</th>
        <th align="left">Expression</th>
        <th align="left">Description</th>
    </tr>
    <tr>
        <td rowspan="8" valign="top">Primary</td>
        <td><em>i</em><br/>@<em>i</em></td>
        <td valign="top">Identifier expression</td>
    </tr>
    <tr>
        <td>(<em>x</em>)</td>
        <td>Parenthesized expression</td>
    </tr>
    <tr>
        <td><em>x</em>[<em>i</em>]</td>
        <td>Lookup</td>
    </tr>
    <tr>
        <td><em>x</em>{<em>y</em>}</td>
        <td>Item access</td>
    </tr>
    <tr>
        <td><em>x</em>(<em>...</em>)</td>
        <td>Function invocation</td>
    </tr>
    <tr>
        <td>{<em>x</em>, <em>y</em>, <em>...</em>}</td>
        <td>List initialization</td>
    </tr>
    <tr>
        <td>[ <em>i</em> = <em>x</em>, <em>...</em> ]</td>
        <td>Record initialization</td>
    </tr>
    <tr>
        <td><em>...</em></td>
        <td>Not implemented</td>
    </tr>
    <tr>
        <td rowspan="3" valign="top">Unary</td>
        <td>+<em>x</em></td>
        <td>Identity</td>
    </tr>
    <tr>
        <td>-<em>x</em></td>
        <td>Negation</td>
    </tr>
    <tr>
        <td><code>not</code> <em>x</em></td>
        <td>Logical negation</td>
    </tr>
    <tr>
        <td>Metadata</td>
        <td><em>x</em> <code>meta</code> <em>y</em></td>
        <td>Associate metadata</td>
    </tr>
    <tr>
        <td rowspan="2" valign="top">Multiplicative</td>
        <td><em>x</em> * <em>y</em></td>
        <td>Multiplication</td>
    </tr>
    <tr>
        <td><em>x</em> / <em>y</em></td>
        <td>Division</td>
    </tr>
    <tr>
        <td rowspan="2" valign="top">Additive</td>
        <td><em>x</em> + <em>y</em></td>
        <td>Addition</td>
    </tr>
    <tr>
        <td><em>x</em> - <em>y</em></td>
        <td>Subtraction</td>
    </tr>
    <tr>
        <td rowspan="4" valign="top">Relational</td>
        <td><em>x</em> < <em>y</em></td>
        <td>Less than</td>
    </tr>
    <tr>
        <td><em>x</em> > <em>y</em></td>
        <td>Greater than</td>
    </tr>
    <tr>
        <td><em>x</em> <= <em>y</em></td>
        <td>Less than or equal</td>
    </tr>
    <tr>
        <td><em>x</em> >= <em>y</em></td>
        <td>Greater than or equal</td>
    </tr>
    <tr>
        <td rospan="2" valign="top">Equality</td>
        <td><em>x</em> = <em>y</em></td>
        <td>Equal</td>
    </tr>
    <tr>
        <td></td>
        <td><em>x</em> <> <em>y</em></td>
        <td>Not equal</td>
    </tr>
    <tr>
        <td>Type assertion</td>
        <td><em>x</em> <code>as</code> <em>y</em></td>
        <td>Is compatible nullable-primitive type or error</td>
    </tr>
    <tr>
        <td>Type conformance</td>
        <td><em>x</em> <code>is</code> <em>y</em></td>
        <td>Test if compatible nullable-primitive type</td>
    </tr>
    <tr>
        <td>Logical AND</td>
        <td><em>x</em> <code>and</code> <em>y</em></td>
        <td>Short-circuiting conjunction</td>
    </tr>
    <tr>
        <td>Logical OR</td>
        <td><em>x</em> <code>or</code> <em>y</em></td>
        <td>Short-circuiting disjunction</td>
    </tr>
</table>

## Operators and metadata

Every value has an associated record value that can carry additional information about the value. This record is referred to as the _metadata record_ for a value. A metadata record can be associated with any kind of value, even `null`. The result of such an association is a new value with the given metadata.

A metadata record is just a regular record and can contain any fields and values that a regular record can, and itself has a metadata record. Associating a metadata record with a value is "non-intrusive". It does not change the value's behavior in evaluations except for those that explicitly inspect metadata records.

Every value has a default metadata record, even if one has not been specified. The default metadata record is empty. The following examples show accessing the metadata record of a text value using the `Value.Metadata` standard library function:

```
Value.Metadata( "Mozart" )   // []
```

Metadata records are generally _not preserved_ when a value is used with an operator or function that constructs a new value. For example, if two text values are concatenated using the `&` operator, the metadata of the resulting text value is the empty record `[]`. The following expressions are equivalent:

```
"Amadeus " & ("Mozart" meta [ Rating = 5 ])  
"Amadeus " & "Mozart"
```

The standard library functions `Value.RemoveMetadata` and `Value.ReplaceMetadata` can be used to remove all metadata from a value and to replace a value's metadata (rather than merge metadata into possibly existing metadata).

The only operator that returns results that carry metadata is the [meta operator](#metadata-operator).

## Structurally recursive operators

Values can be _cyclic_. For example:

```
let l = {0, @l} in l
// {0, {0, {0, ... }}}
[A={B}, B={A}]
// [A = {{ ... }}, B = {{ ... }}]
```

M handles cyclic values by keeping construction of records, lists, and tables lazy. An attempt to construct a cyclic value that does not benefit from interjected lazy structured values yields an error:

```
[A=B, B=A] 
// [A = Error.Record("Expression.Error", 
//         "A cyclic reference was encountered during evaluation"), 
//  B = Error.Record("Expression.Error", 
//         "A cyclic reference was encountered during evaluation"), 
// ]
```

Some operators in M are defined by structural recursion. For instance, equality of records and lists is defined by the conjoined equality of corresponding record fields and item lists, respectively.

For non-cyclic values, applying structural recursion yields a _finite expansion_ of the value: shared nested values will be traversed repeatedly, but the process of recursion always terminates.

A cyclic value has an _infinite expansion_ when applying structural recursion. The semantics of M makes no special accommodations for such infinite expansions&mdash;an attempt to compare cyclic values for equality, for instance, will typically run out of resources and terminate exceptionally.

## Selection and Projection Operators

The selection and projection operators allow data to be extracted from list and record values.

### Item Access

A value may be selected from a list or table based on its zero-based position within that list or table using an _item-access-expression_.

_item-access-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;item-selection<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;optional-item-selection<br/>
item-selection:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;primary-expression_  `{`  _item-selector_  `}`<br/>
_optional-item-selection:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;primary-expression_ `{`  _item-selector_  `} ?`<br/>
_item-selector:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expression_

The _item-access-expression_ `x{y}` returns:

* For a list `x` and a number `y`, the item of list `x` at position `y`. The first item of a list is considered to have an ordinal index of zero. If the requested position does not exist in the list, an error is raised.

* For a table `x` and a number `y`, the row of table `x` at position `y`. The first row of a table is considered to have an ordinal index of zero. If the requested position does not exist in the table, an error is raised.

* For a table `x` and a record `y`, the row of table `x` that matches the field values of record `y` for fields with field names that match corresponding table-column names. If there is no unique matching row in the table, an error is raised.

For example:

```
{"a","b","c"}{0}                        // "a" 
{1, [A=2], 3}{1}                        // [A=2] 
{true, false}{2}                        // error 
#table({"A","B"},{{0,1},{2,1}}){0}      // [A=0,B=1] 
#table({"A","B"},{{0,1},{2,1}}){[A=2]}  // [A=2,B=1]  
#table({"A","B"},{{0,1},{2,1}}){[B=3]}  // error 
#table({"A","B"},{{0,1},{2,1}}){[B=1]}  // error
```

The _item-access-expression_ also supports the form `x{y}?`, which returns `null` when position (or match) `y` does not exist in list or table `x`. If there are multiple matches for `y`, an error is still raised.

For example:

```
{"a","b","c"}{0}?                       // "a" 
{1, [A=2], 3}{1}?                       // [A=2] 
{true, false}{2}?                       // null 
#table({"A","B"},{{0,1},{2,1}}){0}      // [A=0,B=1] 
#table({"A","B"},{{0,1},{2,1}}){[A=2]}  // [A=2,B=1]  
#table({"A","B"},{{0,1},{2,1}}){[B=3]}  // null 
#table({"A","B"},{{0,1},{2,1}}){[B=1]}  // error
```

Item access does not force the evaluation of list or table items other than the one being accessed. For example:

```
{ error "a", 1, error "c"}{1}  // 1 
{ error "a", error "b"}{1}     // error "b"
```

The following holds when the item access operator `x{y}` is evaluated:

* Errors raised during the evaluation of expressions `x` or `y` are propagated.

* The expression `x` produces a list or a table value.

* The expression `y` produces a number value or, if `x` produces a table value, a record value.

* If `y` produces a number value and the value of `y` is negative, an error with reason code `"Expression.Error"` is raised.

* If `y` produces a number value and the value of `y` is greater than or equal to the count of `x`, an error with reason code `"Expression.Error"` is raised unless the optional operator form `x{y}?` is used, in which case the value `null` is returned.

* If `x` produces a table value and `y` produces a record value and there are no matches for `y` in `x`, an error with reason code `"Expression.Error"` is raised unless the optional operator form `x{y}?` is used, in which case the value `null` is returned.

* If `x` produces a table value and `y` produces a record value and there are multiple matches for `y` in `x`, an error with reason code `"Expression.Error"` is raised.

No items in `x` other than that at position `y` is evaluated during the process of item selection. (For streaming lists or tables, the items or rows preceding that at position `y` are skipped over, which may cause their evaluation, depending on the source of the list or table.)

### Field Access

The _field-access-expression_ is used to _select_ a value from a record or to _project_ a record or table to one with fewer fields or columns, respectively.

_field-access-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;field-selection<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;implicit-target-field-selection<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;projection<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;implicit-target-projection<br/> 
field-selection:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;primary-expression field-selector<br/>
field-selector:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;required-field-selector<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;optional-field-selector<br/>
required-field-selector:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[`   _field-name_  `]`<br/>
_optional-field-selector:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[`   _field-name_  `] ?`<br/>
_field-name:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;generalized-identifier<br/>
implicit-target-field-selection:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;field-selector<br/> 
projection:<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;primary-expression required-projection<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;primary-expression optional-projection<br/>
required-projection:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[` _required-selector-list_ `]`<br/>
_optional-projection:_<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[` _required-selector-list_ `] ?`<br/> _required-selector-list:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;required-field-selector<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;required-selector-list_ `,` _required-field-selector<br/> 
implicit-target -projection:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;projection_

The simplest form of field access is _required field selection_. It uses the operator `x[y]` to look up a field in a record by field name. If the field `y` does not exist in `x`, an error is raised. The form `x[y]?` is used to perform _optional_ field selection, and returns `null` if the requested field does not exist in the record.

For example:

```
[A=1,B=2][B]       // 2 
[A=1,B=2][C]       // error 
[A=1,B=2][C]?      // null
```

Collective access of multiple fields is supported by the operators for _required record projection_ and _optional record projection_. The operator `x[[y1],[y2],...]` projects the record to a new record with fewer fields (selected by `y1`, `y2`, `...`). If a selected field does not exist, an error is raised. The operator `x[[y1],[y2],...]` projects the record to a new record with the fields selected by `y1`, `y2`, `...`; if a field is missing, `null` is used instead. 
For example:

```
[A=1,B=2][[B]]           // [B=2] 
[A=1,B=2][[C]]           // error 
[A=1,B=2][[B],[C]]?      // [B=2,C=null]
```

The forms `[y]` and `[y]?` are supported as a _shorthand_ reference to the identifier `_` (underscore). The following two expressions are equivalent:

```
[A]                 
_[A]
```

The following example illustrates the shorthand form of field access:

```
let _ = [A=1,B=2] in [A] //1
```

The form `[[y1],[y2],...]` and `[[y1],[y2],...]?` are also supported as a shorthand and the following two expressions are likewise equivalent:

```
[[A],[B]]                 
_[[A],[B]]
```

The shorthand form is particularly useful in combination with the `each` shorthand, a way to introduce a function of a single parameter named `_` (for details, see [Simplified declarations](m-spec-functions.md#simplified-declarations). Together, the two shorthands simplify common higher-order functional expressions:

```
List.Select( {[a=1, b=1], [a=2, b=4]}, each [a] = [b]) 
// {[a=1, b=1]}
```

The above expression is equivalent to the following more cryptic looking longhand:

```
List.Select( {[a=1, b=1], [a=2, b=4]}, (_) => _[a] = _[b]) 
// {[a=1, b=1]}
```

Field access does not force the evaluation of fields other than the one(s) being accessed. For example:

```
[A=error "a", B=1, C=error "c"][B]  // 1 
[A=error "a", B=error "b"][B]       // error "b"
```
The following holds when a field access operator `x[y]`, `x[y]?`, `x[[y]]`, or `x[[y]]?` is evaluated:

* Errors raised during the evaluation of expression `x` are propagated.

* Errors raised when evaluating field `y` are permanently associated with field `y`, then propagated. Any future access to field `y` will raise the identical error.

* The expression `x` produces a record or table value, or an error is raised.

* If the identifier `y` names a field that does not exist in `x`, an error with reason code `"Expression.Error"` is raised unless the optional operator form `...?` is used, in which case the value `null` is returned.

No fields of `x` other than that named by `y` is evaluated during the process of field access.

## Metadata operator

The metadata record for a value is amended using the _meta operator_ (`x meta y`).

_metadata-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unary-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unary-expression_  `meta`  _unary-expression_

The following example constructs a text value with a metadata record using the `meta` operator and then accesses the metadata record of the resulting value using `Value.Metadata`:

```
Value.Metadata( "Mozart" meta [ Rating = 5 ] ) 
// [Rating = 5 ]
Value.Metadata( "Mozart" meta [ Rating = 5 ] )[Rating] 
// 5
```

The following holds when applying the metadata combining operator `x meta y`:

* Errors raised when evaluating the `x` or `y` expressions are propagated.

* The `y` expression must be a record, or an error with reason code `"Expression.Error"` is raised.

* The resulting metadata record is `x`'s metadata record merged with `y`. (For the semantics of record merge, see [Record merge](#record-merge).)

* The resulting value is the value from the `x` expression, without its metadata, with the newly computed metadata record attached.

The standard library functions `Value.RemoveMetadata` and `Value.ReplaceMetadata` can be used to remove all metadata from a value and to replace a value's metadata (rather than merge metadata into possibly existing metadata). The following expressions are equivalent:

```
x meta y  
Value.ReplaceMetadata(x, Value.Metadata(x) & y) 
Value.RemoveMetadata(x) meta (Value.Metadata(x) & y)
```

## Equality operators

The _equality operator_ `=` is used to determine if two values are the equal. The _inequality operator_ `<>` is used to determine if two values are not equal.

_equality-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;relational-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;relational-expression_  `=`  _equality-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;relational-expression_  `<>`  _equality-expression_

For example:

```
1 = 1            // true 
1 = 2            // false 
1 <> 1           // false 
1 <> 2           // true 
null = true      // false 
null = null      // true
```

Metadata is not part of equality or inequality comparison. For example:

```
(1 meta [ a = 1 ]) = (1 meta [ a = 2 ]) // true 
(1 meta [ a = 1 ]) = 1                  // true
```

The following holds when applying the equality operators `x = y` and `x <> y`:

* Errors raised when evaluating the `x` or `y` expressions are propagated.

* The `=`  operator has a result of `true` if the values are equal, and `false` otherwise.

* The `<>` operator has a result of `false` if the values are equal, and `true` otherwise.

* Metadata records are not included in the comparison.

* If values produced by evaluating the `x` and `y` expressions are not the same kind of value, then the values are not equal.

* If the values produced by evaluating the `x` and `y` expression are the same kind of value, then there are specific rules for determining if they are equal, as defined below.

* The following is always true:

```
    (x = y) = not (x <> y)
```

The equality operators are defined for the following types:

* The `null` value is only equal to itself.

```
    null = null    // true 
    null = true    // false 
    null = false   // false
```

* The logical values `true` and `false` are only equal to themselves. For example:

```
    true = true      // true 
    false = false    // true 
    true = false     // false 
    true = 1         // false
```  
* Numbers are compared using the specified precision:

   * If either number is `#nan`, then the numbers are not the same.

   * When neither number is `#nan`, then the numbers are compared using a bit-wise comparison of the numeric value.

   * `#nan` is the only value that is not equal to itself.

       For example:

```
        1 = 1,              // true 
        1.0 = 1             // true 
        2 = 1               // false 
        #nan = #nan         // false 
        #nan <> #nan        // true
```

* Two durations are equal if they represent the same number of 100-nanosecond ticks.

* Two times are equal if the magnitudes of their parts (hour, minute, second) are equal.

* Two dates are equal if the magnitudes of their parts (year, month, day) are equal.

* Two datetimes are equal if the magnitudes of their parts (year, month, day, hour, minute, second) are equal.

* Two datetimezones are equal if the corresponding UTC datetimes are equal. To arrive at the corresponding UTC datetime, the hours/minutes offset is subtracted from the datetime component of the datetimezone.

* Two text values are equal if using an ordinal, case-sensitive, culture-insensitive comparison they have the same length and equal characters at corresponding positions.

* Two list values are equal if all of the following are true:

   * Both lists contain the same number of items.

   * The values of each positionally corresponding item in the lists are equal. This means that not only do the lists need to contain equal items, the items need to be in the same order.

      For example:

```
        {1, 2} = {1, 2}     // true 
        {2, 1} = {1, 2}     // false 
        {1, 2, 3} = {1, 2}  // false
``` 
* Two records are equal if all of the following are true:

   * The number of fields is the same.

   * Each field name of one record is also present in the other record.

   * The value of each field of one record is equal to the like-named field in the other record.

      For example:

```
        [ A = 1, B = 2 ] = [ A = 1, B = 2 ]        // true 
        [ B = 2, A = 1 ] = [ A = 1, B = 2 ]        // true 
        [ A = 1, B = 2, C = 3 ] = [ A = 1, B = 2 ] // false 
        [ A = 1 ] = [ A = 1, B = 2 ]               // false
```

* Two tables are equal if all of the following are true:

   * The number of columns is the same.

   * Each column name in one table is also present in the other table.

   * The number of rows is the same.

   * Each row has equal values in corresponding cells.

      For example:

```
        #table({"A","B"},{{1,2}}) = #table({"A","B"},{{1,2}}) // true 
        #table({"A","B"},{{1,2}}) = #table({"X","Y"},{{1,2}}) // false 
        #table({"A","B"},{{1,2}}) = #table({"B","A"},{{2,1}}) // true
```
* A function value is equal to itself, but may or may not be equal to another function value. If two function values are considered equal, then they will behave identically when invoked.

   Two given function values will always have the same equality relationship.

* A type value is equal to itself, but may or may not be equal to another type value. If two type values are considered equal, then they will behave identically when queried for conformance.

   Two given type values will always have the same equality relationship.

## Relational operators

The `<`, `>`, `<=`, and `>=` operators are called the _relational operators_.

_relational-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additive-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additive-expression_  `<`  _relational-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additive-expression_  `>`  _relational-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additive-expression_  `<=`  _relational-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additive-expression  `>=`  _relational-expression_

These operators are used to determine the relative ordering relationship between two values, as shown in the following table:

| Operation | Result |
| --------- | ------ |
| `x < y` | `true` if `x` is less than `y`, `false` otherwise |
| `x > y` | `true` if `x` is greater than `y`, `false` otherwise |
| `x <= y` | `true` if `x` is less than or equal to `y`, `false` otherwise |
| `x >= y` | `true` if `x` is greater than or equal to `y`, `false` otherwise |
| | |
 
For example:

```
0 <= 1            // true 
null < 1          // null 
null <= null      // null 
"ab" < "abc"      // true 
#nan >= #nan      // false  
#nan <= #nan      // false
```

The following holds when evaluating an expression containing the relational operators:

* Errors raised when evaluating the `x` or `y` operand expressions are propagated.

* The values produced by evaluating both the `x` and `y` expressions must be a number, date, datetime, datetimezone, duration, logical, null or time value. Otherwise, an error with reason code `"Expression.Error"` is raised.

* If either or both operands are `null`, the result is the `null` value.

* If both operands are logical, the value `true` is considered to be greater than `false`.

* If both operands are durations, then the values are compared according to the total number of 100-nanosecond ticks they represent.

* Two times are compared by comparing their hour parts and, if equal, their minute parts and, if equal, their second parts.

* Two dates are compared by comparing their year parts and, if equal, their month parts and, if equal, their day parts.

* Two datetimes are compared by comparing their year parts and, if equal, their month parts and, if equal, their day parts and, if equal, their hour parts and, if equal, their minute parts and, if equal, their second parts.

* Two datetimezones are compared by normalizing them to UTC by subtracting their hour/minute offset and then comparing their datetime components.

* Two numbers `x` and `y` are compared according to the rules of the IEEE 754 standard:

   * If either operand is `#nan`, the result is `false` for all relational operators.
   * When neither operand is `#nan`, the operators compare the values of the two floatingpoint operands with respect to the ordering


        <code>-&#8734; < -max < ... < -min < -0.0 = +0.0 < +min < ... < +max < +&#8734;</code>

      where min and max are the smallest and largest positive finite values that can be represented. The M names for <code>-&#8734;</code> and <code>+&#8734;</code> are `-#infinity` and `#infinity`.

    Notable effects of this ordering are:

    * Negative and positive zeros are considered equal.

    * A `-#infinity` value is considered less than all other number values, but equal to another `-#infinity`.

    * A `#infinity` value is considered greater than all other number values, but equal to another `#infinity`.

## Conditional logical operators

The `and` and `or` operators are called the conditional logical operators.

_logical-or-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logical-and-expression</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logical-and-expression_  `or`  _logical-or-expression<br/>
logical-and-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;is-expression<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;is-expression_  `and`  _logical-and-expression_

The `or` operator returns `true` when at least one of its operands is `true`. The right operand is evaluated if and only if the left operand is not `true`.

The `and` operator returns `false` when at least one of its operands is `false`. The right operand is evaluated if and only if the left operand is not `false`.

Truth tables for the `or` and `and` operators are shown below, with the result of evaluating the left operand expression on the vertical axis and the result of evaluating the right operand expression on the horizontal axis.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| <b>`and`</b> | `true` | `false` | `null` | `error` |
| `true` | `true` | `false` | `null` | `error` |
| `false` | `false` | `false` | `false` | `false` |
| `null` | `null` | `false` | `null` | `error` |
| `error` | `error` | `error` | `error` | `error` |
| | | | | |

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| <b>`or`</b> | `true` | `false` | `null` | `error` |
| `true` | `true` | `true` | `true` | `true` |
| `false` | `true` | `false` | `null` | `error` |
| `null` | `true` | `null` | `null` | `error` |
| `error ` | `error ` | `error` | `error` | `error` |
| | | | | |
 
The following holds when evaluating an expression containing conditional logical operators:

* Errors raised when evaluating the `x` or `y` expressions are propagated.

* The conditional logical operators are defined over the types `logical` and `null`. If the operand values are not of those types, an error with reason code `"Expression.Error"` is raised.

* The result is a logical value.

* In the expression `x` or `y`, the expression `y` will be evaluated if and only if `x` does not evaluate to `true`.

* In the expression `x` and `y`, the expression `y` will be evaluated if and only if `x` does not evaluate to `false`.

The last two properties give the conditional logical operators their "conditional" qualification; properties also referred to as "short-circuiting". These properties are useful to write compact _guarded predicates_. For example, the following expressions are equivalent:

```
d <> 0 and n/d > 1 if d <> 0 then n/d > 1 else false
```

## Arithmetic Operators

The `+`, `-`, `*` and `/` operators are the _arithmetic operators_.

_additive-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplicative-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additive-expression_  `+`  _multiplicative-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additive-expression_  `-`  _multiplicative-expression<br/>
multiplicative-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;metadata- expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplicative-expression_  `*`  _metadata-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplicative-expression_  `/`  _metadata-expression_

### Precision

Numbers in M are stored using a variety of representations to retain as much information as possible about numbers coming from a variety of sources. Numbers are only converted from one representation to another as needed by operators applied to them. Two precisions are supported in M:

| Precision | Semantics |
| --------- | --------- |
| `Precision.Decimal` | 128-bit decimal representation with a range of &#177;1.0 x 10-28 to &#177;7.9 x 1028 and 28-29 significant digits. |
| `Precision.Double` | Scientific representation using mantissa and exponent; conforms to the 64-bit binary double-precision IEEE 754 arithmetic standard [IEEE 754-2008](https://ieeexplore.ieee.org/servlet/opac?punumber=4610933). |
| | |

Arithmetic operations are performed by choosing a precision, converting both operands to that precision (if necessary), then performing the actual operation, and finally returning a number in the chosen precision.

The built-in arithmetic operators (`+`, `-`, `*`, `/`) use Double Precision. Standard library functions (`Value.Add`, `Value.Subtract`, `Value.Multiply`, `Value.Divide`) can be used to request these operations using a specific precision model.

* No numeric overflow is possible: `#infinity` or `-#infinity` represent values of magnitudes too large to be represented.

* No numeric underflow is possible: `0` and `-0` represent values of magnitudes too small to be represented.

* The IEEE 754 special value `#nan` (NaN&mdash;Not a Number) is used to cover arithmetically invalid cases, such as a division of zero by zero.

* Conversion from Decimal to Double precision is performed by rounding decimal numbers to the nearest equivalent double value.

* Conversion from Double to Decimal precision is performed by rounding double numbers to the nearest equivalent decimal value and, if necessary, overflowing to `#infinity` or `-#infinity` values.

### Addition operator

The interpretation of the addition operator (`x + y`) is dependent on the kind of value of the evaluated expressions x and y, as follows:

| x | y | Result | Interpretation |
| --- | --- | --- | --- |
| `type number` | `type number` | `type number` | Numeric sum |
| `type number` | `null` | `null` | |
| `null` | `type number` | `null` | |
| `type duration` | `type duration` | `type duration` | Numeric sum of magnitudes |
| `type duration` | `null` | `null` | |
| `null` | `type duration` | `null` | |
| `type` _datetime_ | `type duration` | `type` _datetime_ | Datetime offset by duration |
| `type duration` | `type` _datetime_ | `type` _datetime_ | |
| `type` _datetime_ | `null` | `null` | |
| `null` | `type` _datetime_ | `null` | |
| | | | |

In the table, `type` _datetime_ stands for any of `type date`, `type datetime`, `type datetimezone`, or `type time`. When adding a duration and a value of some type _datetime_, the resulting value is of that same type.

For other combinations of values than those listed in the table, an error with reason code `"Expression.Error"` is raised. Each combination is covered in the following sections.

Errors raised when evaluating either operand are propagated.

#### Numeric sum

The sum of two numbers is computed using the _addition operator_, producing a number.

For example:

```
1 + 1             // 2 
#nan + #infinity  // #nan
```

The addition operator `+` over numbers uses Double Precision; the standard library function `Value.Add` can be used to specify Decimal Precision. The following holds when computing a sum of numbers:

* The sum in Double Precision is computed according to the rules of 64-bit binary doubleprecision IEEE 754 arithmetic [IEEE 754-2008](https://ieeexplore.ieee.org/servlet/opac?punumber=4610933). The following table lists the results of all possible combinations of nonzero finite values, zeros, infinities, and NaN's. In the table, `x` and `y` are nonzero finite values, and `z` is the result of `x + y`. If `x` and `y` have the same magnitude but opposite signs, `z` is positive zero. If `x + y` is too large to be represented in the destination type, `z` is an infinity with the same sign as `x + y`. 
 
   | + | y | +0 | -0 | +&#8734; | -&#8734; | NaN |
   | --- | --- | --- | --- | --- | --- | --- |
   | <b>x</b> | z | x | x | +&#8734; | -&#8734; | NaN |
   | <b>+0</b> | y | +0 | +0 | +&#8734; | -&#8734; | NaN |
   | <b>-0</b> | y | +0 | -0 | +&#8734; | -&#8734; | NaN |
   | <b>+&#8734;</b> | +&#8734; | +&#8734; | +&#8734; | +&#8734; | NaN | NaN |
   | <b>-&#8734;</b> | -&#8734; | -&#8734; | -&#8734; | NaN | -&#8734; | NaN |
   | <b>NaN</b> | NaN | NaN | NaN | NaN | NaN | NaN |
   | | | | | | | |

* The sum in Decimal Precision is computed without losing precision. The scale of the result is the larger of the scales of the two operands.

#### Sum of durations

The sum of two durations is the duration representing the sum of the number of 100nanosecond ticks represented by the durations. For example:

```
#duration(2,1,0,15.1) + #duration(0,1,30,45.3) 
// #duration(2, 2, 31, 0.4)
```

#### Datetime offset by duration

A _datetime_ `x` and a duration `y` may be added using `x + y` to compute a new _datetime_ whose distance from `x` on a linear timeline is exactly the magnitude of `y`. Here, _datetime_ stands for any of `Date`, `DateTime`, `DateTimeZone`, or `Time` and a non-null result will be of the same type. The datetime offset by duration may be computed as follows:

* If the datetime's days since epoch value is specified, construct a new datetime with the following information elements:

   * Calculate a new days since epoch equivalent to dividing the magnitude of y by the number of 100-nanosecond ticks in a 24-hour period, truncating the decimal portion of the result, and adding this value to the x's days since epoch.

   * Calculate a new ticks since midnight equivalent to adding the magnitude of y to the x's ticks since midnight, modulo the number of 100-nanosecond ticks in a 24-hour period. If x does not specify a value for ticks since midnight, a value of 0 is assumed.

   * Copy x's value for minutes offset from UTC unchanged.

* If the datetime's days since epoch value is unspecified, construct a new datetime with the following information elements specified:

   * Calculate a new ticks since midnight equivalent to adding the magnitude of y to the x's ticks since midnight, modulo the number of 100-nanosecond ticks in a 24-hour period. If x does not specify a value for ticks since midnight, a value of 0 is assumed.

   * Copy x's values for days since epoch and minutes offset from UTC unchanged.

The following examples show calculating the absolute temporal sum when the datetime specifies the _days since epoch_:

```
#date(2010,05,20) + #duration(0,8,0,0) 
    //#datetime( 2010, 5, 20, 8, 0, 0 ) 
    //2010-05-20T08:00:00 
 
#date(2010,01,31) + #duration(30,08,0,0) 
    //#datetime(2010, 3, 2, 8, 0, 0) 
    //2010-03-02T08:00:00 
 
#datetime(2010,05,20,12,00,00,-08) + #duration(0,04,30,00) 
    //#datetime(2010, 5, 20, 16, 30, 0, -8, 0) 
    //2010-05-20T16:30:00-08:00 
 
#datetime(2010,10,10,0,0,0,0) + #duration(1,0,0,0) 
   //#datetime(2010, 10, 11, 0, 0, 0, 0, 0) 
   //2010-10-11T00:00:00+00:00
```

The following example shows calculating the datetime offset by duration for a given time:

```
#time(8,0,0) + #duration(30,5,0,0) 
   //#time(13, 0, 0) 
   //13:00:00
```

### Subtraction operator

The interpretation of the subtraction operator (`x - y`) is dependent on the kind of the value of the evaluated expressions `x` and `y`, as follows:

| x | Y | Result | Interpretation |
| --- | --- | --- | --- |
| `type number` | `type number` | `type number` | Numeric difference |
| `type number` | `null` | `null` | |
| `null` | `type number` | `null` | |
| `type duration` | `type duration` | `type duration` | Numeric difference of magnitudes |
| `type duration` | `null` | `null` | |
| `null` | `type duration` | `null` | |
| `type` _datetime_ | `type` _datetime_ | `type duration` | Duration between datetimes |
| `type` _datetime_ | `type duration` | `type` _datetime_ | Datetime offset by negated duration |
| `type` _datetime_ | `null` | `null` | |
| `null` | `type` _datetime_ | `null` | |
| | | | |

In the table, `type` _datetime_ stands for any of `type date`, `type datetime`, `type datetimezone`, or `type time`. When subtracting a duration from a value of some type _datetime_, the resulting value is of that same type.

For other combinations of values than those listed in the table, an error with reason code `"Expression.Error"` is raised. Each combination is covered in the following sections.

Errors raised when evaluating either operand are propagated.

#### Numeric difference

The difference between two numbers is computed using the _subtraction operator_, producing a number. For example:

```
1 - 1                // 0 
#nan - #infinity     // #nan
```

The subtraction operator `-` over numbers uses Double Precision; the standard library function `Value.Subtract` can be used to specify Decimal Precision. The following holds when computing a difference of numbers:

* The difference in Double Precision is computed according to the rules of 64-bit binary double-precision IEEE 754 arithmetic [IEEE 754-2008](https://ieeexplore.ieee.org/servlet/opac?punumber=4610933). The following table lists the results of all possible combinations of nonzero finite values, zeros, infinities, and NaN's. In the table, `x` and `y` are nonzero finite values, and `z` is the result of `x - y`. If `x` and `y` are equal, `z` is positive zero. If `x - y` is too large to be represented in the destination type, `z` is an infinity with the same sign as `x - y`. 
 
   | - | y | +0 | -0 | +&#8734; | -&#8734; | NaN |
   | --- | --- | --- | --- | --- | --- | --- |
   | <b>x</b> | z | x | x | -&#8734; | +&#8734; | NaN |
   | <b>+0</b> | -y | +0 | +0 | -&#8734; | +&#8734; | NaN |
   | <b>-0</b> | -y | -0 | +0 | -&#8734; | +&#8734; | NaN |
   | <b>+&#8734;</b> | +&#8734; | +&#8734; | +&#8734; | NaN | +&#8734; | NaN |
   | <b>-&#8734;</b> | -&#8734; | -&#8734; | -&#8734; | -&#8734; | NaN | NaN |
   | <b>NaN</b> | NaN | NaN | NaN | NaN | NaN | NaN |
   | | | | | | | |
 
* The difference in Decimal Precision is computed without losing precision. The scale of the result is the larger of the scales of the two operands.

#### Difference of durations

The difference of two durations is the duration representing the difference between the number of 100-nanosecond ticks represented by each duration. For example:

```
#duration(1,2,30,0) - #duration(0,0,0,30.45) 
// #duration(1, 2, 29, 29.55)
```

#### Datetime offset by negated duration

A _datetime_ `x` and a duration `y` may be subtracted using `x - y` to compute a new _datetime_. Here, _datetime_ stands for any of `date`, `datetime`, `datetimezone`, or `time`. The resulting _datetime_ has a distance from `x` on a linear timeline that is exactly the magnitude of `y`, in the direction opposite the sign of `y`. Subtracting positive durations yields results that are backwards in time relative to `x`, while subtracting negative values yields results that are forwards in time.

```
#date(2010,05,20) - #duration(00,08,00,00) 
   //#datetime(2010, 5, 19, 16, 0, 0) 
   //2010-05-19T16:00:00 
#date(2010,01,31) - #duration( 30,08,00,00) 
   //#datetime(2009, 12, 31, 16, 0, 0) 
   //2009-12-31T16:00:00
```

#### Duration between two datetimes

Two _datetimes_ `t` and `u` may be subtracted using `t - u` to compute the duration between them. Here, _datetime_ stands for any of `date`, `datetime`, `datetimezone`, or `time`. The duration produced by subtracting `u` from `t` must yield `t` when added to `u`.

```
#date(2010,01,31) - #date(2010,01,15) 
// #duration(16,00,00,00) 
// 16.00:00:00 
 
#date(2010,01,15)- #date(2010,01,31) 
// #duration(-16,00,00,00) 
// -16.00:00:00 
 
#datetime(2010,05,20,16,06,00,-08,00) - 
#datetime(2008,12,15,04,19,19,03,00) 
// #duration(521,22,46,41)
// 521.22:46:41
```

Subtracting `t - u` when `u > t` results in a negative duration:

```
#time(01,30,00) - #time(08,00,00) 
// #duration(0, -6, -30, 0)
```

The following holds when subtracting two _datetimes_ using `t - u`:

* u + (t - u) = t

### Multiplication operator

The interpretation of the multiplication operator (`x * y`) is dependent on the kind of value of the evaluated expressions x and y, as follows:

| X | Y | Result | Interpretation |
| --- | --- | --- | --- |
| `type number`  |  `type number` | `type number` | Numeric product |
| `type number` | `null` | `null` | |
| `null` | `type number` | `null` | |
| `type duration` | `type number` | `type duration` | Multiple of duration |
| `type number` | `type duration` | `type duration` | Multiple of duration |
| `type duration` | `null` | `null` | |
| `null` | `type duration` | `null` | |
| | | | | 

For other combinations of values than those listed in the table, an error with reason code `"Expression.Error"` is raised. Each combination is covered in the following sections.

Errors raised when evaluating either operand are propagated.

#### Numeric product
The product of two numbers is computed using the _multiplication operator_, producing a number. For example:

```
2 * 4                // 8 
6 * null             // null 
#nan * #infinity     // #nan
```

The multiplication operator `*` over numbers uses Double Precision; the standard library function `Value.Multiply` can be used to specify Decimal Precision. The following holds when computing a product of numbers:

* The product in Double Precision is computed according to the rules of 64-bit binary double-precision IEEE 754 arithmetic [IEEE 754-2008](https://ieeexplore.ieee.org/servlet/opac?punumber=4610933). The following table lists the results of all possible combinations of nonzero finite values, zeros, infinities, and NaN's. In the table, `x` and `y` are positive finite values. `z` is the result of `x * y`. If the result is too large for the destination type, `z` is infinity. If the result is too small for the destination type, `z` is zero. 

   | * | +y | -y | +0 | -0 | +&#8734; | -&#8734; | NaN |
   | --- | --- | --- | --- | --- | --- | --- | --- |
   | <b>+x</b> | +z | -z | +0 | -0 | +&#8734; | -&#8734; | NaN |
   | <b>-x</b> | -z | +z | -0 | +0 | -&#8734; | +&#8734; | NaN |
   | <b>+0</b> | +0 | -0 | +0 | -0 | NaN | NaN | NaN |
   | <b>-0</b> | -0 | +0 | -0 | +0 | NaN | NaN | NaN |
   | <b>+&#8734;</b> | +&#8734; | -&#8734; | NaN | NaN | +&#8734; | -&#8734; | NaN |
   | <b>-&#8734;</b> | -&#8734; | +&#8734; | NaN | NaN | -&#8734; | +&#8734; | NaN |
   | <b>NaN</b> | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
   | | | | | | | | |

* The product in Decimal Precision is computed without losing precision. The scale of the result is the larger of the scales of the two operands.

#### Multiples of durations

The product of a duration and a number is the duration representing the number of 100nanosecond ticks represented by the duration operand times the number operand. For example:

```
#duration(2,1,0,15.1) * 2 
// #duration(4, 2, 0, 30.2)
```

### Division operator

The interpretation of the division operator (`x / y`) is dependent on the kind of value of the evaluated expressions `x` and `y`, as follows: 

| X | Y | Result | Interpretation |
| --- | --- | --- | --- |
| `type number` | `type number` | `type number` | Numeric quotient |
| `type number` | `null` | `null` | |
| `null` | `type number` | `null` | |
| `type duration` | `type number` | `type duration` | Fraction of duration |
| `type duration` | `type duration` | `type duration` | Numeric quotient of durations |
| `type duration` | `null` | `null` | |
| `null` | `type duration` | `null` | |
| | | | | 

For other combinations of values than those listed in the table, an error with reason code `"Expression.Error"` is raised. Each combination is covered in the following sections.

Errors raised when evaluating either operand are propagated.

#### Numeric quotient

The quotient of two numbers is computed using the _division operator_, producing a number. For example:

```
8 / 2               // 4 
8 / 0               // #infinity 
0 / 0               // #nan 
0 / null            // null 
#nan / #infinity    // #nan
```

The division operator `/` over numbers uses Double Precision; the standard library function `Value.Divide` can be used to specify Decimal Precision. The following holds when computing a quotient of numbers:

* The quotient in Double Precision is computed according to the rules of 64-bit binary double-precision IEEE 754 arithmetic [IEEE 754-2008](https://ieeexplore.ieee.org/servlet/opac?punumber=4610933). The following table lists the results of all possible combinations of nonzero finite values, zeros, infinities, and NaN's. In the table, `x` and `y` are positive finite values. `z` is the result of `x / y`. If the result is too large for the destination type, `z` is infinity. If the result is too small for the destination type, `z` is zero.

   | / | +y | -y | +0 | -0 | +&#8734; | -&#8734; | NaN |
   | --- | --- | --- | --- | --- | --- | --- | --- |
   | <b>+x</b> | +z | -z | +&#8734; | -&#8734; | +0 | -0 | NaN |
   | <b>-x</b> | -z | +z | -&#8734; | +&#8734; | -0 | +0 | NaN |
   | <b>+0</b> | +0 | -0 | NaN | NaN | +0 | -0 | NaN |
   | <b>-0</b> | -0 | +0 | NaN | NaN | -0 | +0 | NaN |
   | <b>+&#8734;</b> | +&#8734; | -&#8734; | +&#8734; | -&#8734; | NaN | NaN | NaN |
   | <b>-&#8734;</b> | -&#8734; | +&#8734; | -&#8734; | +&#8734; | NaN | NaN | NaN |
   | <b>NaN</b> | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
   | | | | | | | | |
 
* The sum in Decimal Precision is computed without losing precision. The scale of the result is the larger of the scales of the two operands.

#### Quotient of durations

The quotient of two durations is the number representing the quotient of the number of 100nanosecond ticks represented by the durations. For example:

```
#duration(2,0,0,0) / #duration(0,1,30,0) 
// 32
```

#### Scaled durations
The quotient of a duration `x` and a number `y` is the duration representing the quotient of the number of 100-nanosecond ticks represented by the duration `x` and the number `y`. For example:

```
#duration(2,0,0,0) / 32 
// #duration(0,1,30,0)
```

## Structure Combination

The combination operator (`x & y`) is defined over the following kinds of values:

| X | Y | Result | Interpretation |
| --- | --- | --- | --- |
| `type text` | `type text` | `type text` | Concatenation |
| `type text` | `null` | `null` | |
| `null` | `type text` | `null` | |
| `type date` | `type time` | `type datetime` | Merge |
| `type date` | `null` | `null` | |
| `null` | `type time` | `null` | |
| `type list` | `type list` | `type list` | Concatenation |
| `type record` | `type record` | `type record` | Merge |
| `type table` | `type table` | `type table` | Concatenation |
| | | | |

### Concatenation

Two text, two list, or two table values can be concatenated using `x & y`.

The following example illustrates concatenating text values:

```
"AB" & "CDE"     // "ABCDE"
```

The following example illustrates concatenating lists:

```
{1, 2} & {3}     // {1, 2, 3}
```

The following holds when concatenating two values using `x & y`:

* Errors raised when evaluating the `x` or `y` expressions are propagated.

* No error is propagated if an item of either `x` or `y` contains an error.

* The result of concatenating two text values is a text value that contains the value of x immediately followed by y. If either of the operands is null and the other is a text value, the result is null.

* The result of concatenating two lists is a list that contains all the items of `x` followed by all the items of `y`.

* The result of concatenating two tables is a table that has the union of the two operand table's columns. The column ordering of `x` is preserved, followed by the columns only appearing in `y`, preserving their relative ordering. For columns appearing only in one of the operands, `null` is used to fill in cell values for the other operand.

### Merge

#### Record merge

Two records can be merged using `x & y`, producing a record that includes fields from both `x` and `y`.

The following examples illustrate merging records:

```
[ x = 1 ] & [ y = 2 ]                // [ x = 1, y = 2 ] 
[ x = 1, y = 2 ] & [ x = 3, z = 4 ]  // [ x = 3, y = 2, z = 4 ]
```

The following holds when merging two records using `x + y`:

* Errors raised when evaluating the `x` or `y` expressions are propagated.

* If a field appears in both `x` and `y`, the value from `y` is used.

* The order of the fields in the resulting record is that of `x`, followed by fields in `y` that are not part of `x`, in the same order that they appear in `y`.

* Merging records does not cause evaluation of the values.

* No error is raised because a field contains an error.

* The result is a record.

#### Date-time merge

A date `x` can be merged with a time `y` using `x & y`, producing a datetime that combines the parts from both `x` and `y`.

The following example illustrates merging a date and a time:

```
#date(2013,02,26) & #time(09,17,00) 
// #datetime(2013,02,26,09,17,00)
```
The following holds when merging two records using `x + y`:

* Errors raised when evaluating the `x` or `y` expressions are propagated.

* The result is a datetime.

## Unary operators

The `+`, `-`, and `not` operators are unary operators.

_unary-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type-expression_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`+` _unary expression_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-` _unary expression_<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`not` _unary expression_

### Unary plus operator

The unary plus operator (`+x`) is defined for the following kinds of values: 
 
| X | Result | Interpretation |
| --- | --- | --- |
| `type number` | `type number` | Unary plus |
| `type duration` | `type duration` | Unary plus |
| `null` | `null | |
| | | | 

For other values, an error with reason code `"Expression.Error"` is raised.

The unary plus operator allows a `+` sign to be applied to a number, datetime, or null value. The result is that same value. For example:

```
+ - 1                 // -1 
+ + 1                 // 1 
+ #nan                // #nan 
+ #duration(0,1,30,0) // #duration(0,1,30,0)
```

The following holds when evaluating the unary plus operator `+x`:

* Errors raised when evaluating `x` are propagated.

* If the result of evaluating `x` is not a number value, then an error with reason code `"Expression.Error"` is raised.

### Unary minus operator

The unary minus operator (`-x`) is defined for the following kinds of values:

| X | Result | Interpretation |
| --- | --- | --- |
| `type number` | `type number ` | Negation |
| `type duration` | `type duration` | Negation |
| `null` | `null` | |
| | | | 

For other values, an error with reason code `"Expression.Error"` is raised.

The unary minus operator is used to change the sign of a number or duration. For example:

```
- (1 + 1)       // -2 
- - 1           // 1 
- - - 1         // -1 
- #nan          // #nan 
- #infinity     // -#infinity 
- #duration(1,0,0,0)  // #duration(-1,0,0,0) 
- #duration(0,1,30,0) // #duration(0,-1,-30,0)
```

The following holds when evaluating the unary minus operator `-x`:

* Errors raised when evaluating `x` are propagated.

* If the expression is a number, then the result is the number value from expression `x` with its sign changed. If the value is NaN, then the result is also NaN.

### Logical negation operator

The logical negation operator (`not`) is defined for the following kinds of values:

| X | Result | Interpretation |
| --- | --- | --- |
| `type logical` | `type logical` | Negation |
| `null` | `null` | |
| | | | 
 
This operator computes the logical `not` operation on a given logical value. For example:

```
not true             // false 
not false            // true 
not (true and true)  // false
```

The following holds when evaluating the logical negation operator `not x`:

* Errors raised when evaluating `x` are propagated.

* The value produced from evaluating expression x must be a logical value, or an error with reason code `"Expression.Error"` must be raised. If the value is `true`, the result is `false`. If the operand is `false`, the result is `true`.

The result is a logical value.

## Type operators

The operators `is` and `as` are known as the type operators.

### Type compatibility operator
The type compatibility operator `x is y`  is defined for the following types of values:

| X | Y | Result |
| --- | --- | --- |
| `type any` | _nullable-primitive-type_ | `type logical` |
| | | |
 
The expression `x is y` returns `true` if the ascribed type of `x` is compatible with `y`, and returns `false` if the ascribed type of `x` is incompatible with `y`. `y` must be a _nullable-primitivetype_.

_is-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;is-expression_  `is`  _nullable-primitive-type<br/> 
nullable-primitive-type:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`nullable`_<sub>opt</sub> primitive-type_

Type compatibility, as supported by the `is` operator, is a subset of [general type compatibility](m-spec-types.md) and is defined using the following rules:

* If `x` is null then it is compatible iff y is a nullable type or the type `any`.

* If `x` is non-null then if it is a compatible if the the primitive type of `x` is the same as `y`.

The following holds when evaluating the expression `x is y`:

* An error raised when evaluating expression `x` is propagated.

### Type assertion operator

The type assertion operator `x as y` is defined for the following types of values:

| X | Y | Result |
| --- | --- | --- |
| `type any` | _nullable-primitive-type_ | `type any` |
| | | |
 
The expression `x as y` asserts that the value `x` is compatible with `y` as per the `is` operator. If it is not compatible, an error is raised. `y` must be a _nullable-primitive-type_.

_as-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;equality-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as-expression_  `as`  _nullable-primitive-type_

The expression `x as y` is evaluated as follows:

* A type compatibility check `x is y` is performed and the assertion returns `x` unchanged if that test succeeds.

* If the compatibility check fails, an error with reason code `"Expression.Error"` is raised.

Examples:

```
1 as number               // 1 
"A" as number             // error 
null as nullable number   // null
```

The following holds when evaluating the expression `x as y`:

* An error raised when evaluating expression `x` is propagated.

