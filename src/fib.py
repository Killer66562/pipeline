from functools import cache
from kfp import dsl, compiler


@dsl.component(base_image='python:3.9')
def fib(n: int) -> int:
    if n < 0:
        raise ValueError("n cannot be smaller than 0!")
    return n if n == 0 or n == 1 else fib(n-1) + fib(n-2)

@dsl.pipeline
def fib_pipeline(n: int) -> int:
    fib_task = fib(n=n)
    return fib_task.output

compiler.Compiler().compile(fib_pipeline, 'fib_pipeline.yaml')