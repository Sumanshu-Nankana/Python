from invoke import Collection, task


# No argument
@task
def build(c):
    print("Building")


"""
Passing argument with default values
It Can be called as
invoke build-and-clean  (No clean parameter provided, so default False will be assumed)
invoke build-and-clean -c (Means we are saying clean parameter should be True)
invoke build-and-clean --clean   (Means we are saying clean parameter should be True)
"""


@task
def build_and_clean(c, clean=False):
    if clean:
        print("Cleaning")
    print("Building")


"""
Passing positional argument but, no default value passed
It can be called as -
invoke greet sumanshu
invoke greet --name sumanshu
invoke greet -n sumanshu
invoke greet -n "sumanshu nankana"
invoke greet -n="sumanshu nankana"
"""


@task
def greet(c, name):
    print(f"Hello {name}")


"""
If we want to know what is actually 'name' :argument
we can use
invoke --help greet-with-metadata-info
"""


@task(help={"name": "Name of the person to say Hello to"})
def greet_with_metadata_info(c, name):
    print(f"Hello {name}")


"""
To run the Shell commands, we need to use the
run function.
"""


@task
def run_shell_command(c):
    c.run("echo sumanshu nankana")
    c.run("python --version")


@task
def task1(c):
    print("Running Task 1")


@task
def task2(c):
    print("Running Task 2")


"""
Now when we invoke the task3
it will first invoke the task1
and then task2
and then finally task3 will executed
"""


@task(task1, task2)
def task3(c):
    print("Running Task3")


"""
This is another way to define the tasks
"""


@task(pre=[task1, task2, task3], post=[run_shell_command])
def task4(c):
    print("Running Task4")


"""
We will group task_a and task_b in one group
and task_c in another group
"""


@task
def task_a(c):
    print("Executing Task A")


@task
def task_b(c):
    print("Executing Task B")


@task
def task_c(c):
    print("Executing Task C")


#
# Create the namespace
group1 = Collection("group1")
# Now add the task in particular namespace
group1.add_task(task_a, "a")
group1.add_task(task_b, "b")

# create another namespace
group2 = Collection("group2")
# Now add the task in this namespace
group2.add_task(task_c, "c")

# Create root namespace
ns = Collection()
ns.add_collection(group1)
ns.add_collection(group2)
