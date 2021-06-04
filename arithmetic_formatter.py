def arithmetic_arranger(problems, answer=False):

    print("Problems -->", problems)
    print()

    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""
    operator = ["+", "-"]

    for problem in problems:

        problemSplit = problem.split()

        if problemSplit[1] not in operator:
            return "Error: Operator must be '+' or '-'."

        if problemSplit[0].isdigit() and problemSplit[2].isdigit():

            if len(problemSplit[0]) > 4 or len(problemSplit[2]) > 4:
                return "Error: Numbers cannot be more than four digits."

            if problems.index(problem) < len(problems) - 1:
                greater_number = len(problemSplit[0]) if len(problemSplit[0]) > len(
                    problemSplit[2]) else len(problemSplit[2])
                first_line += " " * \
                    (greater_number -
                     len(problemSplit[0]) + 2) + problemSplit[0] + " " * 4
                second_line += problemSplit[1] + " " * (greater_number - len(
                    problemSplit[2]) + 1) + problemSplit[2] + " " * 4
                third_line += "-" * (greater_number + 2) + " " * 4
                if answer:
                    result = str(eval(problem))
                    fourth_line += " " * \
                        (greater_number + 2 - len(result)) + result + " " * 4

            else:
                greater_number = len(problemSplit[0]) if len(problemSplit[0]) > len(
                    problemSplit[2]) else len(problemSplit[2])
                first_line += " " * \
                    (greater_number -
                     len(problemSplit[0]) + 2) + problemSplit[0]
                second_line += problemSplit[1] + " " * (
                    greater_number - len(problemSplit[2]) + 1) + problemSplit[2]
                third_line += "-" * (greater_number + 2)
                if answer:
                    result = str(eval(problem))
                    fourth_line += " " * \
                        (greater_number + 2 - len(result)) + result

        else:
            return "Error: Numbers must only contain digits."

    if answer:
        arranged_problems = first_line + '\n' + second_line + \
            '\n' + third_line + '\n' + fourth_line
    else:
        arranged_problems = first_line + '\n' + second_line + '\n' + third_line

    return arranged_problems
