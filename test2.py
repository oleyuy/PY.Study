def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_line = []
    second_line = []
    dashes = []
    answers = []
    
    for problem in problems:
        parts = problem.split()
        if parts[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not (parts[0].isdigit() and parts[2].isdigit()):
            return "Error: Numbers must only contain digits."
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        num1, operator, num2 = parts
        width = max(len(num1), len(num2)) + 2
        
        first_line.append(num1.rjust(width))
        second_line.append(operator + num2.rjust(width - 1))
        dashes.append('-' * width)
        
        if show_answers:
            result = str(eval(problem))
            answers.append(result.rjust(width))
    
    arranged_problems = (
        '    '.join(first_line) + "\n" +
        '    '.join(second_line) + "\n" +
        '    '.join(dashes)
    )
    
    if show_answers:
        arranged_problems += "\n" + '    '.join(answers)
    
    return arranged_problems