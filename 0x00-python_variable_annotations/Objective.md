# What Are Type Annotations?
Type annotations — also known as type signatures — are used to indicate the datatypes of variables and input/outputs of functions and methods.

### Configuring mypy for type checking

Resource - https://blog.logrocket.com/understanding-type-annotation-python/#adding-type-hints-variables

mypy can be configured to suit your workflow and code practices. You can run mypy in strict mode, using the --strict option to flag any code without type hints:

mypy --strict announcement.py

announcement.py:1: error: Function is missing a type annotation
announcement.py:4: error: Call to untyped function "print_release" in typed context
Found 2 errors in 1 file (checked 1 source file)

The --strict option is the most restrictive option and doesn’t support gradual typing. Most of the time, you won’t need to be this strict. Instead, adopt gradual typing to add the type hints in phases.

mypy also provides a --disallow-incomplete-defs option. This option flags functions that don’t have all of their parameters and return values annotated. This option is so handy when you forget to annotate a return value or a newly added parameter, causing mypy to warn you. You can think of this as your compiler that reminds you to abide by the rules of static typing in your code development.

To understand this, add the type hints to the parameters only and omit the return value types (pretending you forgot):


