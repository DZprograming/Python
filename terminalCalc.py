import math

def expression_calculator():
    # Запитуємо весь вираз одним рядком
    expr = input("Введіть математичний вираз (наприклад, 2+2/3*2 або math.sin(3.14)): ")
    
    try:
        # Безпечне обчислення виразу з доступом тільки до math
        # Це дозволяє використовувати +, -, *, /, **, дужки та функції math (sin, cos, sqrt тощо)
        result = eval(expr, {"__builtins__": {}}, {"math": math})
        
        # Виводимо результат
        print(f"Результат: {result}")
    
    except Exception as e:
        # Обробка помилок: невірний вираз, ділення на 0 тощо
        print(f"Помилка: {e}")

# Запускаємо калькулятор
expression_calculator() 