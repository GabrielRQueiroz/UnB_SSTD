def format() -> None:
    check_call(
        ["black", "--check", "--diff", "src/", "tests/"],
    )

def proj1() -> None:
    check_call(
        ["cd", "./project-1/Projeto_1"],
        ["python", "projeto1.ipynb"]
    )
    
def proj2() -> None:
    check_call(
        ["python", "./Projeto_2/projeto_2.ipynb"],
    )