def find_it(seq):
    """
    Encontra o número que aparece um número ímpar de vezes em um array de inteiros.

    Args:
        seq (list): Uma lista de inteiros.

    Returns:
        int: O número que aparece um número ímpar de vezes no array.
    Exemplos:
    >>> find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])
    5
    >>> find_it([1,1,2,-2,5,2,4,4,-1,-2,5])
    -1
    >>> find_it([20,1,1,2,2,3,3,5,5,4,20,4,5])
    5
    >>> find_it([10])
    10
    >>> find_it([10, 10, 10])
    10
    >>> find_it([1,1,1,1,1,1,10,1,1,1,1])
    10
    >>> find_it([5,4,3,2,1,5,4,3,2,10,10])
    1
    
    Para mais informações consulte https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python
    """
    for n in seq:
        if seq.count(n) % 2 != 0:
            return n

# Exemplos de uso
print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))  # Deve retornar 5
print(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]))  # Deve retornar -1
print(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]))  # Deve retornar 5
print(find_it([10]))  # Deve retornar 10
print(find_it([10, 10, 10]))  # Deve retornar 10
print(find_it([1,1,1,1,1,1,10,1,1,1,1]))  # Deve retornar 10
print(find_it([5,4,3,2,1,5,4,3,2,10,10]))  # Deve retornar 1
