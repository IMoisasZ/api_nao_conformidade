def clean_and_validate_string(v: str, min_length: int=0) -> str:
    """Função utilitária genérica para limpar espaços e validar texto não vazio.

    Args:
        v (str): O texto que será verificado.
        min_length (int=0): parametro 

    Returns:
        str: O texto limpo e validado sem espaços nas pontas.

    Raises:
        ValueError: Se o valor não for uma string ou estiver vazio.
    """
    if not isinstance(v, str):
        raise ValueError('O campo deve ser um texto válido.')
       
    cleaned_value = v.strip()
   
    if not cleaned_value or len(cleaned_value) < min_length:
        raise ValueError(f'O campo deve ter pelo menos {min_length} caracteres.')
    
    return cleaned_value