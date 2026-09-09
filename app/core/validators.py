def clean_and_validate_string(v: str) -> str:
    """Função utilitária genérica para limpar espaços e validar texto não vazio.

    Args:
        v (str): O texto que será verificado.

    Returns:
        str: O texto limpo e validado sem espaços nas pontas.

    Raises:
        ValueError: Se o valor não for uma string ou estiver vazio.
    """
    if not isinstance(v, str):
        raise ValueError('O campo deve ser um texto válido.')
       
    cleaned_value = v.strip()
   
    if not cleaned_value:
        raise ValueError('Este campo não pode estar vazio ou conter apenas espaços.')
    
    return cleaned_value