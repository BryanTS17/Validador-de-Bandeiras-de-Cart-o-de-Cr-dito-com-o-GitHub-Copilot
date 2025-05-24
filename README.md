# Validador de Bandeiras de Cartão de Crédito

Este projeto contém um validador de bandeiras de cartão de crédito, que verifica se os números dos cartões pertencem a bandeiras específicas. As bandeiras suportadas incluem:

- MasterCard
- Visa (16 dígitos)
- American Express
- Diners Club
- Discover
- enRoute
- JCB
- Voyager
- HiperCard
- Aura

## Como Usar

1. **Clone o repositório** ou faça o download dos arquivos.
2. **Execute o script** `validador_bandeiras.py` em um ambiente Python.

### Exemplo de Uso

No arquivo `validador_bandeiras.py`, você pode chamar a função de validação passando o número do cartão como argumento. Por exemplo:

```python
from validador_bandeiras import validar_cartao

numero_cartao = "4111111111111111"  # Exemplo de número Visa
resultado = validar_cartao(numero_cartao)

if resultado:
    print("Cartão válido.")
else:
    print("Cartão inválido.")
```

## Bandeiras e Exemplos de Números Válidos

- **MasterCard**: 5555 4444 3333 2222
- **Visa (16 dígitos)**: 4111 1111 1111 1111
- **American Express**: 3782 8224 6310 005
- **Diners Club**: 3056 9309 0259 04
- **Discover**: 6011 1111 1111 1117
- **enRoute**: 2014 1234 5678 9010
- **JCB**: 3530 1113 0200 0000
- **Voyager**: 8699 9999 9999 9999
- **HiperCard**: 6062 0010 0000 0004
- **Aura**: 5078 0000 0000 0000

## Requisitos

- Python 3.x
- Nenhuma biblioteca externa é necessária.

## Contribuições

Sinta-se à vontade para contribuir com melhorias ou correções. Para isso, faça um fork do repositório e envie um pull request.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.# Validador-de-Bandeiras-de-Cart-o-de-Cr-dito-com-o-GitHub-Copilot
