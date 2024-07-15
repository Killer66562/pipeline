from kfp import dsl, compiler


@dsl.component(base_image='python:3.12')
def rand(a: int, b: int) -> int:
    import random
    return random.randint(a, b) if a < b else random.randint(b, a)

@dsl.component(base_image='python:3.12')
def adder(a: int, b: int) -> int:
    return a + b

@dsl.pipeline
def rand_adder_pipeline(a: int, b: int) -> int:
    task_a = rand(a=a, b=b)
    task_b = rand(a=a, b=b)
    task_adder = adder(a=task_a.output, b=task_b.output)
    return task_adder.output

compiler.Compiler().compile(rand_adder_pipeline, 'rand_adder_pipeline.yaml')